# Асинхронный чат

Скрипт для подключения к чату.

## Установка

```bash
>> git clone https://github.com/NeverDieOne/async_minechat.git
>> cd async_minechat
>> python -m venv venv
>> source venv/bin/activate
>> pip install -r requirements.txt
```

## Пример запуска

### Чтение чата:

Необходимые параметры:
* `host` - хост для подключения
* `port` - порт для подключения
* `history` - файл, в который будет выведен результат

```bash
python listen-minechat.py --host minechat.dvmn.org --port 5000 --history logfile.log
```

### Отправка сообщения в чат:

Опциональные параметры:
* `host` - хост для подключения
* `port` - порт для подключения
* `token` - токен, необходимый для подключения
    
```bash
python write-minechat.py --host minechat.dvmn.org --port 5050 --text Hello
```

## <Опционально> `.env`
Так же можно создать файл `.env` и положить в него все необходимые аргументы.

Возможные переменные `.env`:

`HOST`,
`LISTEN_PORT`,
`WRITE_PORT`,
`HISTORY`,
`TOKEN`,

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org/modules)