from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Projects.InstagramBot.bilgiler
import time

from Projects.InstagramBot import bilgiler


def document_initialised(driver):
    return driver.execute_script("return initialised")

def eleman_sec(driver_name, selection_way, selection_data):
    secilecek_eleman = WebDriverWait(driver_name, 10).until(
        EC.presence_of_element_located(
            (selection_way,
             selection_data))
    )
    return secilecek_eleman

options = Options()
options.page_load_strategy = 'eager'

url = "https://www.instagram.com/"
driver = webdriver.Chrome( executable_path="D:\Development\selenium_browser_drivers\chromedriver.exe", options=options)

driver.get( url )
driver.maximize_window()

try:
    username = eleman_sec(driver, By.NAME, "username")
    username.send_keys(bilgiler.kullanici_adi)

    password = eleman_sec(driver, By.NAME, "password")
    password.send_keys(bilgiler.parola)

    btnGiris = eleman_sec(driver, By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    btnGiris.click()

    btnKaydetGec = eleman_sec(driver, By.XPATH, "//*[@id='react-root']/section/main/div/div/div/section/div/button")
    btnKaydetGec.click()

    btnBildirimlerSimdiDegil = eleman_sec(driver, By.XPATH, "/ html / body / div[4] / div / div / div / div[3] / button[2]")
    btnBildirimlerSimdiDegil.click()

    try:
        btnMenu = eleman_sec(driver, By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]")
        btnMenu.click()

        btnProfilim = eleman_sec(driver, By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]")
        btnProfilim.click()

        try:
            takipci_sayisi = eleman_sec(driver, By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            print("Takipçi sayısı : ", takipci_sayisi.text)

        except NoSuchElementException:
            print("BÖyle bir eleman yok")

    except TimeoutException:
        print("bu eleman bulunamadı")

    print("tamam")
    time.sleep(5)
finally:
    driver.quit()


