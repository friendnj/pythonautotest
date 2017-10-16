import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.sina.com'
user='testnj2017@sina.com'
password='testnj2017'

sender='testnj2017@sina.com'
receiver='810455341@qq.com'
subject='Python email test'

msg=MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')



smtp=smtplib.SMTP()
smtp.connect(smtpserver,25)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()