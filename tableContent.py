'''from PySide6.QtWidgets import QApplication,QTableView,QHeaderView,QAbstractItemView
from PySide6.QtCore import Qt'''
from PySide6.QtGui import QStandardItemModel,QStandardItem,QFont,QColor
from PySide6.QtCore import QAbstractTableModel, Qt,Signal # xet thuoc tinh khong chinh sua
from sqliteProcess import *
from common import *
def sscc_rule_generate(line):
    prefix = "(00)"
    N1 = "7"
    GS1 = "840353906"
    N11 = ""
    serial = "0000000"
    N18 = "(Check Sum SSCC)"
    if line == "MT5":
        N11 = "(7,8,9)"
    elif line == "BZ5":
        N11 = "(4,5,6)"
    else:
        N11 = "(0,1,2,3)"
    return f"{prefix}{N1}{GS1}{N11}{serial}{N18}"
def table_content_bts(self,table_obj,region,product,des,line,sku,upc):
    self.model = QStandardItemModel()
    table_obj.setModel(self.model)
    self.model.setHorizontalHeaderLabels(["Item","Standard"])
    no_phone = 0
    no_pallet = 0
    no_carton = 0
    phone_per_pallet = 0
    pack_address = ""
    sscc = ""
    if region not in ['ATT','TMO','VZW']:
        phone_per_pallet = get_qty_packing(line,product,region_convert_pack(region),"Box_Pallet")[0][0]
        no_pallet = 5
        no_carton = get_qty_packing(line,product,region_convert_pack(region),"Shipper_Pallet")[0][0] * 5
        no_phone = phone_per_pallet * 5
        pack_address = get_address_packing("All",product,"IN-Packed")[0][0]
        self.add_row(["1-2D Barcode", f"{"Mã Invoice"},{des},{str(no_phone)},{str(no_pallet)},{str(no_carton)},{str(phone_per_pallet)},{pack_address}, Số PO, Số Pallet,{sscc_rule_generate(line)}"])
        self.add_row(["2-Ship To", get_address_packing("All",product,"Ship to")[0][0]])
        self.add_row(["3-Ship From", pack_address])
        self.add_row(["4-Invoice Number", "Số Invoice liên quan PC"])
        self.add_row(["5-Ship Method", "Air Freight"])
        self.add_row(["6-PO Number", "Số PO, Google cung cấp"])
        self.add_row(["7-SKU", sku])
        self.add_row(["8-Total Unit Qty", phone_per_pallet])
        self.add_row(["9-Total Carton Qty", no_carton/5])
        self.add_row(["10-Qty Per Pallet", phone_per_pallet])
        self.add_row(["11-Pallet Count", "1 to 5"])
        self.add_row(["12-SSCC(Pallet ID)", sscc_rule_generate(line)])
        self.add_row(["13-COO", "Vietnam"])
    elif region =='VZW':
        phone_per_pallet = get_qty_packing(line,product,region_convert_pack(region),"Box_Pallet")[0][0]
        no_pallet = 5
        no_carton = get_qty_packing(line,product,region_convert_pack(region),"Shipper_Pallet")[0][0] * 5
        no_phone = phone_per_pallet * 5
        pack_address = get_address_packing("All",product,"IN-Packed")[0][0]
        self.add_row(["1-2D Barcode", f"{"Số PO, Số Pallet"},{des},{str(no_phone)},{str(no_pallet)},{str(no_carton)},{str(phone_per_pallet)}"])
        self.add_row(["2-Ship To", get_address_packing("All",product,"Ship to")[0][0]])
        self.add_row(["3-Ship From", pack_address])
        self.add_row(["4-Invoice Number", "Số Invoice liên quan PC"])
        self.add_row(["5-Ship Method", "Air Freight"])
        self.add_row(["6-PO Number", "Số PO, Google cung cấp"])
        self.add_row(["7-SKU", sku])
        self.add_row(["8-Total Unit Qty", phone_per_pallet])
        self.add_row(["9-Total Carton Qty", no_carton/5])
        self.add_row(["10-Qty Per Pallet", phone_per_pallet])
        self.add_row(["11-Pallet Count", "1 to 5"])
        self.add_row(["12-SSCC(Pallet ID)", sscc_rule_generate(line)])
        self.add_row(["13-COO", "Vietnam"])
    elif region == "ATT":
        phone_per_pallet = get_qty_packing(line,product,region_convert_pack(region),"Box_Pallet")[0][0]
        no_pallet = 5
        no_carton = get_qty_packing(line,product,region_convert_pack(region),"Shipper_Pallet")[0][0]
        no_retails = get_qty_packing(line,product,region_convert_pack(region),"Box_Shipper")[0][0]
        no_phone = phone_per_pallet * 5
        self.add_row(["1-PO Number", "Số PO, Google cung cấp"])
        self.add_row(["2-SSCC(Pallet ID)", sscc_rule_generate(line)])
        self.add_row(["3-UPC", upc])
        self.add_row(["4-Units/Carton", no_retails])
        self.add_row(["5-Units/Pallet", phone_per_pallet])
        self.add_row(["6-SKU", sku])
        self.add_row(["7-Case/Pallet", no_carton])
    elif region == "TMO":
        phone_per_pallet = get_qty_packing(line,product,region_convert_pack(region),"Box_Pallet")[0][0]
        no_pallet = 5
        no_carton = get_qty_packing(line,product,region_convert_pack(region),"Shipper_Pallet")[0][0] * 5
        no_phone = phone_per_pallet * 5
        pack_address = get_address_packing("All",product,"IN-Packed")[0][0]
        self.add_row(["1-Ship From", pack_address])
        self.add_row(["2-UPC", upc])
        self.add_row(["3-TMO SKU", upc])
        self.add_row(["4-SKU", sku])
        self.add_row(["5-PO Number", "Số PO, Google cung cấp"])
        self.add_row(["6-SSCC(Pallet ID)", sscc_rule_generate(line)])
        self.add_row(["7-Pallet Count", "1 to 5"])
        self.add_row(["8-COO", "Vietnam"])
        self.add_row(["9-Ship To", get_address_packing("All",product,"Ship to")[0][0]])
        self.add_row(["10-Total Unit Qty", phone_per_pallet])
        self.add_row(["11-Ship Date", "Ngày xuất hàng"])
        self.add_row(["12-2D Barcode", f"{"Số PO, Số Pallet"},{des},{str(no_phone)},{str(no_pallet)},{str(no_carton)},{str(phone_per_pallet)}"])
    self.ui.tableView.setColumnWidth(0,110)
    self.ui.tableView.setColumnWidth(1,550)
    self.ui.tableView.setRowHeight(1,50)
    self.ui.tableView.setRowHeight(0,100)
    self.ui.tableView.setRowHeight(2,100)
