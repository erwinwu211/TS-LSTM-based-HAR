# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python27\PyQt\Hellowindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1006, 452)
        Dialog.setSizeGripEnabled(True)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 441, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 180, 261, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 65, 271, 21))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 140, 221, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 370, 101, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
	self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 60, 93, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 331, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(30, 110, 371, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_3 = QtGui.QProgressBar(self.tab)
        self.progressBar_3.setGeometry(QtCore.QRect(30, 240, 371, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.pushButton_7 = QtGui.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 270, 221, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_10 = QtGui.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 310, 261, 41))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 65, 271, 21))
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 60, 93, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 270, 141, 51))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 331, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 370, 101, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
	self.connect(self.pushButton_8, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.pushButton_9 = QtGui.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 140, 221, 41))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.progressBar_2 = QtGui.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 110, 371, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.pushButton_11 = QtGui.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 190, 221, 41))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.videoPlayer = phonon.Phonon.VideoPlayer(Dialog)
        self.videoPlayer.setGeometry(QtCore.QRect(460, 20, 531, 341))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.seekSlider = phonon.Phonon.SeekSlider(Dialog)
        self.seekSlider.setGeometry(QtCore.QRect(470, 390, 511, 22))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ActionRecognition", None))
        self.pushButton_4.setText(_translate("Dialog", "Classify with Single Frame", None))
        self.label.setText(_translate("Dialog", "C:\\Python27", None))
        self.pushButton_3.setText(_translate("Dialog", "Process Single Frames Data", None))
        self.pushButton_2.setText(_translate("Dialog", "Quit", None))
        self.pushButton.setText(_translate("Dialog", "Open...", None))
        self.label_3.setText(_translate("Dialog", "The path of video you want to classify:", None))
        self.pushButton_7.setText(_translate("Dialog", "Compute OpticalFlow Frames", None))
        self.pushButton_10.setText(_translate("Dialog", "Classify with Two-Stream", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Recognize", None))
        self.label_2.setText(_translate("Dialog", "C:\\Python27", None))
        self.pushButton_5.setText(_translate("Dialog", "Open...", None))
        self.pushButton_6.setText(_translate("Dialog", "Start Train", None))
        self.label_4.setText(_translate("Dialog", "The path of videos to train:", None))
        self.pushButton_8.setText(_translate("Dialog", "Quit", None))
        self.pushButton_9.setText(_translate("Dialog", "Process Frames", None))
        self.pushButton_11.setText(_translate("Dialog", "Compute OpticalFlow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Train", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

