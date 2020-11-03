# Bot para votar em Google Forms

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class voteBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/Rayanne/Desktop/Bots-Python/chromedriver.exe')
        
    def open(self):
        driver = self.driver
        driver.get('')
        self.vote()

    def vote(self):
        driver = self.driver
        spans = driver.find_elements_by_xpath("//span[@class='docssharedWizToggleLabeledLabelText exportLabel freebirdFormviewerComponentsQuestionRadioLabel']");
        for i in range(len(spans)):
            if spans[i].text == "":
                spans[i].click()
        btnSend = driver.find_elements_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']");
        btnSend[1].click()
        
testBot = voteBot()
times = 1000
for i in range(0,times):
    print("Execução de número ", i)
    testBot.open()
