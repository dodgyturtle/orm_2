#  Пульт охраны труда
 Отображает сотрудников:
 - С активными картами доступа.
 - Находящимися в хранилище на дату и время запроса.
 - Список посещения хранилища. Если длительность прибывания в хранилища более 60 минут, выставляется флаг "подозрительности".

### Установка
- Скачать скрипт с [GitHub](https://github.com/dumbturtle/orm_2).

- Переименовать `env_template` в `.env`. В файле `.env` необходимо указать настройки для подключения к базе данных. Более подробно смотрите раздел [Настройки](#настройки).


- Установить необходимые пакеты: 
     
```
$ pip install -r requirements.txt
```
- Запустить:
```
$ python manage.py runserver 0.0.0.0:8000
``` 
#### Настройки
Необходимо указать в файле `.env` параметры подключения к базе данных, секретный ключ для корректной работы Django. Так же в случае необходимости можно включить вывод отладочной информации присвоив значение `True` переменной `DJANGO_DEBUG`.
Для переменной `DJANGO_ALLOWED_HOSTS` укажите адрес своего сайта.

```
#Database Settings
DATABASE_HOST="Your Host"
DATABASE_PORT="DataBase Port"
DATABASE_NAME="DataBase Name"
DATABASE_USER="DataBase Username"
DATABASE_PASSWORD="DataBase Password"

#Django Settings
DJANGO_DEBUG=False
DJANGO_SECRET_KEY="REPLACE_ME"
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```