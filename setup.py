#!/usr/dev/python3
#Bednakov-Xack-Live
#2020/01/05

"""

Вы можете повторно запустить setup.py
если вы добавили неправильное значение

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time

def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' this may take some time ...')
		os.system("""
			pip3 установить cython numpy pandas
			python3 -m pip установить cython numpy pandas
			""")
	banner()
	print(gr+'['+cy+'+'+gr+']'+cy+' установка csv merge займет до 10 минут.')
	input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' Вы хотите включить CSV слияния (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(gr+"[+] Установка требований ...")
	os.system("""
		pip3 установить telethon запросы configparser
		python3 -m pip установить запросы на telethon configparser
		коснитесь config.data
		""")
	banner()
	print(gr+"[+] Установленные требования.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(gr+"[+] Ввести api ID : "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(gr+"[+] Ввести hash ID : "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(gr+"[+] введите номер телефона: "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"[+] настройка завершена!")

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(gr+'['+cy+'+'+gr+']'+cy+' merging '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(gr+'['+cy+'+'+gr+']'+cy+' big files can take some time ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'['+cy+'+'+gr+']'+cy+' сохраненный файл как "output.csv"\n')

def update_tool():
	import requests as r
	banner()
	source = r.get("")
	if source.text == '3':
		print(gr+'['+cy+'+'+gr+']'+cy+' уже последняя версия')
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' удаление старых файлов ...')
		os.system('rm *.py');time.sleep(3)
		print(gr+'['+cy+'+'+gr+']'+cy+' получать последние файлы ...')
		os.system("""
			curl -s -O https://github.com/bednakovdenis/TeleGram-Scraper/blob/master/config.data
			curl -s -O https://github.com/bednakovdenis/TeleGram-Scraper/blob/master/scraper.py
			curl -s -O https://github.com/bednakovdenis/TeleGram-Scraper/blob/master/smsbot.py
			curl -s -O https://github.com/bednakovdenis/TeleGram-Scraper/blob/master/setup.py
			chmod 777 *.py
			""");time.sleep(3)
		print(gr+'\n['+cy+'+'+gr+']'+cy+' обновление завершено.\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(gr+'['+cy+'+'+gr+']'+cy+' выбранный модуль : '+re+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(gr+'['+cy+'+'+gr+']'+cy+' выбранный модуль : '+re+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(gr+'['+cy+'+'+gr+']'+cy+' выбранный модуль : '+re+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""$ python3 setup.py -m file1.csv file2.csv

	( --config  / -c ) настройка api-конфигурации
	( --merge   / -m ) объединить 2 файла .csv в один
	( --update  / -u ) обновить инструмент до последней версии
	( --install / -i ) установить требования
	( --help    / -h ) показать это сообщение
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' неизвестный аргумент : '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' для использования помощи : ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' аргумент не указан : '+ sys.argv[1])
	print(gr+'['+re+'!'+gr+']'+cy+' для использования помощи : ')
	print(gr+'['+re+'!'+gr+']'+cy+' https://github.com/bednakovdenis/TeleGram-Scraper')
	print(gr+'$ python3 setup.py -h'+'\n')
