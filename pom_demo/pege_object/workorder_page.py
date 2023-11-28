from pom_demo.BaseObject import base_demo


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