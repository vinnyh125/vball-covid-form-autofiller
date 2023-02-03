from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSehh3iXrXCnIyvZytx6whYW0VHuN_NGGFXiUeIJaAbfCogP7w/viewform")

time.sleep(.25)

email = driver.find_element_by_class_name("quantumWizTextinputPaperinputInput")
email.send_keys("vincenthuang@hvrsd.org")

time.sleep(.25)

name = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
name.send_keys("huang vincent")

time.sleep(.25)

fever = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div")
fever.click()

time.sleep(.25)

cough = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div")
cough.click()

time.sleep(.25)

soreThroat = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div")
soreThroat.click()

time.sleep(.25)

chills = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div")
chills.click()

time.sleep(.25)

muscleAches = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div")
muscleAches.click()

time.sleep(.25)

headache = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div")
headache.click()

time.sleep(.25)

noTaste = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div")
noTaste.click()

time.sleep(.25)

pain = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div")
pain.click()

time.sleep(.25)

sick = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
sick.click()

time.sleep(.25)

covid = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
covid.click()

time.sleep(.25)

travel = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
travel.click()

time.sleep(.25)

states = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
states.click()

time.sleep(.25)

quarantine = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div")
quarantine.click()

time.sleep(.25)

submit = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span")
submit.click()

time.sleep(.5)

driver.quit()