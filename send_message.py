import asyncio
import json
import logging

from environs import Env

from settings import create_parser

log = logging.getLogger(__file__)


async def get_data(reader):
    data = await reader.readline()
    log.debug(f"Получили: {data.decode()}")
    return data.decode()


async def send_message(writer, message):
    writer.write(f'{message}\n\n'.encode())
    await writer.drain()


async def authorise(reader, writer, token):
    await get_data(reader)
    await send_message(writer, token)
    login_data = await get_data(reader)
    return json.loads(login_data.encode())


async def register(writer, reader, nick_name):
    await get_data(reader)
    writer.write(f'\n'.encode())
    await writer.drain()
    await get_data(reader)
    writer.write(f'{nick_name}\n'.encode())
    register_data = await get_data(reader)
    response = json.loads(register_data.encode())
    log.debug(json.loads(register_data.encode()))
    writer.close()
    return response


async def submit_message(writer):
    while True:
        message = input("Введите сообщение: ")
        await send_message(writer, message)


async def start_server(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    hello_message = input("Зарегистрироваться?")
    say_yes = ["y", "Y", "yes", "Yes", "д", "Да", "Д"]

    if hello_message in say_yes:
        nick_name = input("Введите имя пользователя: ")
        register_data = await register(writer, reader, nick_name)
        if register_data:
            reader, writer = await asyncio.open_connection(host, port)
            await authorise(reader, writer, register_data['account_hash'])
            await submit_message(writer)
    else:
        token = input("Введите свой токен: ")
        login_data = await authorise(reader, writer, token)
        if login_data:
            await submit_message(writer)
        else:
            log.error(f"Неуспешная авторизация")


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s', level=logging.WARNING)
    env = Env()
    env.read_env()

    host = env("HOST")
    port_send = env("WRITE_PORT")
    token = env("TOKEN")

    parser = create_parser()
    args = parser.parse_args()
    if args.host and args.port and args.history:
        asyncio.run(start_server(args.host, args.port_send))
    else:
        asyncio.run(start_server(host, port_send))
