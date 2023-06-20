from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser(Enum):
    Chrome = 1
    Edge = 2

class Connection:
    def __init__(self,browser:Browser) -> None:
        if browser in Browser: self.browser = browser
        else: self.browser = Browser.Chrome
        
        if self.browser == Browser.Chrome:
            options = Options()
            options.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif self.browser == Browser.Edge:
            self.driver = webdriver.Edge()