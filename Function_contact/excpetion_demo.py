str_01 = '张三是个邪恶印度人'
import datetime

class xsy_exception(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        print(f'自定义报错信息{self.info}')

    # def __


'''
    file = open(file='xxx', encoding='xxxx', mode='r')
    file.read   这里会把文件全部内容一次性读取，比较消耗空间
    file.readline 会有光标，每次读一行记录位置，会记住读取到的位置，读了一行之后会移动到后面
    file.readlines 把文件的作为list内容读取
    以上是读的情况,w，覆盖
    a在后面接着写
    file.write()
    操作非文本文件 mode使用wb，或者rb
    
    操作文件之后一定需要关闭该文件，释放空间，省的别的代码死锁。
    两个只读不会死锁，但是读文件还是要在使用文件后关闭，因为不知道这个文件会不会被写入，从而导致死锁
    可以调用 with open 使其自动帮你关闭文件
    
'''
with open(file='../directory/error.txt', encoding='utf-8', mode='r+') as readline_demo02:
    readline_demo02.write(f'\n{datetime.datetime.now()}  熊思宇')
    print(readline_demo02.readline())

readline_demo = open(file='../directory/new.txt', encoding='utf-8')
print(readline_demo.readline())
if readline_demo != str_01:
    try:
        print(f'输入的没有问题，输入内容是{str_01}')
        raise xsy_exception('空')
    except:
        raise xsy_exception(readline_demo.readline())

        readline_demo.close()
