import logging.config
import pathlib

filepath = pathlib.Path(__file__)
file = filepath.parents[1].resolve()
path = file / 'conf/log.ini'


def getLogger():
    logging.config.fileConfig(path, encoding='utf-8')
    log = logging.getLogger()
    return log
