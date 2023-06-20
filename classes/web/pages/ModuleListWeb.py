from classes.web.pages.Evaluationweb import Evaluationweb

class ModuleListWeb(Evaluationweb):
    def get_module_name(self,row):
        cells = self.get_row_data_cells(row)
        if cells and len(cells)>1 : return cells[1].text
        else: return False
    def go_to_module_grades(self,row):
        cells = self.get_row_data_cells(row)
        if cells and len(cells)>1 : 
            icon = self.get_css_selector_inside_element(cells[2],'img')
            self.click_into_element(icon)