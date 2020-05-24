# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:52:25 2020

@author: ankitaPC
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login

username = "vivekmaurya1505@gmail.com"
password = "93227455100"

driver = 0
def main():
    global driver
    print("running script...")
    driver = webdriver.Chrome("C://Program Files (x86)/Google/Chrome/Application/chrome.exe")
    l = login.Login(driver,username,password)
    l.signin()
    
if __name__ == "__main__":
    main()
    
    
