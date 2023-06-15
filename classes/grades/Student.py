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