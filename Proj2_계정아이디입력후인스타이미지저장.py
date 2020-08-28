from urllib.request import urlopen
from urllib.parse import quote_plus #한국어로 다시 바꾸는 것, 아이디 영어라 필요없을듯..?
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#https://www.instagram.com/vintage.salon_hongdae
    
baseUrl = 'https://www.instagram.com/'
id_Input = input('해당 계정의 아이디를 입력하세요 : ')
url = baseUrl + quote_plus(id_Input)

#print(url)

driver = webdriver.Chrome()
driver.get(url)


#elements = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[4]/div[1]/div/button/div/div")
#driver.execute_script("arguments[0].click();", elements)


#elements.click()



SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")       

while True:
    # Scroll down to bottom                                                      
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)                                               
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height           
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:                                                
        break

    last_height = new_height
   

    
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')

#print(insta[0])

n = 1
for i in insta:
    print('https://www.instagram.com'+i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./clothes_img/' + id_Input + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()

