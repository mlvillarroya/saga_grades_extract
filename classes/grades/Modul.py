from classes.grades.Unit import Unit

class Modul:
    def __init__(self,name = 'unnamed') -> None:
        self.name = name
        self.units = {}
    
    def get_name(self):
        return self.name
    def get_unit(self,unit_name : str):
        if unit_name in self.units: return self.units[unit_name]
        else:
            unit = Unit(unit_name)
            self.units[unit_name] = unit
            return unit
    
    def get_unit_names(self):
        names = []
        for unit in self.units:
            names.append(unit)
        return names