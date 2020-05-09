## Bednakov-Xack-Live
# -*- coding: utf-8 -*-
# Бедняков Денис Леонидович
# GitHub http://github.com/bednakovdenis
##
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils
import webbrowser

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print(backtomenu_banner)
	backtomenu = input("Bednakov-Xack-Live > ")

	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nОШИБКА: неверный ввод")
		time.sleep(2)
		restart_program()


backtomenu_banner = """
  99) Вернуться в главное меню
  00) Выход из Mr.Robot
"""

clearscreen()
print("""

	        ╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
                 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
                 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

                            version : 0.1
                         Anonimus cicada3301

  Выберите из меню:

	01) Настроить API ID

	02) Создать список для рассылки

	03) Рассылка спама

""")

while True:
	try:
		santet = input("Ваш Выбор > ")

		if santet == "01" or santet == "1":
			webbrowser.open("https://my.telegram.org/", new=2)
			api = open("API.txt","w")
			api.write(input("Введите API ID: "))
			api.close()
			hash = open("hash.txt","w")
			hash.write(input("Введите HASH ID: "))
			hash.close()
			tel = open("tel.txt","w")
			tel.write(input("Введите Номер Телефона: "))
			tel.close()
			backtomenu_option()
		elif santet == "02" or santet == "2":
					#!/usr/dev/python3
					#Bednakov-Xack-Live
					#2020/01/05
					from telethon.sync import TelegramClient
					from telethon.tl.functions.messages import GetDialogsRequest
					from telethon.tl.types import InputPeerEmpty
					import os, sys
					import configparser
					import csv
					import time


					print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 0.1
		 Anonimus cicada3301
								""")

					def banner():
						print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 0.1
		 Anonimus cicada3301
								""")

					cpass = configparser.RawConfigParser()
					#cpass.read('config.data')

					try:
						api = open("API.txt","r")
						api_id = api.read()
						api.close()
						hash = open("hash.txt","r")
						api_hash = hash.read()
						hash.close()
						tel = open("tel.txt","r")
						phone = tel.read()
						tel.close()
						client = TelegramClient(phone, api_id, api_hash)
					except KeyError:
						os.system('clear')
						banner()
						sys.exit(1)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						os.system('clear')
						banner()
						client.sign_in(phone, input('[+] введите код: '))

					os.system('clear')
					banner()
					chats = []
					last_date = None
					chunk_size = 200
					groups=[]

					result = client(GetDialogsRequest(
								 offset_date=last_date,
								 offset_id=0,
								 offset_peer=InputPeerEmpty(),
								 limit=chunk_size,
								 hash = 0
							 ))
					chats.extend(result.chats)

					for chat in chats:
						try:
							if chat.megagroup== True:
								groups.append(chat)
						except:
							continue

					print('[+] Выберите группу, чтобы очистить участников :')
					i=0
					for g in groups:
						print('['+str(i)+']'+' - '+ g.title)
						i+=1

					print('')
					g_index = input("[+] Введите номер : ")
					target_group=groups[int(g_index)]

					print('[+] Выборка участников...')
					time.sleep(1)
					all_participants = []
					all_participants = client.get_participants(target_group, aggressive=True)

					print('[+] Сохранение в файл...')
					time.sleep(1)
					with open("members.csv","w",encoding='UTF-8') as f:
						writer = csv.writer(f,delimiter=",",lineterminator="\n")
						writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
						for user in all_participants:
							if user.username:
								username= user.username
							else:
								username= ""
							if user.first_name:
								first_name= user.first_name
							else:
								first_name= ""
							if user.last_name:
								last_name= user.last_name
							else:
								last_name= ""
							name= (first_name + ' ' + last_name).strip()
							writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
					print('[+] Участники успешно сохранены.')
					backtomenu_option()
		elif santet == "03" or santet == "3":
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
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 0.1
		 Anonimus cicada3301
								""")
			print("\nУстанавливать смс задерку я советую\nУстанавливать не менее 30 сек\n")
			tt = int(input("\nЗадерка между отправкой смс: "))
			SLEEP_TIME = tt

			class main():

				def banner():

					print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 0.1
		 Anonimus cicada3301
								""")

				def send_sms():
					try:
						api = open("API.txt","r")
						api_id = api.read()
						api.close()
						hash = open("hash.txt","r")
						api_hash = hash.read()
						hash.close()
						tel = open("tel.txt","r")
						phone = tel.read()
						tel.close()
						client = TelegramClient(phone, api_id, api_hash)
					except KeyError:
						os.system('clear')
						main.banner()
						sys.exit(1)

					client = TelegramClient(phone, api_id, api_hash)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						os.system('clear')
						main.banner()
						client.sign_in(phone, input('[+] введите код: '))
					os.system('clear')
					main.banner()
					input_file = "members.csv"
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
					print("[1] отправить смс по идентификатору ID\n[2] отправить смс username ")
					mode = int(input("Выбор : "))
					reklama = open("reklama.txt", "r")
					message = reklama.read()
					reklama.close()
					for user in users:
						if mode == 2:
							if user['username'] == "":
								continue
							receiver = client.get_input_entity(user['username'])
						elif mode == 1:
							receiver = InputPeerUser(user['id'],user['access_hash'])
						else:
							print("[!] Неверный режим. Выход.")
							client.disconnect()
							sys.exit()
						try:
							print("[+] Отправка сообщения на:", user['name'])
							client.send_message(receiver, message.format(user['name']))
							print("[+] Ожидание {} секунд".format(SLEEP_TIME))
							time.sleep(SLEEP_TIME)
						except PeerFloodError:
							print("[!] Получение сообщения об ошибке из телеграммы. \n[!] Скрипт останавливается сейчас. \n[!] Пожалуйста, попробуйте еще раз через некоторое время.")
							client.disconnect()
							sys.exit()
						except Exception as e:
							print("[!] ошибка:", e)
							print("[!] Пытаясь продолжить...")
							continue
					client.disconnect()
					print("Выполнено. Сообщение отправлено всем пользователям.")



			main.send_sms()

			backtomenu_option()
		
			restart_program()
	
		elif santet.lower() == "Выход":
			sys.exit()
		else:
			pass

	except(KeyboardInterrupt):
		print("\n[!] Закройте программу...")
		break
	except(EOFError):
		print("\n[!] Закройте программу...")
		break
	except Exception as e:
		print("\n[!] ошибка: "+e)
