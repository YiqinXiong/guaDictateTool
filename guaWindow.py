# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guaWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_add.setMinimumSize(QtCore.QSize(36, 36))
        self.pushButton_add.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_5.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_remove.setMinimumSize(QtCore.QSize(36, 36))
        self.pushButton_remove.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_remove.setFont(font)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout_5.addWidget(self.pushButton_remove)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_undo = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_undo.setMinimumSize(QtCore.QSize(36, 36))
        self.pushButton_undo.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButton_undo.setStyleSheet("QPushButton{border-image: url(:/redo-undo/undo.png);}\n"
"QPushButton:hover{border-image: url(:/redo-undo/undo-2.png);}\n"
"QPushButton:pressed{border-image: url(:/redo-undo/undo-1.png);}")
        self.pushButton_undo.setText("")
        self.pushButton_undo.setObjectName("pushButton_undo")
        self.horizontalLayout_5.addWidget(self.pushButton_undo)
        self.pushButton_redo = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_redo.setMinimumSize(QtCore.QSize(36, 36))
        self.pushButton_redo.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButton_redo.setStyleSheet("QPushButton{border-image: url(:/redo-undo/redo.png);}\n"
"QPushButton:hover{border-image: url(:/redo-undo/redo-2.png);}\n"
"QPushButton:pressed{border-image: url(:/redo-undo/redo-1.png);}")
        self.pushButton_redo.setText("")
        self.pushButton_redo.setObjectName("pushButton_redo")
        self.horizontalLayout_5.addWidget(self.pushButton_redo)
        self.pushButton_add_word_save = QtWidgets.QPushButton(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        self.pushButton_add_word_save.setFont(font)
        self.pushButton_add_word_save.setObjectName("pushButton_add_word_save")
        self.horizontalLayout_5.addWidget(self.pushButton_add_word_save)
        self.gridLayout_11.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.tableWidget_add_word = QtWidgets.QTableWidget(self.groupBox_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_add_word.setFont(font)
        self.tableWidget_add_word.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget_add_word.setObjectName("tableWidget_add_word")
        self.tableWidget_add_word.setColumnCount(5)
        self.tableWidget_add_word.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_add_word.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_add_word.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_add_word.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_add_word.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_add_word.setHorizontalHeaderItem(4, item)
        self.tableWidget_add_word.horizontalHeader().setVisible(False)
        self.tableWidget_add_word.verticalHeader().setVisible(False)
        self.gridLayout_11.addWidget(self.tableWidget_add_word, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_11)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox_year = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_year.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_year.setCurrentText("")
        self.comboBox_year.setObjectName("comboBox_year")
        self.horizontalLayout_3.addWidget(self.comboBox_year)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_lesson = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_lesson.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_lesson.setObjectName("comboBox_lesson")
        self.horizontalLayout_3.addWidget(self.comboBox_lesson)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_search_word = QtWidgets.QLabel(self.groupBox_2)
        self.label_search_word.setObjectName("label_search_word")
        self.horizontalLayout_3.addWidget(self.label_search_word)
        self.lineEdit_search_word = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_search_word.setMinimumSize(QtCore.QSize(240, 0))
        self.lineEdit_search_word.setObjectName("lineEdit_search_word")
        self.horizontalLayout_3.addWidget(self.lineEdit_search_word)
        self.pushButton_search_word = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_search_word.setObjectName("pushButton_search_word")
        self.horizontalLayout_3.addWidget(self.pushButton_search_word)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableWidget_search_word = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_search_word.setObjectName("tableWidget_search_word")
        self.tableWidget_search_word.setColumnCount(5)
        self.tableWidget_search_word.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_word.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_word.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_word.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_word.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_word.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_6.addWidget(self.tableWidget_search_word)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_history = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_history.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_history.setObjectName("listWidget_history")
        self.verticalLayout_4.addWidget(self.listWidget_history)
        self.pushButton_history = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_history.setObjectName("pushButton_history")
        self.verticalLayout_4.addWidget(self.pushButton_history)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.horizontalLayout_6.setStretch(0, 8)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_range_num = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_range_num.setFont(font)
        self.label_range_num.setObjectName("label_range_num")
        self.verticalLayout_2.addWidget(self.label_range_num)
        self.spinBox_num = QtWidgets.QSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.spinBox_num.setFont(font)
        self.spinBox_num.setMaximum(999)
        self.spinBox_num.setSingleStep(5)
        self.spinBox_num.setProperty("value", 30)
        self.spinBox_num.setObjectName("spinBox_num")
        self.verticalLayout_2.addWidget(self.spinBox_num)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton_range_start1 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton_range_start1.setFont(font)
        self.pushButton_range_start1.setObjectName("pushButton_range_start1")
        self.verticalLayout_2.addWidget(self.pushButton_range_start1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 2, 0, 1, 1)
        self.pushButton_range_start2 = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pushButton_range_start2.setFont(font)
        self.pushButton_range_start2.setObjectName("pushButton_range_start2")
        self.gridLayout_5.addWidget(self.pushButton_range_start2, 7, 0, 1, 4)
        self.spinBox_text_from = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_text_from.setMinimum(0)
        self.spinBox_text_from.setMaximum(6)
        self.spinBox_text_from.setProperty("value", 0)
        self.spinBox_text_from.setObjectName("spinBox_text_from")
        self.gridLayout_5.addWidget(self.spinBox_text_from, 3, 1, 1, 1)
        self.spinBox_text_to = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_text_to.setMaximum(6)
        self.spinBox_text_to.setProperty("value", 6)
        self.spinBox_text_to.setObjectName("spinBox_text_to")
        self.gridLayout_5.addWidget(self.spinBox_text_to, 3, 3, 1, 1)
        self.label_range_year = QtWidgets.QLabel(self.groupBox_5)
        self.label_range_year.setObjectName("label_range_year")
        self.gridLayout_5.addWidget(self.label_range_year, 1, 0, 1, 1)
        self.label_range_to = QtWidgets.QLabel(self.groupBox_5)
        self.label_range_to.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_range_to.setObjectName("label_range_to")
        self.gridLayout_5.addWidget(self.label_range_to, 3, 2, 1, 1)
        self.spinBox_year = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_year.setMinimum(2010)
        self.spinBox_year.setMaximum(2021)
        self.spinBox_year.setObjectName("spinBox_year")
        self.gridLayout_5.addWidget(self.spinBox_year, 1, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 0, 0, 1, 1)
        self.label_range_text = QtWidgets.QLabel(self.groupBox_5)
        self.label_range_text.setObjectName("label_range_text")
        self.gridLayout_5.addWidget(self.label_range_text, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 6, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_chinese_attr = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_chinese_attr.setFont(font)
        self.label_chinese_attr.setObjectName("label_chinese_attr")
        self.gridLayout_8.addWidget(self.label_chinese_attr, 3, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_finish = QtWidgets.QLabel(self.groupBox_6)
        self.label_finish.setObjectName("label_finish")
        self.gridLayout_6.addWidget(self.label_finish, 0, 0, 1, 1)
        self.progressBar_finish = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_finish.setProperty("value", 24)
        self.progressBar_finish.setObjectName("progressBar_finish")
        self.gridLayout_6.addWidget(self.progressBar_finish, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_6, 0, 0, 1, 3)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_timer = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_timer.setFont(font)
        self.label_timer.setObjectName("label_timer")
        self.gridLayout_7.addWidget(self.label_timer, 0, 0, 1, 1)
        self.lcdNumber_timer = QtWidgets.QLCDNumber(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.lcdNumber_timer.setFont(font)
        self.lcdNumber_timer.setObjectName("lcdNumber_timer")
        self.gridLayout_7.addWidget(self.lcdNumber_timer, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_7, 1, 0, 1, 3)
        self.lineEdit_input_chinese = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_input_chinese.setObjectName("lineEdit_input_chinese")
        self.gridLayout_8.addWidget(self.lineEdit_input_chinese, 5, 1, 1, 2)
        self.label_word = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.label_word.setFont(font)
        self.label_word.setObjectName("label_word")
        self.gridLayout_8.addWidget(self.label_word, 2, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.pushButton_get_answer = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_get_answer.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_get_answer.setFont(font)
        self.pushButton_get_answer.setObjectName("pushButton_get_answer")
        self.horizontalLayout.addWidget(self.pushButton_get_answer)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.pushButton_add_to_notebook = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_add_to_notebook.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_add_to_notebook.setFont(font)
        self.pushButton_add_to_notebook.setObjectName("pushButton_add_to_notebook")
        self.horizontalLayout.addWidget(self.pushButton_add_to_notebook)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.pushButton_next_word = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_next_word.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_next_word.setFont(font)
        self.pushButton_next_word.setObjectName("pushButton_next_word")
        self.horizontalLayout.addWidget(self.pushButton_next_word)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.gridLayout_8.addLayout(self.horizontalLayout, 6, 0, 1, 3)
        self.label_input_chinese = QtWidgets.QLabel(self.groupBox_4)
        self.label_input_chinese.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_input_chinese.setFont(font)
        self.label_input_chinese.setObjectName("label_input_chinese")
        self.gridLayout_8.addWidget(self.label_input_chinese, 5, 0, 1, 1)
        self.label_input_attr = QtWidgets.QLabel(self.groupBox_4)
        self.label_input_attr.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_input_attr.setFont(font)
        self.label_input_attr.setObjectName("label_input_attr")
        self.gridLayout_8.addWidget(self.label_input_attr, 4, 0, 1, 1)
        self.lineEdit_input_attr = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_input_attr.setObjectName("lineEdit_input_attr")
        self.gridLayout_8.addWidget(self.lineEdit_input_attr, 4, 1, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 5)
        self.gridLayout_4.setColumnStretch(1, 9)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_notebook_addLine = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_notebook_addLine.setObjectName("pushButton_notebook_addLine")
        self.gridLayout_10.addWidget(self.pushButton_notebook_addLine, 1, 0, 1, 1)
        self.tableWidget_notebook = QtWidgets.QTableWidget(self.groupBox_8)
        self.tableWidget_notebook.setObjectName("tableWidget_notebook")
        self.tableWidget_notebook.setColumnCount(0)
        self.tableWidget_notebook.setRowCount(0)
        self.gridLayout_10.addWidget(self.tableWidget_notebook, 0, 0, 1, 1)
        self.pushButton_notebook_delLine = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_notebook_delLine.setObjectName("pushButton_notebook_delLine")
        self.gridLayout_10.addWidget(self.pushButton_notebook_delLine, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_notebook_rollback = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_notebook_rollback.setObjectName("pushButton_notebook_rollback")
        self.horizontalLayout_2.addWidget(self.pushButton_notebook_rollback)
        self.pushButton_notebook_save = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_notebook_save.setObjectName("pushButton_notebook_save")
        self.horizontalLayout_2.addWidget(self.pushButton_notebook_save)
        self.gridLayout_9.addWidget(self.groupBox_9, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.undo_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/redo-undo/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_action.setIcon(icon)
        self.undo_action.setObjectName("undo_action")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_11.setTitle(_translate("MainWindow", "往词典里添加新单词，宝贝可以自己修改添加"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_remove.setText(_translate("MainWindow", "—"))
        self.pushButton_add_word_save.setText(_translate("MainWindow", "SAVE"))
        item = self.tableWidget_add_word.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "年份"))
        item = self.tableWidget_add_word.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Text"))
        item = self.tableWidget_add_word.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "单词"))
        item = self.tableWidget_add_word.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "词性"))
        item = self.tableWidget_add_word.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "中文"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "加新词"))
        self.groupBox_2.setTitle(_translate("MainWindow", "快捷查词"))
        self.label.setText(_translate("MainWindow", "年份："))
        self.label_2.setText(_translate("MainWindow", "Text："))
        self.label_search_word.setText(_translate("MainWindow", "输入查询内容："))
        self.pushButton_search_word.setText(_translate("MainWindow", "快查一下"))
        item = self.tableWidget_search_word.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "年份"))
        item = self.tableWidget_search_word.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Text"))
        item = self.tableWidget_search_word.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "单词"))
        item = self.tableWidget_search_word.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "词性"))
        item = self.tableWidget_search_word.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "中文"))
        self.groupBox.setTitle(_translate("MainWindow", "历史搜索记录"))
        self.pushButton_history.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "查单词"))
        self.groupBox_3.setTitle(_translate("MainWindow", "范围设置"))
        self.label_range_num.setText(_translate("MainWindow", "听写个数："))
        self.pushButton_range_start1.setText(_translate("MainWindow", "全部随机，立即开始！"))
        self.groupBox_5.setTitle(_translate("MainWindow", "手动设置范围"))
        self.pushButton_range_start2.setText(_translate("MainWindow", "选好范围，立即开始！"))
        self.label_range_year.setText(_translate("MainWindow", "年份："))
        self.label_range_to.setText(_translate("MainWindow", "到"))
        self.label_range_text.setText(_translate("MainWindow", "Text："))
        self.groupBox_4.setTitle(_translate("MainWindow", "答题区"))
        self.label_chinese_attr.setText(_translate("MainWindow", "词性和中文在这里"))
        self.label_finish.setText(_translate("MainWindow", "完成0 / 0:"))
        self.label_timer.setText(_translate("MainWindow", "本题倒计时："))
        self.label_word.setText(_translate("MainWindow", "单词在这里"))
        self.pushButton_get_answer.setText(_translate("MainWindow", "查看答案"))
        self.pushButton_add_to_notebook.setText(_translate("MainWindow", "添加到单词复习本"))
        self.pushButton_next_word.setText(_translate("MainWindow", "下一个"))
        self.label_input_chinese.setText(_translate("MainWindow", "中文："))
        self.label_input_attr.setText(_translate("MainWindow", "词性："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "听写"))
        self.groupBox_8.setTitle(_translate("MainWindow", "记录错词和难词，宝贝可以自己修改添加"))
        self.pushButton_notebook_addLine.setText(_translate("MainWindow", "添加一行"))
        self.pushButton_notebook_delLine.setText(_translate("MainWindow", "删除选中行"))
        self.pushButton_notebook_rollback.setText(_translate("MainWindow", "撤销修改"))
        self.pushButton_notebook_save.setText(_translate("MainWindow", "保存修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "复习单词本"))
        self.undo_action.setText(_translate("MainWindow", "撤销"))
        self.undo_action.setToolTip(_translate("MainWindow", "<html><head/><body><p>撤销你的<span style=\" font-weight:600;\">上一步</span>操作</p></body></html>"))
        self.undo_action.setShortcut(_translate("MainWindow", "Ctrl+Z"))
import undoIcon_rc
