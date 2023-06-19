from classes.grades.Module import Module
from miscellaneous.Misc import Misc
class Student:
    def __init__(self,name = 'unnamed') -> None:
        self.name = name
        self.modules = {}
    def get_name(self):
        return self.name
    def get_module(self,module_name : str):
        if module_name in self.modules: return self.modules[module_name]
        else:
            module = Module(module_name)
            self.modules[module_name] = module
            return module
        
    def set_all_grades(self,grades):
        if not grades[0][0].startswith('M'): raise Exception("First grade must be a module")
        module = self.get_module(grades[0][0])
        module.set_grade(grades[0][1])
        module.set_hours(grades[0][2])
        j = 1
        while j < len(grades):
            if grades[j][0].startswith('M'):
                module = self.get_module(grades[j][0])
                module.set_grade(grades[j][1])
                module.set_hours(grades[j][2])
            else:
                unit = module.get_unit(grades[j][0])
                unit.set_grade(grades[j][1])
                unit.set_hours(grades[j][2])
            j+=1

    def get_module_names(self):
        names = []
        for module in self.modules:
            names.append(module)
        return names

    def get_module_and_unit_names_hours(self):
        names = []
        for module in self.modules:
            names.append([self.module_order(module),module,self.modules[module].get_unit_names_hours()])
        names.sort()
        names_sorted = [[name,units] for order,name,units in names]
        return names_sorted
    
    def module_order(self,module):
        module_name = self.get_module(module).get_name()
        trimmed = module_name[module_name.find('P') + 1 : module_name.find('.')]
        number = Misc.try_parse(trimmed)
        if number: return number
        else: return 0