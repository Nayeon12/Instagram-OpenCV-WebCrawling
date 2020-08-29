from urllib.request import urlopen
from urllib.parse import quote_plus 
from bs4 import BeautifulSoup
from selenium import webdriver
import time

    
baseUrl = 'https://www.instagram.com/'
print("=====로그인 하기=====")
user_id = input('ID : ')
user_password = input('PASSWORD : ')


id_Input = input('분석하고자 하는 계정의 아이디를 입력하세요 : ')
url = baseUrl + quote_plus(id_Input)

driver = webdriver.Chrome()
driver.get(baseUrl)

time.sleep(3)


driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(user_id)

driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(user_password)

driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").submit()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()


driver.get(url)

#print(url)