def table_content_generate(self,table_obj,region,sku,upc,imei,line,soft):
    self.model = QStandardItemModel()
    table_obj.setModel(self.model)
    # Dùng table mới
    self.model.setHorizontalHeaderLabels(["Item","Standard"])
    if region == 'ATT':
        self.add_row(["1-SSCC", sscc_rule_generate(line)])
        self.add_row(["2-UPC",upc])
        self.add_row(["3-SAP",f"{imei.split('-')[2]}"])
        self.add_row(["4-1 IMEI Start",imei.split('-')[0]])
        self.add_row(["4-1 IMEI End",imei.split('-')[1]])
        self.add_row(["5-COO","Made in Vietnam"])
        self.add_row(["6-MFG Date",f"Ngày Sản Xuất"])
        self.add_row(["7-2D Code",f"IMEI1, EID1, IMEI2, EID2, ...... IMEI10, EID10"])
        self.add_row(["8-Qty",f"Số lượng phone)"])
        self.add_row(["9-SKU",f"{sku}"])
        self.add_row(["10-EID",f"EID No"])
        self.add_row(["11-Recycle/Logo",f"Logo"])
    elif region == "TMO":
        self.add_row(["1-SKU", sku])
        self.add_row(["2-SAP",f"{imei.split('-')[2]}"])
        self.add_row(["3-UPC",upc])
        self.add_row(["4-1 IMEI Start",imei.split('-')[0]])
        self.add_row(["4-2 IMEI End",imei.split('-')[1]])
        self.add_row(["5-MFG Date",f"Ngày Sản Xuất"])
        self.add_row(["6-COO","Made in Vietnam"])
        self.add_row(["7-SSCC", sscc_rule_generate(line)])
        self.add_row(["8-2D Code",f"{sku},{upc},(Qty),(IMEI)"])
        self.add_row(["9-Qty",f"Số lượng phone)"])
        self.add_row(["10-Sw Ver",soft])
        self.add_row(["11-Recycle/Logo",f"Logo"])
    elif region == "VZW":
        self.add_row(["1-SKU", sku])
        self.add_row(["2-UPC/EAN",upc])
        self.add_row(["3-Quantity","Số Lượng Thực Tế Của Phone"])
        self.add_row(["4-1 IMEI Start",imei.split('-')[0]])
        self.add_row(["4-2 IMEI End",imei.split('-')[1]])
        self.add_row(["5-Carton ID(SSCC)",sscc_rule_generate(line)])
        self.add_row(["6-2D Code",f"{sku},{upc},(Qty),(IMEI)"])
        self.add_row(["7-SW Ver",f"{soft})"])
        self.add_row(["8-COO","Made in Vietnam"])
        self.add_row(["9-MFG Date",f"Ngày Sản Xuất"])
        self.add_row(["10-Recycle/Logo",f"Logo"])        
        self.add_row(["11-Weight",f"Số Cân - Liên Quan IE"])
    elif region == "IN":
        self.add_row(["1-2D Barcode",f"{sku},{upc},số lượng,các IMEI"])
        self.add_row(["2-Imported Address","Check ảnh"])
        self.add_row(["3-Packed by","Check ảnh lấy địa chỉ"])
        self.add_row(["4- Commodity name",'Cellular Phone'])
        self.add_row(["5-Qty","Số lượng phone"])      
    else:
        self.add_row(["1-SKU", sku])
        self.add_row(["2-UPC/EAN",upc])
        self.add_row(["3-Quantity","Số Lượng Thực Tế Của Phone"])
        self.add_row(["4-1 IMEI Start",imei.split('-')[0]])
        self.add_row(["4-2 IMEI End",imei.split('-')[1]])
        self.add_row(["5-Carton ID(SSCC)",sscc_rule_generate(line)])
        self.add_row(["6-COO","Made in Vietnam"])
        self.add_row(["7-2D Code",f"{sku},{upc},(Qty),(IMEI)"])
        self.add_row(["8-SW Ver",f"{soft})"])
        self.add_row(["9-Recycle/Logo",f"Logo"])
        self.add_row(["10-MFG Date",f"Ngày Sản Xuất"])
        self.add_row(["11-Weight",f"Số Cân - Liên Quan IE"])
    self.ui.tableView.setColumnWidth(0,110)
    self.ui.tableView.setColumnWidth(1,250)