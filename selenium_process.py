from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pyautogui
from PySide6.QtWidgets import QMessageBox
from dataChk import sort_dict
from dataProcess import gen_dict_standard
import pandas as pd
import os,sys
def call_maintain_single(key_name,tx_user,tx_pass,project,sku_list,dict_region,dfValue,list_chkbox):
    match key_name:
        case 'Description':
            des_maintain(tx_user,tx_pass,project,sku_list,dict_region,dfValue,key_name,list_chkbox)
        case 'Brand':
            des_maintain(tx_user,tx_pass,project,sku_list,dict_region,dfValue,key_name,list_chkbox)
        case 'UPC':
            pass
        case 'R-Label':
            pass
        case 'B-Label':
            pass
        case 'SAP':
            pass
        case 'Carton_Color':
            pass
        case 'Price':
            pass
        case 'M-Label':
            pass
        case 'QR_CODE':
            pass
def config_selenium():
    # Khong cho Chrome tu tai drive tu internet
    os.environ["WDM_LOG_LEVEL"] = "0"
    os.environ["WDM_LOCAL"] = "1"

    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    chrome_options = webdriver.ChromeOptions()
    # Thêm các tùy chọn cho ChromeOptions
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_experimental_option("detach", True)   
    # Loại bỏ cảnh báo đăng nhập
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #driver = webdriver.Chrome(executable_path=chrome_path)
    #service = Service(ChromeDriverManager().install())
    #browse = webdriver.Chrome(service=service,options=chrome_options)
    d_path = os.path.join(strDirPath,'chromedriver.exe')
    service = Service(d_path)
    browse = webdriver.Chrome(service=service,options=chrome_options)
    #browse.get('http://sfcweb.gg.ftv/Login.aspx')
    #browse.quit()
    return browse
def filter_project(br,project):
    #/html/body/div[2]/div[2]/div[6]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]
    expand = br.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]')
    expand.click()
def login_ifuse(tx_user,tx_pass,project,sku_list,dict_region,suffix):
    browse = config_selenium()
    browse.get('http://sfcweb.gg.ftv/Login.aspx')
    bt_language = browse.find_element(By.XPATH,'//*[@id="divLang"]/div/span[1]')
    bt_product = browse.find_element(By.XPATH,'//*[@id="selLocation"]')
    op_google = browse.find_element(By.XPATH,'//*[@id="selLocation"]/option[4]')
    inp_user = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[4]/div/div/input')
    inp_pass = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[5]/div/div/input')
    bt_login = browse.find_element(By.XPATH,'//*[@id="btnLogin"]')
    bt_language.click()
    bt_product.click()
    op_google.click()
    inp_user.send_keys(tx_user)
    inp_pass.send_keys(tx_pass)
    bt_login.click()
    time.sleep(2)   
    #Product maintain
    product_tab = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/a/i')
    product_tab.click()
    time.sleep(3)
    #Product Config
    product_config = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/ul/li[9]/a')
    product_config.click()
    time.sleep(2)
    #Expand
    expand = browse.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]')
    expand.click()
    #Chon project
    #//*[@id="s2id_selSFamily"]/a/div/b
    combo_project = browse.find_element(By.XPATH,'//*[@id="s2id_selSFamily"]/a/div/b')
    combo_project.click()
    time.sleep(1)
    # duyet chon project
