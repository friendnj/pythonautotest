from xml.dom import minidom
dom=minidom.parse('info.XML')

root=dom.documentElement


logins=root.getElementsByTagName('login')
username=logins[0].getAttribute("username")
print(username)

password=logins[0].getAttribute("password")
print(password)

