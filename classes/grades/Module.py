from classes.grades.Unit import Unit
from classes.grades.BasicGrade import BasicGrade

class Module(BasicGrade):
    def __init__(self, name = 'unnamed', grade = '') -> None:
        self.units = {}
        super().__init__(name,grade)
    
    def get_unit(self,unit_name : str):
        if unit_name in self.units: return self.units[unit_name]
        else:
            unit = Unit(unit_name)
            self.units[unit_name] = unit
            return unit
    
    def get_unit_names_hours(self):
        names = []
        for unit in self.units:
            names.append([unit,self.get_unit(unit).get_hours()])
        return names