from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.firefox.options import Options

import cursor

from config import *

# Pfad zum Chromium-Driver (ersetze '/path/to/chromedriver' durch den tatsächlichen Pfad)
driver_path = '/usr/local/bin/geckodriver'

# Starte den Browser
options = Options()
options.set_preference("browser.fullscreen.autohide", True)
service = webdriver.FirefoxService(executable_path=driver_path, options=options)
driver = webdriver.Firefox(service=service)
action = webdriver.ActionChains(driver)
driver.fullscreen_window()

# Öffne die Excel-Datei in Excel Online
driver.get(excel_url)

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
STAYLOGGEDIN = (By.ID, "declineButton")
MENUBAND_OPTIONS = (By.XPATH, '//*[@id="FibbonModeToggle"]')
AUTOMATIC_HIDE = (By.XPATH, '/html/body/div[18]/div[4]/div/div/div/div/div/div/div/div/ul/li[2]/div/ul/li[3]/button')

# wait for email field and enter email
WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(username)

# Click Next
WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(password)

# Click Login - same id?
WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# Decline stay logged in
WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(STAYLOGGEDIN)).click()

# WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(MENUBAND_OPTIONS)).click()
# WebDriverWait(driver, max_timeout).until(EC.element_to_be_clickable(AUTOMATIC_HIDE)).click()

# Warte darauf, dass die Seite vollständig geladen ist
time.sleep(120)  # Wartezeit in Sekunden (kann je nach Internetverbindung variieren)

while True:
    action.send_keys(Keys.HOME).perform()
    action.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
    time.sleep(5*60*60)

# Schließe den Browser
# driver.quit()
