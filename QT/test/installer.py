'''
Created on 2018年5月9日

@author: 47812
'''
from PyInstaller.__main__ import run
# -F:打包成一个EXE文件 
# -w:不带console输出控制台，window窗体格式 
# --paths：依赖包路径 
# --icon：图标 
# --noupx：不用upx压缩 
# --clean：清理掉临时文件

if __name__ == '__main__':
    opts = ['-F', '-w', '--paths=C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin',
            '--paths=C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\plugins',
            '--paths=C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\xlrd',
            '--paths=C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\xlwt',
            '--paths=C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\future\\moves',
            
            'Main.py']

    run(opts)