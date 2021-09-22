import selenium
from selenium import webdriver

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Users\Zane\source\repos\drivers\chromedriver86.exe')
driver.get("https://website")

sleep(5)

driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys("email@email.com")

driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys("pass")

driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()

sleep(5)

driver.find_element_by_xpath("//button [contains(text(),'Not Now')]")\
    .click()

driver.find_element_by_xpath("//button [contains(text(),'Not Now')]")\
    .click()

sleep(5)


for i in range(5):
    driver.find_element_by_xpath('//button[text() = "Follow" ]')


