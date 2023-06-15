class Unit:

    def __init__(self,name = 'unnamed',grade = 'NP') -> None:
        self.name = name
        self.grade = grade    
    def get_name(self):
        return self.name
    def set_grade(self,grade : int):
        self.grade = grade