from classes.web.Baseweb import Baseweb
from constants import Constants


TEACHER_MENU_ID = 'menu1'
GROUPS_MENU_ID = 'tab10202'
EVALUATION_TITLE = 'Sistema d\'Administració i Gestió Acadèmica - Institut Joaquim Mir'
YOUR_GROUP_XPATH = '//*[@id=\"form_38956696118_tutorAvaluacio\"]/following-sibling::*'

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