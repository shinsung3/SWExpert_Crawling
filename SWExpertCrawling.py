from selenium import webdriver

#webdriver가 있어야 막히지 않음.
driver = webdriver.Chrome("./chromedriver.exe")

#web crwaling 주소 삽입
driver.get("https://swexpertacademy.com/main/main.do")