from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
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

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "https://github.com/Sud-Austral/PROYECTO_MOP")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

    driver = webdriver.Firefox(profile)
    
    driver.get("http://www.geomop.cl/VisorObras/#/home")
    
    return driver
def proceso():
    getDriver()
    print("Hola mundo")
    return


if __name__ == '__main__':
    try:
        proceso()
    except:
        try:
            proceso()
        except:
            error = sys.exc_info()[1]
            print(error)