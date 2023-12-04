import os
import pytest
import yaml
import pathlib
from pom_demo.pege_object import login_page
from pom_demo.pege_object import Home_page
from selenium import webdriver
import allure

filepath = pathlib.Path(__file__)
Project_Root_Path = filepath.parents[2].resolve()


class test_case:
    @allure.epic('实现生成工单业务流程等一系列操作')
    @allure.title('测试标题：工单业务创建')
    @allure.description('这是描述')
    # @pytest.mark.login_setuser
    @pytest.mark.parametrize('users', 'admin')
    @pytest.mark.parametrize('pwd', '123456')
    def test_workflow(self, users, pwd):
        try:
            # print(data['username'])
            edge = webdriver.Edge()
            lg = login_page.LoginPage(edge)
            lg.login(self, user=users, pwd=pwd)
            lg2 = Home_page(edge)
        except:
            with open('../temp/生成工单业务流程.png', 'wb') as file:
                file.write(edge.get_screenshot_as_png())
            raise


if __name__ == "__mian__":
    pytest.main(['-sv', './test_pytest_login'])
    os.system('allure generate ./report_allure -o ./report --clean')
