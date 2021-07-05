from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

url = "https://www.americanas.com.br/?epar=bp_br_00_go_sch_brand_americanas_202002&utm_medium=buscappc&utm_source=google&utm_campaign=marca:acom%3bmidia:buscappc%3bformato:branding%3bsubformato:00%3bidcampanha:sch_brand_americanas_202002&opn=YZMEZP&WT.srch=1&gclid=CjwKCAjwz_WGBhA1EiwAUAxIcbC7EUdGoscK8nbBqNHc_ZNcqRDct3votd0tEZH52d1CVTCiG8qNxBoCRw0QAvD_BwE"

driver = webdriver.Chrome()
driver.get(url)

sleep(3)

x = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div[2]/a[1]/div/div[2]/span')
y = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div[2]/a[2]/div/div[2]/span')
z = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div[2]/a[3]/div/div[2]/span')
t = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div[2]/a[4]/div/div[2]/span')
print(x.text+"\n"+y.text+"\n"+z.text+"\n"+t.text+"\n")
