from classes.web.Evaluationweb import Evaluationweb

GRADES_XPATH = "(((//table)[4]//tr)[4]//input[@type='text'])"

class UnitGradesWeb(Evaluationweb):
    
    def get_unit_names(self):
        names = []
        rows = self.get_table_rows()
        rows = rows[2:]
        for row in rows:
            cells = self.get_row_data_cells(row)
            if not cells or len(cells) < 2: continue
            names.append(cells[1].text)  
        return names

    def get_student_grades(self,row,unit_names):
            cells = self.get_row_data_cells(row)
            if not cells: return False
            student_name = cells[0].text
            grades = []
            cells = self.search_elements_by_XPATH(GRADES_XPATH)
            cells = cells[0:len(unit_names)]
            for i,cell in enumerate(cells):
                grades.append([unit_names[i],cell.get_attribute("value")])
            return [student_name,grades]

    def get_module_matrix(self):
        unit_names = self.get_unit_names()
        rows = self.get_table_rows(table_index = 3)
        rows = rows[3:]
        matrix = []
        for row in rows:
            matrix.append(self.get_student_grades(row,unit_names))
        return matrix
        
