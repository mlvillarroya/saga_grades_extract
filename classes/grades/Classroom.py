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
    def compute_module_matrix(self,matrix):
        for row in matrix:
            student = self.get_student(row[0])
            print(student.name)
            for unit in row[1]:
                print(unit[0])
                print(unit[1])
