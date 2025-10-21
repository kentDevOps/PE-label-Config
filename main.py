import sys,os
import time
import pandas as pd
from pandas import DataFrame
from guide import *
from images import *
'''from PySide6.QtWidgets import QApplication, QMessageBox,QInputDialog,QListView,QAbstractItemView,QGraphicsView, QGraphicsScene,QTableView,QProgressBar
from PySide6.QtCore import QStringListModel,QModelIndex,QAbstractTableModel#QAbstractTableModel dùng cho load dataFrame vào tableView
from PySide6.QtCore import Qt,QSortFilterProxyModel,QThread, Signal#loc
from PySide6.QtGui import QPixmap,QWheelEvent,QTextCharFormat
from PySide6.QtGui import QFont, QStandardItem, QStandardItemModel # dung cho dinh dang
from PySide6.QtCore import QAbstractTableModel, Qt,Signal # xet thuoc tinh khong chinh sua'''
from sqliteProcess import *
from common import *
from log import *
from retail_ui import Ui_retailForm
from bob_view import Ui_bobForm
from loadSku_ui import Ui_skuForm
from functools import partial # cho phép truyền đối số từ hàm trong Pyside gọi bằng signal
from imgProcess import *
from tableContent import *
from gsheet import *
from dataProcess import *
from dataChk import *
from selenium_process import *
import traceback
'''from PySide6.QtWidgets import QInputDialog
from PySide6.QtCore import (
  QObject,
  QRunnable,
  QThreadPool,
  QTimer,
  Signal,
  Slot,
)'''
from PySide6.QtWidgets import (
    QApplication, QMessageBox, QInputDialog, QListView, QAbstractItemView,
    QGraphicsView, QGraphicsScene, QTableView, QProgressBar, QMainWindow,
    QSplashScreen
)
from PySide6.QtCore import (
    QStringListModel, QModelIndex, QAbstractTableModel, Qt,
    QSortFilterProxyModel, QThread, Signal, Slot,
    QObject, QRunnable, QThreadPool, QTimer
)
from PySide6.QtGui import (
    QPixmap, QWheelEvent, QTextCharFormat,
    QFont, QStandardItem, QStandardItemModel
)

#Class dùng cho hiển thị dataFrame vào QTable
class workerSignal(QObject):
    progress = Signal(int)
    finished = Signal()
class worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signal = workerSignal()
    @Slot()
    def run(self):
        total_n = 1000
        for n in range(total_n):
            progress_pc = int(100 * float(n + 1) / total_n) # Progress 0-100% as int
            self.signal.progress.emit(progress_pc)
            time.sleep(0.01)
        self.signal.finished.emit()
class PandasModel(QAbstractTableModel):
    def __init__(self, df: pd.DataFrame, parent=None):
        super().__init__(parent)
        self._df = df

    def rowCount(self, parent=None):
        return len(self._df.index)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            value = self._df.iloc[index.row(), index.column()]
            return str(value)  # đảm bảo hiển thị dạng chuỗi

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return str(self._df.columns[section])  # tên cột
        else:
            return str(self._df.index[section])  # index (nếu muốn hiện số thứ tự)
class imgViewer(QGraphicsView):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # Cho phép kéo ảnh
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)  # Zoom quanh con trỏ chuột
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.scale_factor = 1.2  # Tỉ lệ zoom
    def wheelEvent(self, event: QWheelEvent):
        """Zoom in/out bằng con lăn chuột"""
        if event.angleDelta().y() > 0:  # Lăn lên
            self.scale(self.scale_factor, self.scale_factor)
        else:  # Lăn xuống
            self.scale(1 / self.scale_factor, 1 / self.scale_factor)
class MainWindow(QMainWindow):
    send_text = Signal(str)  # Signal gửi text, from PySide6.QtCore import signal
    send_text_m = Signal(str,str)
    send_text_bts = Signal(str,str,str)
    send_text_b = Signal(str,str,str,str)
#---------------------Khoi Tao----------------------------
    def __init__(self, parent = None):
        try:
#region __Init__ Pyside 6
            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            #Show Window
            self.setWindowTitle("Developed By Kent - ZALO : 0375803690")
            icon_path = self.load_form_icon()
            self.setWindowIcon(icon_path) # set icon cho title
            self.threadpool = QThreadPool()
            self.progress = QProgressBar()
            # Splash screen
            splash = QSplashScreen(
                QPixmap(), 
                Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint
            )
            splash.setFixedSize(400, 100)

            # progress bar trong splash
            progress = QProgressBar(splash)
            progress.setGeometry(20, 40, 360, 25)
            progress.setValue(0)

            splash.show()
            self.show()
            
            #self.execute()
            self.ui.mulPage.setCurrentWidget(self.ui.page)
            self.load_img_avar() # load aver vao page monitor
            self.center_on_screen()# chinh gui vao giua man
            #load data vao cac combobox
            self.load_combobox()
            self.progress.setValue(20)
            #---------------------------------Validation--------------------------------------------
            #--> kiểm tra các folder hệ thống
            #region Check System Folder
            check_mandatory_folder_exists("database")
            self.progress.setValue(40)
            check_mandatory_folder_exists("img")
            self.progress.setValue(60)
            list_file = list_file_in_folder("database")
            print(list_file)
            self.progress.setValue(100)
            # Chuyển đổi các page 
            #region transits Pages
            self.ui.bt_view_config.clicked.connect(lambda: (self.ui.mulPage.setCurrentWidget(self.ui.p_check_config),
                                                   self.hight_light_color(self.ui.bt_view_config)))
            self.ui.bt_bulk_import.clicked.connect(lambda: (self.ui.mulPage.setCurrentWidget(self.ui.p_bulk),
                                                   self.hight_light_color(self.ui.bt_bulk_import)))
            self.ui.bt_single_maintain.clicked.connect(lambda: (self.ui.mulPage.setCurrentWidget(self.ui.p_main_single),
                                                       self.hight_light_color(self.ui.bt_single_maintain)))
            self.ui.bt_realtime_check.clicked.connect(lambda: (self.ui.mulPage.setCurrentWidget(self.ui.p_realtime_chk),
                                                      self.hight_light_color(self.ui.bt_realtime_check)))
            self.ui.bt_chk_modify_date.clicked.connect(self.chk_modify_date)
            # Signal bắt text change của combobox Product
            #region Product changed
            self.ui.cb_view_product.currentTextChanged.connect(self.cb_product_changed)
            self.ui.cb_bulk_product.currentTextChanged.connect(self.cb_bulk_product_changed)
            self.ui.cb_maintain_product_2.currentTextChanged.connect(self.cb_maintain_product_changed)
            self.ui.cb_realtime_product.currentTextChanged.connect(self.cb_realtime_product_changed)
            
            # Signal bắt text change của combobox Project
            #region Project changed
            self.ui.cb_view_project.currentTextChanged.connect(self.view_combo_box_text_changed)
            self.ui.cb_bulk_project.currentTextChanged.connect(self.bulk_combo_box_text_changed)
            self.ui.cb_maintain_project_2.currentTextChanged.connect(self.maintain_combo_box_text_changed)
            self.ui.cb_realtime_project.currentTextChanged.connect(self.realtime_combo_box_text_changed)

            #Signal bắt text change của combobox region
            self.ui.cb_view_region.currentTextChanged.connect(self.view_region_changed)
            #Signal bắt sự kiện click ở listview
            self.reset_view_content()
            self.ui.list_view_sku.clicked.connect(self.view_listsku_clicked)
            #Sự kiện text change của search SKu
            #self.ui.tx_view_skuSearch.textChanged.connect(self.setup_sku_search)
            self.ui.tx_view_skuSearch.returnPressed.connect(self.setup_sku_search)
            self.ui.bt_chk_r.clicked.connect(self.open_retail_form)
            self.ui.bt_chk_m.clicked.connect(partial(self.open_mrp_form,self.ui.tx_view_mlabel.text()))
            self.ui.bt_chk_b.clicked.connect(self.open_bob_form)
            self.ui.bt_chk_carton1.clicked.connect(self.open_carton_form)
            self.ui.bt_chk_carton2.clicked.connect(self.open_carton2_form)
            self.ui.bt_chk_ship.clicked.connect(self.open_ship_form)
            #Bulk Import page -> signal ui
            self.ui.bt_bulk_load_sku.clicked.connect(self.open_load_sku_form)
            self.ui.bt_bulk_keyConfig.clicked.connect(self.keyconfig_create)
            self.ui.bt_bulk_single_inspect.clicked.connect(self.bulk_single_inspect)
            self.ui.bt_bulk_autoLoad_key.clicked.connect(self.auto_upload)
            self.ui.bt_labelPrint_packing.clicked.connect(self.pack_labelPrint_create)
            self.ui.bt_labelPrint_FATP.clicked.connect(self.fatp_labelPrint_create)
            self.ui.bt_labelPrint_CG.clicked.connect(self.cg_labelPrint_create)
            self.ui.bt_labelPrint_BG.clicked.connect(self.bg_labelPrint_create)
            self.ui.bt_labelPrint_autoLoad.clicked.connect(self.labelPrint_auto_upload)
            #Realtime check -> signal ui
            self.ui.bt_realtime_load_sku.clicked.connect(self.open_load_sku_form_realtime)
            self.ui.bt_realtime_inspect.clicked.connect(self.realtime_chk_keyConfig)
            #Maintain Single > Signal ui
            self.ui.bt_maintain_load_sku_2.clicked.connect(self.open_load_sku_form_maintain)
            self.ui.bt_maintain_load_key.clicked.connect(self.maintain_load_keyConfig)
            self.ui.chk_maintain_all.clicked.connect(self.click_unclick_checkbox)
            self.form_b = None
            self.form_m = None
            self.form_bob = None
            self.form_carton = None
            self.form_carton2 = None
            self.form_ship = None
            self.load_sku_form = None
            
        except Exception as e:
            err_msg = traceback.format_exc()
            QMessageBox.critical(self, "Lỗi khởi tạo", str(e))
            #self.ui.lb_notice.setText(f"Error occur : {e}")
            logExport(f"Occur Error : \n {err_msg}")
    def execute(self):
        wk = worker()
        wk.signal.progress.connect(self.update_progress)
        wk.signal.finished.connect(self.hide_progress)
        self.threadpool.start(wk)
    def update_progress(self,progress):
        self.progress.setValue(progress)
    def hide_progress(self):
        self.statusBar().removeWidget(self.progress)
