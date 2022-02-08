import sqlite3
from time import sleep
import requests
import sys


sleep(1)
while True:
    print("=============================================================================================================================")
    print("Bem-vindo ao assistente de configuração do bot, preencha as informações com cuidado , é importante para o funcionamento do bot.")
    print("==============================================================================================================================")
    sleep(1)

    # Conecta com o banco / cria

    banco = sqlite3.connect('database/dados_bomb.db')

    # Cursor
    cursor = banco.cursor()

    # Banco
    cursor.execute("""CREATE TABLE IF NOT EXISTS dados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chat_id VARCHAR(60),
                    token VARCHAR(60)
                    );             
                   """)

    # Recebe Informaçoes
    sleep(1)

    token = input("Vamos começar com o token do bot\n"
                  "\n"
                  "token único utilizado para manipular o bot (não deve ser compartilhado)\n"
                  "\n"
                  "exemplo: 1413778757:AAFxmr611LssAHbZn1uqV_NKFsbwK3TT-wc\n"
                  "\n"
                  "Digite o código do seu token: \n")

    token_guardado = token

    # AVISOS @important
    sleep(1)
    print("======================================== ATENÇÃO ===================================================")
    print("Antes de tudo , crie um grupo e coloque o bot la no telegram, se você não criar não irá funcionar!\n")
    print("====================================================================================================")

    sleep(1)

    print("====================================================================================================")
    print("Pesquisando pelo grupo...\n")
    print("====================================================================================================")

    sleep(10)


    # Procura o ID do chat com base nos updates
    def procura_id_grupo():
        try:
            url = f"https://api.telegram.org/bot{token_guardado}/getUpdates"
            response = requests.get(url)
            if response.status_code == 200:
                json_msg = response.json()
                for json_result in reversed(json_msg['result']):
                    message_keys = json_result['message'].keys()
                    if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys) or (
                            'text' in message_keys):
                        id_chat = json_result['message']['chat']['id']
                        id_chat_str = str(id_chat)
                        print("[+] Grupo localizado!")
                        return id_chat_str
                        break
                    else:
                        print('[-] Nenhum grupo encontrado')
                        break
            else:
                print('[-] A resposta falhou, código de status: {}'.format(response.status_code))

                sys.exit(1)
        except Exception as e:

            print("[-] Erro no getUpdates:", e)

            sys.exit(1)


    retorna_id = procura_id_grupo()

    sleep(1)
    print("=================================================================================================")
    print("Inserindo dados na tabela..\n")
    print("=================================================================================================")

    sleep(1)

    # Inserção de dados
    cursor.execute("DELETE FROM dados")

    sleep(1)

    cursor.execute(f"INSERT INTO dados (token, chat_id) VALUES ('{token_guardado}', '{retorna_id}')")

    banco.commit()

    cursor.fetchall()

    cursor.execute("SELECT * FROM dados")

    linha = cursor.fetchall()

    sleep(1)

    print("=======================================================================================")
    print("Dados gravados com sucesso!\n")
    print("=======================================================================================")

    sleep(1)

    print("=======================================================================================")
    print(f"Configuração finalizada com sucesso! seus dados inseridos na tabelas foram {linha}!\n")
    print("=======================================================================================")
    sleep(2)

    banco.close()

    # Finaliza a config

    break
