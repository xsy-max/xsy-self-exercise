from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get('https://mspopsdev.linkyoyo.com.cn/login')  #在测试的过程众发现get会自动等待页面加载成功
sleep(2)
usr = driver.find_element(by='name', value='username')
usr.clear()
usr.send_keys('admin')
pwd = driver.find_element(by='name', value='password')
pwd.clear()
pwd.send_keys('123456')
sleep(2)
driver.find_element(by='xpath', value="//*[@class='el-button el-button--primary el-button--mini']").click()
