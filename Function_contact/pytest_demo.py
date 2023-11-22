import pytest


class Test_xsy:
    def test_function(self):
        print(f'这是个测试用力内容')


if __name__ == '__main__':
    pytest.main('-s', '-v')
    # 此处 -s -v 是为了，展示print内容在cmd处
