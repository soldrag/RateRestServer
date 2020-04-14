import server
import argparse


def arg_parser() -> tuple:
    default_address = '127.0.0.1'
    default_port = 8000
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store', dest='address', type=str, default='127.0.0.1', help='Server address')
    parser.add_argument('-p', action='store', dest='port', type=int, default=8000, help='Server port')
    args = parser.parse_args()
    address = args.address if args.address else default_address
    port = args.port if args.port else default_port
    return address, port


if __name__ == '__main__':
    srv_address, srv_port = arg_parser()
    server.run(srv_address, srv_port)