#region --- Signal 
#region, maintain page
    def click_unclick_checkbox(self):
        list_chkbox = [self.ui.chk_maintain_des,self.ui.chk_maintain_upc,self.ui.chk_maintain_brand,
                       self.ui.chk_maintain_blabel,self.ui.chk_maintain_rlabel,self.ui.chk_maintain_sap,self.ui.chk_maintain_color,
                       self.ui.chk_maintain_mlabel,self.ui.chk_maintain_price,self.ui.chk_maintain_qr]   
        flag = self.ui.chk_maintain_all.isChecked()
        if flag == True:
            for cb in list_chkbox:
                if cb.isChecked() == False:
                    cb.click()
        elif flag == False:
            for cb in list_chkbox:
                if cb.isChecked() == True:
                    cb.click()            
    def maintain_load_keyConfig(self):
        # check data input
        current_product = self.ui.cb_maintain_product_2.currentText()
        current_project = self.ui.cb_maintain_project_2.currentText()
        suffix = self.ui.tx_maintain_surfix_2.text()
        if current_product == '' or current_project == '':
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
            return
        #Load SKU
        model = self.ui.list_maintain_sku_2.model()
        list_sku = []
        list_suff = []
        for item in range(model.rowCount()):
            index = model.index(item,0)
            value = model.data(index)
            list_sku.append(value)
        print("Dữ liệu:", list_sku)
        #Loc Standard from mapping
        standard_df,dict_region = gen_std(current_project,current_product,list_sku,suffix)
        print(standard_df)
        for item in list_sku:
            if suffix != '':
                list_suff.append(value + '-' + suffix)
            else:
                list_suff.append(value)
        print(standard_df)
        print(dict_region)
        # CHk whether Check box check or not
        list_chkbox = [self.ui.chk_maintain_all,self.ui.chk_maintain_des,self.ui.chk_maintain_upc,self.ui.chk_maintain_brand,
                       self.ui.chk_maintain_blabel,self.ui.chk_maintain_rlabel,self.ui.chk_maintain_sap,self.ui.chk_maintain_color,
                       self.ui.chk_maintain_mlabel,self.ui.chk_maintain_price,self.ui.chk_maintain_qr]
        status_dict = {}
        key_list = []
        user, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập UserName của bạn:")
        if ok and user:
            print("Bạn nhập:", user)
        passW, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập Password của bạn:",QLineEdit.EchoMode.Password)
        if ok and passW:
            print("Bạn nhập:", passW)
        if user == '' or passW == '':
            QMessageBox.critical(self, "Lỗi khởi tạo", "Phải nhập Username , Password!")
            return
        for cb in list_chkbox:
            status_dict[cb.text()] = cb.isChecked()
            key_list.append(cb.text())
        print(status_dict)
        if not any(status_dict.values()):
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Tích Chọn Một Checkbox")
            return    
        dict_data_load = []
        dict_df = {}
        main_df = {} 
        for item in list_suff:
            browse , df_value = des_maintain(user,passW,current_project,list_suff,dict_region,standard_df,list_chkbox)
            region = next(iter(dict_region.values()))
            main_dict_chk = check_exist_keyName(browse,region)
            for key, value in status_dict.items():      
                if value:
                    #call_maintain_single(key,user,passW,current_project,list_suff,dict_region,standard_df,status_dict)
                    dict_df = main_one(browse,df_value,key,dict_region,suffix)
                    print( dict_df)
                    dict_data_load.append(dict_df)
                    print(dict_data_load)
                    #main_df = new_config(browse,df_value,main_dict_chk,region,main_df,suffix)
                    print(dict_data_load)
            for key, value in main_dict_chk.items():   
                print(key,value)   
                if value == 0:
                    main_df = new_config(browse,df_value,main_dict_chk,region,main_df,item)
                    main_dict_chk[key] = 1
                    dict_data_load.append(main_df)
                    print(main_df)
            browse.quit()
            dict_data_load = [x for x in dict_data_load if x is not None] # remove empty dict in list
            print(dict_data_load)
        #dict_data_load.extend(main_df)
        model1 = self.ui.table_maintain_key.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.table_maintain_key.setModel(PandasModel(empty_df))
        fixed_headers = ['SKU', 'Type', 'Value']
        view_df = pd.DataFrame(columns=fixed_headers)
        data_load_df = pd.DataFrame(dict_data_load)
        print(data_load_df)
        view_df = pd.concat([view_df , data_load_df], ignore_index=True).dropna()
        print(view_df)
        self.model = PandasModel(view_df)
        self.ui.table_maintain_key.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.table_maintain_key.setFont(font)
        self.ui.table_maintain_key.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.table_maintain_key.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.table_maintain_key.setColumnWidth(0,60)
        self.ui.table_maintain_key.setColumnWidth(1,50)
        self.ui.table_maintain_key.setColumnWidth(2,250)
        QMessageBox.information(self, "Thông Báo", "Maintain Done!!!")
#region , Realtime  Page
    def realtime_chk_keyConfig(self):
        # check data input
        current_product = self.ui.cb_realtime_product.currentText()
        current_project = self.ui.cb_realtime_project.currentText()
        suffix = self.ui.cb_realtime_surfix.text()
        if current_product == '' or current_project == '':
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
            return
        #Load SKU
        model = self.ui.list_realtime_sku.model()
        list_sku = []
        list_suff = []
        for item in range(model.rowCount()):
            index = model.index(item,0)
            value = model.data(index)
            list_sku.append(value)
        print("Dữ liệu:", list_sku)
        #Loc Standard from mapping
        standard_df,dict_region = gen_std(current_project,current_product,list_sku,suffix)
        # Extract Data From Ifuse
        user, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập UserName của bạn:")
        if ok and user:
            print("Bạn nhập:", user)
        passW, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập Password của bạn:",QLineEdit.EchoMode.Password)
        if ok and passW:
            print("Bạn nhập:", passW)
        if user == '' or passW == '':
            QMessageBox.critical(self, "Lỗi khởi tạo", "Phải nhập Username , Password!")
            return
        ifuse_df = login_ifuse(user,passW,current_project,list_sku,dict_region,suffix)
        #Hien thi Extracted Data len Table View
        model1 = self.ui.table_realtime_keyconfig.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.table_realtime_keyconfig.setModel(PandasModel(empty_df))    
        self.ui.lb_notice.setText("Export and Comparing , Please Wait!!!")
        self.model = PandasModel(standard_df)
        self.ui.table_realtime_keyconfig.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.table_realtime_keyconfig.setFont(font)
        self.ui.table_realtime_keyconfig.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.table_realtime_keyconfig.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.table_realtime_keyconfig.setColumnWidth(0,60)
        self.ui.table_realtime_keyconfig.setColumnWidth(1,50)
        self.ui.table_realtime_keyconfig.setColumnWidth(2,250)
        df_data = compare_ifuse_std(standard_df,ifuse_df)
        out_file =export_compare_result(df_data,current_project)
        self.ui.lb_notice.setText(out_file)
        to_mau(out_file)
        #Hien thi Extracted Data len Table View
        model = self.ui.table_realtime_result.model()
        if model is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.table_realtime_result.setModel(PandasModel(empty_df))
        self.ui.lb_notice.setText("Export and Comparing , Please Wait!!!")
        self.model = PandasModel(df_data)
        self.ui.table_realtime_result.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.table_realtime_result.setFont(font)
        self.ui.table_realtime_result.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.table_realtime_result.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.table_realtime_result.setColumnWidth(0,60)
        self.ui.table_realtime_result.setColumnWidth(1,50)
        self.ui.table_realtime_result.setColumnWidth(2,100)
        self.ui.table_realtime_result.setColumnWidth(3,100)
        self.ui.table_realtime_result.setColumnWidth(4,60)
        os.startfile(out_file)
