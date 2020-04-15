import server
import argparse
import logging
import sys


def set_logger(address: str, port: int, logger, level) -> None:
    """
    Set logger for project
    """
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter(f'%(levelname)s - {address}:{port} - %(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def arg_parser() -> tuple:
    """
    The function parses cmd arguments. If there are no arguments, it uses the default values.
    :return: tuple from address and port
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store', dest='address', type=str, default='0.0.0.0', help='Server address')
    parser.add_argument('-p', action='store', dest='port', type=int, default=8000, help='Server port')
    parser.add_argument('-l', action='store', dest='log_number', type=int, default=1, help='Log level 0-2')
    args = parser.parse_args()
    arg_address = args.address
    arg_port = args.port
    arg_log_number = args.log_number
    return arg_address, arg_port, arg_log_number


def get_log_level(number):
    log_level_dict = {
        0: logging.DEBUG,
        1: logging.INFO,
        2: logging.ERROR
    }
    return log_level_dict.get(number, logging.INFO)


if __name__ == '__main__':
    srv_address, srv_port, log_number = arg_parser()
    log_level = get_log_level(log_number)
    root_logger = logging.getLogger()
    set_logger(srv_address, srv_port, root_logger, log_level)
    root_logger.info('Starting server')
    server.run(srv_address, srv_port)
