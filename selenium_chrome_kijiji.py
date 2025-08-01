#!.\Scripts\python

import time, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

def func():
    DELAY = 5

    PATH_PWD = os.path.dirname(os.path.realpath(__file__))
    PATH_CHROME_USERDATA = r"C:\Users\R324\AppData\Local\Google\Chrome\User Data\Profile 1"
    PATH_CHROMEDRIVER = os.path.join(PATH_PWD,"chromedriver.exe")

    ADD_ARG_OPT = [
        '--headless=new', #Do not open the browser
        '--no-sandbox',
        '--start-maximized',
        '--disable-dev-shm-usage',
        '--disable-blink-features=AutomationControlled',
        '--disable-xss-auditor',
        '--disable-web-security',
        '--ignore-certificate-errors',
        '--log-level=3',
        '--disable-notifications',
        '--disable-infobars',
        '--disable-gpu',
        '--disable-extensions',
        f'--user-data-dir={PATH_CHROME_USERDATA}',
        '--profile-directory=Profile 1'
    ]

    ADD_EXP_OPT = [
        ("detach", True) # keep the browser open after the process has ended
    ]
   
    options = webdriver.ChromeOptions()
    print('[*] Loading Options\n')
    
    [options.add_argument(arg) for arg in ADD_ARG_OPT]
    [options.add_experimental_option(*arg) for arg in ADD_EXP_OPT]
   
    service=Service(executable_path=PATH_CHROMEDRIVER)
    
    print('[*] Starting Driver\n')

    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://www.kijiji.ca')
    print('[*] Visited Website\n')

    time.sleep(DELAY)

    driver.get(r'https://www.kijiji.ca/m-my-ads/active/1')
    print('[*] Visited Ad Page\n')

    time.sleep(DELAY)

    num = driver.find_element(By.XPATH, '//div[contains(text(),"Active")]//span').text
    print('[*] Number of ads:', num, '\n')

    if int(num) > 0:
        print('[!] Deleting Ad\n')

        time.sleep(DELAY)

        driver.find_element(By.XPATH, '//span[contains(text(),"Delete")]').click()
        print('[*] Clicking Delete\n')

        time.sleep(DELAY)

        driver.find_element(By.XPATH, '//button[contains(text(),"Prefer not to say")]').click()
        print('[*] Selecting Prefer...\n')

        time.sleep(DELAY)

        driver.find_element(By.XPATH, '//button[contains(text(),"Delete My Ad")]').click()
        print('[*] Selecting Delete My Ad\n')

        time.sleep(DELAY)
    
    
    driver.get('https://www.kijiji.ca/p-select-category.html')
    print('[*] Visited Category Page\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//textarea[@id="AdTitleForm"]').send_keys('$650/mo room Kensington / Cannon - Professionals / Students')
    print('[*] Inputting Ad Title\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//textarea[@id="AdTitleForm"]').send_keys(Keys.ENTER)
    print('[*] Clicking Enter\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//span[contains(text(),"Real Estate")]/parent::button').click()
    print('[*] Selecting Real Estate\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//span[contains(text(),"For Rent")]/parent::button').click()
    print('[*] Selecting For Rent\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//span[contains(text(),"Room Rentals & Roommates")]/parent::button').click()
    print('[*] Selecting Room Rentals\n')
    
    time.sleep(DELAY)
    print('[*] Inputting Ad Info\n')

    driver.find_element(By.XPATH, '//label[contains(text(), "Furnished")]').click()
    print('[*] Selecting Funished Option\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//label[@for="petsallowed_s-1"]').click()
    print('[*] Selecting Pets Option\n')
    
    time.sleep(DELAY)
    
    with open(PATH_PWD + os.path.sep + 'ad.txt','r') as fout:
        ad = fout.read()
    driver.find_element(By.XPATH, '//textarea[@id="pstad-descrptn"]').send_keys(ad)
    print('[*] Description Entered\n')

    time.sleep(DELAY)

    for i in [1,2,3,4,6,7,8,9,10]:
        try:
            driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(os.path.join(PATH_PWD, 'housePics', f'{i}.JPG'))
            time.sleep(1)
        except: pass
    print('[*] Inputting Pictures\n')

    time.sleep(DELAY)
    
    driver.find_element(By.XPATH, '//input[@name="postAdForm.priceAmount"]').send_keys('650')
    print('[*] Price Entered\n')

    time.sleep(DELAY)

    driver.find_elements(By.XPATH, '//span[contains(text(), "Select")]')[0].click()
    print('[*] Selecting Package\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    print('[*] Selecting Submit\n')

    time.sleep(DELAY)

    driver.quit()

if __name__ == "__main__":
    func()
