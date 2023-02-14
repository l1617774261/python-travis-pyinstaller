#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-10 14:05
# @Author  : ARM
# @Site    : 
# @File    : py2exe.py
# @Software: PyCharm
import py2exe_ui
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import os
from pathlib import PureWindowsPath

def dabao():
    """执行打包操作"""
    fullpath = ui.fileT.text()
    f = PureWindowsPath(fullpath)
    filedir = fullpath.replace(f.name,"")
    if ui.checkBox.isChecked() == True:

"       ""判断是否"""        second = os.system("cd " + filedir + "&&pyinstaller -F --clean -w " + fullpath)
if second == 0:
            QMessageBox.about(mainWindow, "执行结果", "恭喜！成功打包exe")
        else:
            QMessageBox.about(mainWindow, "执行结果", "请选择py文件路径")
    else:
        second = os.system("cd " + filedir + "&&pyinstaller -F --clean " + fullpath)
        if second == 0:
            QMessageBox.about(mainWindow, "执行结果", "恭喜，成功打包exe")
        else:
            QMessageBox.about(mainWindow, "执行结果", "请选择py文件路径")


if __name__=="__main__":
    app = QApplication(sys.argv)
    #创建一个窗口
    mainWindow = QMainWindow()
    ui = py2exe_ui.Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.pushButton_2.clicked.connect(dabao)
    mainWindow.show()
    sys.exit(app.exec_())
    
    #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-10 14:05
# @Author  : ARM
# @Site    : 
# @File    : py2exe_ui.py
# @Software: PyCharm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 设置按键参数
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(70, 20, 101, 31))
        self.file.setObjectName("file")
        self.file.setStyleSheet("background-color:rgb(111,180,219)")
        # 设置显示窗口参数
        self.fileT = QtWidgets.QLineEdit(self.centralwidget)
        self.fileT.setGeometry(QtCore.QRect(180, 20, 381, 31))
        self.fileT.setObjectName("file")
        # 是否隐藏
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(80, 120, 241, 21))
        self.checkBox.setObjectName("checkBox")
        # 打包按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 160, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        # exe存放路径描述
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 241, 21))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setPointSize(15)
        # self.label_3.setFont(font)  # 跟随系统字体
        # 页面布局
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################button按钮点击事件回调函数################
        self.file.clicked.connect(self.msg)   #  选择py文件
        # self.file_exe.clicked.connect(self.openimage)  # 选择图片
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "py2exe by test"))
        self.file.setText(_translate("MainWindow", "选择py文件"))
        self.fileT.setText(_translate("MainWindow", ""))
        self.checkBox.setText(_translate("MainWindow", "启动exe程序时是否隐藏cmd窗口"))
        self.pushButton_2.setText(_translate("MainWindow", "开始打包"))
        # self.file_exe.setText(_translate("MainWindow", "选择exe文件"))
        # self.fileT_exe.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "注：exe保存路径为源文件所在文件！"))


    def msg(self, Filepath):
        """选择文件路径"""
        get_filename_path, ok = QFileDialog.getOpenFileName(None, "选取单个文件", "C:/", "All Files (*);;Text Files (*.txt)")
        if ok:
            self.fileT.setText(str(get_filename_path))

    # def openimage(self, Filepath):
    #     """选择图片路径"""
    #     imgName, imgType = QFileDialog.getOpenFileName(None, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
    #     # jpg = QtGui.QPixmap(imgName).scaled(self.fileT_exe.width(), self.fileT_exe.height())
    #     self.fileT_exe.setText(imgName)
