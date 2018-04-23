'''
Created on 2018年3月30日

@author: Administrator
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from test.Table import table_data
# from test.Data import *
from test.ProfileWizard import InputDialog
from test.mianrun import runexe
from test.aboutqt import Ui_AboutDialog
import time
class window(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.myui()        
    def myui(self):
        self.widget1 = table_data()
        self.widget1.first_show() 
        self.setCentralWidget(self.widget1)
        self.qtdialog__init__()
        
        exitAction=QAction(QIcon("res/exit.png"),"退出",self)
        exitAction.setShortcut("ctrl+q")
        exitAction.setStatusTip("退出")       
        exitAction.triggered.connect(qApp.quit)
        
        openfile=QAction(QIcon("res/open.png"),"打开测试用例",self)
        openfile.setShortcut("ctrl+o")
        openfile.setStatusTip("打开测试用例")        
        openfile.triggered.connect(self.openfile_data)
        
        savefile=QAction(QIcon("res/save.png"),"保存",self)
        savefile.setShortcut("ctrl+s")
        savefile.setStatusTip("保存")       
        savefile.triggered.connect(self.save)
        
        saveas=QAction(QIcon("res/save.png"),"另保存",self)
        saveas.setShortcut("ctrl+s+s")
        saveas.setStatusTip("另保存")       
        saveas.triggered.connect(self.save_as)
        
        self.runaction=QAction(QIcon("res/run.png"),"运行",self)
        self.runaction.setShortcut("ctrl+r")
        self.runaction.setStatusTip("运行")
        self.runaction.triggered.connect(self.run)
        
        qtaction=QAction(QIcon("res/qt.png"),"关于qt",self)
        qtaction.setStatusTip("关于qt")
        qtaction.triggered.connect(self.qt)
        
        aboutaction=QAction(QIcon("res/aboutus.png"),"关于我们",self)
        aboutaction.setStatusTip("关于我们")
        aboutaction.triggered.connect(self.aboutus)
        
        freshenaction=QAction(QIcon("res/aboutus.png"),"刷新",self)
        freshenaction.setStatusTip("刷新列表")
        freshenaction.setShortcut("F5")
        freshenaction.triggered.connect(self.guide)

        
        filemenubar1=self.menuBar()
        filemenu=filemenubar1.addMenu("文件")       
        filemenu.addAction(openfile)
        filemenu.addAction(self.runaction)
        filemenu.addAction(savefile)
        filemenu.addAction(saveas)        
        filemenu.addAction(exitAction)
        
        filemenubar2=self.menuBar()
        filemenu=filemenubar2.addMenu("关于")       
        filemenu.addAction(qtaction)
        filemenu.addAction(aboutaction)

        
        filemenubar3=self.menuBar()
        filemenu=filemenubar3.addMenu("刷新")       
        filemenu.addAction(freshenaction)
        
    
        timer=MyTimer() 
        tb=self.addToolBar("工具栏")      
        tb.addAction(self.runaction)    
        tb.addAction(openfile)      
        tb.addAction(savefile)
        
        tb.addAction(freshenaction)
        tb.setMovable(True)
        tb.insertSeparator(openfile)
        tb.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        tb.addWidget(timer)
                
        self.text=QTextEdit()
        self.text.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)

        self.pbar=QProgressBar(self)        
        self.pbar.setGeometry(1050, 730, 100, 20) 
        self.setGeometry(100,100,1120,750)        
        self.setWindowTitle("自动化测试")     
        self.setWindowIcon(QIcon("res/aboutus.png"))  
        self.center()
        self.show()
    def qtdialog__init__(self):
        self.Form=QDialog()
        self.ui=Ui_AboutDialog()
        self.ui.setupUi(self.Form)
        self.ui.retranslateUi(self.Form)    
    def guide(self): 
        self.myshow1=InputDialog()
        self.myshow1.show()
    def run(self):               
        self.runaction.setDisabled(True)
        self.runmian=runexe()        
        self.runmian.sinOut.connect(self.finsh)
        self.runmian.start()
        print("测试程序正在启动......")
    def finsh(self):
        self.runaction.setDisabled(False) 
  
    def openfile_data(self):
        path = QFileDialog.getOpenFileName(self, '选择测试用例',  
                                    './config/case',  
                                    'excel(*.xls)')
        filename=path[0]
        self.widget = table_data(filename)        
        self.widget.open_path() 
        self.setCentralWidget(self.widget)          
    def save(self):        
        self.widget = table_data()        
        self.widget.save_table()
    def center(self):
        qr = self.frameGeometry()              
        cp = QDesktopWidget().availableGeometry().center()                                               
        qr.moveCenter(cp)                      
        self.move(qr.topLeft())
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, '提示？',
            "你确定要退出么?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def aboutus(self):
        import webbrowser
        webbrowser.open("http://www.microcorecn.com/about/toMcHome.do", new=0, autoraise=True)
    def qt(self):
        self.Form.show()
    def save_as(self): 
#         fname2 = QFileDialog.getOpenFileName(self, 'save as', '/home')
#         filepath=fname2[0]
        pass
class MyTimer(QWidget):
    def __init__(self, parent = None):
        super(MyTimer, self).__init__(parent)                        
        self.lcd = QLCDNumber()      
        self.lcd.setDigitCount(10)      
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
 
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)       
        self.setLayout(layout)          
        self.timer = QTimer()      
        self.timer.setInterval(1000)       
        self.timer.start()            
        self.timer.timeout.connect(self.onTimerOut)
    def onTimerOut(self):        
        self.lcd.display(time.strftime("%X",time.localtime()))
