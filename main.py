from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dotenv import dotenv_values
from constants import Constants
from classes.web.Signin import Signin
from classes.web.Evaluationweb import Evaluationweb
from classes.web.ModuleListWeb import ModuleListWeb
from classes.web.UnitGradesWeb import UnitGradesWeb

secrets = dotenv_values(".env")
driver = webdriver.Edge()
# ACCESS SAGA #
driver.get(Constants.SAGA_URL)
# SIGN IN PAGE #
signin_page = Signin(driver,secrets)
signin_page.do_login()
print(driver.title)
# ENTER EVALUATION PAGE #
evaluation_page = Evaluationweb(driver)
evaluation_page.go_to_teacher_menu()
evaluation_page.go_to_groups_menu()
evaluation_page.go_to_your_group()
# MODULE LIST #
module_list_page = ModuleListWeb(driver)
modules = module_list_page.get_table_rows()
for module in module_list_page.get_table_rows():
    module_name = module_list_page.get_module_name(module)
    if not module_name: continue
    module_list_page.go_to_module_grades(module)
    # UNIT GRADES #
    unit_grades_page = UnitGradesWeb(driver)
    matrix = unit_grades_page.get_module_matrix()
    pass




