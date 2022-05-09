import asyncio
import datetime
import argparse
from environs import Env
import logging

log = logging.getLogger(__file__)
handler = logging.FileHandler('logfile.log')
log.addHandler(handler)

def create_parser():
    parser = argparse.ArgumentParser(description='Подключаемся к подпольному чату Minecraft')
    parser.add_argument('--host', help='host', type=str)
    parser.add_argument('--port', help='port', type=int)
    parser.add_argument( '--history', help='history', type=str)
    return parser

async def start_listening(host, port, history):
    while True:
        reader, writer = await asyncio.open_connection(host, port)
        date = datetime.datetime.now()
        formatted_date = date.strftime("%d.%m.%Y %H:%M")

        data = await reader.read(1000)
        message = f"[{formatted_date}] {data.decode()}"

        log.info(message)
        with open(history,"a") as f:
            f.write(message)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    env = Env()
    env.read_env()

    host = env("host")
    port = env("port")
    history = env("history")

    parser = create_parser()
    args = parser.parse_args()
    if args.host and args.port and args.history:
        asyncio.run(start_listening(args.host, args.port, args.history))
    else:
        asyncio.run(start_listening(host, port, history))