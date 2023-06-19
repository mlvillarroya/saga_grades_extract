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
module_unit_names_hours = classroom.get_modules_unit_names_hours_from_student(1)
unit_grades_list = classroom.extract_unit_grades_list(students_list,module_unit_names_hours)

myexcel = Myexcel(group_name + '_statistics.xlsx',group_name)
myexcel.create_passed_units_statistics(students_list,module_unit_names_hours,unit_grades_list)