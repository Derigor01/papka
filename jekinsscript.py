from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\chromedriver.exe")
driver.get("https://novaposhta.ua/")

driver.quit()
