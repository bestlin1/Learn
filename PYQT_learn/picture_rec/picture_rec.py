# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picture_rec.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from aip import AipImageClassify


APP_ID = '14757979'
API_KEY = 'SGYvICm0gko3gKtoWN1tvPhf'
SECRET_KEY = 'FllhDBjTgItoOVfmGP9Ewb7bbvoGmNsT'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(775, 547)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.checkBox.setObjectName("checkBox")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 451, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 50, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 80, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 80, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(480, 110, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 310, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.rec_cai)
        self.pushButton_3.clicked.connect(self.car_rec)
        self.pushButton_4.clicked.connect(self.logo_rec)
        self.pushButton_5.clicked.connect(self.animal_rec)
        self.pushButton_6.clicked.connect(self.plant)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像识别示例程序"))
        self.pushButton.setText(_translate("Form", "打开图像"))
        self.checkBox.setText(_translate("Form", "检测人脸"))
        self.pushButton_2.setText(_translate("Form", "菜品识别"))
        self.pushButton_3.setText(_translate("Form", "车型识别"))
        self.pushButton_4.setText(_translate("Form", "商标识别"))
        self.pushButton_5.setText(_translate("Form", "动物识别"))
        self.pushButton_6.setText(_translate("Form", "识别植物"))


    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.Form, "选择图片", r"C:\Users\Tao xia\Desktop\Demo\测试图像")
        img = QImage()
        img.load(file_path)  # 载入图片
        self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)
        # 打开图片文件
        with open(file_path, 'rb') as f:
            image = f.read()
            self.textBrowser.clear()

        options={}
        options['baike_num']=5
        baike_info=client.advancedGeneral(image, options)['result'][0]
        print(baike_info)

        if not baike_info['baike_info']:
            baike_info=baike_info['keyword']
        else:
            baike_info=baike_info['description']

        self.textBrowser_2.clear()
        self.textBrowser_2.append(baike_info)
        self.image = image


    def rec_cai(self):  # 调用百度API
        self.textBrowser.clear()
        result = client.dishDetect(self.image)['result']  # 调用API
        display = ''
        for r in result:
            print("----r-----", r)
            display += '菜品名称：' + r['name'] + '\n'
            display += '卡路里：' + r['calorie'] + '\n'
            display += '置信度：' + r['probability'] + '\n'
            display += '\n'
        self.textBrowser.append(display)


    def car_rec(self):
        self.textBrowser.clear()
        result = client.carDetect(self.image)['result']
        print(result)
        display = ''
        for r in result:
            print("----r-----",r)
            display += '车型：' + r['name'] + '\n'
            display += '年份：' + r['year'] + '\n'
            display += '置信度：' + str(r['score']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def logo_rec(self):
        self.textBrowser.clear()
        result = client.logoSearch(self.image)['result']
        print(result)
        display = ''
        for r in result:
            display += '商标：' + r['name'] + '\n'
            display += '置信度：' + str(r['probability']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def animal_rec(self):
        self.textBrowser.clear()
        result = client.animalDetect(self.image)['result']
        display = ''
        for r in result:
            display += '动物：' + r['name'] + '\n'
            display += '置信度：' + str(r['score']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def plant(self):
        self.textBrowser.clear()
        result = client.plantDetect(self.image)['result']
        display = ''
        for r in result:
            display += '动物：' + r['name'] + '\n'
            display += '置信度：' + str(r['score']) + '\n'
            display += '\n'
        self.textBrowser.append(display)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())