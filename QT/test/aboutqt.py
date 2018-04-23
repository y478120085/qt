import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QLabel, QApplication,QDesktopWidget, QVBoxLayout,QGroupBox
from PyQt5.QtGui import QPixmap,QIcon


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  
class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(428, 201)
        AboutDialog.setWindowIcon(QIcon("res/aboutus.png"))
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.iconLabel = QtWidgets.QLabel(self.groupBox)
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap("res/qt.png"))
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.verticalLayout_3.addWidget(self.iconLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About Qt"))
        AboutDialog.setWhatsThis(_translate("AboutDialog", "Qt "))
        self.groupBox.setTitle(_translate("AboutDialog", "PYQT5"))
        self.iconLabel.setWhatsThis(_translate("AboutDialog", "Product Icon"))
        self.label_2.setWhatsThis(_translate("AboutDialog", "About test tool "))
        self.label_2.setText(_translate("AboutDialog", "About test tool "))
        self.label_3.setText(_translate("AboutDialog", "Version:"))
        self.label_4.setText(_translate("AboutDialog", "v1.0.0"))
        self.label_5.setText(_translate("AboutDialog", "Company:"))
        self.label_6.setText(_translate("AboutDialog", "Chengdu Microcore Technology Corp., LTD"))
        self.label_7.setText(_translate("AboutDialog", "Homepage:"))
        self.label_8.setText(_translate("AboutDialog", "www.microcorecn.com"))
        self.label_9.setText(_translate("AboutDialog", "Tel:"))
        self.label_10.setText(_translate("AboutDialog", "（8628）83378533 "))        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form=QtWidgets.QDialog()
    ui=Ui_AboutDialog()
    ui.setupUi(Form)
    ui.retranslateUi(Form)
    Form.show()
    sys.exit(app.exec_())

