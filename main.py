# -*- coding: utf-8 -*-
import mss.tools
import pyautogui
import requests
import cv2
import pytesseract
import re
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import localtime, strftime
import sqlite3
import json
from src.logger import logger, loggerMapClicked


cat = """
  ____                        _        ____                          _           
 | __ )    ___    _ __ ___   | |__    / ___|  _ __   _   _   _ __   | |_    ___  
 |  _ \   / _ \  | '_ ` _ \  | '_ \  | |     | '__| | | | | | '_ \  | __|  / _ \ 
 | |_) | | (_) | | | | | | | | |_) | | |___  | |    | |_| | | |_) | | |_  | (_) |
 |____/   \___/  |_| |_| |_| |_.__/   \____| |_|     \__, | | .__/   \__|  \___/ 
                                                     |___/  |_| 
                                                     
                         _.-^^---....,,--       
                 _--                  --_  
                <                        >)
                |                         | 
                 \._                   _./  
                    ```--. . , ; .--'''       
                          | |   |             
                       .-=||  | |=-.   
                       `-=#$%&%$#=-'   
                          | ;  :|     
                 _____.,-#%&$@%#&#~,._____     
 
=========================================================================
========== ✨ Faça sua boa ação de hoje, manda aquela gorjeta! 😊 =======
=========================================================================
======================== vvv BCOIN BUSD BNB vvv =========================
============== 0xbd06182D8360FB7AC1B05e871e56c76372510dDf ===============
=========================================================================
===== https://www.paypal.com/donate?hosted_button_id=JVYSC6ZYCNQQQ ======
=========================================================================
=====                        Modified By Deyvão                    ======
=====                   Carteira do dev principal mantida          ======
=========================================================================

>>---> Press ctrl + c to kill the bot.

>>---> Some configs can be found in the config.yaml file."""

# ============================= Base De Dados Sql3      =============================
# Conecta com o banco / cria

banco = sqlite3.connect('database/dados_bomb.db')

# Cursor
cursor = banco.cursor()
sleep(1)
# =========================== Verifica se está na hora =============================
# Pega o horário do pc
# horas_minutos = '03:03'

horas_minutos = strftime("%H:%M", localtime())

# Horários para enviar as mensagens , pode modificar de boa que não quebra o código

horario_to_send = '03:00', '03:01', '03:02', '03:03',  '06:00', '06:01', '06:02', '06:03', '09:00', '09:01', '09:02', '09:03', '13:00', '13:01', '13:02', '13:03', '16:00', '16:01', '16:02', '16:03', '19:00', '19:01', '19:02', '19:03', '21:00', '21:01', '21:02', '21:03', '23:00', '23:01', '23:02', '23:03'

# Verifica se está no horário de mandar a mensagem , para não sobrecarregar seu lindo pc com as regex em vão e não flodar seu chat

if horas_minutos in horario_to_send:

    sleep(1)
    # =========================== Obter codigo fonte da pagina ==========================
    url = 'https://coinmarketcap.com/pt-br/currencies/bombcrypto/'


    def obterCodigoFonte(url):
        s = Service('chromedriver_dir/chromedriver.exe')
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=s, options=chrome_options)
        driver.get(url)
        return driver.page_source


    def processarCodigoFonte(cf):
        soup = BeautifulSoup(cf, 'html.parser')
        getValueFromDiv = soup.find_all('p')
        return getValueFromDiv


    try:
        codigoFonte = obterCodigoFonte(url)

        # Pega o código html e joga na variavel e separa somente os valores com BRL

        separa_codigo_html = re.findall(r"R\$([0-9]{1,2},[0-9]{1,2}).BRL", codigoFonte)

        # Transforma em string

        valor_string_html = "".join(separa_codigo_html)

        # print(len(valor_string_html))

        # Tira as letras
        if len(valor_string_html) == 4:

            separa_valor = re.findall(r"\d.\d\d", valor_string_html)
        else:
            separa_valor = re.findall(r"\d\d.\d\d", valor_string_html)

        # Transforma em string

        bcoin_somente_numeros = "".join(separa_valor)
        # Troca a virgula por ponto

        tira_virgula = re.sub(r",", ".", bcoin_somente_numeros)
        # Converte em float

        bcoin_valor_float_ = float(tira_virgula)

    except ValueError as error:

        logger("[-] Erro Com as RegEX ou com o ChromeDriver\n")

    # Time para o pc pensar kkk
    sleep(2)

    # ====================================================================================

    # token único utilizado para manipular o bot (não deve ser compartilhado)
    # utilizei o BotFather para obter o bot
    # exemplo: '1413778757:AAFxmr611LssAHbZn1uqV_NKFsbwK3TT-wc'

    # Puxa o token do banco
    try:
        cursor.execute("SELECT token FROM dados")
        # Define a variavel

        token_errado = cursor.fetchall()
        # Converte em str

        token_str = ''.join(str(e) for e in token_errado)
        # Tira ( , ' do token

        token = token_str.replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    except ValueError or TypeError or NameError as error:

        token = None

        logger("[-] Erro ao recuperar dados da tabela , verifique as configurações\n")

    # Da um time para não sair clicando onde não deve
    sleep(1)

    # Da uma pageUp para caso a pagina esteja muito em baixo assim atrapalhando o bot

    pyautogui.hotkey('PageUp')

    # Identificar os baus no mapa [BETA]
    # ==========================================================================================
    # Valores dos báus

    valor_bau_madeira = 0.01

    valor_bau_roxo = 0.03

    valor_bau_ouro = 0.16

    valor_bau_diamante = 0.33

    jaula = "1 Herói"

    # Localiza os baús na tela

    # ========================================

    # Localiza o Baú
    try:
        local_bau = pyautogui.locateOnScreen("bau_image_dir/bau.png", grayscale=False)

    except OSError as error:
        local_bau = None

        logger("[-] Icone do bau não lozalizado na pasta do projeto\n")

    # Verifica se encontrou o icone báu na sua tela

    if local_bau is not None:

        try:
            pyautogui.click("bau_image_dir/bau.png", duration=1)

            logger(f"[+] Achei seu baú! {local_bau}\n")

        except TypeError as error:

            logger("[-] Erro no pyautogui\n")

    else:
        logger("[-] Não encontrei seu báu, verifique a resolução da tela ou a pasta de imagens\n")

    # Se prepara para capturar a tela

    sleep(2)

    # Localiza o local adequado para passar os parametros de ShotScreen
    try:
        local_foto = pyautogui.locateOnScreen("bau_image_dir/bcoin.png")

    except OSError as error:

        local_foto = None

        logger("[-] Erro ao localizar o icone do bcoin na pasta do projeto\n")

    # Verifica se achou o valor dos Bcoins

    if local_foto is not None:
        logger(f'[+] Achei Os Bcoins ! {local_foto}\n')

    else:
        logger("[-] Não encontrei seus Bcoins , Verifique a pasta targets e/ou a resolução da tela\n")

    sleep(1)
    with mss.mss() as sct:
        # Bcoins dentro do báu com base na localização (pode mudar dependendo da resolução do seu monitor)

        with open('database/dados.json', 'r') as arquivo:
            valores = json.load(arquivo)
            try:
                top = int(valores['top'])
                left = int(valores['left'])
                width = int(valores['width'])
                height = int(valores['height'])

            except ValueError or TypeError as error:

                logger('[-] Erro , verifique o arquivo json\n')

        region = {'top': top, 'left': left, 'width': width, 'height': height}
        logger(f"[+] A Região de captura foi {region}!\n")
        # Captura a foto do valor para converter em string

        img = sct.grab(region)

        # Salva a foto na pasta targets para ser analisada no futuro

        mss.tools.to_png(img.rgb, img.size, output='bau_image_dir/foto.png')

    # ===================== Parte da I.A =================================================
    # Caminho dos drivers do pytesseract

    caminho = "pytesseract_dir"

    # Define o Executavel

    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

    # Abre a imagem para fazer a leitura

    imagem = cv2.imread("bau_image_dir/foto.png")

    # Configuração para aumentar a probabilidade de leitura

    config = r'--oem 3 --psm 8'

    # Converte a imagem para texto

    texto = pytesseract.image_to_string(imagem, config=config)

    # Tirar a quebra de linha que vem com o texto

    valor_bcoin = texto.split("\n")

    # Tranforma em String

    valor_bcoin_certo = "".join(valor_bcoin)

    # Substitui a , por .

    valor_bcoin_com_ponto = valor_bcoin_certo.replace(",", ".")

    # Converte para float

    try:
        valor_bcoin_float = float(valor_bcoin_com_ponto)
        # Calcula o valor do bcoin x o valor do real

        # noinspection PyUnboundLocalVariable
        valor_bcoin_reais = valor_bcoin_float * bcoin_valor_float_

        # Mensagem a ser enviada
        emoji_dinheiro = "\U0001F4B0"
        emoji_ativo = "\U00002714"
        emoji_bomb = "\U0001F4A3"
        emoji_cash = "\U0001FA99"
        emoji_gratidao = "\U0001F4CA"
        msg = f"""
        
            {emoji_bomb} Sistema BombCrypto {emoji_bomb}
        
{emoji_ativo} Sua conta Primaria Está ativa\n
{emoji_dinheiro} Você tem {valor_bcoin_com_ponto} Bcoins\n
{emoji_bomb} O Bcoin custa R${bcoin_valor_float_}\n
{emoji_cash} Totalizando R${valor_bcoin_reais:.2f}\n 
{emoji_gratidao} Obrigado BombCrypto!
        
                    """

    except ValueError as error:
        logger("[-] Erro ao indentificar valores do Bcoin em sua conta , verifique a configuração do pytessseract\n")

        msg = "[-] Ocorreu um erro ao processar sua solicitação" \
              "[-] talvez a conta Primária está [OFF]" \
              "[-]ou a I.A não achou Os valores do Bcoin."

    # ========================================================================================

    # ================================ Parte do chat ========================================

    def send_message(token, chat_id, message):
        try:
            data = {"chat_id": chat_id, "text": msg}

            url_mensagem = f"https://api.telegram.org/bot{token}/sendMessage"

            requests.post(url_mensagem, data)

        except Exception as e:

            logger("[-] Erro no sendMessage:", e)


    # Laço try para não parar o bot
    try:
        cursor.execute("SELECT chat_id FROM dados")

        resultado_chat_id = cursor.fetchall()

    except TypeError or ValueError or NameError as error:

        resultado_chat_id = None

        logger("[-] Erro ao recuperar dados das tabelas, verifique as configurações\n")

    # ====================================================================================
    send_message(token, resultado_chat_id[0], msg)
    logger('[+] Mensagem  enviada com sucesso!\n')
    # ====================================================================================
    # for more accounts

    # pyautogui.hotkey("alt", "tab")
    # repeat code * account
else:
    logger("[!] Não está na hora de enviar mensagem, Prosseguindo.")

