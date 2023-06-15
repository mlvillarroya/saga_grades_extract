from selenium.webdriver.common.by import By
from exceptions.DifferentPageException import DifferentPageException
from exceptions.ElementNotFoundException import ElementNotFoundException
from exceptions.ElementNotClickable import ElementNotClickable
import time

class Baseweb:
    def __init__(self,driver,title):
        self.driver = driver
        if (driver.title != title):
            time.sleep(5)
            if (driver.title != title): raise DifferentPageException(driver.current_url)

    def go_to_first_frame(self):
        self.driver.switch_to.default_content()
        iframes = self.driver.find_elements(By.TAG_NAME,'frame')
        self.driver.switch_to.frame(iframes[0])

    def go_to_second_frame(self):
        self.driver.switch_to.default_content()
        iframes = self.driver.find_elements(By.TAG_NAME,'frame')
        self.driver.switch_to.frame(iframes[1])

    def search_by_CSS_SELECTOR(self,element_id,index = 0):
        if (len(self.driver.find_elements(By.CSS_SELECTOR,element_id))==0): raise ElementNotFoundException(element_id)
        return self.driver.find_elements(By.CSS_SELECTOR,element_id)[index]

    def search_by_ID(self,element_id):
        if (len(self.driver.find_elements(By.ID,element_id))==0): raise ElementNotFoundException(element_id)
        return self.driver.find_element(By.ID,element_id)
    
    def search_element_by_XPATH(self,element_xpath):
        if (len(self.driver.find_elements(By.XPATH,element_xpath))==0): raise ElementNotFoundException(element_xpath)
        return self.driver.find_element(By.XPATH,element_xpath)

    def search_elements_by_XPATH(self,element_xpath):
        if (len(self.driver.find_elements(By.XPATH,element_xpath))==0): raise ElementNotFoundException(element_xpath)
        return self.driver.find_elements(By.XPATH,element_xpath)

    def search_and_click_by_ID(self,element_id):
        element = self.search_by_ID(element_id)
        try:
            element.click()
        except:
            raise ElementNotClickable(element_id)
        
    def search_and_click_by_XPATH(self,element_xpath):
        element = self.search_element_by_XPATH(element_xpath)
        try:
            element.click()
        except:
            raise ElementNotClickable(element_xpath)
        
    def search_by_ID_and_fill(self,element_id,content):
        element = self.search_by_ID(element_id)
        element.send_keys(content)

    def search_by_XPATH_and_fill(self,element_xpath,content):
        element = self.search_element_by_XPATH(element_xpath)
        element.send_keys(content)

    def search_table(self,index = 0):
        return self.search_by_CSS_SELECTOR('table',index)
    
    def get_table_rows(self,table_index = 0):
        table = self.search_table(table_index)
        return table.find_elements(By.CSS_SELECTOR,'tr')
    
    def get_row_data_cells(self,row):
        cells = row.find_elements(By.CSS_SELECTOR,'td')
        if len(cells) > 0: return cells
        else: return False
         
    def get_css_selector_inside_element(self,element,selector):
        results = element.find_elements(By.CSS_SELECTOR,selector)
        if len(results) == 0: return False
        else: return results[0]

    def get_xpath_inside_element(self,element,xpath):
        results = element.find_elements(By.XPATH,xpath)
        if len(results) == 0: return False
        else: return results[0]
        
    def click_into_element(self,element):
        try:
            element.click()
        except:
            raise ElementNotClickable(element)
        
    def click_go_back(self):
        self.search_and_click_by_XPATH("//input[@value=\"Enrere\"]")
        
    def data_cell_content(self,cell):
        return cell.text