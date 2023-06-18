from selenium import webdriver
from dotenv import dotenv_values
from classes.web.Signin import Signin
from classes.web.Evaluationweb import Evaluationweb
from classes.web.StudentListWeb import StudentListWeb
from classes.web.StudentGradesWeb import StudentGradesWeb
import json

from classes.grades.Classroom import Classroom
from miscellaneous.Misc import Misc

from classes.myexcel.Myexcel import Myexcel

secrets = dotenv_values(".env")
# driver = webdriver.Edge()
# # ACCESS SAGA #
# driver.get(Constants.SAGA_URL)
# # SIGN IN PAGE #
# signin_page = Signin(driver,secrets)
# signin_page.do_login()
# print(driver.title)
# # ENTER EVALUATION PAGE #
# evaluation_page = Evaluationweb(driver)
# evaluation_page.go_to_teacher_menu()
# evaluation_page.go_to_groups_menu()
# evaluation_page.go_to_group(secrets['GROUP_NAME'])
# # ENTER STUDENT LIST #
# student_list_page = StudentListWeb(driver)
# students_list = student_list_page.get_student_list()
# class_grades = []
# for i in range(len(students_list)):
#     student_list_page.click_into_student(students_list[i])
#     # ENTER STUDENT'S GRADES #
#     student_grades_web = StudentGradesWeb(driver)
#     class_grades.append(student_grades_web.get_grades_matrix())
#     student_grades_web.click_go_back()
# driver.quit()

# WHILE TESTING, LOAD DATA FROM FILE #
file = open("grades.json")
class_grades = json.load(file)
file = open("students.json")
students_list = json.load(file)
######################################
group_name = secrets['GROUP_NAME'] or 'unnamed'
classroom = Classroom(group_name)
for i,student in enumerate(students_list):
    student = classroom.get_student(student)
    student.get_grades(class_grades[i])

myexcel = Myexcel('grades.xlsx',group_name)
module_unit_names = classroom.get_modules_unit_names_from_first_student()
classroom_students = classroom.get_student_names()
myexcel.create_module_header_with_modules_units(module_unit_names)
myexcel.create_first_column_with_student_names(classroom_students)
myexcel.save_file()

pass