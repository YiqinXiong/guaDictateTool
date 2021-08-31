#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
guaDictateTool

An dictate tool for LTH.

Author: Yiqin Xiong
Create: August 2021
"""
import os
import random
import sys
from shutil import copyfile

from PyQt5.QtGui import QIcon, QCursor, QKeySequence
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, \
    QHeaderView, QTableWidgetItem, QAbstractItemView, QMenu, QUndoStack, QUndoCommand
from guaWindow import Ui_MainWindow
from PyQt5.QtCore import Qt, pyqtSlot, QTimer
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
        self.pushButton_search_word.setShortcut("Return")
        self.pushButton_add_word_save.setShortcut("Ctrl+S")
        self.tableWidget_add_word.horizontalHeader().setVisible(True)
        self.timer = QTimer()
        self.label_word.setDisabled(True)
        self.label_chinese_attr.setDisabled(True)
        self.pushButton_get_answer.setDisabled(True)
        self.pushButton_add_to_notebook.setDisabled(True)
        self.pushButton_next_word.setDisabled(True)
        self.progressBar_finish.setValue(0)
        self.lineEdit_input_attr.setDisabled(True)
        self.lineEdit_input_chinese.setDisabled(True)
        # private variables
        self.db = 'save.db'
        self.undo_stack = QUndoStack()
        self.previous_cell_text = None
        self.dict_time = 30  # 默认每个单词思考30秒
        self.choices = None
        self.cur_dict_idx = 0
        self.in_dictating = False
        # init actions
        self.undo_action = self.undo_stack.createUndoAction(self, '撤销')
        self.redo_action = self.undo_stack.createRedoAction(self, '重做')
        self.undo_action.setShortcut(QKeySequence.Undo)
        self.redo_action.setShortcut(QKeySequence.Redo)
        self.addAction(self.undo_action)
        self.addAction(self.redo_action)
        # connect SIGNALS and SLOTS
        self.tableWidget_add_word.customContextMenuRequested.connect(self.tableWidget_add_word_showMenu)
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
        # self.tableWidget_add_word.itemDoubleClicked.connect(self.tableWidget_add_word_itemDoubleClicked)
        self.tableWidget_add_word.cellDoubleClicked.connect(self.tableWidget_add_word_cellDoubleClicked)
        self.tableWidget_add_word.itemChanged.connect(self.tableWidget_add_word_itemChanged)
        self.pushButton_search_word.clicked.connect(self.pushButton_search_word_clicked)
        self.comboBox_year.activated.connect(self.pushButton_search_word_clicked)
        self.comboBox_lesson.activated.connect(self.pushButton_search_word_clicked)
        self.pushButton_history.clicked.connect(self.pushButton_history_clicked)
        self.listWidget_history.itemClicked.connect(self.listWidget_history_itemClicked)
        self.pushButton_range_start1.clicked.connect(self.pushButton_range_start1_clicked)
        self.pushButton_range_start2.clicked.connect(self.pushButton_range_start2_clicked)
        self.timer.timeout.connect(self.timer_timeout)
        self.pushButton_get_answer.clicked.connect(self.pushButton_get_answer_clicked)
        self.pushButton_add_to_notebook.clicked.connect(self.pushButton_add_to_notebook_clicked)
        self.pushButton_next_word.clicked.connect(self.pushButton_next_word_clicked)
        # actions after init
        self._check_db_exist()
        self._flush_tab_1()
        self._flush_tab_2()

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
        try:
            cur.executemany("INSERT INTO dict VALUES (?,?,?,?,?)", dict_data)
            if len(data.sheets()) == 2:
                cur.executemany("INSERT INTO notebook VALUES (?,?)", notebook_data)
            conn.commit()
        except Exception as e:
            print(f'_import_excel_to_sqlite: {e}')
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    # 对sqlite进行[查]操作
    def _get_sql_data(self, sql_query):
        conn = self._connect_to_db()
        cur = conn.cursor()
        try:
            cur.execute(sql_query)
            data = cur.fetchall()
        except Exception as e:
            print(f'_get_sql_data: {e}')
            data = []
        finally:
            cur.close()
            conn.close()
        return data

    # 对sqlite进行[增删改]操作
    def _change_sql_data(self, sql_query):
        conn = self._connect_to_db()
        cur = conn.cursor()
        try:
            cur.execute(sql_query)
            conn.commit()
        except Exception as e:
            print(f'_change_sql_data: {e}')
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    # sqlite的create table建立dict和notebook两个表的结构
    def _create_new_db(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        try:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS "
                "dict(year INTEGER,text INTEGER,word TEXT NOT NULL PRIMARY KEY,attr TEXT,chinese TEXT)")
            cur.execute(
                "CREATE TABLE IF NOT EXISTS "
                "notebook(word TEXT NOT NULL PRIMARY KEY,count INTEGER,"
                "CONSTRAINT FK_Notebook FOREIGN KEY (word) REFERENCES dict(word))")
            conn.commit()
        except Exception as e:
            print(f'_create_new_db: {e}')
            conn.rollback()
        finally:
            cur.close()
            conn.close()

    # 连接到sqlite，返回conn
    def _connect_to_db(self):
        if self.db == "":
            QMessageBox.warning(self, '打开词典数据库失败', '数据库文件路径为空')
            return None
        # 指定SQLite数据库的文件名
        conn = sqlite3.connect(self.db)
        return conn

    # 连接到sqlite，执行search的查询任务
    def _search_by_condition(self, year, text, keyword):
        # 清除原有表格内容
        self.tableWidget_search_word.clearContents()
        # 构造SQL语句
        if year == '不限' and text == '不限':
            query = f"SELECT * FROM dict WHERE word LIKE '%{keyword}%' " \
                    f"ORDER BY year DESC, text, word"
        elif year == '不限':
            query = f"SELECT * FROM dict WHERE text = '{text}' AND word LIKE '%{keyword}%' " \
                    f"ORDER BY year DESC, text, word"
        elif text == '不限':
            query = f"SELECT * FROM dict WHERE year = '{year}' AND word LIKE '%{keyword}%' " \
                    f"ORDER BY year DESC, text, word"
        else:
            query = f"SELECT * FROM dict WHERE year = '{year}' AND text = '{text}' AND word LIKE '%{keyword}%' " \
                    f"ORDER BY year DESC, text, word"
        data = self._get_sql_data(query)
        # 设置表格内容
        set_data_to_tableWidget(self.tableWidget_search_word, data)

    def _reset_dict_ui(self):
        self.label_word.setText('单词在这里')
        self.label_word.setDisabled(True)
        self.label_chinese_attr.setText('词性和中文在这里')
        self.label_chinese_attr.setDisabled(True)
        self.label_finish.setText(f'完成{self.cur_dict_idx} / {self.progressBar_finish.maximum()}')
        self.progressBar_finish.setValue(self.cur_dict_idx)
        self.lcdNumber_timer.setStyleSheet("")
        self._reset_dict_time()
        self.lcdNumber_timer.display(self.dict_time)
        self.lineEdit_input_attr.clear()
        self.lineEdit_input_chinese.clear()
        self.pushButton_get_answer.setDisabled(False)
        self.pushButton_add_to_notebook.setDisabled(False)

    def _show_word(self):
        # ui相关
        self._reset_dict_ui()
        # 内容相关
        self.label_word.setDisabled(False)
        self.label_word.setText(self.choices[self.cur_dict_idx][0])
        self.timer.start(1000)

    # 重置听写倒计时
    def _reset_dict_time(self):
        self.dict_time = 30

    # 开始听写
    def _start_dict(self, data):
        num = self.spinBox_num.value()
        # 数据相关
        weight = [int(((d[3] + 1) ** 0.5) * 10) for d in data]  # 神奇的开根号除以10算法
        self.choices = random.choices(data, weight, k=num)
        # ui相关
        self.progressBar_finish.setMaximum(num)
        self.label_word.setDisabled(False)
        self.pushButton_range_start1.setDisabled(True)
        self.pushButton_range_start2.setDisabled(True)
        self.pushButton_get_answer.setDisabled(False)
        self.pushButton_add_to_notebook.setDisabled(False)
        self.pushButton_next_word.setDisabled(False)
        self.spinBox_num.setDisabled(True)
        self.spinBox_year.setDisabled(True)
        self.spinBox_text_from.setDisabled(True)
        self.spinBox_text_to.setDisabled(True)
        self.lineEdit_input_attr.setDisabled(False)
        self.lineEdit_input_chinese.setDisabled(False)
        # 开始听写
        self.in_dictating = True
        self.cur_dict_idx = -1
        try:
            self.pushButton_next_word_clicked()
        except Exception as e:
            print(f'_start_dict:{e}')

    # 刷新加新词页面
    def _flush_tab_1(self):
        # tableWidget相关
        self.tableWidget_add_word.clearContents()
        data = self._get_sql_data("SELECT * FROM dict ORDER BY year DESC, text, word")
        set_data_to_tableWidget(self.tableWidget_add_word, data)

    # 刷新查词页面
    def _flush_tab_2(self):
        # comboBox相关
        self.comboBox_year.clear()
        self.comboBox_lesson.clear()
        self.comboBox_year.addItem('不限')
        self.comboBox_lesson.addItem('不限')
        # self.comboBox_year.setCurrentIndex()
        try:
            conn = self._connect_to_db()
            cur = conn.cursor()
            # 查询所有不重复的year（可能为空）
            cur.execute("select distinct year from dict order by year desc")
            years = [str(year[0]) for year in cur.fetchall()]
            # 查询所有不重复的text（可能为空）
            cur.execute("select distinct text from dict order by text")
            texts = [str(text[0]) for text in cur.fetchall()]
        except Exception as e:
            print(f'_flush_tab_2: {e}')
            years = texts = []
        finally:
            cur.close()
            conn.close()
        print(years, texts)
        self.comboBox_year.addItems(years)
        self.comboBox_lesson.addItems(texts)

        # tableWidget相关
        self.tableWidget_search_word.clearContents()
        data = self._get_sql_data("SELECT * FROM dict ORDER BY year DESC, text, word")
        set_data_to_tableWidget(self.tableWidget_search_word, data)

    ################## 槽函数（SLOT） #################

    # 切换页面时触发
    def tabWidget_currentChanged(self):
        sender = self.sender()
        idx = sender.currentIndex()
        if idx == 0:
            # 加新词页面
            print('切换到加新词页面')
            if self.in_dictating:
                self.timer.stop()
        elif idx == 1:
            # 查单词页面
            print('切换到查单词页面')
            if self.in_dictating:
                self.timer.stop()
        elif idx == 2:
            # 听写页面
            print('切换到听写页面')
            if self.in_dictating:
                self.timer.start()
        elif idx == 3:
            # 复习单词本页面
            print('切换到复习单词本页面')
            if self.in_dictating:
                self.timer.stop()
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

    # 点击加新词页面的”SAVE“按钮后触发
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
            # 关闭连接
            cur.close()
            conn.close()
            self.setWindowTitle('LTH的单词听写机')
        self._flush_tab_2()

    # 加新词页面表格的内容修改后触发
    def tableWidget_add_word_itemChanged(self):
        print(f'tableWidget_add_word_itemChanged: {self.previous_cell_text}')
        if self.previous_cell_text is None:
            return
        row = self.previous_cell_text[0]
        col = self.previous_cell_text[1]
        text = self.previous_cell_text[2]
        if self.tableWidget_add_word.item(row, col).text() != text:
            change_item = ChangeItemCommand(self.tableWidget_add_word, row, col, text)
            self.undo_stack.push(change_item)
        self.previous_cell_text = None

    # 双击加新词页面表格的单元格时触发
    def tableWidget_add_word_cellDoubleClicked(self, row, col):
        item = self.tableWidget_add_word.item(row, col)
        print(
            f'tableWidget_add_word_cellDoubleClicked: row {row}, col {col}, item {item}')
        # self.tableWidget_add_word.cellActivated()
        text = item.text() if item is not None else ''
        self.previous_cell_text = (row, col, text)

    # 点击”快查一下“时触发
    @pyqtSlot()
    def pushButton_search_word_clicked(self):
        # 获取查询条件
        year = self.comboBox_year.currentText()
        text = self.comboBox_lesson.currentText()
        keyword = self.lineEdit_search_word.text()
        print(f'search word: 年份:{year}，Text:{text}，关键词:{keyword}')
        self._search_by_condition(year, text, keyword)
        self.listWidget_history.addItem(f'[{year}], [{text}], [{keyword}]')

    # 点击清空搜索历史记录时触发
    @pyqtSlot()
    def pushButton_history_clicked(self):
        self.listWidget_history.clear()

    # 点击搜索记录里的条目时触发
    def listWidget_history_itemClicked(self, item):
        text = item.text()
        # 获取查询条件
        conditions = text.split(', ')
        if len(conditions) != 3:
            print("查询条件解析错误！")
        year, text, keyword = [con[1:-1] for con in conditions]
        self._search_by_condition(year, text, keyword)

    # 点击”全部随机，立即开始“时触发
    @pyqtSlot()
    def pushButton_range_start1_clicked(self):
        data = self._get_sql_data(
            "select dict.word,attr,chinese,case when count is null then 0 else count end "
            "from dict left join notebook n on dict.word = n.word")
        print(data)
        if len(data) == 0:
            QMessageBox.warning(self, '听写失败', '没有单词可供听写')
        else:
            self._start_dict(data)

    # 点击”选好范围，立即开始“时触发
    @pyqtSlot()
    def pushButton_range_start2_clicked(self):
        year = self.spinBox_year.value()
        text_from = self.spinBox_text_from.value()
        text_to = self.spinBox_text_to.value()
        if text_from > text_to:
            text_from, text_to = text_to, text_from
        data = self._get_sql_data(
            f"select dict.word,attr,chinese,case when count is null then 0 else count end "
            f"from dict left join notebook n on dict.word = n.word "
            f"where dict.year = {year} and dict.text between {text_from} and {text_to}")
        print(data)
        if len(data) == 0:
            QMessageBox.warning(self, '听写失败', '该范围没有单词可供听写')
        else:
            self._start_dict(data)

    def timer_timeout(self):
        if self.dict_time > 0:
            if self.dict_time <= 5:
                self.lcdNumber_timer.setStyleSheet("color: rgb(255, 0, 0)")
            self.dict_time -= 1
            self.lcdNumber_timer.display(self.dict_time)
            self.timer.start(1000)  # 开始下一秒的计时
        else:
            QMessageBox.information(self, '已超时', '超时啦，自动添加到错题本')
            self.pushButton_add_to_notebook_clicked()
            self.timer.stop()
            self.pushButton_next_word_clicked()

    # 点击听写页面的”查看答案“时触发
    @pyqtSlot()
    def pushButton_get_answer_clicked(self):
        try:
            self.pushButton_get_answer.setDisabled(True)
            cur_choice = self.choices[self.cur_dict_idx]
            self.label_chinese_attr.setDisabled(False)
            self.label_chinese_attr.setText(f'{cur_choice[1]}  {cur_choice[2]}')
        except Exception as e:
            print(f'pushButton_get_answer_clicked:{e}')

    # 点击听写页面的”添加到单词复习本“时触发
    @pyqtSlot()
    def pushButton_add_to_notebook_clicked(self):
        self.pushButton_add_to_notebook.setDisabled(True)
        cur_choice = self.choices[self.cur_dict_idx]
        word = cur_choice[0]
        count = cur_choice[3] + 1
        sql_query = f"replace into notebook(word,count) values ('{word}',{count})"
        self._change_sql_data(sql_query)
        self.pushButton_get_answer_clicked()

    # 点击听写页面的”下一个“时触发
    @pyqtSlot()
    def pushButton_next_word_clicked(self):
        self.cur_dict_idx += 1
        try:
            if self.cur_dict_idx >= self.progressBar_finish.maximum():
                # 听写结束
                self.in_dictating = False
                self.timer.stop()
                QMessageBox.information(self, "听写结束",
                                        f"完成了一轮听写（{self.progressBar_finish.maximum()}个单词），牛蹄滑给力奥！")
                self.cur_dict_idx = 0
                self._reset_dict_ui()
                self.label_word.setDisabled(True)
                self.pushButton_range_start1.setDisabled(False)
                self.pushButton_range_start2.setDisabled(False)
                self.pushButton_get_answer.setDisabled(True)
                self.pushButton_add_to_notebook.setDisabled(True)
                self.pushButton_next_word.setDisabled(True)
                self.spinBox_num.setDisabled(False)
                self.spinBox_year.setDisabled(False)
                self.spinBox_text_from.setDisabled(False)
                self.spinBox_text_to.setDisabled(False)
                self.label_finish.setText(f'完成{self.cur_dict_idx} / {0}')
            else:
                self._show_word()
        except Exception as e:
            print(f'pushButton_next_word_clicked: {e}')


class InsertCommand(QUndoCommand):
    def __init__(self, table, row_idx):
        super(InsertCommand, self).__init__()
        self.table = table
        self.row_idx = row_idx
        self.main_window = table.parent().parent().parent().parent().parent().parent()

    def redo(self):
        self.table.insertRow(self.row_idx)
        self.main_window.setWindowTitle('LTH的单词听写机（未保存！！）')

    def undo(self):
        self.table.removeRow(self.row_idx)
        self.main_window.setWindowTitle('LTH的单词听写机（未保存！！）')
        # print(
        #     f'canRedo:{self.main_window.undo_stack.canRedo()} isClean:{self.main_window.undo_stack.isClean()} '
        #     f'count:{self.main_window.undo_stack.count()} index:{self.main_window.undo_stack.index()}')
        if self.main_window.undo_stack.index() == 1:
            self.main_window.setWindowTitle('LTH的单词听写机')


class DeleteSelectedCommand(QUndoCommand):
    def __init__(self, table, rows):
        super(DeleteSelectedCommand, self).__init__()
        self.table = table
        self.rows = rows
        self.rows_rev = rows[::-1]
        self.rows_data = get_data_from_tableWidget(table, self.rows_rev, list(range(table.columnCount())))
        self.main_window = table.parent().parent().parent().parent().parent().parent()

    def redo(self):
        for r in self.rows:
            self.table.removeRow(r)
        self.main_window.setWindowTitle('LTH的单词听写机（未保存！！）')

    def undo(self):
        for i, r in enumerate(self.rows_rev):
            self.table.insertRow(r)
            for j, item in enumerate(self.rows_data[i]):
                item = QTableWidgetItem(str(item))
                item.setTextAlignment(Qt.AlignJustify | Qt.AlignVCenter)
                self.table.setItem(r, j, item)
        self.main_window.setWindowTitle('LTH的单词听写机（未保存！！）')
        # print(
        #     f'canRedo:{self.main_window.undo_stack.canRedo()} isClean:{self.main_window.undo_stack.isClean()} '
        #     f'count:{self.main_window.undo_stack.count()} index:{self.main_window.undo_stack.index()}')
        if self.main_window.undo_stack.index() == 1:
            self.main_window.setWindowTitle('LTH的单词听写机')


class ChangeItemCommand(QUndoCommand):
    def __init__(self, table, row, col, text):
        super(ChangeItemCommand, self).__init__()
        self.table = table
        self.row = row
        self.col = col
        self.text = text
        self.main_window = table.parent().parent().parent().parent().parent().parent()

    def redo(self):
        self.main_window.setWindowTitle('LTH的单词听写机（未保存！！）')
        pass

    def undo(self):
        self.table.item(self.row, self.col).setText(self.text)
        self.main_window.setWindowTitle('LTH的单词听写机（未保存！！）')
        # print(
        #     f'canRedo:{self.main_window.undo_stack.canRedo()} isClean:{self.main_window.undo_stack.isClean()} '
        #     f'count:{self.main_window.undo_stack.count()} index:{}')
        if self.main_window.undo_stack.index() == 1:
            self.main_window.setWindowTitle('LTH的单词听写机')


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


# 设置tableWidget的显示内容（从sqlite读取数据）
def set_data_to_tableWidget(table, data):
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    table.setRowCount(len(data))
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            item = QTableWidgetItem(str(item))
            item.setTextAlignment(Qt.AlignJustify | Qt.AlignVCenter)
            table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MWindow()
    m.show()
    sys.exit(app.exec_())
