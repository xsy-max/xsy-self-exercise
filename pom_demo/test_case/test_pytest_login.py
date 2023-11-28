import os
import pytest
import yaml
import pathlib
from pom_demo.pege_object import login_page
from selenium import webdriver
import allure

filepath = pathlib.Path(__file__)
Project_Root_Path = filepath.parents[2].resolve()


class TestWorkFlow01:
    @allure.epic('实现生成工单业务流程')
    @pytest.mark.login_setuser1
    @pytest.mark.parametrize('users', 'admin')
    @pytest.mark.parametrize('pwd', '123456')
    def test_workflow(self, users, pwd):
        # print(data['username'])
        edge = webdriver.Edge()
        lg = login_page.LoginPage(edge)
        lg.login(self, user=users, pwd=pwd)



if __name__ == "__mian__":
    pytest.main(['-sv', './test_pytest_login'])
    os.system('allure generate ./report_allure -o ./')
