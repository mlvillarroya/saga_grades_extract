from classes.web.Baseweb import Baseweb
from selenium.webdriver.common.by import By

USER_BOX_ID = 'user'
PASS_BOX_ID = 'password'
SUBMIT_BUTTON_XPATH = '//input[@type="submit"]'
SIGNIN_TITLE = 'Formulari de login GICAR'

class Signin(Baseweb):
    def __init__(self,driver,secrets):
        self.secrets = secrets
        super().__init__(driver,SIGNIN_TITLE)
    
    def do_login(self):
        self.search_by_ID_and_fill(USER_BOX_ID,self.secrets['SAGA_USER'])
        self.search_by_ID_and_fill(PASS_BOX_ID,self.secrets['SAGA_PASS'])
        self.search_and_click_by_XPATH(SUBMIT_BUTTON_XPATH)