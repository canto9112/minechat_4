import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Подключаемся к подпольному чату Minecraft')
    parser.add_argument('--host', help='host', type=str, default="minechat.dvmn.org")
    parser.add_argument('--port', help='port', type=int, default=5000)
    parser.add_argument('--port_send', help='port_send', type=int, default=5050)
    parser.add_argument('--history', help='history', type=str, default="logfile.log")
    parser.add_argument('--token', help='token', type=str, default="fb91c77c-d001-11ec-8c47-0242ac110002")
    return parser