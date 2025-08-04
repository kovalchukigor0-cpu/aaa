from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver

driver = webdriver.Chrome()
for x in range (1,2):
	driver.get("https://armtek.ru/assortment/category/rulevye-reyki-9255?PRICE%5BMIN_VALUE%5D=3000&PRICE%5BMAX_VALUE%5D=100000&viewType=list"+"&page="+str(x))
	time.sleep(5)
	prvs = ''
	elements_number = driver.find_elements(By.XPATH , "//div[@class='content']/div[1]/div[1]/div[3]/a")
	elements_brand = driver.find_elements(By.XPATH , "//div[@class='content']/div[1]/div[1]/div[3]/span[1]")
	elements_name = driver.find_elements(By.XPATH , "//div[@class='content']//div[@class='item-info-row']")
	brand_count = 0

	for i in elements_name:
		print(str(i.text))
	print(len(elements_name))
driver.quit()



