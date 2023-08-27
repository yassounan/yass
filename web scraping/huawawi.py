from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint


driver=webdriver.Chrome()
url=("https://www.tunisianet.com.tn/smartphone-tunisie/66496-smartphone-huawei-nova-11-pro-4g-8-go-256-go-noir-freebuds-5-tablette-matepad-t8-freebuds-se.html")
driver.get(url)
product={}

title_element=driver.find_element(By.CLASS_NAME,"h1")
title=title_element.text
product["title"]=title

refference_element=driver.find_element(By.ID,"product-description-short-66496" )
refference=refference_element.text
product["refference"]=refference

prix_element=driver.find_element(By.CLASS_NAME,"current-price")
prix=prix_element.text
product["prix"]=prix


availibility_element=driver.find_element(By.ID,"stock_availability" )
available=availibility_element.text
product["available"]=available



pprint(product)
time.sleep(1)
driver.close()