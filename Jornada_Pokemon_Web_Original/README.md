# Jornada Pokémon Web

Interface web para executar o jogo Python original sem editar a lógica do jogo.

## Como iniciar no Windows
1. Instale o Python 3.10 ou mais recente.
2. Extraia este ZIP para uma pasta.
3. Dê dois cliques em `INICIAR_NO_WINDOWS.bat`.
4. Aguarde o servidor iniciar e abra `http://127.0.0.1:8000` no navegador.

## O que esta versão tem
- Arena de batalha com Pokémon dos dois lados e barras de HP quando a saída do jogo fornece essas informações. A interface usa o nome que o jogo realmente imprime, então os Pokémon rivais dos encontros e ginásios também são exibidos.
- Sprites animados do Pokémon Showdown e fallback para a API pública do PokéAPI, cobrindo Pokémon com nomes canônicos e apelidos conhecidos.
- Efeitos visuais de ataque, dano, captura e evolução quando as mensagens do jogo indicam essas ações.
- Interface responsiva com menus, botões de escolha, registro da aventura e lista visual de Pokémon reconhecidos no texto. A exploração agora mostra apenas um painel de escolhas, sem duplicar a mesma lista em dois lugares.
- O jogo continua sendo executado pelo Python original: os botões encaminham escolhas para a entrada do programa.

## Importante sobre o código original
`jogo_original.py` é uma cópia byte a byte do arquivo fornecido e não foi alterado. A interface web está em `static/index.html` e a ponte entre o navegador e o processo Python está em `app.py`.

Algumas telas e ações do jogo original só podem ser exibidas como texto quando o programa não fornece dados estruturados para a interface. Os sprites externos e o fallback do PokéAPI precisam de conexão com a internet.