#region , Bulk Page ---
    def labelPrint_auto_upload(self):
        user, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập UserName của bạn:")
        if ok and user:
            print("Bạn nhập:", user)
        passW, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập Password của bạn:",QLineEdit.EchoMode.Password)
        if ok and passW:
            print("Bạn nhập:", passW)
        if user == '' or passW == '':
            QMessageBox.critical(self, "Lỗi khởi tạo", "Phải nhập Username , Password!")
            return
        br = config_selenium()
        br.get('http://sfcweb.gg.ftv/Login.aspx')
        #//*[@id="divLang"]/div/span[1]
        auto_load_labelPrint(br,user,passW,self.ui.lb_notice.text())
         
    def bg_labelPrint_create(self):
        #Load sku list
        model = self.ui.list_bulk_sku.model()
        list_sku = []
        for row in range(model.rowCount()):
            index = model.index(row,0)
            value = model.data(index)
            list_sku.append(value)
        print("Dữ liệu:", list_sku)
        model1 = self.ui.tableView_3.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.tableView_3.setModel(PandasModel(empty_df))
        product = self.ui.cb_bulk_product.currentText()
        project = self.ui.cb_bulk_project.currentText()
        suf_fix = self.ui.tx_bulk_surfix.text()
        if product == None or project == "" or project == None:
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
            return 
        output_path,df = bg_labelPrint_generate(project,list_sku,suf_fix,product)    
        self.ui.lb_notice.setText(output_path)
        QMessageBox.information(self,"Thông Báo","Xuất File Bulk labelPrint Thành Công!")
        self.model = PandasModel(df)
        self.ui.tableView_3.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.tableView_3.setFont(font)
        self.ui.tableView_3.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.setColumnWidth(0,60)
        self.ui.tableView_3.setColumnWidth(1,50)
        self.ui.tableView_3.setColumnWidth(2,50)
        self.ui.tableView_3.setColumnWidth(3,67)
        self.ui.tableView_3.setColumnWidth(4,20)
        os.startfile(output_path) 
    def cg_labelPrint_create(self):
        #Load sku list
        model = self.ui.list_bulk_sku.model()
        list_sku = []
        for row in range(model.rowCount()):
            index = model.index(row,0)
            value = model.data(index)
            list_sku.append(value)
        print("Dữ liệu:", list_sku)
        model1 = self.ui.tableView_3.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.tableView_3.setModel(PandasModel(empty_df))
        product = self.ui.cb_bulk_product.currentText()
        project = self.ui.cb_bulk_project.currentText()
        suf_fix = self.ui.tx_bulk_surfix.text()
        if product == None or project == "" or project == None:
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
            return 
        output_path,df = cg_labelPrint_generate(project,list_sku,suf_fix,product)    
        self.ui.lb_notice.setText(output_path)
        QMessageBox.information(self,"Thông Báo","Xuất File Bulk labelPrint Thành Công!")
        self.model = PandasModel(df)
        self.ui.tableView_3.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.tableView_3.setFont(font)
        self.ui.tableView_3.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.setColumnWidth(0,60)
        self.ui.tableView_3.setColumnWidth(1,50)
        self.ui.tableView_3.setColumnWidth(2,50)
        self.ui.tableView_3.setColumnWidth(3,67)
        self.ui.tableView_3.setColumnWidth(4,20)
        os.startfile(output_path)        
    def fatp_labelPrint_create(self):
        #Load sku list
        model = self.ui.list_bulk_sku.model()
        list_sku = []
        for row in range(model.rowCount()):
            index = model.index(row,0)
            value = model.data(index)
            list_sku.append(value)
        print("Dữ liệu:", list_sku)
        model1 = self.ui.tableView_3.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.tableView_3.setModel(PandasModel(empty_df))
        product = self.ui.cb_bulk_product.currentText()
        project = self.ui.cb_bulk_project.currentText()
        suf_fix = self.ui.tx_bulk_surfix.text()
        if product == None or project == "" or project == None:
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
            return 
        output_path,df = fatp_labelPrint_generate(project,list_sku,suf_fix,product)    
        self.ui.lb_notice.setText(output_path)
        QMessageBox.information(self,"Thông Báo","Xuất File Bulk labelPrint Thành Công!")
        self.model = PandasModel(df)
        self.ui.tableView_3.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.tableView_3.setFont(font)
        self.ui.tableView_3.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.setColumnWidth(0,60)
        self.ui.tableView_3.setColumnWidth(1,50)
        self.ui.tableView_3.setColumnWidth(2,50)
        self.ui.tableView_3.setColumnWidth(3,67)
        self.ui.tableView_3.setColumnWidth(4,20)
        os.startfile(output_path)
    def pack_labelPrint_create(self):
        #Load sku list
        model = self.ui.list_bulk_sku.model()
        list_sku = []
        for row in range(model.rowCount()):
            index = model.index(row,0)
            value = model.data(index)
            list_sku.append(value)
        print("Dữ liệu:", list_sku)
        model1 = self.ui.tableView_3.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.tableView_3.setModel(PandasModel(empty_df))
        product = self.ui.cb_bulk_product.currentText()
        project = self.ui.cb_bulk_project.currentText()
        suf_fix = self.ui.tx_bulk_surfix.text()
        if product == None or project == "" or project == None:
            QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
            return  
        output_path,df = packing_labelPrint_generate(project,list_sku,suf_fix,product)    
        self.ui.lb_notice.setText(output_path)
        QMessageBox.information(self,"Thông Báo","Xuất File Bulk labelPrint Thành Công!")
        self.model = PandasModel(df)
        self.ui.tableView_3.setModel(self.model)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.tableView_3.setFont(font)
        self.ui.tableView_3.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.tableView_3.setColumnWidth(0,60)
        self.ui.tableView_3.setColumnWidth(1,50)
        self.ui.tableView_3.setColumnWidth(2,50)
        self.ui.tableView_3.setColumnWidth(3,67)
        self.ui.tableView_3.setColumnWidth(4,20)
        os.startfile(output_path) 
    def auto_upload(self):
        user, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập UserName của bạn:")
        if ok and user:
            print("Bạn nhập:", user)
        passW, ok = QInputDialog.getText(None, "Ifuse Account", "Nhập Password của bạn:",QLineEdit.EchoMode.Password)
        if ok and passW:
            print("Bạn nhập:", passW)
        if user == '' or passW == '':
            QMessageBox.critical(self, "Lỗi khởi tạo", "Phải nhập Username , Password!")
            return
        br = config_selenium()
        br.get('http://sfcweb.gg.ftv/Login.aspx')
        #//*[@id="divLang"]/div/span[1]
        change_language(br,user,passW,self.ui.lb_notice.text())
        #QMessageBox.information(self, "Thông báo", "Upload KeyConfig to Ifuse OK!")
    def bulk_single_inspect(self):
        model1 = self.ui.list_bulk_labelPrint.model()
        if model1 is not None:
            empty_df = pd.DataFrame()
            # Gán lại model rỗng cho tableView
            self.ui.list_bulk_labelPrint.setModel(PandasModel(empty_df))
        product = self.ui.cb_bulk_product.currentText()
        project = self.ui.cb_bulk_project.currentText()
        key_path = self.ui.lb_notice.text()
        df = main_chk(project,product,key_path)
        self.model = PandasModel(df)
        self.ui.list_bulk_labelPrint.setModel(self.model)
        self.ui.list_bulk_labelPrint.setColumnWidth(0,60)
        self.ui.list_bulk_labelPrint.setColumnWidth(1,38)
        self.ui.list_bulk_labelPrint.setColumnWidth(2,40)
        self.ui.list_bulk_labelPrint.setColumnWidth(3,47)
        self.ui.list_bulk_labelPrint.setColumnWidth(4,40)
        font = QFont()
        font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
        self.ui.list_bulk_labelPrint.setFont(font)
        #self.ui.list_bulk_keyConfig.setFont(font)
        self.ui.list_bulk_labelPrint.horizontalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )
        self.ui.list_bulk_labelPrint.verticalHeader().setStyleSheet(
            "QHeaderView::section { font-size: 7pt; }"
        )

    def keyconfig_create(self):
        try:
            model = self.ui.list_bulk_keyConfig.model()
            if model is not None:
                empty_df = pd.DataFrame()
                # Gán lại model rỗng cho tableView
                self.ui.list_bulk_keyConfig.setModel(PandasModel(empty_df))
            model1 = self.ui.list_bulk_labelPrint.model()
            if model1 is not None:
                empty_df = pd.DataFrame()
                # Gán lại model rỗng cho tableView
                self.ui.list_bulk_labelPrint.setModel(PandasModel(empty_df))
            product = self.ui.cb_bulk_product.currentText()
            project = self.ui.cb_bulk_project.currentText()
            suf_fix = self.ui.tx_bulk_surfix.text()
            if product == None or project == "" or project == None:
                QMessageBox.critical(self,"Lỗi Khởi Tạo","Cần Chọn Product,Project")
                return
            #Load sku list
            model = self.ui.list_bulk_sku.model()
            list_sku = []
            for row in range(model.rowCount()):
                index = model.index(row,0)
                value = model.data(index)
                list_sku.append(value)
            print("Dữ liệu:", list_sku)
            output_path,df = main_generate(project,list_sku,suf_fix,product)
            self.ui.lb_notice.setText(output_path)
            QMessageBox.information(self,"Thông Báo","Xuất File Bulk_Keyconfig Thành Công!")
            self.model = PandasModel(df)
            self.ui.list_bulk_keyConfig.setModel(self.model)
            font = QFont()
            font.setPointSize(7)   # chỉnh cỡ chữ (mặc định khoảng 11-12)
            self.ui.list_bulk_keyConfig.setFont(font)
            self.ui.list_bulk_keyConfig.horizontalHeader().setStyleSheet(
                "QHeaderView::section { font-size: 7pt; }"
            )
            self.ui.list_bulk_keyConfig.verticalHeader().setStyleSheet(
                "QHeaderView::section { font-size: 7pt; }"
            )
            self.ui.list_bulk_keyConfig.setColumnWidth(0,60)
            self.ui.list_bulk_keyConfig.setColumnWidth(1,25)
            self.ui.list_bulk_keyConfig.setColumnWidth(2,40)
            self.ui.list_bulk_keyConfig.setColumnWidth(3,40)
            self.ui.list_bulk_keyConfig.setColumnWidth(4,100)
            self.ui.list_bulk_keyConfig.setColumnWidth(5,100)
            os.startfile(output_path)
        except Exception as e:
            err_msg = traceback.format_exc()
            QMessageBox.critical(self, "Lỗi khởi tạo", str(e))
            #self.ui.lb_notice.setText(f"Error occur : {e}")
            logExport(f"Occur Error : \n {err_msg}")
