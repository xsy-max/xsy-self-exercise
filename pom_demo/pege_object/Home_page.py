from pom_demo.BaseObject import base_demo
from selenium import webdriver
from pom_demo.pege_object import login_page
from time import sleep
'''
这里的操作是跳转到别的界面
思路 读取yaml文件  yaml文件里存在 跳转至不同页面的button的xpath  干脆就直接放在这里得了  根据跳转的需求
输入对应下标 跳转到想去的界面
'''


class HomePage(base_demo.BaseDemo):
    url = 'https://mspopsdev.linkyoyo.com.cn/hcmsp-bill-aws/#/dashboard'
    main_button = ('xpath', '//*[@class="service el-tooltip__trigger el-tooltip__trigger"]')
    button_list = [('xpath', '//div[contains(text(),"系统设置管理")]'),
                   ('xpath', '//div[contains(text(),"平台审计")]'),
                   ('xpath', '//div[contains(text(),"MSP工单")]')]  # 这个地方如果需要新增跳转点，就需要复制模块

    def jumpto_workorder(self):
        self.open(self.url)
        self.click(self.main_button)
        self.click(self.button_list[2])

    def jumpto_systemsetting(self):
        self.open(self.url)
        self.click(self.main_button)
        self.click(self.button_list[0])

# if __name__ =='__main__':
#     Edge = webdriver.Edge()
#     lg = login_page.LoginPage(Edge)
#     lg.login('admin','123456')
#     lg2 = HomePage(Edge)
#     lg2.jumpto_systemsetting()
#     sleep(2)
