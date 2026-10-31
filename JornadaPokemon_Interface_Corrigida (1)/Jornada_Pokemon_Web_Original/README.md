# Jornada Pokémon — interface web do jogo original

Esta versão transforma a execução do jogo Python em uma interface no navegador. **A lógica do jogo permanece no arquivo `jogo_original.py`, sem alterações.** A página apenas apresenta o texto e os menus que o próprio Python imprime e envia ao jogo a opção escolhida.

## Como iniciar no Windows

1. Instale o Python 3.10 ou superior.
2. Extraia todo o conteúdo do ZIP para uma pasta.
3. Dê dois cliques em `INICIAR_NO_WINDOWS.bat`.
4. Aguarde a instalação das dependências e a inicialização do servidor.
5. Abra `http://127.0.0.1:8000` no navegador.
6. Clique em **Iniciar jornada**.

Mantenha a janela preta aberta enquanto estiver jogando. Para encerrar, feche essa janela.

## Como jogar

- Quando o Python mostrar opções numeradas, a interface cria um botão para cada opção exatamente como ela aparece no jogo.
- Quando o jogo pedir um nome, número ou confirmação, digite no campo e clique em **Enviar**.
- Durante as batalhas, use somente as opções exibidas pelo próprio jogo.
- Para tentar capturar um Pokémon, escolha **Capturar** no menu de batalha. O código original seleciona automaticamente a Pokébola disponível de maior chance. A tentativa pode falhar conforme a probabilidade original; nesse caso, a batalha continua.
- O botão **Reiniciar jornada** reinicia o processo do jogo.

## Estrutura

- `jogo_original.py`: código original do jogo, preservado.
- `app.py`: servidor local e ponte de entrada/saída entre Python e navegador.
- `static/index.html`: interface web simples, baseada nos menus reais do jogo.
- `requirements.txt`: dependências.
- `INICIAR_NO_WINDOWS.bat`: inicializador para Windows.
