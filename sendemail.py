from email.mime.text import MIMEText
import smtplib
msg = MIMEText('你好谭谭，明天有空吗', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = r'15252570034@163.com'
password = r'beautiful11'
# 输入收件人地址:
to_addr = r'1412680345@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'


server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
