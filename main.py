from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Documents\\Selenium\\chromedriver.exe")
driver.maximize_window();

#Going to the google form.
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(1)

driver.find_element(By.NAME, "firstname").send_keys("Kabir")
time.sleep(0.5)

driver.find_element(By.NAME, "lastname").send_keys("Wiit")
time.sleep(0.5)

driver.find_element(By.ID, "sex-0").click()

driver.find_element(By.ID, "exp-1").click()

driver.find_element(By.XPATH, '//input[@id="datepicker"]').send_keys("16/11/1998")

driver.find_element(By.ID, "profession-1").click()
time.sleep(2)

continents = Select(driver.find_element(By.ID, "continents"))
continents.select_by_visible_text("Europe")
time.sleep(1)

commands= Select(driver.find_element(By.ID, "selenium_commands"))
commands.select_by_visible_text("Wait Commands")
time.sleep(1.5)

driver.find_element(By.XPATH, '//input[@class="input-file"]').send_keys("C:\\Users\\Administrator\\Pictures")
time.sleep(2)

driver.find_element(By.XPATH, '//button[@id="submit"]').click()




