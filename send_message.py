import asyncio
from environs import Env
import logging



async def start_listening(host, port):
    while True:
        reader, writer = await asyncio.open_connection(host, port)
        data = await reader.read(1000)
        message = f"[{data.decode()}"
        print(message)

        data = input('Введите сообзение: ')
        writer.write(data.encode('utf-8'))
        await writer.drain()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    env = Env()
    env.read_env()

    host = env("host")
    send_port = env("send_port")
    user_hash = env("user_hash")


    asyncio.run(start_listening(host, send_port))