# Lấy tất cả các thẻ <li> trong danh sách select2
    items = browse.find_elements(By.CSS_SELECTOR, "ul.select2-results li")
    for item in items:
        text = item.text.strip()
        if text == project:      # nếu text là MT5
            item.click()       # click vào thẻ đó
            break
    select = Select(browse.find_element(By.ID, "selSSectionName"))
    select.select_by_value("PACKING")
    # Click button search
    bt_tim = browse.find_element(By.XPATH,'//*[@id="btnSearch"]')
    bt_tim.click()
    #duyet tim sku
    time.sleep(3)
    fixed_headers = ['SKU', 'Type', 'Value']
    main_df = pd.DataFrame(columns=fixed_headers)
    suff_item = ''
    for item in sku_list:
        #rows = browse.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr')
        #rows = browse.find_elements(By.XPATH, '//table[@id="data-table"]/tbody/tr')
        if suffix != '':
            suff_item = item + '-' + suffix
        else:
            suff_item = item
        table_element = browse.find_element(By.CLASS_NAME, 'obj')
        rows = table_element.find_elements(By.XPATH, './/tr[contains(@class, "dhx_skyblue")]')
        ifuse_dic = dict()
        list_data = list()
        dict_new = dict()
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, 'td')
            if len(tds) >= 2:
                td_value = tds[1].text.strip()   # chỉ số 1 là cột thứ 2
                if td_value == suff_item:
                    row.click()
                    print(f"Đã click vào dòng có giá trị: {td_value}")
                    break
        time.sleep(2)
        task_key = browse.find_element(By.XPATH,'//*[@id="tab2"]')
        task_key.click()
        time.sleep(5)
        #Duyet key config
        xpath_table_rows = '//table[@id="tblBasicElseConfig"]/tbody/tr'
        rowsK = browse.find_elements(By.XPATH, xpath_table_rows)
        for row in rowsK:
            # ... code của bạn để xử lý từng dòng
            tds = row.find_elements(By.TAG_NAME, 'td')
            if len(tds) >= 4:
                key_name = tds[3].text.strip()
                print(key_name)
                value_name = tds[5].text
                if key_name == 'Description':
                    row.click()
                    print(value_name)
                    ifuse_dic['Des'] = value_name
                elif key_name == 'Brand':
                    row.click()
                    print(value_name)
                    ifuse_dic['Brand'] = value_name
                elif key_name == 'UPC':
                    row.click()
                    print(value_name)
                    ifuse_dic['UPC'] = value_name
                elif key_name == 'R-Label':
                    row.click()
                    print(value_name)
                    ifuse_dic['Rap'] = value_name
                elif key_name == 'B-Label':
                    row.click()
                    print(value_name)
                    ifuse_dic['Bob'] = value_name
                elif key_name == 'SAP':
                    row.click()
                    print(value_name)
                    ifuse_dic['sap'] = value_name
                elif key_name == 'Carton_Color':
                    row.click()
                    print(value_name)
                    ifuse_dic['color'] = value_name
                elif key_name == 'PRICE':
                    row.click()
                    print(value_name)
                    ifuse_dic['price'] = value_name
                elif key_name == 'M-Label':
                    row.click()
                    print(value_name)
                    ifuse_dic['mrp'] = value_name
                elif key_name == 'QR_CODE':
                    row.click()
                    print(value_name)
                    ifuse_dic['qr-code'] = value_name
        print(ifuse_dic)
        dict_new = sort_dict(ifuse_dic)
        list_data = list(dict_new.values())
        list_frame = list()
        if dict_new.get("Des") is not None:
            Des_list = gen_dict_standard(dict_region[item],list_data,suff_item,'Des')
        else:
            Des_list = {'SKU':item,'Type':'Des','Value':''}
        if dict_new.get("Brand") is not None:   
            brand_list = gen_dict_standard(dict_region[item],list_data,suff_item,'Brand')
        else:
            brand_list = {'SKU':item,'Type':'Brand','Value':''}
        if dict_new.get("UPC") is not None:
            upc_list = gen_dict_standard(dict_region[item],list_data,suff_item,'UPC')
        else:
            upc_list = {'SKU':item,'Type':'UPC','Value':''}
        if 'CLNR' in item:
            rap_list = {'SKU':item,'Type':'Rap','Value':''}
            bob_list = {'SKU':item,'Type':'Bob','Value':''}
            list_frame = [Des_list,brand_list,upc_list,rap_list,bob_list]
            if dict_region[item] in ['ATT','TMO']:
                sap_list = {'SKU':item,'Type':'sap','Value':''}
                color_list = {'SKU':item,'Type':'color','Value':''}
                list_frame.append(sap_list)
                list_frame.append(color_list)
            elif dict_region[item] in ['IN']: 
                price_list = {'SKU':item,'price':'Rap','Value':''}
                mrp_list = {'SKU':item,'Type':'mrp','Value':''}
                qr_list = {'SKU':item,'Type':'qr-code','Value':''}
                list_frame.append(price_list)
                list_frame.append(mrp_list)
                list_frame.append(qr_list)
        else:
            if dict_new.get("Rap") is not None:
                rap_list = gen_dict_standard(dict_region[item],list_data,suff_item,'Rap')
            else:
                rap_list = {'SKU':item,'Type':'Rap','Value':''}
            if dict_new.get("Bob") is not None:   
                bob_list = gen_dict_standard(dict_region[item],list_data,suff_item,'Bob')     
            else:
                bob_list = {'SKU':item,'Type':'Bob','Value':''}    
            list_frame = [Des_list,brand_list,upc_list,rap_list,bob_list]
            if dict_region[item] in ['ATT','TMO']:
                if dict_new.get("sap") is not None:
                    sap_list = gen_dict_standard(dict_region[item],list_data,suff_item,'sap')
                else:
                    sap_list = {'SKU':item,'Type':'sap','Value':''} 
                if dict_new.get("color") is not None:
                    color_list = gen_dict_standard(dict_region[item],list_data,suff_item,'color')
                else:
                    color_list = {'SKU':item,'Type':'color','Value':''} 
                list_frame.append(sap_list)
                list_frame.append(color_list)
            elif dict_region[item] in ['IN']: 
                if dict_new.get("price") is not None:
                    price_list = gen_dict_standard(dict_region[item],list_data,suff_item,'price')
                else:
                    price_list = {'SKU':item,'Type':'price','Value':''}
                if dict_new.get("mrp") is not None:
                    mrp_list = gen_dict_standard(dict_region[item],list_data,suff_item,'mrp')
                else:
                    mrp_list = {'SKU':item,'Type':'mrp','Value':''}
                if dict_new.get("qr-code") is not None:
                    qr_list = gen_dict_standard(dict_region[item],list_data,suff_item,'qr-code')
                else:
                    qr_list = {'SKU':item,'Type':'qr-code','Value':''}
                list_frame.append(price_list)
                list_frame.append(mrp_list)
                list_frame.append(qr_list)
        print(list_frame)
        new_rows_df = pd.DataFrame(list_frame)
        main_df = pd.concat([main_df , new_rows_df], ignore_index=True)
    print(main_df)
    browse.quit()
    return main_df