#region view Page 
    def chk_modify_date(self):
        #load modifer của mapping table
        mt,bz,fl = get_timer()
        self.ui.lb_notice.setText(f"Last Modified Time --> MT5:{mt} , BZ5:{bz} , FL5:{fl}")
    def open_load_sku_form(self):
        if self.load_sku_form is None:
            self.load_sku_form = formLoadSku(self)
        self.load_sku_form.dataSaved.connect(self.receiveData)  # kết nối signal
        self.load_sku_form.show()
    def open_load_sku_form_maintain(self):
        self.load_sku_form = formLoadSku(self)
        self.load_sku_form.dataSaved.connect(self.receiveData_maintain)  # kết nối signal
        self.load_sku_form.show()       
    def open_load_sku_form_realtime(self):
        if self.load_sku_form is None:
            self.load_sku_form = formLoadSku(self)
        self.load_sku_form.dataSaved.connect(self.receiveData_realtime)  # kết nối signal
        self.load_sku_form.show()
    def receiveData_maintain(self, text):
        print(text)
        list_sku = text.split('\n')
        for item in list_sku:
            if item == '':
                list_sku.remove(item)
        model = QStringListModel()
        model.setStringList(list_sku)
        modelFont = QStandardItemModel()
        for item_text in list_sku:
            item = QStandardItem(str(item_text))
                # Set font (ví dụ: in đậm và cỡ chữ 12)
            font = QFont()
            font.setPointSize(12)
            font.setBold(True)
            item.setFont(font)
            
            # Set căn giữa (cả chiều ngang và chiều dọc)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            modelFont.appendRow(item)
        self.ui.list_maintain_sku_2.setModel(modelFont)
        self.ui.list_maintain_sku_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    def receiveData_realtime(self, text):
        print(text)
        list_sku = text.split('\n')
        for item in list_sku:
            if item == '':
                list_sku.remove(item)
        model = QStringListModel()
        model.setStringList(list_sku)
        modelFont = QStandardItemModel()
        for item_text in list_sku:
            item = QStandardItem(str(item_text))
                # Set font (ví dụ: in đậm và cỡ chữ 12)
            font = QFont()
            font.setPointSize(12)
            font.setBold(True)
            item.setFont(font)
            
            # Set căn giữa (cả chiều ngang và chiều dọc)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            modelFont.appendRow(item)
        self.ui.list_realtime_sku.setModel(modelFont)
        self.ui.list_realtime_sku.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    def receiveData(self, text):
        print(text)
        list_sku = text.split('\n')
        for item in list_sku:
            if item == '':
                list_sku.remove(item)
        model = QStringListModel()
        model.setStringList(list_sku)
        modelFont = QStandardItemModel()
        for item_text in list_sku:
            item = QStandardItem(str(item_text))
                # Set font (ví dụ: in đậm và cỡ chữ 12)
            font = QFont()
            font.setPointSize(12)
            font.setBold(True)
            item.setFont(font)
            
            # Set căn giữa (cả chiều ngang và chiều dọc)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            modelFont.appendRow(item)
        self.ui.list_bulk_sku.setModel(modelFont)
        self.ui.list_bulk_sku.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    def open_ship_form(self):
        if self.form_ship is None:
            self.form_ship = formBob(self)
        if self.ui.lb_notice.text() != 'Notification':
            self.send_text_b.connect(self.form_ship.update_ship)# Dùng send_text để kết nối tới form retail
            self.form_ship.show()
            self.send_text_b.emit(self.ui.lb_notice.text(),self.ui.tx_view_des.text(),self.ui.cb_view_product.currentText(),self.ui.tx_view_upc.text())
    def open_carton2_form(self):
        if self.form_carton2 is None and "IN" in self.ui.lb_notice.text():
            self.form_carton2 = formBob(self)
        else:
            return
        if self.ui.lb_notice.text() != 'Notification' and "IN" in self.ui.lb_notice.text():
            self.send_text_b.connect(self.form_carton2.update_carton2)# Dùng send_text để kết nối tới form retail
            self.form_carton2.show()
            self.send_text_b.emit(self.ui.lb_notice.text(),self.ui.tx_view_upc.text(),
                                  self.ui.tx_IMEI_start.text(), self.ui.tx_view_IMEI_end.text())
        else:
            return
    def open_carton_form(self):
        if self.form_carton is None:
            self.form_carton = formBob(self)
        if self.ui.lb_notice.text() != 'Notification':
            self.send_text_b.connect(self.form_carton.update_carton)# Dùng send_text để kết nối tới form retail
            self.form_carton.show()
            self.send_text_b.emit(self.ui.lb_notice.text(),self.ui.tx_view_upc.text(),self.ui.tx_view_softVer.text(),
                                  self.ui.tx_IMEI_start.text() + "-" + self.ui.tx_view_IMEI_end.text() + "-" + self.ui.tx_view_sap.text())
    def open_bob_form(self):
        if self.form_bob is None:
            self.form_bob = formBob(self)
        if self.ui.lb_notice.text() != 'Notification':
            self.send_text.connect(self.form_bob.update_bob)# Dùng send_text để kết nối tới form retail
            self.form_bob.show()
            self.send_text.emit(self.ui.lb_notice.text())
    def open_mrp_form(self,crr_item):
        crr_item = self.ui.tx_view_mlabel.text()
        if not crr_item:  # Kiểm tra rỗng
            QMessageBox.warning(self, "Alarm", "Your selected is not IN region.")
            return
        if self.form_m is None:
            self.form_m = formRetail(self)  
        if self.ui.lb_notice.text() != 'Notification':
            self.send_text_m.connect(self.form_m.update_mrp)# Dùng send_text để kết nối tới form retail
            self.form_m.show()
            self.send_text_m.emit(self.ui.lb_notice.text(),self.ui.tx_view_qr.text()) #emit để truyền text sang form B sau khi show form B      
    def open_retail_form(self):
        if self.form_b is None:
            self.form_b = formRetail(self)
        if self.ui.lb_notice.text() != 'Notification':
            self.send_text.connect(self.form_b.update_label)# Dùng send_text để kết nối tới form retail
            self.form_b.show()
            self.send_text.emit(self.ui.lb_notice.text()) #emit để truyền text sang form B sau khi show form B
    def load_sku_data(self):
        """Giả sử bạn đã load dữ liệu SKU vào list_view_sku"""
        model = self.ui.list_view_sku.model()
        if model is not None:
            self.sku_data_original = [
                    model.data(model.index(row, 0))
                    for row in range(model.rowCount())
                ]
        return self.sku_data_original
#region format
    #Format
    def format_listView(self,pd_list_view):
        modelFont = QStandardItemModel()
        # Lặp qua dữ liệu và thêm từng mục vào model
        data_list = pd_list_view.iloc[:, 0].tolist()
        for item_text in data_list:
            item = QStandardItem(str(item_text))
            
            # Set font (ví dụ: in đậm và cỡ chữ 12)
            font = QFont()
            font.setPointSize(15)
            font.setBold(True)
            item.setFont(font)
            
            # Set căn giữa (cả chiều ngang và chiều dọc)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            modelFont.appendRow(item)
        return modelFont
    #--> Hàm set nút bấm chính khi bấm sẽ bôi đậm màu
    def hight_light_color(self,clicked_button):
        buttons = [self.ui.bt_view_config, self.ui.bt_bulk_import, self.ui.bt_single_maintain,self.ui.bt_realtime_check]
        
        for btn in buttons:
            if btn == clicked_button:
                btn.setStyleSheet("background-color: #181f30; color: white; font-weight: bold;")  # màu đậm hơn #1f2c42
            else:
                btn.setStyleSheet("background-color: #26364d; color: white; font-weight: normal;")
    #--> Hàm add data vào combobox Project của tab Realtime 
    def cb_realtime_product_changed(self):
        gt_loc = (self.ui.cb_realtime_product.currentText(),)
        print(gt_loc)
        rows = get_value_by_product('projectTab','project','product',gt_loc)
        print(rows)
        #Project combobox
        self.ui.cb_realtime_project.clear()
        self.ui.cb_realtime_project.addItem("None")
        for row in rows:
            self.ui.cb_realtime_project.addItems(row)
    #--> Hàm add data vào combobox Project của tab Maintain 
    def cb_maintain_product_changed(self):
        gt_loc = (self.ui.cb_maintain_product_2.currentText(),)
        print(gt_loc)
        rows = get_value_by_product('projectTab','project','product',gt_loc)
        print(rows)
        #Project combobox
        self.ui.cb_maintain_project_2.clear()
        self.ui.cb_maintain_project_2.addItem("None")
        for row in rows:
            self.ui.cb_maintain_project_2.addItems(row)
    #--> Hàm add data vào combobox Project của tab Bulk Import 
    def cb_bulk_product_changed(self):
        gt_loc = (self.ui.cb_bulk_product.currentText(),)
        print(gt_loc)
        rows = get_value_by_product('projectTab','project','product',gt_loc)
        print(rows)
        #Project combobox
        self.ui.cb_bulk_project.clear()
        self.ui.cb_bulk_project.addItem("None")
        for row in rows:
            self.ui.cb_bulk_project.addItems(row)
    #--> Hàm add data vào combobox Project của tab View Config 
    def cb_product_changed(self):
        gt_loc = (self.ui.cb_view_product.currentText(),)
        print(gt_loc)
        rows = get_value_by_product('projectTab','project','product',gt_loc)
        regs = get_value_by_product('regionTab','region','product',gt_loc)
        print(rows)
        #Project combobox
        self.ui.cb_view_project.clear()
        self.ui.cb_view_region.clear()
        self.ui.cb_view_project.addItem("None")
        for row in rows:
            self.ui.cb_view_project.addItems(row)
        self.ui.cb_view_region.addItem("All")
        for row in regs:
            self.ui.cb_view_region.addItems(row)
    #--> Hàm add data vào combobox Product của all tab
    def load_combobox(self):
        #product combobox
        sp = get_value_db('productTab','product')[0]
        print(sp)
        self.ui.cb_view_product.addItem("None") 
        self.ui.cb_view_product.addItems(sp) 
        self.ui.cb_bulk_product.addItems(["None"]) 
        self.ui.cb_bulk_product.addItems(sp)           
        self.ui.cb_maintain_product_2.addItems(["None"])      
        self.ui.cb_maintain_product_2.addItems(sp)      
        self.ui.cb_realtime_product.addItems(["None"])  
        self.ui.cb_realtime_product.addItems(sp)  
        
        #region combobox
    #--> Hàm Load icon cho title của mainWindow
    def load_form_icon(self):
        strAbsPath = os.path.abspath(sys.argv[0])
        print(strAbsPath) 
        strCrrPath = os.path.dirname(strAbsPath)
        print(strCrrPath)
        strImgPath = os.path.join(strCrrPath,"img") + r"\profile.png"
        pixmap = QPixmap(strImgPath)
        return pixmap
    #--> Hàm load avar cho page chính
    def load_img_avar(self):
        strAbsPath = os.path.abspath(sys.argv[0])
        print(strAbsPath) 
        strCrrPath = os.path.dirname(strAbsPath)
        print(strCrrPath)
        strImgPath = os.path.join(strCrrPath,"img") + r"\avar.png"
        print(strImgPath)
        pixmap = QPixmap(strImgPath)
        #self.ui.lb_avartar.setPixmap(pixmap) # set ảnh vào label
        self.ui.lb_avartar.setScaledContents(True) # Set ảnh khớp với size của label
        # Lấy kích thước label hiện tại
        label_width = self.ui.lb_avartar.width()
        label_height = self.ui.lb_avartar.height()
        
        # Co ảnh cho vừa kích thước label, giữ tỉ lệ
        scaled_pixmap = pixmap.scaled(label_width, label_height)
        self.ui.lb_avartar.setPixmap(scaled_pixmap)
    #--> Hàm set vị trí center khi chạy của mainWindow
    def center_on_screen(self):
        # Lấy màn hình hiện tại
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Lấy kích thước form
        size = self.frameGeometry()

        # Tính vị trí chính giữa
        center_point = screen_geometry.center()
        size.moveCenter(center_point)

        # Đặt lại vị trí cửa sổ
        self.move(size.topLeft())
