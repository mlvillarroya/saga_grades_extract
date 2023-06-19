from classes.grades.Student import Student

class Classroom:
    def __init__(self,name = 'unnamed') -> None:
        self.name = name
        self.students = {}
    
    def get_name(self):
        return self.name
    
    def get_student(self,student_name : str):
        if student_name in self.students: return self.students[student_name]
        else:
            student = Student(student_name)
            self.students[student_name] = student
            return student
        
    def get_modules_unit_names_hours_from_student(self,student_index = 0):
        return self.students[list(self.students.keys())[student_index]].get_module_and_unit_names_hours()
    
    def get_student_names(self):
        names = []
        for student in self.students:
            names.append(student)
        return names
    
    def extract_unit_grades(self,student,module_unit_names_hours):
        student = self.get_student(student)
        grades = []
        for module,unit_hours in module_unit_names_hours:
            modul = student.get_modul(module)
            for unit,hours in unit_hours:
                grades.append(modul.get_unit(unit).get_grade())
        return grades
    
    def build_classroom_structure_from_students_amb_grades(self,students_list,class_grades):
        for i,student in enumerate(students_list):
            student = self.get_student(student)
            student.set_all_grades(class_grades[i])

    def extract_unit_grades_list(self,students_list,module_unit_names_hours):
        unit_grades_list = []
        for i,student in enumerate(students_list):
            unit_grades_list.append(self.extract_unit_grades(student,module_unit_names_hours))
        return unit_grades_list