def mainTab_select(browse):
    product_tab = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/a/i')
    product_tab.click()
    time.sleep(3)
def subTab_select(browse):
    product_config = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/ul/li[9]/a')
    product_config.click()
    time.sleep(2)
def auto_load_labelPrint(browse,tx_user,tx_pass,text_file):
    bt_language = browse.find_element(By.XPATH,'//*[@id="divLang"]/div/span[1]')
    bt_product = browse.find_element(By.XPATH,'//*[@id="selLocation"]')
    op_google = browse.find_element(By.XPATH,'//*[@id="selLocation"]/option[4]')
    inp_user = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[4]/div/div/input')
    inp_pass = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[5]/div/div/input')
    bt_login = browse.find_element(By.XPATH,'//*[@id="btnLogin"]')
    bt_language.click()
    bt_product.click()
    op_google.click()
    inp_user.send_keys(tx_user)
    inp_pass.send_keys(tx_pass)
    bt_login.click()
    #/html/body/div[2]/div[1]/ul/li[5]/ul/li[11]/a
    product_tab = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/a/i')
    model_excel = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/ul/li[11]/a')
    product_tab.click()
    time.sleep(3)
    model_excel.click()
    time.sleep(2)
    #click choose file
    pyautogui.moveTo(263, 366, duration=0.2)
    pyautogui.doubleClick()
    time.sleep(1)
    # dien address
    pyautogui.moveTo(297, 527, duration=0.2)
    pyautogui.click()
    pyautogui.typewrite(text_file)
    time.sleep(2)   
    # click open
    pyautogui.moveTo(769, 568, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    # dien address
    pyautogui.moveTo(297, 527, duration=0.2)
    pyautogui.click()
    pyautogui.typewrite(text_file)
    time.sleep(2)   
    # click open
    pyautogui.moveTo(769, 568, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    # click len tren
    for i in range (1,6):
        pyautogui.moveTo(1305, 206, duration=0.2)
        pyautogui.click()
    time.sleep(1)
    # click upload
    pyautogui.moveTo(1170, 277, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    browse.quit()
    QMessageBox.information(None,"Thông báo", "Upload Label Print to Ifuse OK!")
def change_language(browse,tx_user,tx_pass,text_file):
    #//*[@id="divLang"]/div/span[1]
    bt_language = browse.find_element(By.XPATH,'//*[@id="divLang"]/div/span[1]')
    bt_product = browse.find_element(By.XPATH,'//*[@id="selLocation"]')
    op_google = browse.find_element(By.XPATH,'//*[@id="selLocation"]/option[4]')
    inp_user = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[4]/div/div/input')
    inp_pass = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[5]/div/div/input')
    bt_login = browse.find_element(By.XPATH,'//*[@id="btnLogin"]')
    bt_language.click()
    bt_product.click()
    op_google.click()
    inp_user.send_keys(tx_user)
    inp_pass.send_keys(tx_pass)
    bt_login.click()
    time.sleep(3)
    #/html/body/div[2]/div[1]/ul/li[5]/a/i
    product_tab = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/a/i')
    product_config = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/ul/li[9]/a')
    product_tab.click()
    time.sleep(3)
    product_config.click()
    time.sleep(2)
    keyConfig_tab = browse.find_element(By.XPATH,'//*[@id="tab2"]')
    keyConfig_tab.click()
    bt_bulk_import = browse.find_element(By.XPATH,'//*[@id="uploadinto"]')
    bt_bulk_import.click()
    time.sleep(2)
    #iframe = browse.find_element(By.ID, "frmupload1")
    #browse.switch_to.frame(iframe)
    #bt_chooseFile = browse.find_element(By.ID,'file2')
    #bt_chooseFile = browse.find_element(By.XPATH,'/html/body/form/div[3]/input')
    pyautogui.moveTo(281, 635, duration=0.2)
    pyautogui.doubleClick()
    #bt_chooseFile.click()
    pyautogui.moveTo(290, 525, duration=0.5)
    pyautogui.click()
    # Sau đó gõ text
    time.sleep(1)
    pyautogui.typewrite(text_file)
    pyautogui.moveTo(666, 565, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(766, 565, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(290, 525, duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(text_file)
    time.sleep(1)
    pyautogui.moveTo(766, 565, duration=0.2)
    pyautogui.click()
    #bt_load = browse.find_element(By.XPATH,'//*[@id="btnUpload1"]')
    #bt_load.click()
    time.sleep(1)
    pyautogui.moveTo(294, 748, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    browse.quit()
    QMessageBox.information(None,"Thông báo", "Upload KeyConfig to Ifuse OK!")
'''from selenium import webdriver
def config_selenium():
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--lang=en")
    edge_options.add_argument("--disable-features=NetworkService")
    edge_options.add_experimental_option("detach", True)
    edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Dùng Edge mặc định, cần có msedgedriver.exe trong PATH hoặc cùng thư mục script
    browse = webdriver.Edge(options=edge_options)
    browse.get('http://sfcweb.gg.ftv/Login.aspx')294 747'''
def des_maintain(tx_user,tx_pass,project,sku_list,dict_region,df_value,list_chkbox):
    browse = config_selenium()
    browse.get('http://sfcweb.gg.ftv/Login.aspx')
    bt_language = browse.find_element(By.XPATH,'//*[@id="divLang"]/div/span[1]')
    bt_product = browse.find_element(By.XPATH,'//*[@id="selLocation"]')
    op_google = browse.find_element(By.XPATH,'//*[@id="selLocation"]/option[4]')
    inp_user = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[4]/div/div/input')
    inp_pass = browse.find_element(By.XPATH,'/html/body/div[2]/form[1]/div[5]/div/div/input')
    bt_login = browse.find_element(By.XPATH,'//*[@id="btnLogin"]')
    bt_language.click()
    bt_product.click()
    op_google.click()
    inp_user.send_keys(tx_user)
    inp_pass.send_keys(tx_pass)
    bt_login.click()
    time.sleep(2)   
    #Product maintain
    product_tab = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/a/i')
    product_tab.click()
    time.sleep(3)
    #Product Config
    product_config = browse.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]/ul/li[9]/a')
    product_config.click()
    time.sleep(2)
    #Expand
    expand = browse.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]')
    expand.click()
    #Chon project
    #//*[@id="s2id_selSFamily"]/a/div/b
    combo_project = browse.find_element(By.XPATH,'//*[@id="s2id_selSFamily"]/a/div/b')
    combo_project.click()
    time.sleep(1)
    # duyet chon project
# Lấy tất cả các thẻ <li> trong danh sách select2
    items = browse.find_elements(By.CSS_SELECTOR, "ul.select2-results li")
    for item in items:
        text = item.text.strip()
        if text == project:      # nếu text là MT5
            item.click()       # click vào thẻ đó
            break
    select = Select(browse.find_element(By.ID, "selSSectionName"))
    select.select_by_value("PACKING")
    # Click button search
    bt_tim = browse.find_element(By.XPATH,'//*[@id="btnSearch"]')
    bt_tim.click()
    #duyet tim sku
    time.sleep(3)
    for item in sku_list:
        table_element = browse.find_element(By.CLASS_NAME, 'obj')
        rows = table_element.find_elements(By.XPATH, './/tr[contains(@class, "dhx_skyblue")]')
        ifuse_dic = dict()
        list_data = list()
        dict_new = dict()
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, 'td')
            if len(tds) >= 2:
                td_value = tds[1].text.strip()   # chỉ số 1 là cột thứ 2
                if td_value == item:
                    row.click()
                    print(f"Đã click vào dòng có giá trị: {td_value}")
                    break
        time.sleep(2)
        task_key = browse.find_element(By.XPATH,'//*[@id="tab2"]')
        task_key.click()
        time.sleep(5)
        #Duyet key config
        #for key, value in list_chkbox.items():
            #if value == True:
        #main_one(browse,df_value)
    return browse,df_value
def check_exist_keyName(browse,region):
    main_dict_chk = {'Description':0,'Brand':0,'UPC':0,'R-Label':0,'B-Label':0,
                     'SAP':0,'Carton-Color':0,'M-Label':0,'PRICE':0,'QR_CODE':0}
    key_name = ''
    xpath_table_rows = '//table[@id="tblBasicElseConfig"]/tbody/tr'
    rowsK = browse.find_elements(By.XPATH, xpath_table_rows)   
    for row in rowsK:
        # ... code của bạn để xử lý từng dòng
        tds = row.find_elements(By.TAG_NAME, 'td')
        if len(tds) >= 4:
            key_name = tds[3].text.strip()
            if key_name != '':
                if key_name == 'Description':
                    main_dict_chk['Description'] =1
                if key_name == 'Brand':
                    main_dict_chk['Brand'] =1
                if key_name == 'UPC':
                    main_dict_chk['UPC'] =1
                if key_name == 'R-Label':
                    main_dict_chk['R-Label'] =1
                if key_name == 'B-Label':
                    main_dict_chk['B-Label'] =1
                if region in ['ATT','TMO']:
                    if key_name == 'SAP':
                        main_dict_chk['SAP'] =1
                    if key_name == 'Carton-Color':
                        main_dict_chk['Carton-Color'] =1
                elif region in ['IN']:
                    if key_name == 'M-Label':
                        main_dict_chk['M-Label'] =1
                    if key_name == 'PRICE':
                        main_dict_chk['PRICE'] =1
                    if key_name == 'QR_CODE':
                        main_dict_chk['QR_CODE'] =1    
    return main_dict_chk
def new_config(browse,df_value,main_dict_chk,region,main_df,suff_item):
    bt_new_config = browse.find_element(By.XPATH,'//*[@id="btnElseBasic"]')
    if region in ['ATT','TMO']:
        if main_dict_chk['SAP'] == 0:
            bt_new_config.click()
            time.sleep(1)
            op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
            op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
            op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')
            #//*[@id="txtElseBasicKeyName"]/option[9]
            op_key_type.click()
            general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
            general_id.click()

            op_key_ver
            ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
            ver.click()

            op_key_name.click()
            key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[49]')
            key.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[5,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[5,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()
            time.sleep(1)
            #browse.quit()
            value = df_value.iloc[5,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = 'SAP'
            main_df['Value'] = df_value.iloc[5,2]
            return main_df
        if main_dict_chk['Carton_Color'] == 0:
            bt_new_config.click()
            time.sleep(1)
            op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
            op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
            op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')
            #//*[@id="txtElseBasicKeyName"]/option[9]
            op_key_type.click()
            general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
            general_id.click()

            op_key_ver
            ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
            ver.click()

            op_key_name.click()
            key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[64]')
            key.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[6,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[6,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()
            time.sleep(1)
            #browse.quit()
            value = df_value.iloc[6,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = 'Carton_Color'
            main_df['Value'] = df_value.iloc[6,2]
            return main_df
    if region in ['IN']:
        if main_dict_chk['M-Label'] == 0:
            bt_new_config.click()
            time.sleep(1)
            op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
            op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
            op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')
            #//*[@id="txtElseBasicKeyName"]/option[9]
            op_key_type.click()
            general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
            general_id.click()

            op_key_ver
            ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
            ver.click()

            op_key_name.click()
            key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[14]')
            key.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[6,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[6,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()
            time.sleep(1)
            #browse.quit()
            value = df_value.iloc[6,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = 'M-Label'
            main_df['Value'] = df_value.iloc[6,2]
            return main_df
        if main_dict_chk['PRICE'] == 0:
            bt_new_config.click()
            time.sleep(1)
            op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
            op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
            op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')
            #//*[@id="txtElseBasicKeyName"]/option[9]
            op_key_type.click()
            general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
            general_id.click()

            op_key_ver
            ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
            ver.click()

            op_key_name.click()
            key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[9]')
            key.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[5,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[5,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()
            time.sleep(1)
            #browse.quit()
            value = df_value.iloc[5,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = 'PRICE'
            main_df['Value'] = value
            return main_df
        if main_dict_chk['QR_CODE'] == 0:
        #//*[@id="txtElseBasicKeyName"]/option[15]
            bt_new_config.click()
            op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
            op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
            op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')

            op_key_type.click()
            general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
            general_id.click()

            op_key_ver
            ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
            ver.click()

            op_key_name.click()
            key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[15]')
            key.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[7,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[7,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()
            time.sleep(1)
            #browse.quit()
            value = df_value.iloc[7,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = 'QR_CODE'
            main_df['Value'] = value
            return main_df
    if main_dict_chk['Description'] == 0:
        bt_new_config.click()
        time.sleep(1)
        op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
        op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
        op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')

        op_key_type.click()
        general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
        general_id.click()

        op_key_ver
        ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
        ver.click()

        op_key_name.click()
        key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[23]')
        key.click()
        des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
        bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
        time.sleep(1)
        #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
        #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[0,2]}';
        """)
        time.sleep(1)
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[0,2]}';
        """)
        bt_save.click()
        time.sleep(1)
        bt_close.click()
        time.sleep(1)
        #browse.quit()
        value = df_value.iloc[0,2]
        main_df['SKU'] = suff_item
        main_df['Type'] = 'Description'
        main_df['Value'] = value
        return main_df
    if main_dict_chk['Brand'] == 0:
        bt_new_config.click()
        time.sleep(1)
        op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
        op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
        op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')

        op_key_type.click()
        general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
        general_id.click()

        op_key_ver
        ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
        ver.click()

        op_key_name.click()
        key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[71]')
        key.click()
        des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
        bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
        time.sleep(1)
        #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
        #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[1,2]}';
        """)
        time.sleep(1)
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[1,2]}';
        """)
        bt_save.click()
        time.sleep(1)
        bt_close.click()
        time.sleep(1)
        #browse.quit()
        value = df_value.iloc[1,2]
        main_df['SKU'] = suff_item
        main_df['Type'] = 'Brand'
        main_df['Value'] = value
        return main_df
    if main_dict_chk['UPC'] == 0:
        bt_new_config.click()
        time.sleep(1)
        op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
        op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
        op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')

        op_key_type.click()
        general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
        general_id.click()

        op_key_ver
        ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
        ver.click()

        op_key_name.click()
        time.sleep(1)
        key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[35]')
        key.click()
        des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
        bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
        time.sleep(1)
        #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
        #//*[@id="divProductElseBasic"]/div[3]/div/button[1] //*[@id="txtElseBasicKeyName"]/option[35]
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[2,2]}';
        """)
        time.sleep(1)
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[2,2]}';
        """)
        bt_save.click()
        time.sleep(1)
        bt_close.click()
        time.sleep(1)
        #browse.quit()
        value = df_value.iloc[2,2]
        main_df['SKU'] = suff_item
        main_df['Type'] = 'UPC'
        main_df['Value'] = value
        return main_df
    if main_dict_chk['R-Label'] == 0:
        bt_new_config.click()
        time.sleep(1)
        op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
        op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
        op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')

        op_key_type.click()
        general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
        general_id.click()

        op_key_ver
        ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
        ver.click()

        op_key_name.click()
        key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[12]')
        key.click()
        des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
        bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
        time.sleep(1)
        #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
        #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[3,2]}';
        """)
        time.sleep(1)
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[3,2]}';
        """)
        bt_save.click()
        time.sleep(1)
        bt_close.click()
        time.sleep(1)
        #browse.quit()
        value = df_value.iloc[0,2]
        main_df['SKU'] = suff_item
        main_df['Type'] = 'R-Label'
        main_df['Value'] = value
        return main_df
    if main_dict_chk['B-Label'] == 0:
        bt_new_config.click()
        time.sleep(1)
        op_key_type = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]')
        op_key_ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]')
        op_key_name = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]')

        op_key_type.click()
        general_id = browse.find_element(By.XPATH,'//*[@id="selElseBasicKeyType"]/option[4]')
        general_id.click()

        op_key_ver
        ver = browse.find_element(By.XPATH,'//*[@id="selElseBasicVerNo"]/option[4]')
        ver.click()

        op_key_name.click()
        key = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyName"]/option[13]')
        key.click()
        des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
        bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
        bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
        time.sleep(1)
        #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
        #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[4,2]}';
        """)
        time.sleep(1)
        browse.execute_script(f"""
            document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[4,2]}';
        """)
        bt_save.click()
        time.sleep(1)
        bt_close.click()
        time.sleep(1)
        #browse.quit()
        value = df_value.iloc[4,2]
        main_df['SKU'] = suff_item
        main_df['Type'] = 'B-Label'
        main_df['Value'] = value
        return main_df
def main_one(browse,df_value,key,region,suffix):
    #fixed_headers = ['SKU', 'Type', 'Value']
    region_new = next(iter(region.values()))
    sku = next(iter(region))
    if suffix != '':
        suff_item = sku + '-' + suffix
    else:
        suff_item = sku
    value = ''
    #main_df = pd.DataFrame(columns=fixed_headers)
    #main_dict_chk = check_exist_keyName(browse,region_new)
    main_df = {}
    
    xpath_table_rows = '//table[@id="tblBasicElseConfig"]/tbody/tr'
    rowsK = browse.find_elements(By.XPATH, xpath_table_rows)
    bt_new_config = browse.find_element(By.XPATH,'//*[@id="btnElseBasic"]')
    for row in rowsK:
        # ... code của bạn để xử lý từng dòng
        tds = row.find_elements(By.TAG_NAME, 'td')
        if len(tds) >= 4:
            key_name = tds[3].text.strip()
            edit_rng = tds[8]
            print(key_name)
            value_name = tds[5].text
            if region in ['ATT','TMO']:
                if key_name == 'SAP' and key_name == key:
                    row.click()
                    print(value_name)
                    edit_rng.click()
                    des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
                    bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
                    time.sleep(1)
                    #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
                    #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[5,2]}';
                    """)
                    time.sleep(1)
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[5,2]}';
                    """)
                    bt_save.click()
                    time.sleep(1)
                    bt_close.click()  
                    time.sleep(1) 
                    #browse.quit()
                    value = df_value.iloc[5,2]
                    main_df['SKU'] = suff_item
                    main_df['Type'] = key
                    main_df['Value'] = value
                    return  main_df
                if key_name == 'Carton_Color' and key_name == key:
                    row.click()
                    print(value_name)
                    edit_rng.click()
                    des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
                    bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
                    time.sleep(1)
                    #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
                    #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[6,2]}';
                    """)
                    time.sleep(1)
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[6,2]}';
                    """)
                    bt_save.click()
                    time.sleep(1)
                    bt_close.click()  
                    time.sleep(1) 
                    #browse
                    value = df_value.iloc[6,2]
                    main_df['SKU'] = suff_item
                    main_df['Type'] = key
                    main_df['Value'] = value
                    return main_df
            if region in ['IN']:
                if key_name == 'M-Label' and key_name == key:
                    row.click()
                    print(value_name)
                    edit_rng.click()
                    des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
                    bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
                    time.sleep(1)
                    #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
                    #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[6,2]}';
                    """)
                    time.sleep(1)
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[6,2]}';
                    """)
                    bt_save.click()
                    time.sleep(1)
                    bt_close.click()  
                    time.sleep(1) 
                    #browse.quit()
                    value = df_value.iloc[6,2]
                    main_df['SKU'] = suff_item
                    main_df['Type'] = key
                    main_df['Value'] = value
                    return  main_df
                if key_name == 'PRICE' and key_name == key:
                    row.click()
                    print(value_name)
                    edit_rng.click()
                    des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
                    bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
                    time.sleep(1)
                    #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
                    #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[5,2]}';
                    """)
                    time.sleep(1)
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[5,2]}';
                    """)
                    bt_save.click()
                    time.sleep(1)
                    bt_close.click()  
                    time.sleep(1) 
                    value = df_value.iloc[5,2]
                    main_df['SKU'] = suff_item
                    main_df['Type'] = key
                    main_df['Value'] = value
                    return main_df
                if key_name == 'QR_CODE' and key_name == key:
                    row.click()
                    print(value_name)
                    edit_rng.click()
                    des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
                    bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
                    bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
                    time.sleep(1)
                    #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
                    #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[7,2]}';
                    """)
                    time.sleep(1)
                    browse.execute_script(f"""
                        document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[7,2]}';
                    """)
                    bt_save.click()
                    time.sleep(1)
                    bt_close.click()  
                    time.sleep(1) 
                    value = df_value.iloc[7,2]
                    main_df['SKU'] = suff_item
                    main_df['Type'] = key
                    main_df['Value'] = value
                    return main_df
        if key_name == 'Description' and key_name == key:
            row.click()
            print(value_name)
            edit_rng.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[0,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[0,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()
            time.sleep(1)
            #browse.quit()
            value = df_value.iloc[0,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = key
            main_df['Value'] = value
            return main_df
        if key_name == 'Brand' and key_name == key:
            row.click()
            print(value_name)
            edit_rng.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[1,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[1,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()  
            time.sleep(1) 
            #browse.quit()
            value = df_value.iloc[1,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = key
            main_df['Value'] = value
            return  main_df
        if key_name == 'UPC' and key_name == key:
            row.click()
            print(value_name)
            edit_rng.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[2,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[2,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()  
            time.sleep(1) 
            #browse.quit()
            value = df_value.iloc[2,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = key
            main_df['Value'] = value
            return main_df
        if key_name == 'R-Label' and key_name == key:
            row.click()
            print(value_name)
            edit_rng.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[3,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[3,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()  
            time.sleep(1) 
            #browse.quit()
            value = df_value.iloc[3,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = key
            main_df['Value'] = value
            return  main_df
        if key_name == 'B-Label' and key_name == key:
            row.click()
            print(value_name)
            edit_rng.click()
            des_k = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            des_v = browse.find_element(By.XPATH,'//*[@id="txtElseBasicKeyDesc"]')
            bt_save = browse.find_element(By.XPATH,'//*[@id="btnElseBasicDone"]')
            bt_close = browse.find_element(By.XPATH,'//*[@id="divProductElseBasic"]/div[3]/div/button[1]')
            time.sleep(1)
            #des_k.send_keys(df_value.iloc[0,2]) //*[@id="btnElseBasicDone"] //*[@id="txtElseBasicKeyValue"] 
            #//*[@id="divProductElseBasic"]/div[3]/div/button[1]
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyDesc').value = '{df_value.iloc[4,2]}';
            """)
            time.sleep(1)
            browse.execute_script(f"""
                document.getElementById('txtElseBasicKeyValue').value = '{df_value.iloc[4,2]}';
            """)
            bt_save.click()
            time.sleep(1)
            bt_close.click()  
            time.sleep(1) 
            #browse.quit()
            value = df_value.iloc[4,2]
            main_df['SKU'] = suff_item
            main_df['Type'] = key
            main_df['Value'] = value
            return main_df
    #main_df = new_config(browse,df_value,main_dict_chk,region_new,main_df,suff_item)
    return main_df

                      
   