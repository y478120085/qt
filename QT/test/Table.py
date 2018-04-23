'''
Created on 2018年4月2日

@author: Administrator

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
import xlrd
import xlwt

class table_data(QWidget):
    def __init__(self,filename='config/case/TestData1.xls'):
        super().__init__()
        self.filename=filename
        self.open_excel() 
        self.first_show()
    def open_excel(self):
        try:
            data=xlrd.open_workbook(self.filename)
            return  data
        except IOError:
            print ("文件打开异常")
            return  None         
    def first_show(self):       
        table = self.open_excel().sheet_by_index(0)
        self.table_widget=QTableWidget()
        self.table_widget.setRowCount(table.nrows)
        self.table_widget.setColumnCount(table.ncols+1)
        list1=[]
        for i in range(table.nrows):
            if i!=0:                
                list1.append(str(i))
        self.table_widget.setVerticalHeaderLabels(list1)          
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.removeRow(table.nrows-1)
        self.table_widget.setColumnWidth(0,40)
        hhbox = QHBoxLayout()
        for i in range(table.nrows):
            if i!=0:
                combox=QComboBox()
                combox.addItems(["通过","不通过"])
                self.table_widget.setCellWidget(i-1,table.ncols,combox)
                
            else:
                pass    
            for x in range(table.ncols):
                if i!=0:                   
                    excl_value=table.cell(i,x).value
                    X=QTableWidgetItem(str(excl_value))
                    self.table_widget.setItem(int(i-1),int(x),X)
                else:                    
                    labels_list=table.row_values(0)
                    labels_list.append("状态")
                    self.table_widget.setHorizontalHeaderLabels(labels_list)
        m=table.cell(0,table.ncols-1).value
        if  str(m)==None:            
            self.table_widget.removeColumn(table.ncols-1)         
        hhbox.addWidget(self.table_widget)    #把表格加入布局 
        self.setLayout(hhbox)            #创建布局    
#         print(combox.currentTextChanged())
#         print(combox.currentText())
#         self.connect(combox, QtCore.SIGNAL('activated(QString)'),self.onActivated)
#     def onActivated(self, text):  
#         print (text)        
#         self.table_widget.isw
    def open_path(self):
        return self.first_show()
    def save_table(self):
        wb = xlwt.Workbook(encoding = 'utf-8')
        sh = wb.add_sheet("mySheet")
        for x in range(self.table_widget.rowCount()):                
            for y in range(self.table_widget.columnCount()-1): 
                sh.write(x,y,str(self.table_widget.item(x,y).text()))
            sh.write(x,self.table_widget.columnCount()-1,"通过") 
        wb.save("report/report.xls")         
               
        

