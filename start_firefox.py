from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.firefox.options import Options

import cursor

from config import *

driver_path = '/usr/local/bin/geckodriver'

# Count number of crashs with autofill --> When max. number exceeded, start without trying to fill out anything
number_crashs = 0
auto_fill = True
max_autofill_retries = 5

while True:
    try:
        # Start the browser
        options = Options()
        options.set_preference("browser.fullscreen.autohide", True)
        service = webdriver.FirefoxService(executable_path=driver_path, options=options)
        driver = webdriver.Firefox(service=service)
        action = webdriver.ActionChains(driver)
        driver.fullscreen_window()

        # Open the website
        driver.get(excel_url)
        
        if auto_fill:
            # Elements on HTML site
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

            # Wait until page is loaded
            time.sleep(120)  # Wartezeit in Sekunden (kann je nach Internetverbindung variieren)

            while True:
                # Move selected cell regularly in cell A1
                action.send_keys(Keys.HOME).perform()
                action.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(5*60*60)

        else:
            # Do nothing when no auto fill (just stay alive)
            while True:
                time.sleep(60)
    except KeyboardInterrupt:
        # Exit script when Ctrl+C is pressed
        exit()
    except Exception as e:
        # When error occured: close browser and reopen it
        print(e)
        driver.quit()
        number_crashs += 1
        if number_crashs == max_autofill_retries:
            auto_fill = False
            
        