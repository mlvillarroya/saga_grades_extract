from classes.web.Baseweb import Baseweb
from constants import Constants


TEACHER_MENU_ID = 'menu1'
GROUPS_MENU_ID = 'tab10202'
EVALUATION_TITLE = 'Sistema d\'Administració i Gestió Acadèmica - Institut Joaquim Mir'
YOUR_GROUP_XPATH = '//*[@id=\"form_38956696118_tutorAvaluacio\"]/following-sibling::*'
GROUP_ROW_XPATH = '//td[@title=\"GROUP_NAME\"]/parent::*'
GROUP_ICON_XPATH = './/img[@title=\"Veure els alumnes del grup\"]'

class Evaluationweb(Baseweb):
    def __init__(self,driver):
        super().__init__(driver,EVALUATION_TITLE)


    def go_to_teacher_menu(self):
        self.go_to_first_frame()
        self.search_and_click_by_ID(TEACHER_MENU_ID)

    def go_to_groups_menu(self):
        self.go_to_first_frame()
        self.search_and_click_by_ID(GROUPS_MENU_ID)

    def go_to_your_group(self):
        self.go_to_second_frame()
        self.search_and_click_by_XPATH(YOUR_GROUP_XPATH)

    def search_group_row(self,group_name):
        group_xpath = GROUP_ROW_XPATH.replace("GROUP_NAME",group_name)
        try:
            return self.search_element_by_XPATH(group_xpath)
        except:
            raise Exception("Group not found")
    
    def go_to_group(self,group_name):
        self.go_to_second_frame()
        group_row = self.search_group_row(group_name)
        group_icon = self.get_xpath_inside_element(group_row,GROUP_ICON_XPATH)
        if group_icon: self.click_into_element(group_icon)
