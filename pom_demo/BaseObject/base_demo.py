from time import sleep
import traceback


class BaseDemo:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open(self, url):
        self.driver.get(url)

    def location(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        xsy = self.location(loc)
        xsy.clear()
        xsy.send_keys(txt)

    def click(self, loc):
        xsy = self.location(loc)
        xsy.click()

    def quit(self):
        self.driver.quit()

    def wait(self, time):
        sleep(int(time))

    # 文本断言
    def assert_in(self, expected, loc):
        try:
            reality = self.location(loc).text
            assert expected in reality, f'''
                断言失败：
                    expected：{expected}
                    reality：{reality}
                    expected != reality
            '''
            return True
        except:
            traceback.print_exc()
            return False
