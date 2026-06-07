# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 06:54:41 2026

@author: 91733
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )