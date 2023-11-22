# 定义用户数据
user_data = {
    'user1': {'username': 'admin', 'password': '123456'},
    'user2': {'username': 'admin2', 'password': '1234567'}
}

# 获取每个用户的数据
user1_data = user_data.get('user1')
user2_data = user_data.get('user2', {})

# 打印用户数据
print("User1 data:", user1_data)
print("User1name data:", user1_data.get("username"))

print("User2 data:", user2_data)
