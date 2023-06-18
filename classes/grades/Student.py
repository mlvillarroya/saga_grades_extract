from classes.grades.Modul import Modul

class Student:
    def __init__(self,name = 'unnamed') -> None:
        self.name = name
        self.moduls = {}
    def get_name(self):
        return self.name
    def get_modul(self,modul_name : str):
        if modul_name in self.moduls: return self.moduls[modul_name]
        else:
            modul = Modul(modul_name)
            self.moduls[modul_name] = modul
            return modul
        
    def set_all_grades(self,grades):
        if not grades[0][0].startswith('M'): raise Exception("First grade must be a module")
        modul = self.get_modul(grades[0][0])
        modul.set_grade(grades[0][1])
        modul.set_hours(grades[0][2])
        j = 1
        while j < len(grades):
            if grades[j][0].startswith('M'):
                modul = self.get_modul(grades[j][0])
                modul.set_grade(grades[j][1])
                modul.set_hours(grades[j][2])
            else:
                unit = modul.get_unit(grades[j][0])
                unit.set_grade(grades[j][1])
                unit.set_hours(grades[j][2])
            j+=1

    def get_module_names(self):
        names = []
        for module in self.moduls:
            names.append(module)
        return names

    def get_module_and_unit_names_hours(self):
        names = []
        for module in self.moduls:
            names.append([module,self.moduls[module].get_unit_names_hours()])
        return names