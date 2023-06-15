from selenium import webdriver
from dotenv import dotenv_values
from constants import Constants
from classes.web.Signin import Signin
from classes.web.Evaluationweb import Evaluationweb
from classes.web.ModuleListWeb import ModuleListWeb
from classes.web.StudentListWeb import StudentListWeb

from classes.grades.Classroom import Classroom
from miscellaneous.Misc import Misc

secrets = dotenv_values(".env")
classroom = Classroom()
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
evaluation_page.go_to_group(secrets['GROUP_NAME'])
# ENTER STUDENT LIST #
student_list_page = StudentListWeb(driver)
students_list = student_list_page.get_student_list()
for i in range(len(students_list)):
    student_list_page.click_into_student(students_list[i])
    
    pass


