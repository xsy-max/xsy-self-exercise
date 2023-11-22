import datetime


class ReadFunction():
    def __init__(self, location):
        self.location = location
        print(f'调用了读取类')

    # def read_fuction(loction,mode):
    #     '''
    #
    #     :param loction: 传入文件的地址
    #     :param mode:
    #      a在后面接着写
    #     r读取
    #     w写入
    #     rb读取非文本文件
    #     wb写入非文本文件
    #     r+可以又读又写
    #     :return:
    #     '''
    #
    def for_use(self):
        text = open(file=self.location, mode='r', encoding="utf-8")
        readline = text.readline()
        print(readline)
        text.close()


class WriteFunction():
    def __init__(self, location, text):
        self.location = location
        self.text = text
        print(f'调用了写入类,写入对象是{text}')

    def for_use(self):
        file = open(file=self.location, mode='a', encoding='utf-8')
        file.write(f'\n{datetime.datetime.now()} 这里是时间 {self.text}  写入内容')
        file.close()
        file2 = open(file=self.location, mode='r', encoding='utf-8')
        print(f'现在的文本内容如下 \n\n{file2.read()}')
