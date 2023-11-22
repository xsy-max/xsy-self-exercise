import configparser
import pathlib


def read():
    file = pathlib.Path(__file__).parents[1].resolve() / 'conf/smtp.ini'
    # 读取ini文件
    conf = configparser.ConfigParser()
    conf.read(file)
    values = dict(conf.items('email_group_2'))
    print(values)

read()

