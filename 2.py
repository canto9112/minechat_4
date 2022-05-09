import asyncio

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('minechat.dvmn.org', 5050)

    data = await reader.read(100)
    print(f'Отправил: {data.decode()!r}')
    return data.decode()



    # writer.close()


asyncio.run(tcp_echo_client())