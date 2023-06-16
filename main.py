from selenium import webdriver
from dotenv import dotenv_values
from constants import Constants
from classes.web.Signin import Signin
from classes.web.Evaluationweb import Evaluationweb
from classes.web.StudentListWeb import StudentListWeb
from classes.web.StudentGradesWeb import StudentGradesWeb
import json

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
class_grades = []
for i in range(len(students_list)):
    student_list_page.click_into_student(students_list[i])
    student_grades_web = StudentGradesWeb(driver)
    class_grades.append(student_grades_web.get_grades_matrix())
    student_grades_web.click_go_back()
class_grades_json = json.dumps(class_grades)
print(class_grades_json)
pass

