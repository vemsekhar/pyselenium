from lib2to3.pgen2 import driver
from turtle import title
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
print(driver)
driver.get("https://www.google.com/")

print(driver.get(title))


driver.quit()