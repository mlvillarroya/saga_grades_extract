from openpyxl import Workbook 
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder 
from openpyxl.utils import get_column_letter

class Myexcel:
    def __init__(self,file_name,sheet_name = 'Sheet') -> None:
        self.wb = Workbook()
        self.ws = self.wb['Sheet']
        self.ws.title = sheet_name
        self.file_name = file_name

    def create_module_header_with_modules_units(self,module_unit_list):
        # ROW 1: MODULES, ROW 2: UNITS #
        col = 2
        for module,units in module_unit_list:
            start_col = col
            self.ws.cell(row=1, column=col).value = module
            for unit in units:
                self.ws.cell(row=2, column=col).value = unit
                col += 1
            end_col = col - 1
            self.ws.merge_cells(start_row=1, start_column=start_col, end_row=1, end_column=end_col)
    
    def create_first_column_with_student_names(self,student_list):
        for row,student in enumerate(student_list,start=3):
            self.ws.cell(row=row, column=1).value = student
            # self.adjust_col_dimensions()

    # def adjust_col_dimensions(self):        
    #     dims = {}
    #     for row in self.ws.rows:
    #         for cell in row:
    #             if cell.value:
    #                 dims[cell.column] = max((dims.get(cell.column, 0), len(str(cell.value))))    
    #     for col, value in dims.items():
    #         self.ws.column_dimensions[get_column_letter(col)].width = value

    def save_file(self):
        self.wb.save(self.file_name)