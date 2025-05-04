import requests
import datetime
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
    "CASTGC": "TGT-123456-AAXf-aaaa-UHwq5fTxaCJpdXYcSBJIDsARoi1XXuMhg3d-HGzMN2uWGMXVV-EQCCIbkb512782a77f4",
    "PHPSESSID": "ST-1234567-cFh5mBtJHJLJhNi1vgRFMZWeFLkb512782a77f4",
    "vjuid": "123456",
    "vjvd": "123cf984a85f7fde4944b705806d9dcb",
    "vt": "123907175"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Referer": "https://ehall.bjut.edu.cn/v2/reserve/reserveDetail?id=56",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept": "application/json, text/plain, */*"
}

data = ('resource_id=56&code=&remarks=&deduct_num=&data=%5B%7B%22date%22%3A%222025-05-06%22%2C%22period%22%3A1815%2C%22sub_resource_id%22%3A1562%7D%2C%7B%22date%22%3A%222025-05-06%22%2C%22period%22%3A1816%2C%22sub_resource_id%22%3A1561%7D%5D&position_data=')
url = "https://ehall.bjut.edu.cn/site/reservation/launch"

now = datetime.datetime.now()
target_time = now.replace(hour=6, minute=59, second=59, microsecond=900000)
target_time += datetime.timedelta(days=1)

now = datetime.datetime.now()
wait_until = now.replace(hour=6, minute=59, second=55, microsecond=0)
wait_until += datetime.timedelta(days=1)

seconds_to_wait = (wait_until - now).total_seconds()
print('start sleep')
time.sleep(seconds_to_wait)

session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookies)
session.get('https://ehall.bjut.edu.cn')

while True:
    now = datetime.datetime.now()
    if now >= target_time:
        break

now = datetime.datetime.now()
print(now)
response = session.post(url, data=data)
now = datetime.datetime.now()
print(now)
print("Response Text:", response.text)
