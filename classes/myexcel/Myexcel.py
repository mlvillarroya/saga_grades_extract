from openpyxl import Workbook 
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder 
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

class Myexcel:
    def __init__(self,file_name,sheet_name = 'Sheet') -> None:
        self.wb = Workbook()
        self.ws = self.wb['Sheet']
        self.ws.title = sheet_name
        self.file_name = file_name

    def create_module_header_with_modules_units_hours(self,module_unit_hours_list):
        # ROW 1: MODULES, ROW 2: UNITS #
        col = 2
        for module,units_hours in module_unit_hours_list:
            start_col = col
            self.ws.cell(row=1, column=col).value = module[:3]
            self.ws.cell(row=1, column=col).comment = Comment(module,'admin')
            for unit,hours in units_hours:
                self.ws.cell(row=2, column=col).value = unit[:3]
                self.ws.cell(row=2, column=col).comment = Comment(unit,'admin')
                self.ws.cell(row=3, column=col).value = hours
                col += 1
            end_col = col - 1
            self.ws.merge_cells(start_row=1, start_column=start_col, end_row=1, end_column=end_col)
    
    def create_first_column_with_student_names(self,student_list):
        for row,student in enumerate(student_list,start=3):
            self.ws.cell(row=row, column=1).value = student
        self.adjust_col_dimensions(1)

    def adjust_col_dimensions(self,col_number):
        col_letter = get_column_letter(col_number)        
        dim = 0        
        for cell in self.ws[col_letter]:
            if cell.value:
                dim = max(dim, len(str(cell.value)))    
        self.ws.column_dimensions[col_letter].width = dim

    def save_file(self):
        self.wb.save(self.file_name)