#region check Database
# --------------------Hàm check file Databse ---------------------------
    def view_combo_box_text_changed(self):
        # kiem tra file Mapping co ton tai hay khong
        current_text = self.ui.cb_view_project.currentText()
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_text,list_file)
        if mapp_path == '' and current_text != "None" and current_text !='':
            print(f"File Standard '{os.path.basename('mapping table')}' Is Not Exists!!!")
            raise FileNotFoundError(f"File Standard '{os.path.basename(mapp_path)}' Is Not Exists!!!")
        elif current_text == '' or current_text == "None" and mapp_path != '':
            return
        elif current_text !='' and mapp_path !='':
            print(f"File Standard '{os.path.basename('mapping table')}'  Exists!!!")
            # get toan bo SKU trong file mapping
            column_names = ['sku', 'des', 'storage','colorName','colorId','region','upc','ean','sap','startImei','endImei','bob_code','retailCode','mrpCode','overlayCode']
            pd_list_view = pd.DataFrame(columns=column_names)
            if current_text == 'MT5' and current_text != "None":
                pd_mapping = pd.read_excel(mapp_path,sheet_name='VN MP SKU Mapping Table',header=2,dtype={'EAN': str,'UPC碼' : str})
                pd_list_view = pd_mapping.iloc[:,[1,5,7,14,17,18,20,21,22,23,24,25,40,41,42,43]] # ':' la lay tat ca cac hang, con [] la cac cot can lay
                print(pd_list_view)
            elif current_text == 'FL5' and current_text != "None" :
                pd_mapping = pd.read_excel(mapp_path,sheet_name='FL5_POR_包裝對照表 (Mapping Table)',header=10,dtype={'UPC Code-12': str,'EAN Code-13' : str})
                filtered_df = pd_mapping[pd_mapping.iloc[:, 3] != 'Cancel']
                pd_list_view = filtered_df.iloc[:, [4,3]]
                print(pd_list_view)
            elif current_text =='BZ5' and current_text != "None":
                pd_mapping = pd.read_excel(mapp_path,sheet_name='BZ5 MP Control table_ VN',header=6,dtype={'UPC Code-12\n(except EMEA)': str,'EAN Code-13\n(EMEA only)' : str,'SKU ID (C-SKU for ATT only)': str})
                pd_des = pd.read_excel(mapp_path,sheet_name='POR Config List')
                pd_list_view = pd_mapping.iloc[:,[6]]
            #print(pd_mapping)
            #print(pd_list_view)
            #set data Frame vao QlistView
            model = QStringListModel()
            model.setStringList(pd_list_view.iloc[:, 0].tolist())
            #self.ui.list_view_sku.setModel(model)
            # Tạo model để chỉnh font
            modelFont = QStandardItemModel()
            # Lặp qua dữ liệu và thêm từng mục vào model
            data_list = pd_list_view.iloc[:, 0].tolist()
            for item_text in data_list:
                item = QStandardItem(str(item_text))
                
                # Set font (ví dụ: in đậm và cỡ chữ 12)
                font = QFont()
                font.setPointSize(15)
                font.setBold(True)
                item.setFont(font)
                
                # Set căn giữa (cả chiều ngang và chiều dọc)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
                modelFont.appendRow(item)

            # Gán model cho QListView
            self.ui.list_view_sku.setModel(modelFont)
            # Tắt tất cả các cách chỉnh sửa
            self.ui.list_view_sku.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    def bulk_combo_box_text_changed(self):
        current_text = self.ui.cb_bulk_project.currentText()
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_text,list_file)
        if mapp_path == '' and current_text != "None":
            print(f"File Standard '{os.path.basename('mapping table')}' Is Not Exists!!!")
            raise FileNotFoundError(f"File Standard '{os.path.basename(mapp_path)}' Is Not Exists!!!")
        else:
            print(f"File Standard '{os.path.basename('mapping table')}'  Exists!!!")
    def maintain_combo_box_text_changed(self):
        current_text = self.ui.cb_maintain_project_2.currentText()
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_text,list_file)
        if mapp_path == '' and current_text != "None":
            print(f"File Standard '{os.path.basename('mapping table')}' Is Not Exists!!!")
            raise FileNotFoundError(f"File Standard '{os.path.basename(mapp_path)}' Is Not Exists!!!")
        else:
            print(f"File Standard '{os.path.basename('mapping table')}'  Exists!!!")
    def realtime_combo_box_text_changed(self):
        current_text = self.ui.cb_realtime_project.currentText()
        if current_text == '':
            return
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_text,list_file)
        if mapp_path == '' and current_text != "None":
            print(f"File Standard '{os.path.basename('mapping table')}' Is Not Exists!!!")
            raise FileNotFoundError(f"File Standard '{os.path.basename(mapp_path)}' Is Not Exists!!!")
        else:
            print(f"File Standard '{os.path.basename('mapping table')}'  Exists!!!")
    #Region change
    def view_region_changed(self):
        if self.ui.cb_view_region.currentText() == 'All' and self.ui.cb_view_project.currentText() =='None':
            return
        list_file = []
        current_project = self.ui.cb_view_project.currentText()
        current_region = self.ui.cb_view_region.currentText()
        if current_project == '' or current_region == '':
            return
        column_names = ['sku']
        pd_list_view = pd.DataFrame(columns=column_names)  
        mapp_path = get_file_path(current_project,list_file)
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_project,list_file)
        if current_project == 'MT5':
            pd_mapping = pd.read_excel(mapp_path,sheet_name='VN MP SKU Mapping Table',header=2,dtype={'EAN': str,'UPC碼' : str})
            if current_region == "All" or current_region == "None":
                pd_list_view = pd_mapping['出貨PN']
                sku_list = pd_list_view.tolist() 
            else:
                condition = pd_mapping['SKU'].apply(region_convert) == current_region
                pd_list_view = pd_mapping.loc[condition, ['出貨PN']]
                print(pd_list_view)
                sku_list = pd_list_view.iloc[:, 0].tolist() 
        elif current_project == 'FL5':
            pd_mapping = pd.read_excel(mapp_path,sheet_name='FL5_POR_包裝對照表 (Mapping Table)',header=10,dtype={'UPC Code-12': str,'EAN Code-13' : str})
            if current_region == "All" or current_region == "None":
                pd_list_view = pd_mapping['Sales SKU']
                sku_list = pd_list_view.tolist() 
            else:
                condition = pd_mapping['SKU Name'].apply(region_convert) == current_region
                pd_list_view = pd_mapping.loc[condition, ['Sales SKU']]
                print(pd_list_view)
                sku_list = pd_list_view.iloc[:, 0].tolist() 
        elif current_project == 'BZ5':
            pd_mapping = pd.read_excel(mapp_path,sheet_name='BZ5 MP Control table_ VN',header=6,dtype={'UPC Code-12\n(except EMEA)': str,'EAN Code-13\n(EMEA only)' : str,'SKU ID (C-SKU for ATT only)': str})
            if current_region == "All" or current_region == "None":
                pd_list_view = pd_mapping.iloc[:, 6]#iloc[:,[6,7]]
                sku_list = pd_list_view.tolist() 
            else:
                condition = pd_mapping['SKU Name'].apply(region_convert) == current_region
                pd_list_view = pd_mapping.loc[condition, [pd_mapping.columns[6]]]
                print(pd_list_view)
                sku_list = pd_list_view.iloc[:,0].tolist()          
        modelFont = QStandardItemModel()
        # Lặp qua dữ liệu và thêm từng mục vào model
        for item_text in sku_list:
            item = QStandardItem(str(item_text))
            
            # Set font (ví dụ: in đậm và cỡ chữ 12)
            font = QFont()
            font.setPointSize(15)
            font.setBold(True)
            item.setFont(font)
            
            # Set căn giữa (cả chiều ngang và chiều dọc)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            modelFont.appendRow(item)
        self.ui.list_view_sku.setModel(modelFont)
    def reset_view_content(self):
        print(">>> ĐANG CHẠY HÀM RESET VIEW CONTENT...")
        self.ui.tx_view_blabel.setText('')
        self.ui.tx_view_des.setText('')
        self.ui.tx_view_rlabel.setText('')
        self.ui.tx_view_upc.setText('')
        self.ui.tx_view_brand.setText('')
        self.ui.tx_view_qr.setText('')
        self.ui.tx_view_price.setText('')
        self.ui.tx_view_mlabel.setText('')
        self.ui.tx_view_sap.setText('')
        self.ui.tx_view_color.setText('')

        self.ui.tx_view_carton.setText('')
        self.ui.tx_view_carton2.setText('')
        self.ui.tx_view_pallet1.setText('')
        self.ui.tx_view_pallet2.setText('')
        self.ui.tx_view_pallet3.setText('')
        self.ui.tx_view_repair.setText('')
        self.ui.tx_view_ship.setText('')
        self.ui.tx_view_overlay.setText('')
        self.ui.tx_view_wic.setText('')
        self.ui.tx_view_softVer.setText('')
        self.ui.tx_view_IMEI_end.setText('')
        self.ui.tx_IMEI_start.setText('')

    def view_listsku_clicked(self):
        list_file=[]
        current_project = self.ui.cb_view_project.currentText()
        current_region = self.ui.cb_view_region.currentText()
        mapp_path = get_file_path(current_project,list_file)
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_project,list_file)
        current_index = self.ui.list_view_sku.currentIndex()
        item_value = current_index.data(Qt.ItemDataRole.DisplayRole)
        #condition = pd_mapping.iloc[:, 1] == item_value
        if current_project == 'MT5':
            #pd_list_view = pd.DataFrame(columns=column_names)  
            pd_mapping = pd.read_excel(mapp_path,sheet_name='VN MP SKU Mapping Table',header=2,dtype={'EAN': str,'UPC碼' : str})
            condition = pd_mapping.iloc[:, 1] == item_value
            BOB_code = pd_mapping.loc[condition, pd_mapping.columns[40]].item().strip()
            if '\n' in BOB_code :
                mark = BOB_code.split('\n')
                BOB_code =  mark[1][:-2]
                rev = mark[1][-1:]
                BOB_code = BOB_code + f"_rev{rev}"
            else:
                if len(BOB_code)==15:
                    mark = BOB_code[:-2]
                    rev = BOB_code[-1:]
                    BOB_code = mark + f"_rev{rev}"
                else:
                    BOB_code=BOB_code
            Des_code = pd_mapping.loc[condition, pd_mapping.columns[5]]
            rap_code = pd_mapping.loc[condition, pd_mapping.columns[41]]            
            brand_code = pd_mapping.loc[condition, pd_mapping.columns[7]]         
            color_code = pd_mapping.loc[condition, pd_mapping.columns[18]]
            qr_code = pd_mapping.loc[condition, pd_mapping.columns[42]]
            #a = upc_code.item()
            storage_code = pd_mapping.loc[condition, pd_mapping.columns[14]]
            price_code = get_price_In("MT5")[0][0]
            m_code = 'MT5 MRP'
            region_code = region_convert(pd_mapping.loc[condition, pd_mapping.columns[20]].item())
            sw_ver = pd_mapping.loc[condition, pd_mapping.columns[32]].item()
            start_IMEI = pd_mapping.loc[condition, pd_mapping.columns[24]].item()
            end_IMEI = pd_mapping.loc[condition, pd_mapping.columns[25]].item()
            # Reset
            self.reset_view_content()
            #Xet BOB 
            product = self.ui.cb_view_product.currentText()
            bob_list = get_bob_list(BOB_code,product)
            if bob_list:
                self.ui.tx_view_blabel.setText(bob_list[0][0])
            else:
                self.ui.tx_view_blabel.setText('')
            self.ui.tx_view_des.setText(Des_code.item())
            #self.ui.tx_view_rlabel.setText(rap_code.item())         
            self.ui.tx_view_brand.setText(brand_code.item())
            self.ui.tx_view_softVer.setText(sw_ver)
            self.ui.tx_IMEI_start.setText(start_IMEI)
            self.ui.tx_view_IMEI_end.setText(end_IMEI)
            mapp_rap=''
            if region_code == 'ATT' or region_code == 'TMO':
                sap_code = pd_mapping.loc[condition, pd_mapping.columns[23]]
                self.ui.tx_view_sap.setText(sap_code.item())
                self.ui.tx_view_color.setText(color_code.item())
                mapp_rap = 'MT5' +'_FIHVN_RAP' + '_' + region_code + '_' + storage_code.item() + '_' + color_code.item() + '_MP'
                upc_code = pd_mapping.loc[condition, pd_mapping.columns[21]]
                self.ui.tx_view_rlabel.setText(mapp_rap)
                self.ui.tx_view_upc.setText(upc_code.item())
            elif region_code == 'IN':
                #self.ui.tx_view_qr.setText(sap_code.item())
                self.ui.tx_view_price.setText(color_code.item())                
                self.ui.tx_view_mlabel.setText(price_code)  
                mapp_rap = 'MT5' +'_FIHVN_RAP' + '_' + region_code + '_' +  'MP'
                upc_code = pd_mapping.loc[condition, pd_mapping.columns[21]]
                self.ui.tx_view_rlabel.setText(mapp_rap)
                self.ui.tx_view_upc.setText(upc_code.item())
                self.ui.tx_view_mlabel.setText(m_code)
                self.ui.tx_view_qr.setText(qr_code.item())

                in2 = kitting_process("carton2","retail","MT5","packing")
                self.ui.tx_view_carton2.setText(in2[0][0] + "_" + in2[0][1])
                self.ui.tx_view_carton2.setToolTip(in2[0][0] + "_" + in2[0][1])
                wic = kitting_process("wic","retail","MT5","packing")
                self.ui.tx_view_wic.setText(wic[0][0] + "_" + wic[0][1])
                self.ui.tx_view_wic.setToolTip(wic[0][0] + "_" + wic[0][1])
            elif region_code == 'EMEA':
                mapp_rap = 'MT5' +'_FIHVN_RAP' + '_' + region_code + '_' +  'MP_45'
                ean_code = pd_mapping.loc[condition, pd_mapping.columns[22]].item()
                self.ui.tx_view_rlabel.setText(mapp_rap)   
                self.ui.tx_view_upc.setText(ean_code)
            else:
                mapp_rap = 'MT5' +'_FIHVN_RAP' + '_' + region_code + '_' +  'MP'
                upc_code = pd_mapping.loc[condition, pd_mapping.columns[21]]
                self.ui.tx_view_rlabel.setText(mapp_rap)  
                self.ui.tx_view_upc.setText(upc_code.item()) 
            product = self.ui.cb_bulk_product.currentText()
        # label print fill
            carton_name = label_print_process(item_value,region_code,"packing","carton","MT5",0)
            ship_name = label_print_process(item_value,region_code,"packing","ship","MT5",1)
            overLay_name = label_print_process(item_value,region_code,"packing","over","MT5",0)
            self.ui.tx_view_carton.setText(carton_name[0][0] + "_" + carton_name[0][1])
            self.ui.tx_view_carton.setToolTip(carton_name[0][0] + "_" + carton_name[0][1])
            pl1 = kitting_process("pallet1","kit","MT5","packing")
            pl2 = kitting_process("pallet2","kit","MT5","packing")
            pl3 = kitting_process("pallet3","kit","MT5","packing")
            repair = kitting_process("repair-in","kit","MT5","packing")
            self.ui.tx_view_pallet1.setText(pl1[0][0] + "_" + pl1[0][1])
            self.ui.tx_view_pallet1.setToolTip(pl1[0][0] + "_" + pl1[0][1])
            self.ui.tx_view_pallet2.setText(pl2[0][0] + "_" + pl2[0][1])
            self.ui.tx_view_pallet2.setToolTip(pl2[0][0] + "_" + pl2[0][1])
            self.ui.tx_view_pallet3.setText(pl3[0][0] + "_" + pl3[0][1])
            self.ui.tx_view_pallet3.setToolTip(pl3[0][0] + "_" + pl3[0][1])
            self.ui.tx_view_ship.setText(ship_name[0][0] + "_" + ship_name[0][1])
            self.ui.tx_view_ship.setToolTip(ship_name[0][0] + "_" + ship_name[0][1])
            self.ui.tx_view_repair.setText(repair[0][0] + "_" + repair[0][1])
            self.ui.tx_view_repair.setToolTip(repair[0][0] + "_" + repair[0][1])
            self.ui.tx_view_overlay.setText(overLay_name[0][0] + "_" + overLay_name[0][1])
            self.ui.tx_view_overlay.setToolTip(overLay_name[0][0] + "_" + overLay_name[0][1])

            self.ui.lb_notice.setText(f"{"MT5"},{item_value},{region_code},{BOB_code}")
        elif current_project == 'FL5':
            product = self.ui.cb_view_product.currentText()
            pd_mapping = pd.read_excel(mapp_path,sheet_name='FL5_POR_包裝對照表 (Mapping Table)',
                                       header=10,dtype={'UPC Code-12': str,'EAN Code-13' : str})  
            (BOB_code,Des_code,rap_code,brand_code,color_code,qr_code,storage_code,price_code,m_code,
            sw_ver,start_IMEI,end_IMEI,sap_code,mapp_rap,upc_code,region_code) = label_infor_return(pd_mapping,item_value,4,55,
                                                                                        28,56,11,9,68,44,5,"FL5",32,19,20,48,49,50,product)
            self.reset_view_content()
            
            self.ui.tx_view_blabel.setText(BOB_code)
            self.ui.tx_view_des.setText(Des_code)
            #self.ui.tx_view_rlabel.setText(rap_code.item())         
            self.ui.tx_view_brand.setText(brand_code)
            self.ui.tx_view_softVer.setText(sw_ver)
            self.ui.tx_IMEI_start.setText(start_IMEI)
            self.ui.tx_view_IMEI_end.setText(end_IMEI)
            self.ui.tx_view_sap.setText(sap_code)
            self.ui.tx_view_color.setText(color_code)
            self.ui.tx_view_rlabel.setText(mapp_rap)
            self.ui.tx_view_upc.setText(upc_code)
            #self.ui.tx_view_rlabel.setText(mapp_rap)
            self.ui.tx_view_mlabel.setText(m_code)
            self.ui.tx_view_qr.setText(qr_code)
            self.ui.tx_view_price.setText(price_code)

        # label print fill
            carton_name = label_print_process(item_value,region_code,"packing","carton","FL5",0)
            ship_name = label_print_process(item_value,region_code,"packing","ship","FL5",1)
            overLay_name = label_print_process(item_value,region_code,"packing","over","FL5",0)
            self.ui.tx_view_carton.setText(carton_name[0][0] + "_" + carton_name[0][1])
            self.ui.tx_view_carton.setToolTip(carton_name[0][0] + "_" + carton_name[0][1])
            pl1 = kitting_process("pallet1","kit","FL5","packing")
            pl2 = kitting_process("pallet2","kit","FL5","packing")
            pl3 = kitting_process("pallet3","kit","FL5","packing")
            repair = kitting_process("repair-in","kit","FL5","packing")
            self.ui.tx_view_pallet1.setText(pl1[0][0] + "_" + pl1[0][1])
            self.ui.tx_view_pallet1.setToolTip(pl1[0][0] + "_" + pl1[0][1])
            self.ui.tx_view_pallet2.setText(pl2[0][0] + "_" + pl2[0][1])
            self.ui.tx_view_pallet2.setToolTip(pl2[0][0] + "_" + pl2[0][1])
            self.ui.tx_view_pallet3.setText(pl3[0][0] + "_" + pl3[0][1])
            self.ui.tx_view_pallet3.setToolTip(pl3[0][0] + "_" + pl3[0][1])
            self.ui.tx_view_ship.setText(ship_name[0][0] + "_" + ship_name[0][1])
            self.ui.tx_view_ship.setToolTip(ship_name[0][0] + "_" + ship_name[0][1])
            self.ui.tx_view_repair.setText(repair[0][0] + "_" + repair[0][1])
            self.ui.tx_view_repair.setToolTip(repair[0][0] + "_" + repair[0][1])
            self.ui.tx_view_overlay.setText(overLay_name[0][0] + "_" + overLay_name[0][1])
            self.ui.tx_view_overlay.setToolTip(overLay_name[0][0] + "_" + overLay_name[0][1])
            if region_code == 'IN':
                in2 = kitting_process("carton2","retail","FL5","packing")
                self.ui.tx_view_carton2.setText(in2[0][0] + "_" + in2[0][1])
                self.ui.tx_view_carton2.setToolTip(in2[0][0] + "_" + in2[0][1])
                wic = kitting_process("wic","retail","FL5","packing")
                self.ui.tx_view_wic.setText(wic[0][0] + "_" + wic[0][1])
                self.ui.tx_view_wic.setToolTip(wic[0][0] + "_" + wic[0][1])
            BOB_code = BOB_code[:13]
            self.ui.lb_notice.setText(f"{"FL5"},{item_value},{region_code},{BOB_code}")
        elif current_project == 'BZ5':
            product = self.ui.cb_view_product.currentText()
            pd_mapping = pd.read_excel(mapp_path,sheet_name='BZ5 MP Control table_ VN',header=6,
                                       dtype={'UPC Code-12\n(except EMEA)': str,'EAN Code-13\n(EMEA only)' : str,
                                              'SKU ID (C-SKU for ATT only)': str})
            (BOB_code,Des_code,rap_code,brand_code,color_code,qr_code,storage_code,price_code,m_code,
            sw_ver,start_IMEI,end_IMEI,sap_code,mapp_rap,upc_code,region_code) = label_infor_return(pd_mapping,item_value,6,45,26,46,14,12,47,19,7,"BZ5",41,22,23,16,17,18,product)
            
            self.reset_view_content()
            self.ui.tx_view_blabel.setText(BOB_code)
            self.ui.tx_view_des.setText(Des_code)
            #self.ui.tx_view_rlabel.setText(rap_code.item())         
            self.ui.tx_view_brand.setText(brand_code)
            self.ui.tx_view_softVer.setText(sw_ver)
            self.ui.tx_IMEI_start.setText(start_IMEI)
            self.ui.tx_view_IMEI_end.setText(end_IMEI)
            self.ui.tx_view_sap.setText(sap_code)
            self.ui.tx_view_color.setText(color_code)
            self.ui.tx_view_rlabel.setText(mapp_rap)
            self.ui.tx_view_upc.setText(upc_code)
            #self.ui.tx_view_rlabel.setText(mapp_rap)
            self.ui.tx_view_mlabel.setText(m_code)
            self.ui.tx_view_qr.setText(qr_code)
            self.ui.tx_view_price.setText(price_code)
            
        # label print fill
            carton_name = label_print_process(item_value,region_code,"packing","carton","BZ5",0)
            ship_name = label_print_process(item_value,region_code,"packing","ship","BZ5",1)
            overLay_name = label_print_process(item_value,region_code,"packing","over","BZ5",0)
            self.ui.tx_view_carton.setText(carton_name[0][0] + "_" + carton_name[0][1])
            self.ui.tx_view_carton.setToolTip(carton_name[0][0] + "_" + carton_name[0][1])
            pl1 = kitting_process("pallet1","kit","BZ5","packing")
            pl2 = kitting_process("pallet2","kit","BZ5","packing")
            pl3 = kitting_process("pallet3","kit","BZ5","packing")
            repair = kitting_process("repair-in","kit","BZ5","packing")
            self.ui.tx_view_pallet1.setText(pl1[0][0] + "_" + pl1[0][1])
            self.ui.tx_view_pallet1.setToolTip(pl1[0][0] + "_" + pl1[0][1])
            self.ui.tx_view_pallet2.setText(pl2[0][0] + "_" + pl2[0][1])
            self.ui.tx_view_pallet2.setToolTip(pl2[0][0] + "_" + pl2[0][1])
            self.ui.tx_view_pallet3.setText(pl3[0][0] + "_" + pl3[0][1])
            self.ui.tx_view_pallet3.setToolTip(pl3[0][0] + "_" + pl3[0][1])
            self.ui.tx_view_ship.setText(ship_name[0][0] + "_" + ship_name[0][1])
            self.ui.tx_view_ship.setToolTip(ship_name[0][0] + "_" + ship_name[0][1])
            self.ui.tx_view_repair.setText(repair[0][0] + "_" + repair[0][1])
            self.ui.tx_view_repair.setToolTip(repair[0][0] + "_" + repair[0][1])
            self.ui.tx_view_overlay.setText(overLay_name[0][0] + "_" + overLay_name[0][1])
            self.ui.tx_view_overlay.setToolTip(overLay_name[0][0] + "_" + overLay_name[0][1])
            if region_code == 'IN':
                in2 = kitting_process("carton2","retail","BZ5","packing")
                self.ui.tx_view_carton2.setText(in2[0][0] + "_" + in2[0][1])
                self.ui.tx_view_carton2.setToolTip(in2[0][0] + "_" + in2[0][1])
                wic = kitting_process("wic","retail","BZ5","packing")
                self.ui.tx_view_wic.setText(wic[0][0] + "_" + wic[0][1])
                self.ui.tx_view_wic.setToolTip(wic[0][0] + "_" + wic[0][1])
            BOB_code = BOB_code[:13]
            self.ui.lb_notice.setText(f"{"BZ5"},{item_value},{region_code},{BOB_code}")
    def filter_sku_list(self):
        """Hàm lọc và hiển thị kết quả tìm kiếm."""
        source_model = self.ui.list_view_sku.model()
        #self.model.clear()
        
        # Chuyển đổi văn bản tìm kiếm sang chữ thường để tìm kiếm không phân biệt chữ hoa, chữ thường
        #search_text = text.strip().lower()
        # Tạo proxy model để lọc
        self.sku_proxy_model = QSortFilterProxyModel(self)
        self.sku_proxy_model.setSourceModel(source_model)
        self.sku_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)  # Không phân biệt hoa/thường
        self.sku_proxy_model.setFilterKeyColumn(0)
        # Gán proxy model vào list_view_sku
        self.ui.list_view_sku.setModel(self.sku_proxy_model)
        # Kết nối QLineEdit để lọc khi gõ
        self.ui.tx_view_skuSearch.textChanged.connect(
            lambda text: self.sku_proxy_model.setFilterFixedString(text)
        )
    def setup_sku_search(self):
        self.reset_view_content()
        current_text = self.ui.cb_view_project.currentText()
        list_file = list_file_in_folder("database")
        mapp_path = get_file_path(current_text,list_file)
        sku_list = []
        if self.ui.cb_view_project.currentText() == 'MT5':
            pd_mapping = pd.read_excel(mapp_path,sheet_name='VN MP SKU Mapping Table',header=2,dtype={'EAN': str,'UPC碼' : str})
            sku_list = pd_mapping.iloc[:,1].to_list()
            print(sku_list)
        elif self.ui.cb_view_project.currentText() == 'FL5':
            pd_mapping = pd.read_excel(mapp_path,sheet_name='FL5_POR_包裝對照表 (Mapping Table)',header=10,dtype={'UPC Code-12': str,'EAN Code-13' : str})
            filtered_df = pd_mapping[pd_mapping.iloc[:, 3] != 'Cancel']
            print(filtered_df)
            sku_list = filtered_df.iloc[:,4]
        elif self.ui.cb_view_project.currentText() == 'BZ5':
            pd_mapping = pd.read_excel(mapp_path,sheet_name='BZ5 MP Control table_ VN',header=6,dtype={'UPC Code-12\n(except EMEA)': str,'EAN Code-13\n(EMEA only)' : str,'SKU ID (C-SKU for ATT only)': str})
            sku_list = pd_mapping.iloc[:,6]
            sku_list = sku_list.dropna().to_list()
        print(sku_list)
        rs_list = []
        txt = self.ui.tx_view_skuSearch.text().strip().lower()
        for item in sku_list:
            print(item)
            if len(str(item))>6 and item != 'nan':
                if txt in item.lower():
                    a = item
        print('?')
        rs_list = [item for item in sku_list if txt in str(item).lower() and str(item) != 'nan']
        print(rs_list)
        self.format_load_listView(rs_list,self.ui.list_view_sku)
    def format_load_listView(self,list_sku,list_view):
        modelFont = QStandardItemModel()
        # Lặp qua dữ liệu và thêm từng mục vào model
        for item_text in list_sku:
            item = QStandardItem(str(item_text))
            
            # Set font (ví dụ: in đậm và cỡ chữ 12)
            font = QFont()
            font.setPointSize(15)
            font.setBold(True)
            item.setFont(font)
            
            # Set căn giữa (cả chiều ngang và chiều dọc)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            modelFont.appendRow(item)
        list_view.setModel(modelFont)
