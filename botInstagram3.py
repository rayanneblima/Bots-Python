# Bot para comentar em fotos de uma tag específica do Instagram

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot3:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/rayan/Desktop/Cursos Quarentena/Bots - Python/chromedriver.exe')
        
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
        self.comentarFotosdaTag('sorteio')
    
    @staticmethod
    def digitarComoHumano(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)
    
    def comentarFotosdaTag(self, hashtag):
        links_de_posts = []
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except:
                pass
        
        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                comentarios = ['1', '2', '3']
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")
                time.sleep(5)
                self.digitarComoHumano(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(30,120))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)
                
testBot = InstagramBot3('','')  # TODO: inserir username e senha
testBot.login()