# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\plugins', 'C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\xlrd', 'C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\xlwt', 'C:\\Users\\47812\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\future\\moves', 'C:\\Users\\47812\\cangku\\QT\\test'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )