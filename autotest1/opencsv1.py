import csv
date=csv.reader(open('D:\\test.csv', 'r'))
#date=csv.reader(open('D:\\test.csv', 'r',encoding='utf8',newline=''))


for user in date:
    print(user)
