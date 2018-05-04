import logging


def log(exception, ca_log):
    logging.basicConfig(filename='.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f'Exception type: {exception} : {ca_log}')

    if exception == 'KeyError':
        err = 'Bad request'
    elif exception == 'IndexError':
        err = 'Bad syntax'
    elif exception == 'JSONDecodeError':
        err = 'Ticker not found'
    else:
        err = f'An exception occured [E: {exception}]'

    return err


