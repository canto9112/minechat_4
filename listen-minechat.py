import asyncio
import datetime
import logging

import aiofiles
from environs import Env

from settings import create_parser

log = logging.getLogger(__file__)


async def start_listening(host, port, history):

    while True:
        try:
            reader, writer = await asyncio.open_connection(host, port)
            date = datetime.datetime.now()
            formatted_date = date.strftime("%d.%m.%Y %H:%M")

            data = await reader.read(1000)
            message = f"[{formatted_date}] {data.decode()}"
            log.info(message)

            async with aiofiles.open(history, mode="a") as file:
                await file.write(message)
        except TimeoutError:
            log.error("Пропало соединение с сетью")


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s',
                        level=logging.INFO)
    env = Env()
    env.read_env()

    host = env("HOST")
    port = env("LISTEN_PORT")
    history = env("HISTORY")

    parser = create_parser()
    args = parser.parse_args()

    if args.host and args.port and args.history:
        asyncio.run(start_listening(args.host, args.port, args.history))
    else:
        asyncio.run(start_listening(host, port, history))