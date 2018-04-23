'''
Created on 2018年4月19日

@author: Administrator
'''
from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout, QLabel, QPushButton, QFrame,QFileDialog,QDesktopWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
class InputDialog(QWidget):
    
    changetext = pyqtSignal(str) 
    def __init__(self,path='config/config.ini'):       
        super(InputDialog,self).__init__()
        self.path=path
        self.initUi()
    def initUi(self):
        self.setWindowTitle("配置文件")
        self.setGeometry(500,500,470,310)
        self.setWindowIcon(QIcon("res/aboutus.png"))  
        

        label1=QLabel("用例目录路径:")
        label2=QLabel("数据文件路径:")
        label3=QLabel("程序执行路径:")
        label4=QLabel("测试报告路径:")
        label5=QLabel("配置文件路径:")


        self.caseLable = QLabel("config/case")
        self.caseLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.dataLable = QLabel("config/casedata")
        self.dataLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.exeLable = QLabel("config/app")
        self.exeLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.reportLable = QLabel("report")
        self.reportLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.configLable = QLabel("config")
        self.configLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)


        caseButton=QPushButton("浏览")
        caseButton.clicked.connect(self.selectcase)      
        dataButton=QPushButton("浏览")
        dataButton.clicked.connect(self.selectdata)
        exeButton=QPushButton("浏览")
        exeButton.clicked.connect(self.selectexe)
        reportButton=QPushButton("浏览")
        reportButton.clicked.connect(self.selectreport)
        configButton=QPushButton("浏览")
        configButton.clicked.connect(self.selectconfig)
        self.changetext.connect(self.savemetainf)


        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        mainLayout.addWidget(self.caseLable,0,1)
        mainLayout.addWidget(caseButton,0,2)
        mainLayout.addWidget(label2,1,0)
        mainLayout.addWidget(self.dataLable,1,1)
        mainLayout.addWidget(dataButton,1,2)
        mainLayout.addWidget(label3,2,0)
        mainLayout.addWidget(self.exeLable,2,1)
        mainLayout.addWidget(exeButton,2,2)
        mainLayout.addWidget(label4,3,0)
        mainLayout.addWidget(self.reportLable,3,1)
        mainLayout.addWidget(reportButton,3,2)
        mainLayout.addWidget(label5,4,0)
        mainLayout.addWidget(self.configLable,4,1)
        mainLayout.addWidget(configButton,4,2)

        


        self.setLayout(mainLayout)
        self.center()
        self.savemetainf()
    def selectcase(self):
        path = QFileDialog.getOpenFileName(self, '选择测试用例',  
                                    './config/case',  
                                    'excel(*.xls)')
        self.filename=path[0]
        chu=self.caseLable.text()
        self.caseLable.setText(self.filename)
        dangqian=self.caseLable.text()
        if chu!=dangqian:
            self.changetext.emit(dangqian)
        else:
            pass   
    def selectdata(self):
        path = QFileDialog.getOpenFileName(self, '选择数据文件',  
                                    './config/casedata',  
                                    'extension(*.xml)')
        filename=path[0]
        chu=self.dataLable.text()
        self.dataLable.setText(filename)
        dangqian=self.dataLable.text()
        if chu!=dangqian:
            self.changetext.emit(dangqian)
        else:
            pass  

    def selectexe(self):
        path = QFileDialog.getOpenFileName(self, '选择程序执行',  
                                    './config/app',  
                                    'app(*.exe)')
        filename=path[0]
        chu=self.exeLable.text()
        self.exeLable.setText(filename)
        dangqian=self.exeLable.text()
        if chu!=dangqian:
            self.changetext.emit(dangqian)
        else:
            pass 
    def selectreport(self):
        path = QFileDialog.getOpenFileName(self, '选择测试报告',  
                                    './report',  
                                    'excel(*.xls)')
        filename=path[0]
        chu=self.reportLable.text()
        self.reportLable.setText(filename)
        dangqian=self.reportLable.text()
        if chu!=dangqian:
            self.changetext.emit(dangqian)
        else:
            pass 
    def selectconfig(self):
        path = QFileDialog.getOpenFileName(self, '选择配置文件',  
                                    './config',  
                                    'config(*.ini)')
        filename=path[0]
        chu=self.configLable.text()
        self.configLable.setText(filename)
        dangqian=self.configLable.text()
        if chu!=dangqian:
            self.path=dangqian
            with open(self.path, mode='w+', encoding='utf-8') as f:
                f.write("用例位置:         "+self.caseLable.text())
                f.write("\n"+"xml路径:          "+self.dataLable.text())
                f.write("\n"+"运行程序路径:     "+self.exeLable.text())
                f.write("\n"+"报告输出路径:     "+self.reportLable.text())
                f.write("\n"+"配置文件路径:     "+self.configLable.text())
        else:
            pass 
    def center(self):
        qr = self.frameGeometry()              
        cp = QDesktopWidget().availableGeometry().center()                                               
        qr.moveCenter(cp)                      
        self.move(qr.topLeft())
    def savemetainf(self):
        with open(self.path, mode='w+', encoding='utf-8') as f:
            f.write("用例位置:         "+self.caseLable.text())
            f.write("\n"+"xml路径:          "+self.dataLable.text())
            f.write("\n"+"运行程序路径:     "+self.exeLable.text())
            f.write("\n"+"报告输出路径:     "+self.reportLable.text())

    
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())