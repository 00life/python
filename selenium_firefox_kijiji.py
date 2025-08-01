import time, os


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service


def func():
    global ad

    DELAY = 5
    PATH_PWD = os.path.dirname(os.path.realpath(__file__))

    FF_OPTIONS = [
        # '--headless',
        '--no-sandbox',
        '--start-maximized',
        '--start-fullscreen',
        '--single-process',
        '--disable-dev-shm-usage',
        '--incognito',
        '--disable-blink-features=AutomationControlled',
        '--disable-xss-auditor',
        '--disable-web-security',
        '--ignore-certificate-errors',
        '--log-level=3',
        '--disable-notifications',
        '--disable-infobars',
        '--disable-gpu',
        '--disable-extensions',
        
    ]

    SET_PREF = {
        'general.useragent.override':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'permissions.default.desktop-notification': 1,
        'dom.webnotifications.enabled': 1,
        'dom.push.enabled': 1,
        'intl.accept_languages': 'en-US',
        # 'network.proxy.type': 1,
        # "network.proxy.http": '127.0.0.1',
        # 'network.proxy.http_port': 9224,
    }
    
    myOptions = FirefoxOptions()
    [myOptions.add_argument(opt) for opt in FF_OPTIONS]
    [myOptions.set_preference(key, value) for key, value in SET_PREF.items()]
    
    
    path_gecko = os.path.join(PATH_PWD, 'geckodriver-v0.33.0-win32', 'geckodriver.exe')
    path_firefoxBin = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    path_profile = 'C:\\Users\\R324\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\mx7b8yvr.default-release-1680794538761'
    path_pics = os.path.join(PATH_PWD,'pics','cat.jpg')
    myOptions.add_argument('-profile')
    myOptions.add_argument(path_profile)

    print('[*] path_gecko:', os.path.exists(path_gecko))
    print('[*] path_firefoxBin:', os.path.exists(path_firefoxBin))

    myService = Service(path_gecko)
    myOptions.binary_location = path_firefoxBin

    print('[*] Starting Driver\n')
    
    driver = webdriver.Firefox(service=myService, options=myOptions)
    

    driver.get('https://www.kijiji.ca')
    print('[*] Visited Website\n')

    time.sleep(DELAY)

    driver.get('https://www.kijiji.ca/m-my-ads/active/1')
    print('[*] Visited Ad Page\n')

    time.sleep(DELAY)

    num = driver.find_element(By.XPATH, '//div[contains(text(),"Active")]//span').text
    print('[*] Number of ads:', num, '\n')

    if num == '1':
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

    driver.find_element(By.XPATH, '//textarea[@id="AdTitleForm"]').send_keys('$700/mo room Kensington / Cannon - Professionals / Students')
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

    driver.find_element(By.XPATH, '//label[contains(text(), "Pet Friendly")]').click()
    print('[*] Selecting Pets Option\n')
    
    time.sleep(DELAY)
    
    with open(PATH_PWD + os.path.sep + 'ad.txt','r') as fout:
        ad = fout.read()
    driver.find_element(By.XPATH, '//textarea[@id="pstad-descrptn"]').send_keys(ad)
    print('[*] Description Entered\n')

    time.sleep(DELAY)

    for i in [1,2,3,4,6,7,8,9,10]:
        driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(os.path.join(PATH_PWD, 'housePics', f'{i}.JPG'))
        time.sleep(1)
    print('[*] Inputting Pictures\n')

    time.sleep(DELAY)
    
    driver.find_element(By.XPATH, '//input[@name="postAdForm.priceAmount"]').send_keys('700')
    print('[*] Price Entered\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//button[@data-qa-id="package-0-bottom-select"]').click()
    print('[*] Selecting Package\n')

    time.sleep(DELAY)

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    print('[*] Selecting Submit\n')

if __name__ == '__main__':
    func()
