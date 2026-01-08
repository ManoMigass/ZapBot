📱 ZapBot – Automação para WhatsApp Web

ZapBot é um projeto em Python que automatiza o envio de mensagens via WhatsApp Web, utilizando interação com o navegador e reconhecimento de tela.
O foco do projeto é educacional, voltado para aprendizado de automação, manipulação de arquivos e criação de interfaces gráficas.

🚀 Funcionalidades
Interface gráfica simples (Tkinter)
Envio automático de mensagens pelo WhatsApp Web
Sorteio de mensagens a partir de uma lista definida pelo usuário
Remoção automática dos números já processados
Botões de Start e Stop
Compatível com execução em .py ou geração de .exe
Estrutura organizada e fácil de modificar

🧠 Objetivo do Projeto
Este projeto foi desenvolvido com o objetivo de:
Praticar Python aplicado à automação
Trabalhar com arquivos .txt
Implementar controle de fluxo (start/stop)
Criar aplicações com interface gráfica
Entender os desafios de automação sem uso de APIs oficiais

🛠️ Tecnologias Utilizadas
Python 3
Tkinter
PyAutoGUI
Webbrowser
WhatsApp Web

▶️ Como Executar o Projeto
1️⃣ Clonar o repositório

git clone https://github.com/seu-usuario/zapbot.git
cd zapbot

2️⃣ Criar ambiente virtual (opcional, recomendado)
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências
pip install pyautogui

4️⃣ Executar o programa
python app.py

📝 Arquivo telefones.txt
Deve conter um número por linha
Apenas números (DDD + número)
Exemplo:

11999999999
33999072004

Os números são removidos automaticamente após o processamento.
⚠️ Aviso Importante

Este projeto não utiliza a API oficial do WhatsApp.
O uso indevido pode violar os termos de serviço da plataforma.

⚠️ Utilize apenas para fins educacionais e testes pessoais.

O autor não se responsabiliza por usos inadequados.

📦 Gerar Executável (.exe)
Para gerar um executável no Windows, utilize o PyInstaller:
python -m PyInstaller --noconsole --add-data "enviar.png;." app.py

O executável será gerado na pasta dist/.

📌 Observações
O WhatsApp Web precisa estar logado manualmente
O botão de envio é identificado por imagem (enviar.png)
Pequenas mudanças de layout do WhatsApp podem exigir ajustes

👨‍💻 Autor

Projeto desenvolvido para fins de estudo e aprendizado em automação com Python.
