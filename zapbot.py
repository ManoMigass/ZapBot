import os
import sys
import time
import random
import webbrowser
import pyautogui
from urllib.parse import quote

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CAMINHO_TELEFONES = os.path.join(BASE_DIR, "telefones.txt")


# ===== FUNÇÕES =====

def ler_numeros():
    if not os.path.exists(CAMINHO_TELEFONES):
        return []

    with open(CAMINHO_TELEFONES, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]


def remover_numero(numero):
    numeros = ler_numeros()
    if numero in numeros:
        numeros.remove(numero)

        with open(CAMINHO_TELEFONES, "w", encoding="utf-8") as f:
            for n in numeros:
                f.write(n + "\n")


# ===== BOT PRINCIPAL =====

def rodar_zapbot(stop_event, mensagens, atualizar_status=None):

    if atualizar_status:
        atualizar_status("Abrindo WhatsApp Web...")

    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(15)  # tempo para login manual

    if atualizar_status:
        atualizar_status("ZapBot rodando")

    while not stop_event.is_set():
        numeros = ler_numeros()

        if not numeros:
            if atualizar_status:
                atualizar_status("Todos os números processados")
            break

        numero = numeros[0]

        try:
            mensagem = quote(random.choice(mensagens))
            linkzap = f"https://web.whatsapp.com/send?phone=55{numero}&text={mensagem}"

            webbrowser.open(linkzap)
            time.sleep(random.randint(12, 20))

            enviar = pyautogui.locateCenterOnScreen(
                "enviar.png",
                confidence=0.8
            )

            if enviar:
                pyautogui.click(enviar)
                print(f"[OK] Mensagem enviada para {numero}")
            else:
                print(f"[ERRO] Botão enviar não encontrado ({numero})")

        except Exception as e:
            print(f"[ERRO] {numero}: {e}")

        finally:
            # REMOVE O NÚMERO INDEPENDENTE DO RESULTADO
            remover_numero(numero)

            pyautogui.hotkey("ctrl", "w")
            time.sleep(random.randint(6, 10))

    if atualizar_status:
        atualizar_status("ZapBot parado")
