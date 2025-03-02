import xlsxwriter
from file1 import *
from file2 import *

class Cclass(Aclass, Bclass):
    def __init__(self, filename):
        Aclass.__init__(self)
        Bclass.__init__(self)
        self.Workbook = xlsxwriter.Workbook(filename)

    def add_sheet(self):
        self.sheet1 = self.Workbook.add_worksheet("Gold")
        self.sheet2 = self.Workbook.add_worksheet("Currency")
        return self.sheet1, self.sheet2

    def final_method(self):
        sheet1, sheet2 = self.add_sheet()

        sheet1.write("A1", "name")
        sheet1.write("B1", "price")

        sheet1.write_column("A2", self.lst_name1)
        sheet1.write_column("B2", self.lst_price1)
        
        sheet2.write("A1", "name")
        sheet2.write("B1", "price")

        sheet2.write_column("A2", self.lst_name2)
        sheet2.write_column("B2", self.lst_price2)

        self.Workbook.close()  

object1 = Cclass("file1014.xlsx")
object1.final_method()