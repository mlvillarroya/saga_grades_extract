from classes.web.Evaluationweb import Evaluationweb
from miscellaneous.Misc import Misc

STUDENT_ROW_XPATH = '//*[@title=\"STUDENT_NAME\"]/parent::*'
AVALUATION_ICON_XPATH = './/*[@title=\"Avalua\"]'

class StudentListWeb(Evaluationweb):
    def get_student_list(self):
        rows = self.get_table_rows()
        rows_cleaned = []
        for row in rows:
            data_cells = self.get_row_data_cells(row)
            if data_cells \
                    and (len(data_cells) >= 3) \
                    and Misc.tryparse(self.data_cell_content(data_cells[0])):
                rows_cleaned.append(self.data_cell_content(data_cells[1]))
        return rows_cleaned
    
    def click_into_student(self,student_name):
        student_row_xpath = STUDENT_ROW_XPATH.replace("STUDENT_NAME",student_name)
        student_row = self.search_element_by_XPATH(student_row_xpath)
        avaluation_icon = self.get_element_inside_element_by_xpath(student_row,AVALUATION_ICON_XPATH)
        if avaluation_icon: self.click_into_element(avaluation_icon)   