#!/usr/dev/python3
#Bednakov-Xack-Live
#2020/01/05
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
print(f"""
    {re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    {re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
    {re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

                version : 0.1
            Bednakov-Xack-Live
            """)
def telegr(int):
    return int * int
print("   Для запуска программы вам нужно ввести login \n  И ключ активации , Для Получения логина и ключа \n           Отправте смс с текстом tg-spam\n        на Email: denisbednakov@gmail.com ")
print("\n   ***************************************\n")
while True:
    log = input("              Введите Login: \n")
    if log == "telega":
        break
    else:
        try:
            log == int(log)
        except ValueError:
            print("\nНеверный Login\nПопробуйте снова")
while True:
    pas = input("\nВведите Password: ")
    if pas == "2020":
        break
    else:
        try:
            pas == int(pas)
        except ValueError:
            print("\nНеверный Password\nПопробуйте снова\n")
print("\n       Авторизация прошла Успешна !!! \n")
print("\nУстановка задерки на отправки я советую \nставить не менее 40 секунд так как из-за \nкороткого промежутка акаунт могут заблокировать !\n")
SLEEP_TIME = input(gr+"\nУстановить задерку между смс:  "+re)

class main():

    def banner():

        print(f"""
    {re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    {re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
    {re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

                version : 0.1
            Bednakov-Xack-Live
            """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] сначала запустите python3 setup.py!!\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] введите код: '+re))
        os.system('clear')
        main.banner()
        input_file = sys.argv[1]
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        print(gr+"[1] отправить смс по идентификатору ID\n[2] отправить смс username ")
        mode = int(input(gr+"Выбор : "+re))

        message = input(gr+"[+] Введите ваше сообщение: "+re)

        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(re+"[!] Неверный режим. Выход.")
                client.disconnect()
                sys.exit()
            try:
                print(gr+"[+] Отправка сообщения на:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print(gr+"[+] Ожидание {} секунд".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print(re+"[!] Получение сообщения об ошибке из телеграммы. \n[!] Скрипт останавливается сейчас. \n[!] Пожалуйста, попробуйте еще раз через некоторое время.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print(re+"[!] ошибка:", e)
                print(re+"[!] Пытаясь продолжить...")
                continue
        client.disconnect()
        print("Выполнено. Сообщение отправлено всем пользователям.")



main.send_sms()
