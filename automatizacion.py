from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service
import http.client, urllib.request, urllib.parse, urllib.error, base64
import shutil
import datetime
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import os
import glob
import sys

def getDriver():
    options = Options()
    #profile = webdriver.FirefoxProfile()
    #profile.set_preference("browser.download.folderList", 2)
    #profile.set_preference("browser.download.manager.showWhenStarting", False)
    #profile.set_preference("browser.download.dir", "descarga/")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    #service = Service(executable_path="chromedriver")
    #driver = webdriver.Chrome(service=service)
    #driver = webdriver.Firefox(options=options,service=service)
    #driver.set_page_load_timeout("60")
    #driver.get("http://www.geomop.cl/VisorObras/#/home")
    
    #return driver
    return
def proceso():
    print("Comenzamos")
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")
    #options.set_preference("browser.download.dir", "/home/runner/work/PROYECTO_MOP/PROYECTO_MOP")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", os.getcwd())
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/json")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout("60")
    #driver.get("http://www.geomop.cl/VisorObras/#/home")
    url = "https://ide.mop.gob.cl/VisorObras/#/home"
    driver.get(url)
    btndescarga = driver.find_element_by_xpath('/html/body/app-root/app-home/div/app-filter/div/section/button[2]')
    btndescarga.click()
    print("Aca0")
    print(btndescarga.text)
    time.sleep(30)
    try:
        print("Aca1")
        btngeojson = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/button[3]')
        btngeojson.click()
        print("Descarga Hecha")
        
    except:
        print("Aca2")
        error = sys.exc_info()[1]
        print(error)
        btngeojson = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/button[3]')
        btngeojson.click()
        print("Aca3")
    now = datetime.datetime.now()
    shutil.move(f"geometriaMOP {now.strftime('%d')}-{str(int(now.strftime('%m')))}-{now.strftime('%Y')}.json", f"Data_Legacy/geometriaMOP {now.strftime('%d')}-{str(int(now.strftime('%m')))}-{now.strftime('%Y')}.json")
    print("Aca")
    #driver = getDriver()
    #btndescarga = driver.find_element_by_xpath('/html/body/app-root/app-home/div/app-filter/div/section/button[2]')
    #btndescarga.click()
    #print(btndescarga.text)
    #btngeojson = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/button[3]')
    #btngeojson.click()
    #time.sleep(30)
    #print("Terminamos")
    return


if __name__ == '__main__':
    proceso()
    #try:
    #    proceso()
    #    print("Todo bien")
    #except:
    #    try:
    #        proceso()
    #        print("Todo bien")
    #    except:
    #        error = sys.exc_info()[1]
    #        print(error)