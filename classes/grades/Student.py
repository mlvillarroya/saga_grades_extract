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
        
    def get_grades(self,grades):
        if not grades[0][0].startswith('M'): raise Exception("First grade must be a module")
        modul = self.get_modul(grades[0][0])
        j = 1
        while j < len(grades):
            if grades[j][0].startswith('M'):
                modul = self.get_modul(grades[j][0])
            else:
                unit = modul.get_unit(grades[j][0])
                unit.set_grade(grades[j][1])
            j+=1

    def get_module_names(self):
        names = []
        for module in self.moduls:
            names.append(module)
        return names