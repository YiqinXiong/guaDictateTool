#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
guaDictateTool

An dictate tool for LTH.

Author: Yiqin Xiong
Create: August 2021
"""
import os
import sys
from shutil import copyfile

from PyQt5.QtGui import QIcon, QCursor, QKeySequence
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, \
    QHeaderView, QTableWidgetItem, QAbstractItemView, QMenu, QUndoStack, QUndoCommand
from guaWindow import Ui_MainWindow
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sqlite3


class MWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MWindow, self).__init__()
        # about UI
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/icon/icon.png'))
        self.setWindowTitle('LTH的单词听写机')
        self.tabWidget.setCurrentIndex(0)
        self.save_box = QMessageBox(QMessageBox.Warning, '错误，找不到存档', '找不到本地存档，请选择：')
        self.tableWidget_add_word.setContextMenuPolicy(Qt.CustomContextMenu)

        # private variables
        self.db = 'save.db'
        self.undo_stack = QUndoStack()
        self.previous_cell_text = None
        # init actions
        self.undo_action = self.undo_stack.createUndoAction(self, '撤销')
        self.redo_action = self.undo_stack.createRedoAction(self, '重做')
        self.undo_action.setShortcut(QKeySequence.Undo)
        self.redo_action.setShortcut(QKeySequence.Redo)
        self.addAction(self.undo_action)
        self.addAction(self.redo_action)
        # connect SIGNALS and SLOTS
        self.tableWidget_add_word.customContextMenuRequested.connect(self.tableWidget_add_word_showMenu)
        self.pushButton_next_word.clicked.connect(self.pushButton_next_word_clicked)
        self.tabWidget.currentChanged.connect(self.tabWidget_currentChanged)
        self.pushButton_add.clicked.connect(self.tableWidget_add_word_insert_behind)
        self.pushButton_remove.clicked.connect(self.tableWidget_add_word_delete_selected)
        self.pushButton_add_word_save.clicked.connect(self.pushButton_add_word_save_clicked)
        self.pushButton_undo.clicked.connect(self.undo_action.trigger)
        self.pushButton_redo.clicked.connect(self.redo_action.trigger)
        # self.tableWidget_add_word.currentItemChanged.connect(
        #     self.tableWidget_add_word_currentItemChanged)
        # self.tableWidget_add_word.dataChanged.connect(self.tableWidget_add_word_currentItemChanged)
        # self.tableWidget_add_word.clicked.connect(self.tableWidget_add_word_clicked)
        self.tableWidget_add_word.itemDoubleClicked.connect(self.tableWidget_add_word_itemDoubleClicked)
        self.tableWidget_add_word.itemChanged.connect(self.tableWidget_add_word_itemChanged)
        # actions after init
        self._check_db_exist()
        self._set_tableWidget_add_word()

    # 设置tableWidget_add_word的显示内容（从sqlite读取数据）
    def _set_tableWidget_add_word(self):
        self.tableWidget_add_word.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_add_word.setSelectionBehavior(QAbstractItemView.SelectRows)
        data = self._get_all_data_from_table('dict')
        self.tableWidget_add_word.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignJustify | Qt.AlignVCenter)
                self.tableWidget_add_word.setItem(i, j, item)

    # 检查存档是否存在
    def _check_db_exist(self):
        if not os.path.exists(self.db):
            from_excel = self.save_box.addButton('从Excel导入', QMessageBox.ActionRole)
            from_db = self.save_box.addButton('从.db文件导入', QMessageBox.ActionRole)
            from_new = self.save_box.addButton('新建存档', QMessageBox.ActionRole)
            cancel = self.save_box.addButton('退出', QMessageBox.RejectRole)
            self.save_box.setDefaultButton(cancel)
            self.save_box.exec_()

            if self.save_box.clickedButton() == cancel:
                sys.exit(0)
            elif self.save_box.clickedButton() == from_db:
                file_name = QFileDialog.getOpenFileName(self, '选取词典数据库文件', '', 'SQLite Database(*.db)')
                if file_name[0]:
                    copyfile(file_name[0], self.db)
            else:
                self._create_new_db()
                if self.save_box.clickedButton() == from_excel:
                    file_name = QFileDialog.getOpenFileName(self, '选取Excel文件', '', 'Excel(*.xls, *.xlsx)')
                    if file_name[0]:
                        self._import_excel_to_sqlite(file_name[0])

    # 从excel读取内容到sqlite
    def _import_excel_to_sqlite(self, excel_file_path):
        # 读取excel内容
        import xlrd
        data = xlrd.open_workbook(excel_file_path)
        dict_sheet = data.sheet_by_index(0)
        if dict_sheet.ncols != 5:
            QMessageBox.warning(self, 'excel解析错误', '此excel格式不符，请检查')
            self.create_new_db()
            return
        dict_data = [tuple(dict_sheet.row_values(row_idx)) for row_idx in range(1, dict_sheet.nrows)]
        if len(data.sheets()) == 2:
            notebook_sheet = data.sheet_by_index(1)
            notebook_data = [tuple(notebook_sheet.row_values(row_idx)) for row_idx in range(1, notebook_sheet.nrows)]
        # 写入数据库
        conn = self._connect_to_db()
        cur = conn.cursor()
        cur.executemany("INSERT INTO dict VALUES (?,?,?,?,?)", dict_data)
        if len(data.sheets()) == 2:
            cur.executemany("INSERT INTO notebook VALUES (?,?)", notebook_data)
        cur.close()
        conn.commit()
        conn.close()

    # 从sqlite读取内容到tableWidget
    def _get_all_data_from_table(self, table_name):
        conn = self._connect_to_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        return cur.fetchall()

    # sqlite的create table建立dict和notebook两个表的结构
    def _create_new_db(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS dict(year INTEGER,text INTEGER,word TEXT NOT NULL PRIMARY KEY,attr TEXT,chinese TEXT)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS notebook(word TEXT NOT NULL PRIMARY KEY,count INTEGER,CONSTRAINT FK_Notebook FOREIGN KEY (word) REFERENCES dict(word))")

    # 连接到sqlite，返回conn
    def _connect_to_db(self):
        if self.db == "":
            QMessageBox.warning(self, '打开词典数据库失败', '数据库文件路径为空')
            return None
        # 指定SQLite数据库的文件名
        conn = sqlite3.connect(self.db)
        return conn

    ################## 槽函数（SLOT） #################

    # 点击听写页面的”下一个“时触发
    def pushButton_next_word_clicked(self):
        QMessageBox.information(self, '标题你刚才点了下一个！', '你刚才点了下一个！')

    # 切换页面时触发
    def tabWidget_currentChanged(self):
        sender = self.sender()
        idx = sender.currentIndex()
        if idx == 0:
            # 加新词页面
            print('切换到加新词页面')
        elif idx == 1:
            # 查单词页面
            print('切换到查单词页面')
        elif idx == 2:
            # 听写页面
            print('切换到听写页面')
        elif idx == 3:
            # 复习单词本页面
            print('切换到复习单词本页面')
        else:
            pass

    # 在tableWidget_add_word上单击右键时触发右键菜单
    def tableWidget_add_word_showMenu(self, pos):
        pop_menu = QMenu(self.tableWidget_add_word)
        insert_action = pop_menu.addAction('添加一行')
        delete_action = pop_menu.addAction('删除选中的行')
        insert_action.triggered.connect(lambda: self.tableWidget_add_word_insert(pos))
        delete_action.triggered.connect(self.tableWidget_add_word_delete_selected)
        pop_menu.exec_(QCursor.pos())

    # def tableWidget_add_word_delete(self, pos):
    #     row_id = self.tableWidget_add_word.rowAt(pos.y())
    #     self.tableWidget_add_word.removeRow(row_id)

    # 在tableWidget_add_word中删除选中行
    def tableWidget_add_word_delete_selected(self):
        rows = self.tableWidget_add_word.selectionModel().selectedRows()
        if len(rows) == 0:
            return
        row_ids = [r.row() for r in rows]  # 获得需要删除的行号的list
        row_ids.sort(key=int, reverse=True)  # 用sort方法将list进行降序排列
        delete_selection = DeleteSelectedCommand(self.tableWidget_add_word, row_ids)
        self.undo_stack.push(delete_selection)

    # 在tableWidget_add_word中鼠标右键位置插入
    def tableWidget_add_word_insert(self, pos):
        row_id = self.tableWidget_add_word.rowAt(pos.y())
        insert = InsertCommand(self.tableWidget_add_word, row_id + 1)
        self.undo_stack.push(insert)

    # 在tableWidget_add_word中最末尾插入
    def tableWidget_add_word_insert_behind(self):
        insert = InsertCommand(self.tableWidget_add_word, self.tableWidget_add_word.rowCount())
        self.undo_stack.push(insert)

    # 从tableWidget保存内容到sqlite
    def pushButton_add_word_save_clicked(self):
        row_count = self.tableWidget_add_word.rowCount()
        col_count = self.tableWidget_add_word.columnCount()
        data = get_data_from_tableWidget(self.tableWidget_add_word, list(range(row_count)), list(range(col_count)))
        # 写入数据库
        conn = self._connect_to_db()
        cur = conn.cursor()
        try:
            # # 备份notebook的数据
            # cur.execute("CREATE TABLE notebook_bak AS SELECT * from notebook")
            # # 删表
            # cur.execute("TRUNCATE TABLE notebook")
            # cur.execute("TRUNCATE TABLE dict")
            # # 重建dict表
            # cur.executemany("INSERT INTO dict VALUES (?,?,?,?,?)", data)
            # # 重建notebook表，可能会有外键约束错误，忽略掉错误的行
            # cur.execute("INSERT INTO notebook SELECT * FROM notebook_bak")
            # # 删除notebook_bak表
            # cur.execute("DROP TABLE notebook_bak")
            # 删表
            cur.execute("DELETE FROM dict")
            # 重建dict表
            cur.executemany("INSERT INTO dict VALUES (?,?,?,?,?)", data)
            conn.commit()
        except Exception as e:

            if 'UNIQUE constraint failed' in str(e):
                QMessageBox.warning(self, '保存失败', '不允许有相同的单词出现噢，请检查一下')
            else:
                QMessageBox.warning(self, '保存失败', f'SQL错误信息：{e}')
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    def tableWidget_add_word_itemChanged(self):
        print(self.previous_cell_text)
        if self.previous_cell_text is None:
            return
        row = self.previous_cell_text[0]
        col = self.previous_cell_text[1]
        text = self.previous_cell_text[2]
        if self.tableWidget_add_word.item(row, col).text() != text:
            change_item = ChangeItemCommand(self.tableWidget_add_word, row, col, text)
            self.undo_stack.push(change_item)
        self.previous_cell_text = None

    def tableWidget_add_word_itemDoubleClicked(self, item):
        print(item)
        self.previous_cell_text = (
            self.tableWidget_add_word.currentRow(), self.tableWidget_add_word.currentColumn(), item.text())


class InsertCommand(QUndoCommand):
    def __init__(self, table, row_idx):
        super(InsertCommand, self).__init__()
        self.table = table
        self.row_idx = row_idx

    def redo(self):
        self.table.insertRow(self.row_idx)

    def undo(self):
        self.table.removeRow(self.row_idx)


class DeleteSelectedCommand(QUndoCommand):
    def __init__(self, table, rows):
        super(DeleteSelectedCommand, self).__init__()
        self.table = table
        self.rows = rows
        self.rows_rev = rows[::-1]
        self.rows_data = get_data_from_tableWidget(table, self.rows_rev, list(range(table.columnCount())))

    def redo(self):
        for r in self.rows:
            self.table.removeRow(r)

    def undo(self):
        for i, r in enumerate(self.rows_rev):
            self.table.insertRow(r)
            for j, item in enumerate(self.rows_data[i]):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignJustify | Qt.AlignVCenter)
                self.table.setItem(r, j, item)


class ChangeItemCommand(QUndoCommand):
    def __init__(self, table, row, col, text):
        super(ChangeItemCommand, self).__init__()
        self.table = table
        self.row = row
        self.col = col
        self.text = text

    def redo(self):
        pass

    def undo(self):
        self.table.item(self.row, self.col).setText(self.text)


# 从tableWidget读取内容到data
def get_data_from_tableWidget(table_widget, rows, cols):
    # data = [tuple(self.tableWidget_add_word.item(i, j).text() for j in range(col_count)) for i in range(row_count)]
    # 按下面的方式遍历，可以对item特殊处理
    data = []
    for i in rows:
        row_data = []
        for j in cols:
            if table_widget.item(i, j) is None:
                row_data.append('')
            else:
                if j < 2:
                    if str.isdigit(table_widget.item(i, j).text()):
                        row_data.append(int(table_widget.item(i, j).text()))
                    else:
                        row_data.append('')
                else:
                    row_data.append(table_widget.item(i, j).text())
        data.append(tuple(row_data))
    print(f'get_all_data_from_tableWidget: {data}')
    return data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MWindow()
    m.show()
    sys.exit(app.exec_())
