## Bednakov-Xack-Live
# -*- coding: utf-8 -*-
# Бедняков Денис Леонидович
# GitHub http://github.com/bednakovdenis
import sys, time, socket, random, requests
import time
from os import system
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils
import os
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
	backtomenu = input("Ваш Выбор > ")

	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nОШИБКА: неверный ввод")
		time.sleep(1)
		restart_program()



def get_tor_session():
    session = requests.session()

    session.proxies = {'http':  'socks5://127.0.0.1:9150',
                       'https': 'socks5://127.0.0.1:9150'}
    return session


session = get_tor_session()


addd = requests.get("http://httpbin.org/ip").text



print("\n       Подключение через Тор , Ваш IP Адрес ", addd)
time.sleep(2)


print("""


  Выберите из меню:

	01) Подключить К Удаленному серверу для шифрования

	02) Подключить Акаунт Telegram

	03) Создать список Username из Групп

	04) Свой список расылки 
	
	00) Очистеть свой список 

	05) Рассылка спама по списку username

	06) Рассылка спама по Своему списку Username

	07) Рассылка по id группы или username

	08) Набивка Группы

	09) Текст для Рассылки

        _____________________________________________
       |                                             |
       |   Для связи со Мной в Telegram: Satanasat   |
       |_____________________________________________|
""")
while True:
	try:
		santet = input("Ваш Выбор > ")

		if santet == "01" or santet == "1":
			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty
			import os, sys
			import configparser
			import csv
			import time
			tel = open("tel.txt","w")
			tel.write(input("\nВведите Номер Телефона: "))
			tel.close()
			webbrowser.open("https://my.telegram.org/", new=2)
			api = open("API.txt","w")
			api.write(input("\nВведите API ID: "))
			api.close()
			hash = open("hash.txt","w")
			hash.write(input("\nВведите HASH ID: "))
			hash.close()





			def banner():
				print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 18
		 Anonimus cicada3301
								""")

			cpass = configparser.RawConfigParser()


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
				banner()
				sys.exit(1)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				banner()
				client.sign_in(phone, input('[+] введите код из смс: '))

			restart_program()

		elif santet == "09" or santet == "9":

			wer = open("reklama.txt", "w")
			wer.write(input("\nВведите СМС Для рассылки \nТекст смс будет сохранет до следущей перезаписи его: "))
			wer.close()
                
			restart_program()

		elif santet == "04" or santet == "4":
			sp = open("members2.csv", "a", encoding='UTF-8')
			sp.write(input('\nДобавить Username к списку: ') + '\n')
			sp.close()
			
                       


			restart_program()
			
			
			
		elif santet == "00" or santet == "0":
			ty = open("members2.csv", "w", encoding='UTF-8')
			

			restart_program()
		elif santet == "03" or santet == "3":
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




					def banner():
						print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 18
		 Anonimus cicada3301
								""")

					cpass = configparser.RawConfigParser()


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
						banner()
						sys.exit(1)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						banner()
						client.sign_in(phone, input('[+] введите код из смс: '))

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

					print('[+] Выберите группу, чтобы спиздить участников :')
					i=0
					for g in groups:
						print('['+str(i)+']'+' - '+ g.title)
						i+=1

					print('')
					g_index = input("[+] Введите номер : ")
					target_group=groups[int(g_index)]

					print('[+] Выборка участников...')
					time.sleep(2.5)
					all_participants = []
					all_participants = client.get_participants(target_group, aggressive=True)

					print('[+] Сохранение в файл...')
					time.sleep(2)
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
                                                        
							print('['+str(i)+']'+' - '+ username.title)
                                                        i+=1
                                                        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
                                                        
					print('[+] Участники успешно сохранены.')
					restart_program()

		elif santet == "05" or santet == "5":
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
			my_list = []




			print("\nУстанавливать смс задерку между отправкой смс \n")
			tt = int(input("\nЗадерка между отправкой смс: "))
			SLEEP_TIME = tt

			class main():

				def banner():

					print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 18
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
						main.banner()
						sys.exit(1)

					client = TelegramClient(phone, api_id, api_hash)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						main.banner()
						client.sign_in(phone, input('[+] введите код из смс: '))
					main.banner()


					input_file = "members2.csv"
					users = []
					with open(input_file, encoding='UTF-8') as f:
						rows = csv.reader(f,delimiter=",",lineterminator="\n")
						next(rows, None)
						for row in rows:
							user = {}
							user['username'] = row[0]
							#user['id'] = int(row[1])
							#user['access_hash'] = int(row[2])
							#user['name'] = row[3]
							users.append(user)
					#print("[1] отправить смс по идентификатору ID\n[2] отправить смс username ")
					mode = 2
					reklama = open('reklama.txt', "r")
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
							print("[+] Отправка сообщения на:", user['username'])
							client.send_message(receiver, message.format(user['username']))
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

			restart_program()
		elif santet == "06" or santet == "6":
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

			print("\nУстанавливать смс задерку я советую\nУстанавливать не менее 30 сек\n")
			tt = int(input("\nЗадерка между отправкой смс: "))
			SLEEP_TIME = tt

			class main():

				def banner():

					print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 18
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
						main.banner()
						sys.exit(1)

					client = TelegramClient(phone, api_id, api_hash)

					client.connect()
					if not client.is_user_authorized():
						client.send_code_request(phone)
						main.banner()
						client.sign_in(phone, input('[+] введите код из смс: '))
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
					#print("[1] отправить смс по идентификатору ID\n[2] отправить смс username ")
					mode = 2
					reklama = open('reklama.txt', "r")
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
							print("[+] Отправка сообщения на:", user['username'])
							client.send_message(receiver, message.format(user['username']))
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

			restart_program()
		elif santet == "07" or santet == "7":
			import time
			api = open("API.txt","r")
			api_id = api.read()
			api.close()
			hash = open("hash.txt","r")
			api_hash = hash.read()
			hash.close()
			#api_id = 1148490
			#api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			tel = open("tel.txt","r")
			phone = tel.read()
			tel.close()
			client = TelegramClient(phone, api_id, api_hash)
			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				main.banner()
				client.sign_in(phone, input('[+] введите код: '))
			#client = TelegramClient('client',phone,api_id,api_hash).start()
			target = input("\nCicada3301 > установить USERNAME/ID ")
			try: count = int(input("\nCicada3301 > установить Значение(шт) "))
			except(ValueError): count = 100
			rek = open("reklama.txt", "r")
			urmsg = rek.read()
			rek.close()
			for x in range(count):

				client.send_message(target, urmsg)
				sys.stdout.write(u"\u001b[1000D[*] Отправлено {} сообщения для {}...".format(x+1, target))
				sys.stdout.flush()
			print("\n[!] Выполнено ... !!\n")
			restart_program()

		elif santet == "02" or santet == "2":
			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty
			import os, sys
			import configparser
			import csv
			import time
			tel = open("tel.txt","w")
			tel.write(input("\nВведите Номер Телефона: "))
			tel.close()




			def banner():
				print(f"""
	╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
	 ║ ├┤ │  ├┤ ║ ╦  ╚═╗│  ├┬┘├─┤├─┘├┤ ├┬┘
	 ╩ └─┘┴─┘└─┘╚═╝  ╚═╝└─┘┴└─┴ ┴┴  └─┘┴└─

			version : 18
		 Anonimus cicada3301
								""")

			cpass = configparser.RawConfigParser()


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
				banner()
				sys.exit(1)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				banner()
				client.sign_in(phone, input('[+] введите код из смс: '))

			restart_program()



		elif santet == "08" or santet == "8":

			from telethon.sync import TelegramClient
			from telethon.tl.functions.messages import GetDialogsRequest
			from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
			from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
			from telethon.tl.functions.channels import InviteToChannelRequest
			import sys
			import csv
			import traceback
			import time
			api = open("API.txt","r")
			api_id = api.read()
			api.close()
			hash = open("hash.txt","r")
			api_hash = hash.read()
			hash.close()
			#api_id = 1148490
			#api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			tel = open("tel.txt","r")
			phone = tel.read()
			tel.close()
			#ddd = int(input("\nЗадержка: "))
			#api_id = '1353967'
			#api_hash = '12520790aa605f218215a2f742cbec09'
			#phone = '+22565440130'
			client = TelegramClient(phone, api_id, api_hash)

			client.connect()
			if not client.is_user_authorized():
				client.send_code_request(phone)
				client.sign_in(phone, input('введите код из смс: '))

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

			print('Выберите группу для добавления участников:')
			i=0
			for group in groups:
				print(str(i) + '- ' + group.title)
				i+=1

			g_index = input("Введите номер: ")
			target_group=groups[int(g_index)]

			target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

			mode = int(input("Введите 1 для добавления по имени пользователя или 2 для добавления по идентификатору: "))

			for user in users:
				try:
					print ("Adding {}".format(user['id']))
					if mode == 1:
						if user['username'] == "":
							continue
						user_to_add = client.get_input_entity(user['username'])
					elif mode == 2:
						user_to_add = InputPeerUser(user['id'], user['access_hash'])
					else:
						sys.exit("Invalid Mode Selected. Please Try Again.")
					client(InviteToChannelRequest(target_group_entity,[user_to_add]))
					#print("Waiting", ddd, " Seconds...")
					time.sleep(random.randint(15, 100))
				except PeerFloodError:
					print("Получение сообщения об ошибке из телеграммы. Скрипт останавливается сейчас. Пожалуйста, попробуйте еще раз через некоторое время.")
				except UserPrivacyRestrictedError:
					print("Настройки конфиденциальности пользователя не позволяют вам сделать это. Пропуская.")
				except:
					traceback.print_exc()
					print("Непредвиденная ошибка")
					continue

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
