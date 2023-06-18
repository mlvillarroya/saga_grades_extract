from miscellaneous.Misc import Misc
class BasicGrade:

    def __init__(self,name = 'unnamed', grade = '') -> None:
        self.name = name
        self.grade = grade
        
    def get_name(self):
        return self.name
    
    def compute_grade(self,grade):
        if (grade == 'NP'): return grade
        if (grade.startswith('A) ')): 
            grade = grade[3:]
        grade = Misc.tryparse(grade)
        if not grade: raise Exception("Problems parsing grade")
        return grade

    def set_grade(self,grade):
        grade = self.compute_grade(grade)
        self.grade = grade
