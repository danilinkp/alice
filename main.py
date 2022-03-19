import logging
import requests

logging.basicConfig(filename='example.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


def log_to_file():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1


if __name__ == '__main__':
    logging.info('start script')
    log_to_file()
    requests.get('https://ya.ru')
    logging.info('end script')