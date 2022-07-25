import requests
from config import proxy_password, proxy_login, seasson_password, seasson_login
import re
import time

proxies = {
    "http": f"http://{proxy_login}:{proxy_password}@45.155.200.159:8000"
}
# user = fake_useragent.UserAgent().random
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}
form_data = {
    "login": seasson_login,
    "password": seasson_password
}
session = requests.Session()
auth_link = "http://seasonvar.ru/?mod=login"
auth = session.post(auth_link, headers=headers, data=form_data, proxies=proxies)
time.sleep(5)
url = input("Введите url сериала: ")
serial_id = re.findall("\d+", url)
data = {
    "download": serial_id[0],
}
all_links_down = session.post("http://seasonvar.ru/ajax.php", headers=headers, data=data, proxies=proxies)
print(all_links_down)
with open("source_links.txt", 'w') as file:
    file.write(all_links_down.text)
