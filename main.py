# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from Function_contact import def_Readfunction

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    b = def_Readfunction.WriteFunction('./directory/test.txt', '写入一点内容')
    b.for_use()
    a = def_Readfunction.ReadFunction('./directory/test.txt')
    a.for_use()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
