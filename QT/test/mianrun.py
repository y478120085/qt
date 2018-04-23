'''

Created on 2018年4月17日

@author: Administrator
'''
import os
def  del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path,i) #取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
            print('正在移除文件: ' + path_file)
        else:
            del_file(path_file)
def delete_gap_dir(path):
    if os.path.isdir(path):
        for d in os.listdir(path):
            delete_gap_dir(os.path.join(path, d))
    if not os.listdir(path):
        os.rmdir(path)
        print('正在移除空目录: ' + path)
from subprocess import Popen, PIPE
import subprocess
from PyQt5.QtCore import QThread,pyqtSignal
class runexe(QThread):
    sinOut = pyqtSignal()       
    def __init__(self,path="config/app/release"):
        super(runexe,self).__init__()
        self.path=path
    def run(self):   
        configfilepath=self.path+ "/config"
        if os.path.exists(configfilepath)==True:
            p = Popen(['tasklist'],stdout=PIPE, stderr=PIPE)
            process_lists = str(p.stdout.read())
            while 'app.exe' in process_lists:
                Popen('taskkill /F /IM app.exe /T')
            del_file(configfilepath)
            delete_gap_dir(configfilepath)
        else:
            pass
        apppath=self.path+ "/app.exe"
        subprocess.call(apppath)
        self.sinOut.emit()
        print("测试程序已停止运行")       
if __name__=="__main__":
    ex=runexe()
    ex.run()
    
        
        
        