from dotenv import dotenv_values
from classes.web.Web import Web
from classes.grades.Classroom import Classroom
from miscellaneous.Misc import Misc

from classes.myexcel.Myexcel import Myexcel

secrets = dotenv_values(".env")
# web_extractor = Web()
# students_list,class_grades = web_extractor.take_grades_from_student_page(secrets)

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
classroom.build_classroom_structure_from_students_amb_grades(students_list,class_grades)
module_unit_names_hours = classroom.get_modules_unit_names_hours_from_first_student()

myexcel = Myexcel('grades.xlsx',group_name)
myexcel.create_module_header_with_modules_units_hours(module_unit_names_hours)
myexcel.create_first_column_with_student_names(students_list)
for i,student in enumerate(students_list):
    student_grades = classroom.extract_unit_grades(student,module_unit_names_hours)
    myexcel.set_passed_grades(i,student_grades)
myexcel.adjust_columns_width(5,2)
myexcel.set_grades_percent(4,2)
myexcel.draw_all_lines()
myexcel.freeze_until('B4')
myexcel.save_file()