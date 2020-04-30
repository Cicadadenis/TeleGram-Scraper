
---

## • Настройка API
* Зайдите на http://my.telegram.org и войдите в систему.
* Нажмите на инструменты разработки API и заполните необходимые поля.
* введите название нужного вам приложения и выберите другое в платформе. Пример:
* скопируйте «api_id» и «api_hash» после нажатия кнопки «создать приложение» (будет использоваться в setup.py)

## • Как установить и использовать

`$ pkg install -y git python`

`$ git clone https://github.com/bednakovdenis/TeleGram-Scraper.git

`$ cd TeleGram-Scraper`

* Install requierments

`$ python3 setup.py -i`

* настроить файл конфигурации (apiID, apiHASH)

`$ python3 setup.py -c`

* Создать пользовательские данные

`$ python3 scraper.py`

* (members.csv используется по умолчанию, если вы изменили имя, используйте его)
* Отправить смс на собранные данные

`$ python3 smsbot.py members.csv`

* Инструмент обновления

`$ python3 setup.py -u`

---
