# pytest 存在默认格式 测试的文件需要以 test_*。py开头 并且 类和用例需要以test开头
from logging import getLogger
import traceback
import pytest
import Function_contact.getLogger
from Function_contact.getLogger import getLogger

logger = getLogger()


class Test_xiongsiyu:
    try:
        def test_login_username(self):
            print('登录流程用户名')

        def test_login_password(self):
            print('登录流程密码')
    except:
        raise logger.error(traceback.format_exc())


if __name__ == '__main__':
    pytest.main(['-v'])
