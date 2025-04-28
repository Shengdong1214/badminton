import requests
import datetime
import threading
import time

'''
			       1号场	2号场	3号场	4号场
	时间编号		场地编号	
12:00	1809		1568	1576	1584	1592
13:00	1810		1567	1575	1583	1591
14:00	1811		1566	1574	1582	1590
15:00	1812		1565	1573	1581	1589
16:00	1813		1564	1572	1580	1588
17:00	1814		1563	1571	1579	1587
18:00	1815		1562	1570	1578	1586
19:00	1816		1561	1569	1577	1585

'''

cookies = {
    "CASTGC": "TGT-000000-bS8pUVgHL5xJh-Clz5H5JUAThj9slEHyA4NYyKCl8QjhYUQm1gDbNUi5YoNlfQthiD0e4baddbe7695",
    "PHPSESSID": "ST-0000000-uO-auvf1bg8eU1XVwHHJ-o6oyd8e4baddbe7695",
    "vjuid": "000000",
    "vjvd": "00000054ee794bbb4d480527bd6e171d",
    "vt": "000000"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Referer": "https://ehall.bjut.edu.cn/v2/reserve/reserveDetail?id=56",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept": "application/json, text/plain, */*"
}

data1 = ('resource_id=56&code=&remarks=&deduct_num=&data=%5B%7B%22date%22%3A%222025-05-02%22%2C%22period%22%3A1815%2C%22sub_resource_id%22%3A1562%7D%5D&position_data=')
data2 = ('resource_id=56&code=&remarks=&deduct_num=&data=%5B%7B%22date%22%3A%222025-05-02%22%2C%22period%22%3A1816%2C%22sub_resource_id%22%3A1561%7D%5D&position_data=')
data_list = [data1, data2]
url = "https://ehall.bjut.edu.cn/site/reservation/launch"

def send_request(data):
    session.post(url, data=data)

def yuyue_all():
    threads = []
    for data in data_list:
        t = threading.Thread(target=send_request, args=(data,))
        threads.append(t)
        t.start()
        time.sleep(0.05)
'''
now = datetime.datetime.now()
target_time = now.replace(hour=7, minute=0, second=0, microsecond=100)
#target_time += datetime.timedelta(days=1)

now = datetime.datetime.now()
wait_until = now.replace(hour=6, minute=59, second=57, microsecond=0)
#wait_until += datetime.timedelta(days=1)

seconds_to_wait = (wait_until - now).total_seconds()
print('start sleep')
time.sleep(seconds_to_wait)
'''
session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookies)
session.get('https://ehall.bjut.edu.cn')
'''
while True:
    now = datetime.datetime.now()
    if now >= target_time:
        break
'''
yuyue_all()



