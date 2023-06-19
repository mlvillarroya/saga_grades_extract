from classes.web.Evaluationweb import Evaluationweb
from miscellaneous.Misc import Misc

GRADES_TABLE_ID = 'taula_38956696119'
GRADE_ROWS_XPATH = './/tr[contains(@class,"td")]'
GRADES_INPUT_XPATH = ".//input[@type='text']"
GRADES_SELECT_XPATH = ".//option[@selected='selected']"
HOURS_XPATH = './/b'

class StudentGradesWeb(Evaluationweb):

    def get_grade_from_cell(self,cell):
        grade_element = self.get_element_inside_element_by_xpath(cell,GRADES_INPUT_XPATH)
        if grade_element: return grade_element.get_attribute("value")
        else: grade_element = self.get_element_inside_element_by_xpath(cell,GRADES_SELECT_XPATH)
        if grade_element: return grade_element.get_attribute("value")
        else: return 0

    def get_hours_from_cell(self,cell):
        hours_cell = self.get_element_inside_element_by_xpath(cell,HOURS_XPATH)
        if (hours_cell) and Misc.try_parse(hours_cell.text): return int(hours_cell.text)
        else: return 0

    def get_grades_matrix(self):
        table = self.search_by_ID(GRADES_TABLE_ID)
        grade_rows = self.get_elements_inside_element_by_xpath(table,GRADE_ROWS_XPATH)
        if not grade_rows: raise Exception("Not grades in this screen")
        grades = []
        for row in grade_rows:
            cells = self.get_row_data_cells(row)
            if not cells: raise Exception("Row without cells")
            grades.append([cells[1].text,self.get_grade_from_cell(cells[3]),self.get_hours_from_cell(cells[2])])
        return grades