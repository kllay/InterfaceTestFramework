#coding:utf-8
import  xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        try:
            if file_name:
                if sheet_id:
                    self.sheet_id=sheet_id
                else:
                    self.sheet_id = 0
                self.file_name = file_name
            else:
                self.file_name='../dataconfig/jiekou.xls'
                self.sheet_id=0
            self.data=self.get_data()
        except:
            print("excel文档不存在!"+self.file_name)

    #获取excel内容
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        return tables
    #获取总行数
    def get_rows(self):
        rows=self.data.nrows
        return rows
    #获取某行某列的值
    def get_value(self,row,col):
        value=self.data.cell_value(row,col)
        return  value

    #写入实际结果值
    def write_value(self,row,col,value):
        try:
            read_data=xlrd.open_workbook(self.file_name)
            write_data=copy(read_data)
            sheet_data=write_data.get_sheet(0)
            sheet_data.write(row,col,value)
            write_data.save(self.file_name)
        except:
            print("excel文档被打开了!请先关闭")

    #根据对应caseid 找到行的内容
    def get_rows_data(self,case_id):
        row_num=self.get_rows_num(case_id)
        row_data=self.get_rows_value(row_num)
        return  row_data

    #根据对应的caseid 查找到行号
    def get_rows_num(self,case_id):
        num=0
        cols_data=self.get_col_value()
        for col_data in cols_data:
            if case_id in col_data:
                return  num
            num=num+1

    #根据行号找到对应的内容
    def get_rows_value(self,row):
        table=self.data
        row_Data=table.row_values(row)
        return row_Data

    #获取某一列的值
    def get_col_value(self,col_id=None):
        if col_id != None:
            cols=self.data.col_values(col_id)
        else:
            cols=self.data.col_values(0)
        return cols






if __name__=='__main__':
    exceldx=OperationExcel()
    #data=exceldx.get_data('jiekou.xlsx',0)
    print(exceldx.get_rows())
    print(exceldx.get_value(1,3))










