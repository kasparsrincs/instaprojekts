import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


parole = "lkjlkj12"
lvards = "janisprogrametajs12"


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
url = "https://www.instagram.com"
driver.get(url)
time.sleep(3)
              
       
atlaut_cepumus=driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
atlaut_cepumus.click()

log_liet=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
log_liet.send_keys(lvards)

log_par=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
log_par.send_keys(parole)
time.sleep(1)
login=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
login.click()

time.sleep(4)

login=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
login.click()  
time.sleep(1)
pele=driver.find_element(By.XPATH," /html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
pele.click()
time.sleep(2)
pele=driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div")
pele.click()
time.sleep(2)
pele=driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
pele.click


time.sleep(1)
pele=driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
pele.click()


















input()