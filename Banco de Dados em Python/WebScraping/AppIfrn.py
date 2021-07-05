
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from datetime import datetime

cidades = ['apodi','caico','canguaretama','ceara-mirim','curraisnovos','joaocamara','paudosferros','jucurutu','lajes','macau','mossoro','natalcentral','natalcidadealta','natalzonanorte']
for x in cidades:
    url = "https://portal.ifrn.edu.br/campus/"+x

    driver = webdriver.Chrome()
    driver.get(url)

    sleep(2)
    title1 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[1]/a/span[1]')
    title2 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[2]/a/span[1]')
    title3 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[3]/a/span[1]')
    title4 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[4]/a/span[1]')
    title5 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[5]/a/span[1]')
    title6 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[6]/a/span[1]')
    title7 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[7]/a/span[1]')
    title8 = driver.find_element_by_xpath('//*[@id="principal_news"]/div[8]/a/span[1]')
    
    
    with open("noticias.txt",'a') as arq:
        arq.write(x+' - ('+str(datetime.now())+')\n'+title1.text+'\n'+title2.text+'\n'+title3.text+'\n'+title4.text+'\n'+title5.text+'\n'+title6.text+'\n'+title7.text+'\n'+title8.text+'\n\n')
    
print("ACABOU!")