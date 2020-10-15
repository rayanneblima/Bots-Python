# Bot para curtir fotos de uma tag do Instagram

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/Rayanne/Desktop/Bots-Python/chromedriver.exe')
        
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtirFotos('') # TODO: escolher a tag pra curtir

    def curtirFotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            if hashtag in href and href.index("https://www.instagram.com/p") != -1
        ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("Pulando link inválido..")
                continue
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//button[@class='wpO6b ']").click()
                time.sleep(20)
            except Exception as e:
                print(e)
                time.sleep(5)
        

testBot = instagramBot('','') # TODO: inserir username e senha
testBot.login()
