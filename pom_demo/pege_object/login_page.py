from pom_demo.BaseObject import base_demo
from selenium import webdriver

'''
这里的操作是登录，如果有别的操作后面再加
'''
class LoginPage(base_demo.BaseDemo):
    url = 'https://mspopsdev.linkyoyo.com.cn/login'
    username = ('name', 'username')
    password = ('name', 'password')
    button = ('xpath', '//*[@class = "el-button el-button--primary el-button--mini"]')

    def login(self, user, pwd):
        self.open(self.url)
        self.input(self.username, user)
        self.input(self.password, pwd)
        self.click(self.button)


# if __name__ =='__main__':
#     Edge = webdriver.Edge()
#     lg = LoginPage(Edge)
#     lg.login('admin','123456')
