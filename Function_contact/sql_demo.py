import psycopg2
import configparser
import pathlib
import pgdb


try:

    file = pathlib.Path(__file__).parents[1].resolve() / 'conf/sql.ini'
    # 读取ini文件
    conf = configparser.ConfigParser()
    conf.read(file)
    values = dict(conf.items('pgsql_conf'))
    print(values)
    connection = psycopg2.connect(**values)
    cursor = connection.cursor()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
