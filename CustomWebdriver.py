# -*- coding: utf-8 -*-
from selenium import webdriver
"""
Created on Thu Sep  3 19:56:45 2020

@author: Jorge
"""
class CustomWebdriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def set_IP(self, proxy):
        print("Setting IP & port to: " + proxy)
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        
        self.driver = webdriver.Chrome(options=chrome_options)