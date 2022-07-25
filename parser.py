from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from pathlib import Path
# from fake_useragent import UserAgent
from config import proxy_password, proxy_login, seasson_password, seasson_login

p = Path("..")
path = p.joinpath(p.cwd(), "firefoxdriver/geckodriver")

# options
options = webdriver.FirefoxOptions()

proxy_options = {
    "proxy": {
        "https": f"http://{proxy_login}:{proxy_password}@45.155.200.159:8000"
    }
}


# # disable webdriver mode
options.set_preference("dom.webdriver.enable", False)
#
# headless mode
options.headless = True

url = "http://seasonvar.ru/?mod=login"
driver = webdriver.Firefox(executable_path=path, seleniumwire_options=proxy_options)

try:
    driver.get(url=url)
    time.sleep(5)

    login_input = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[1]/input[1]')
    login_input.clear()
    login_input.send_keys(seasson_login)
    time.sleep(3)

    password_input = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[1]/input[2]')
    password_input.clear()
    password_input.send_keys(seasson_password)
    time.sleep(5)

    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # input serial link
    url = input("Введите ссыылку на сериал который нужно скачать: ")
    download_serial = driver.get(url=url)
    time.sleep(15)
    click_download = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/ul/li[3]")
    click_download.click()
    page = driver.find_element_by_class_name("pgs-afterplay-d").text
    with open("response_page.txt", "w") as file:
        file.write(page)
    time.sleep(30)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()