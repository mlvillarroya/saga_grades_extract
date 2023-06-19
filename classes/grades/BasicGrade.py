from miscellaneous.Misc import Misc
class BasicGrade:

    def __init__(self,name = 'unnamed', grade = '', hours = 0) -> None:
        self.name = name
        self.grade = grade
        self.hours = hours
        
    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade
    def get_hours(self):
        return self.hours
    
    def compute_grade(self,grade):
        if (grade == 'NP') or (grade == ''): return grade
        if (grade.startswith('A) ')): 
            grade = grade[3:]
        grade = Misc.try_parse(grade)
        if not grade: raise Exception("Problems parsing grade")
        return grade
    
    def compute_hours(self,hours):
        hours = Misc.try_parse(hours)
        if not hours: raise Exception("Problems parsing hours")
        return hours
    
    def set_grade(self,grade):
        grade = self.compute_grade(grade)
        self.grade = grade

    def set_hours(self,hours):
        grade = self.compute_hours(hours)
        self.hours = hours
