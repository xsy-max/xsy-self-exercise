import psycopg2
import pymysql


sql = 'select * from city where %s'

try:
    connection = pymysql.connect(
        host="localhost",
        database="world",
        user="root",
        password="xsy614XSY"
    )
    cursor = connection.cursor()

    # 执行数据库操作
    # 例如，执行SQL查询或插入数据

except (Exception, pymysql.Error) as error:
    print("Error while connecting to mysql:", error)

finally:
    if connection:
        c_code = input('输入流程需求select * from city where ')
        cursor.execute(sql , (c_code))
        result = cursor.fetchall()
        for i in result:
            print(i)
        # 查询不需要提交
        # 但是增删改需要对业务进行commit
        # connection.commit() 此处使得修改生效
        # connection.rollback() 撤销之前的操作

        cursor.close()
        connection.close()
        print("mysql connection is closed")