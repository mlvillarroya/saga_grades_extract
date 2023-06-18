from selenium import webdriver
from dotenv import dotenv_values
from classes.web.Signin import Signin
from classes.web.Evaluationweb import Evaluationweb
from classes.web.StudentListWeb import StudentListWeb
from classes.web.StudentGradesWeb import StudentGradesWeb

from classes.grades.Classroom import Classroom
from miscellaneous.Misc import Misc

from classes.myexcel.Myexcel import Myexcel

secrets = dotenv_values(".env")
# saga_url = secrets['SAGA_URL'] or ''
# if secrets == '': raise Exception('URL not provided')
# driver = webdriver.Edge()
# # ACCESS SAGA #
# driver.get(saga_url)
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

# # CONVERTING GRADES INTO JSON #
# Misc.objecttojsonfile(class_grades,'grades.json')
# # CONVERTING STUDENTS INTO JSON #
# Misc.objecttojsonfile(students_list,'students.json')
# jsonFile = open("students.json", "w")
# students_json = json.dumps(students_list,ensure_ascii=False)
# jsonFile.write(students_json)
# jsonFile.close()

# WHILE TESTING, LOAD DATA FROM FILE #
class_grades = Misc.jsonfiletoobject('grades.json')
students_list = Misc.jsonfiletoobject('students.json')
######################################

group_name = secrets['GROUP_NAME'] or 'unnamed'
classroom = Classroom(group_name)
for i,student in enumerate(students_list):
    student = classroom.get_student(student)
    student.get_grades(class_grades[i])

myexcel = Myexcel('grades.xlsx',group_name)
module_unit_names_hours = classroom.get_modules_unit_names_from_first_student()
classroom_students = classroom.get_student_names()
myexcel.create_module_header_with_modules_units_hours(module_unit_names_hours)
myexcel.create_first_column_with_student_names(classroom_students)
myexcel.save_file()

pass