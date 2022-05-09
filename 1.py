import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(1000)
    message = data.decode()

    print(f"Получил: {message!r}")

    writer.write(data)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())