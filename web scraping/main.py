from selenium import webdriver
import time

from get_product import get_product
from save_product import save_product
from get_products import get_products_urls

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)
urls = get_products_urls(driver)
print(urls)

for url in urls:
    product = get_product(driver, url)
    save_product(product)

time.sleep(1)
driver.close()