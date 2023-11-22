import smtplib
import pathlib
import configparser
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def read():
    file = pathlib.Path(__file__).parents[1].resolve() / 'conf/smtp.ini'
    # 读取ini文件
    conf = configparser.ConfigParser()
    conf.read(file)
    values = dict(conf.items('email_group_1'))
    return values


data = read()
sender = data['sender']
receivers =[]
for r in data['receiver'].split(','):
    receivers.append(r)
receiver = receivers


pass_code = data['pass_code']

conn = smtplib.SMTP('smtp.qq.com', 25)  # 建立邮件连接

test = 'xiongsiyu 测试邮件内容'
content = MIMEText(test, 'plain', 'utf-8')

email = MIMEMultipart()  # 发送的邮件主体

with open('../directory/log.log', 'rb') as file:  # 走网络传输的文件要以bytes格式传输，所以以rb格式读取不会出问题
    att = MIMEText(file.read(), 'base64', 'utf-8')
att.add_header('Content-Type', 'octet-stream')
att.add_header('Content-Disposition', 'attachment', filename='错误日志')  # 自定义附件格式，名称等

email.attach(att)  # 加入附件
email.attach(content)

email_theme = 'xsy测试邮件的主题'
email['Subject'] = Header(email_theme, 'utf-8')

# 发件人和收件人
email['From'] = sender
email['To'] = str(receiver)

# 发送邮件操作，利用建立起来的连接

conn.login(sender, pass_code)
conn.sendmail(sender, receiver, email.as_string())
conn.close()
