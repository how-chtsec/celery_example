from proj.tasks import post_data
from proj.checker import check_iotgoat_default_creds
from celery import chain

url = 'https://10.7.30.17/cgi-bin/luci'

passwords = ['admin','root','password','iotgoathardcodedpassword', '12345678', 'tomcat']
for password in passwords:
    data = {'luci_username': 'root',
            'luci_password': password}
    c = (post_data.s(url, data) | check_iotgoat_default_creds.s().set(queue='checker'))
    c()