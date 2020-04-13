import server
import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', type=str, help='Address for port listening')
    parser.add_argument('port', type=int, help='Port for server')
    args = parser.parse_args()
    return args.address, args.port


if __name__ == '__main__':
    params = arg_parser()
    server.run(*params)