#region form BOB
class formBob(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self)
        self.parent = parent
        self.ui = Ui_bobForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Check Real BOB Image")
        self.setWindowIcon(QIcon('img/kca.ico'))
        # Thay thế Qgraphicviewer bằng imgViewer để có thể zoom và di chuyển ảnh
        parent_layout = self.ui.view_bob_img.parent().layout()
        parent_layout1 = self.ui.view_bob_print.parent().layout()
        self.bob_img = imgViewer(self)
        self.bob_print = imgViewer(self)
        parent_layout.replaceWidget(self.ui.view_bob_img,self.bob_img)
        parent_layout1.replaceWidget(self.ui.view_bob_print,self.bob_print)
        self.ui.view_bob_img.deleteLater()
        self.ui.view_bob_print.deleteLater()
        self.ui.view_bob_img = self.bob_img
        self.ui.view_bob_print = self.bob_print
        if self.parent:
            parent_pos = self.parent.pos()
            self.move(parent_pos.x() , parent_pos.y() )   
    def update_ship(self,text,des,product,upc):
        arr = text.split(',')
        line = arr[0]
        sku = arr[1]
        region = arr[2]
        bob_code = arr[3]
        self.ui.lb_region.setText(region) 
        self.ui.lb_sku.setText(sku) 
        root = get_sys_path_sql("approve") 
        img_path = os.path.join(root,line,'ship','img',sku + '.png')
        if region not in ['ATT','TMO','VZW']:
            region_load = 'std'
        elif region in ['ATT','TMO','VZW']:
            region_load = region
        print_path = os.path.join(root,line,'ship','plan',region_load + '.png')   
        load_img_bob(img_path,self.ui.view_bob_img,self,10,10)
        load_img_bob(print_path,self.ui.view_bob_print,self,1,1)     
        table_content_bts(self,self.ui.tableView,region,product,des,line,sku,upc)     
    def update_bob(self,text):
        arr = text.split(',')
        line = arr[0]
        sku = arr[1]
        region = arr[2]
        bob_code = arr[3]
        self.ui.lb_region.setText(region) 
        self.ui.lb_sku.setText(sku) 
        root = get_sys_path_sql("approve") 
        img_path = os.path.join(root,line,'bob','img',sku + '.png')
        print_path = os.path.join(root,line,'bob','plan',bob_code + '.png')
        load_img_bob(img_path,self.ui.view_bob_img,self,10,10)
        load_img_bob(print_path,self.ui.view_bob_print,self,1,1)
    def update_carton(self,txt,upc,soft,imei):
        arr = txt.split(',')
        line = arr[0]
        sku = arr[1]
        region = arr[2]
        bob_code = arr[3]
        self.ui.lb_region.setText(region) 
        self.ui.lb_sku.setText(sku) 
        root = get_sys_path_sql("approve") 
        img_path = os.path.join(root,line,'carton','img',sku + '.png')
        print_path = os.path.join(root,line,'carton','plan',region + '.png')
        load_img_bob(img_path,self.ui.view_bob_img,self,25,25)
        load_img_bob(print_path,self.ui.view_bob_print,self,1,1)
        table_content_generate(self,self.ui.tableView,region,sku,upc,imei,line,soft)
    def update_carton2(self,txt,upc,imei1,imei2):
        arr = txt.split(',')
        line = arr[0]
        sku = arr[1]
        region = arr[2]
        bob_code = arr[3]
        self.ui.lb_region.setText(region) 
        self.ui.lb_sku.setText(sku) 
        root = get_sys_path_sql("approve") 
        img_path = os.path.join(root,line,'carton2', 'in_img.png')
        print_path = os.path.join(root,line,'carton2','in_plan.png')
        load_img_bob(img_path,self.ui.view_bob_img,self,25,25)
        #traceback.print_stack()
        load_img_bob(print_path,self.ui.view_bob_print,self,1,1)
        table_content_generate(self,self.ui.tableView,region,sku,upc,imei1,line,imei2)        
    def add_row(self, data: list):
        """Thêm một dòng dữ liệu"""
        items = [QStandardItem(str(val)) for val in data]
        self.model.appendRow(items)
    def format_cell(self, row: int, col: int,
                    font: QFont = None,
                    color: QColor = None,
                    align: Qt.AlignmentFlag = None):
        """Định dạng 1 ô"""
        item = self.model.item(row, col)
        if item:
            if font:
                item.setFont(font)
            if color:
                item.setForeground(color)
            if align:
                item.setTextAlignment(align)
