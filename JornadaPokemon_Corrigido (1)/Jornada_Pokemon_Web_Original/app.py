from __future__ import annotations

import os
import queue
import subprocess
import sys
import threading
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
GAME_FILE = BASE_DIR / "jogo_original.py"

app = FastAPI(title="Jornada Pokémon — interface web")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

_lock = threading.RLock()
_process: Optional[subprocess.Popen[str]] = None
_output = ""
_error = ""
_reader_thread: Optional[threading.Thread] = None


def _read_output(proc: subprocess.Popen[str]) -> None:
    global _output, _error
    try:
        assert proc.stdout is not None
        while True:
            chunk = proc.stdout.read(1)
            if chunk == "":
                break
            with _lock:
                _output += chunk
    except Exception as exc:
        with _lock:
            _error = f"Falha ao ler a saída do jogo: {exc}"
    finally:
        with _lock:
            if proc.poll() is None:
                try:
                    proc.wait(timeout=0.2)
                except subprocess.TimeoutExpired:
                    pass


def _start_game() -> None:
    global _process, _output, _error, _reader_thread
    with _lock:
        if _process is not None and _process.poll() is None:
            return
        _output = ""
        _error = ""
        if not GAME_FILE.exists():
            raise RuntimeError("O arquivo jogo_original.py não foi encontrado.")
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        _process = subprocess.Popen(
            [sys.executable, "-u", str(GAME_FILE)],
            cwd=str(BASE_DIR),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
            env=env,
        )
        _reader_thread = threading.Thread(target=_read_output, args=(_process,), daemon=True)
        _reader_thread.start()


class InputMessage(BaseModel):
    value: str


@app.get("/")
def index():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.post("/api/start")
def start():
    try:
        _start_game()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"ok": True}


@app.get("/api/state")
def state(since: int = 0):
    with _lock:
        text = _output[max(0, since):]
        proc = _process
        return {
            "output": text,
            "length": len(_output),
            "running": bool(proc is not None and proc.poll() is None),
            "error": _error,
            "exit_code": proc.poll() if proc is not None else None,
        }


@app.post("/api/input")
def send_input(message: InputMessage):
    with _lock:
        proc = _process
        if proc is None or proc.poll() is not None or proc.stdin is None:
            raise HTTPException(status_code=409, detail="O jogo não está em execução. Clique em Iniciar jogo.")
        try:
            proc.stdin.write(message.value + "\n")
            proc.stdin.flush()
        except (BrokenPipeError, OSError) as exc:
            raise HTTPException(status_code=409, detail="O jogo encerrou a entrada.") from exc
    return {"ok": True}


@app.post("/api/restart")
def restart():
    global _process
    with _lock:
        proc = _process
        if proc is not None and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=2)
        _process = None
    _start_game()
    return {"ok": True}
