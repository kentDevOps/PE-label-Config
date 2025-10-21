import sqlite3
#from common import *
import os,sys

def get_sys_path_sql(strFolder):
    strMainPath = os.path.abspath(sys.argv[0])
    strCrrPath = os.path.dirname(strMainPath)
    return os.path.join(strCrrPath,strFolder)
def create_sql_connect():
    db_path = get_sys_path_sql("database") + r"\database.db"
    conn = sqlite3.connect(db_path)
    # Tạo cursor để thao tác với DB
    cursor = conn.cursor()
    return conn,cursor
def get_value_db(tenBang,tenCot):
    cnn,cur = create_sql_connect()
    cur.execute(f"SELECT {tenCot} FROM {tenBang}")
    rows = cur.fetchall()
    return rows
def get_header_title(tenCot,gtLoc):
    cnn,cur = create_sql_connect()
    cur.execute(f"SELECT {tenCot} FROM titleFormat WHERE product = ?",(gtLoc,))
    rows = cur.fetchall()
    return rows  
def get_header_title_label_print(tenCot,gtLoc):
    cnn,cur = create_sql_connect()
    cur.execute(f"SELECT {tenCot} FROM labelPrint_title WHERE product = ?",(gtLoc,))
    rows = cur.fetchall()
    return rows  
def get_value_by_product(tenBang,tenCot,cotLoc,giatri_loc):
    cnn,cur = create_sql_connect()
    cur.execute(f"SELECT {tenCot} FROM {tenBang} WHERE {cotLoc} = ?",(giatri_loc))
    rows = cur.fetchall()
    return rows  
def get_temp_id(tenBang,tenCot,type_col,type_val,station_colum,station_value,reg_col,reg_val,line_col,line_val):
    cnn,cur = create_sql_connect()
    cur.execute(f"SELECT {tenCot} FROM {tenBang} WHERE {type_col} = ? AND {station_colum} = ? AND {reg_col} = ? AND {line_col} = ?",(type_val,station_value,reg_val,line_val))
    rows = cur.fetchall()
    return rows 
def create_new_table():
    conn,cursor = create_sql_connect()
    cursor.execute("""
        CREATE TABLE bobList (
            project TEXT,
            bob TEXT NOT NULL
        )
    """)
    print("Bảng 'san_pham' đã được tạo thành công!")
def add_bob_to_sql():
    conn,cursor = create_sql_connect()
    bob_path = r'C:\01_Job\01_Packing Plan\BobLabel'
    list_bob = os.listdir(bob_path)
    file_list_without_pdf = []
    for file_name in list_bob:
        # Kiểm tra xem file có phải là file PDF hay không
        if file_name.endswith('.pdf'):
            # Loại bỏ đuôi '.pdf'
            name_without_extension = file_name.replace('.pdf', '')
            file_list_without_pdf.append(name_without_extension)
    insert_sql = "INSERT INTO bobList (bob) VALUES (?)"
    for item in file_list_without_pdf:
        cursor.execute(insert_sql, (item,))
    print('Done')
    conn.commit() # save        
def update_sp():
    conn,cursor = create_sql_connect()
    update_sql = "UPDATE bobList SET project = 'P25'"
    cursor.execute(update_sql)
    conn.commit()
#update_sp()
def get_qty_packing(line,product,region,item_name):
    conn,cursor = create_sql_connect()
    cursor.execute(f"SELECT {item_name} FROM packQty WHERE Project = ? AND Product = ? AND Region = ?",(line,product,region,))
    rows = cursor.fetchall()
    return rows
def get_address_packing(line,product,type):
    conn,cursor = create_sql_connect()
    cursor.execute(f"SELECT value FROM address WHERE project = ? AND product = ? AND type = ?",(line,product,type,))
    rows = cursor.fetchall()
    return rows
def get_bob_list(giatri_loc,product):
    conn,cursor = create_sql_connect()
    cursor.execute(f"SELECT bob FROM bobList WHERE bob LIKE ? AND project = ?",(f'%{giatri_loc.strip()}%',product,))
    rows = cursor.fetchall()
    return rows
def get_price_In(line):
    conn,cursor = create_sql_connect()
    cursor.execute(f"SELECT price FROM priceIn WHERE project = ?",(line,))
    rows = cursor.fetchall()
    return rows
def label_print_process(sku_item,regionValue,typeValue,stationValues,project,key):
    line = ""
    tableName = ""
    if key == 1:
        if regionValue in ['ATT','TMO','VZW','JP','EMEA']:
            regionValue = regionValue
        else:
            regionValue = 'ROR'
            if regionValue == 'ROR' and stationValues == 'over':
                return [('','')]  
    else:      
        if regionValue in ['ATT','TMO','VZW']:
            regionValue = regionValue
        else:
            regionValue = 'ROR'
            if regionValue == 'ROR' and stationValues == 'over':
                return [('','')]
    if project == "MT5":
        tableName = "mt5Temp"
    elif project == "FL5":
        tableName = "fl5Temp"
    elif project == "BZ5":
        tableName = "bz5Temp"
    if "CLNR" in sku_item:
        line = "fru"
        if line == 'fru' and stationValues == 'over':
            return [('','')]
    else:
        line = "retail"
    cnn,cur = create_sql_connect()
    cur.execute(f"SELECT tempName,tempId FROM {tableName} WHERE type = ? AND station = ? AND region = ? AND line = ?"
                ,(typeValue,stationValues,regionValue,line,))
    rows = cur.fetchall()
    return rows
def kitting_process(pallet,line,project,type):
    cnn,cur = create_sql_connect()
    if project == "MT5":
        tableName = "mt5Temp"
    elif project == "FL5":
        tableName = "fl5Temp"
    elif project == "BZ5":
        tableName = "bz5Temp"
    cur.execute(f"SELECT tempName,tempId FROM {tableName} WHERE type = ? AND station = ? AND line = ?"
                ,(type,pallet,line,))
    rows = cur.fetchall()
    return rows