#region form load SKU 
class formLoadSku(QMainWindow):
    dataSaved = Signal(str)
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_skuForm()
        self.ui.setupUi(self)
        #self.ui.tx_sku.textChanged.connect(self.format_tx_sku_load)
        self.ui.bt_save.clicked.connect(self.save_sku_list)
    def save_sku_list(self):
        sku_list = self.ui.tx_sku.toPlainText()
        self.dataSaved.emit(sku_list)   # phát signal về Form A
        self.close() 
    def format_tx_sku_load(self):
        cursor = self.ui.tx_sku.textCursor()

        fmt = QTextCharFormat()
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        fmt.setFont(font)

        # Áp format vào đoạn text vừa nhập
        cursor.mergeCharFormat(fmt)

        # Căn giữa đoạn hiện tại
        block_fmt = cursor.blockFormat()
        block_fmt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cursor.setBlockFormat(block_fmt)

        # Trả cursor lại (nếu không thì nó bị kẹt)
        self.ui.tx_sku.setTextCursor(cursor)
    #region form Retail
class formRetail(QMainWindow):
#------Khoi Tao---------------------------------------------------
    def __init__(self, parent = None ):
        QMainWindow.__init__(self)
        self.ui = Ui_retailForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Check Real Retail Image")
        self.setWindowIcon(QIcon('img/kca.ico'))
        # Thay thế QGraphicsView mặc định bằng class imgViewer có hỗ trợ zoom
        parent_layout = self.ui.view_retail.parent().layout()

        self.viewer_retail = imgViewer(self)
        parent_layout.replaceWidget(self.ui.view_retail, self.viewer_retail)
        self.ui.view_retail.deleteLater()
        self.ui.view_retail = self.viewer_retail 
        #show window 
        #self.show()
    def update_mrp(self,text,mlabel):
        arr = text.split(',')
        line = arr[0]
        sku = arr[1]
        region = arr[2]
        self.ui.lb_r_sku.setText(sku)   
        self.ui.lb_r_region.setText(f"2D Barcode : {mlabel[:-2]} {sku} MFG Date")   
        root = get_sys_path_sql("approve") 
        retail_path = os.path.join(root,line,'wic',line + ' MRP.png') 
        scene = QGraphicsScene(self)
        pixmap = QPixmap(retail_path)
        scene.addPixmap(pixmap)
        self.ui.view_retail.setScene(scene)
        self.ui.view_retail.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        # Kích hoạt kéo tay và zoom dưới con trỏ
        self.ui.view_retail.setDragMode(self.ui.view_retail.DragMode.ScrollHandDrag)
        self.ui.view_retail.setTransformationAnchor(self.ui.view_retail.ViewportAnchor.AnchorUnderMouse)   
    def update_label(self, text):
        print(text)
        arr = text.split(',')
        line = arr[0]
        sku = arr[1]
        region = arr[2]
        self.ui.lb_r_sku.setText(sku)   
        self.ui.lb_r_region.setText(region) 
        root = get_sys_path_sql("approve") 
        retail_path = os.path.join(root,line,'retail',sku + '.png')
        print(retail_path)
        scene = QGraphicsScene(self)
        pixmap = QPixmap(retail_path)
        scene.addPixmap(pixmap)
        self.ui.view_retail.setScene(scene)
        self.ui.view_retail.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        # Kích hoạt kéo tay và zoom dưới con trỏ
        self.ui.view_retail.setDragMode(self.ui.view_retail.DragMode.ScrollHandDrag)
        self.ui.view_retail.setTransformationAnchor(self.ui.view_retail.ViewportAnchor.AnchorUnderMouse)

#check xem có phải Hàm main không và show form
if __name__ == "__main__":
    # Bat loi toan cuc
    def exception_hook(exctype, value, tb):
        import traceback
        err_msg = "".join(traceback.format_exception(exctype, value, tb))
        logExport(f"Uncaught Exception:\n{err_msg}")
        QMessageBox.critical(None, "Lỗi không bắt được", str(value))
    sys.excepthook = exception_hook
    #add_bob_to_sql()
    #update_sp()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 
    
    '''except Exception as e:
        QMessageBox.critical("Lỗi khởi tạo", str(e))
        #self.ui.lb_notice.setText(f"Error occur : {e}")
        file,func,line = get_details_error(e)
        logExport(f"Occur Error : \n -File name: {file} \n -Function : {func} \n -Line Name: {line} \n -Error Content: {e}")'''