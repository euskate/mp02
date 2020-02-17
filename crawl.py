from selenium import webdriver
import urllib.request
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

# options.add_argument('headless') #화면 표시 X
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', options=options)

# startday = "2018-07-01"
# endday = "2018-09-30"
# startday = "2019-01-01"
# endday = "2019-03-31"
# startday = "2019-04-01"
# endday = "2019-06-30"
# startday = "2019-07-01"
# endday = "2019-09-30"
startday = "2019-10-01"
endday = "2019-12-31"

url = f"https://www.kamis.or.kr/customer/price/retail/period.do?action=daily&startday={startday}&endday={endday}&countycode=&itemcategorycode=200&itemcode=231&kindcode=&productrankcode=&convert_kg_yn=N"

driver.get(url)
time.sleep(2)

target = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section[3]/div/a")
target.click()

