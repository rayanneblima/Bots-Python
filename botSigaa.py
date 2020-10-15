# Bot para baixar os materiais do SIGAA e, assim, contar presença no EAD XXXD

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class sigaaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/Rayanne/Desktop/Bots-Python/chromedriver.exe')
        
    def login(self):
        driver = self.driver
        driver.get('https://sig.ifsudestemg.edu.br/sigaa/')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='user.login']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='user.senha']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.entrarMateria()

    def entrarMateria(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[@id='form_acessarTurmaVirtual:turmaVirtual']").click()
        time.sleep(5)
        form = driver.find_element_by_xpath("//form[@id='formAva']")
        materiais = form.find_elements_by_xpath("//span[contains(@id,'j_id_jsp_1337189032_343')]")
        print(len(materiais))
        for material in materiais:
          material.find_element_by_tag_name('a').click()
          time.sleep(5)
        print("Acabei de baixar tudo!!")
        time.sleep(5)

    def trocarTurma(self):
      driver = self.driver
      driver.find_element_by_xpath("//button[@id='formAcoesTurma:botaoTrocarTurma']").click()
      formTurma = driver.find_element_by_xpath("//form[@id='formTurma']")
      turmas = formTurma.find_elements_by_tag_name('a')
      turmas[1].click()

testBot = sigaaBot('','') # TODO: inserir username e senha
testBot.login()

# TODO: criar executável
# TODO: pedir usuário, senha e número de matérias
# TODO: recursividade entre as funções para executar de 1 até o numero de materias vezes
