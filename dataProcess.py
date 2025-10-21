from log import *
from sqliteProcess import *
import os,sys
import pandas as pd
import openpyxl
#from selenium_process import *

def chk_mandatory_folder(strAbsPath,strDirPath):
    if not os.path.isdir(os.path.join(strDirPath,'database')):
        print(f'Folder {os.path.join(strDirPath,'database')} is not Exists!!!')
        raise FileNotFoundError(f"Folder {os.path.join(strDirPath,'data')} is not Exists!!!")
    if not os.path.isdir(os.path.join(strDirPath,'approve')):
        print(f'Folder {os.path.join(strDirPath,'approve')} is not Exists!!!')
        raise FileNotFoundError(f"Folder {os.path.join(strDirPath,'keyFile')} is not Exists!!!")
def chk_mandatary_file(config_path,mapping_path,keyFile_path):
    if mapping_path == '':
        print(f"File Standard '{os.path.basename('mapping table')}' Is Not Exists!!!")
        raise FileNotFoundError(f"File Standard '{os.path.basename(mapping_path)}' Is Not Exists!!!")
def bg_labelPrint_generate(project,sku_list,suffix,product):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    sku = get_header_title_label_print('sku','P25')[0][0]
    station = get_header_title_label_print('station','P25')[0][0]
    type = get_header_title_label_print('type','P25')[0][0]
    id = get_header_title_label_print('id','P25')[0][0]
    qty = get_header_title_label_print('qty','P25')[0][0]
    mapp_region = ''
    suffix = ''
    fixed_headers = [sku,type,station,id,qty]
    #tạo một frame rỗng với fixed_headers
    main_df = pd.DataFrame(columns=fixed_headers)    
    for item in sku_list:
        if project == 'MT5':
            tab_name = 'mt5Temp'
        elif project == 'BZ5':
            tab_name = 'bz5Temp'
        else:
            tab_name = 'fl5Temp'
        tempId_bip = get_temp_id(tab_name,'tempId','type','BSN','station','BIP','region','ROR','line','bg')[0][0]
        tempId_co = get_temp_id(tab_name,'tempId','type','BSN','station','CO','region','ROR','line','bg')[0][0]
        tempId_label = get_temp_id(tab_name,'tempId','type','BSN','station','label_print','region','ROR','line','bg')[0][0]
        tempId_repair = get_temp_id(tab_name,'tempId','type','repair','station','repair-in','region','ROR','line','bg')[0][0]
        tempId_carton = get_temp_id(tab_name,'tempId','type','carton','station','BCP','region','ROR','line','bg')[0][0]

        list_bip = ['BSN','BIP',tempId_bip,1]
        list_co = ['BSN','CO',tempId_co,1]
        list_label = ['BSN','LABLE_PRINT',tempId_label,1]
        list_rp = ['REPAIR_IN','REPAIR-IN',tempId_repair,1]
        list_car = ['CARTON','BCP',tempId_carton,1]

        dic_bip = add_information_labelPrint(item,list_bip,suffix,sku,station,type,id,qty)
        dic_co = add_information_labelPrint(item,list_co,suffix,sku,station,type,id,qty)
        dic_label = add_information_labelPrint(item,list_label,suffix,sku,station,type,id,qty)
        dic_rp = add_information_labelPrint(item,list_rp,suffix,sku,station,type,id,qty)
        dic_car = add_information_labelPrint(item,list_car,suffix,sku,station,type,id,qty)
        list_combine=[dic_bip,dic_co,dic_label,dic_rp,dic_car]
        new_row = pd.DataFrame(list_combine)
        print(new_row)
        main_df = pd.concat([main_df , new_row], ignore_index=True)
        print(main_df)
    #Export file
    output_file = f'GetModelNameLoad ({datetime.now().strftime("%Y%m%d%H%M%S")}).xlsx'
    if not os.path.exists(os.path.join(strDirPath,'report')):
        os.makedirs(os.path.join(strDirPath,'report'))
    if not os.path.exists(os.path.join(strDirPath,'report',project)):
        os.makedirs(os.path.join(strDirPath,'report',project))
    if not os.path.exists(os.path.join(strDirPath,'report',project,'labelPrint')):
        os.makedirs(os.path.join(strDirPath,'report',project,'labelPrint'))
    output_file = os.path.join(os.path.join(strDirPath,'report',project,'labelPrint'),output_file)
    main_df.to_excel(output_file, index=False, sheet_name='Sheet1')
    return output_file,main_df   
def cg_labelPrint_generate(project,sku_list,suffix,product):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    sku = get_header_title_label_print('sku','P25')[0][0]
    station = get_header_title_label_print('station','P25')[0][0]
    type = get_header_title_label_print('type','P25')[0][0]
    id = get_header_title_label_print('id','P25')[0][0]
    qty = get_header_title_label_print('qty','P25')[0][0]
    mapp_region = ''
    suffix = ''
    fixed_headers = [sku,type,station,id,qty]
    #tạo một frame rỗng với fixed_headers
    main_df = pd.DataFrame(columns=fixed_headers)    
    for item in sku_list:
        if project == 'MT5':
            tab_name = 'mt5Temp'
        elif project == 'BZ5':
            tab_name = 'bz5Temp'
        else:
            tab_name = 'fl5Temp'
        tempId_cip = get_temp_id(tab_name,'tempId','type','BSN','station','CIP','region','ROR','line','cg')[0][0]
        tempId_co = get_temp_id(tab_name,'tempId','type','BSN','station','CO','region','ROR','line','cg')[0][0]
        tempId_label = get_temp_id(tab_name,'tempId','type','BSN','station','label_print','region','ROR','line','cg')[0][0]
        tempId_repair = get_temp_id(tab_name,'tempId','type','repair','station','repair-in','region','ROR','line','cg')[0][0]
        tempId_carton = get_temp_id(tab_name,'tempId','type','carton','station','CCP','region','ROR','line','cg')[0][0]

        list_cip = ['BSN','CIP',tempId_cip,1]
        list_co = ['BSN','CO',tempId_co,1]
        list_label = ['BSN','LABLE_PRINT',tempId_label,1]
        list_rp = ['REPAIR_IN','REPAIR-IN',tempId_repair,1]
        list_car = ['CARTON','CCP',tempId_carton,1]

        dic_cip = add_information_labelPrint(item,list_cip,suffix,sku,station,type,id,qty)
        dic_co = add_information_labelPrint(item,list_co,suffix,sku,station,type,id,qty)
        dic_label = add_information_labelPrint(item,list_label,suffix,sku,station,type,id,qty)
        dic_rp = add_information_labelPrint(item,list_rp,suffix,sku,station,type,id,qty)
        dic_car = add_information_labelPrint(item,list_car,suffix,sku,station,type,id,qty)
        list_combine=[dic_cip,dic_co,dic_label,dic_rp,dic_car]
        new_row = pd.DataFrame(list_combine)
        print(new_row)
        main_df = pd.concat([main_df , new_row], ignore_index=True)
        print(main_df)
    #Export file
    output_file = f'GetModelNameLoad ({datetime.now().strftime("%Y%m%d%H%M%S")}).xlsx'
    if not os.path.exists(os.path.join(strDirPath,'report')):
        os.makedirs(os.path.join(strDirPath,'report'))
    if not os.path.exists(os.path.join(strDirPath,'report',project)):
        os.makedirs(os.path.join(strDirPath,'report',project))
    if not os.path.exists(os.path.join(strDirPath,'report',project,'labelPrint')):
        os.makedirs(os.path.join(strDirPath,'report',project,'labelPrint'))
    output_file = os.path.join(os.path.join(strDirPath,'report',project,'labelPrint'),output_file)
    main_df.to_excel(output_file, index=False, sheet_name='Sheet1')
    return output_file,main_df
def fatp_labelPrint_generate(project,sku_list,suffix,product):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    sku = get_header_title_label_print('sku','P25')[0][0]
    station = get_header_title_label_print('station','P25')[0][0]
    type = get_header_title_label_print('type','P25')[0][0]
    id = get_header_title_label_print('id','P25')[0][0]
    qty = get_header_title_label_print('qty','P25')[0][0]
    mapp_region = ''
    suffix = ''
    fixed_headers = [sku,type,station,id,qty]
    #tạo một frame rỗng với fixed_headers
    main_df = pd.DataFrame(columns=fixed_headers)    
    for item in sku_list:
        if project == 'MT5':
            tab_name = 'mt5Temp'
        elif project == 'BZ5':
            tab_name = 'bz5Temp'
        else:
            tab_name = 'fl5Temp'
        tempId_eip = get_temp_id(tab_name,'tempId','type','BSN','station','EIP','region','ROR','line','fatp')[0][0]
        tempId_co = get_temp_id(tab_name,'tempId','type','BSN','station','CO','region','ROR','line','fatp')[0][0]
        tempId_label = get_temp_id(tab_name,'tempId','type','BSN','station','label_print','region','ROR','line','fatp')[0][0]
        tempId_repair = get_temp_id(tab_name,'tempId','type','packing','station','repair-in','region','ROR','line','kit')[0][0]
        tempId_carton = get_temp_id(tab_name,'tempId','type','carton','station','ECP','region','ROR','line','fatp')[0][0]

        list_eip = ['BSN','EIP',tempId_eip,1]
        list_co = ['BSN','CO',tempId_co,1]
        list_label = ['BSN','LABLE_PRINT',tempId_label,1]
        list_rp = ['REPAIR_IN','REPAIR-IN',tempId_repair,1]
        list_car = ['CARTON','ECP',tempId_carton,2]

        dic_eip = add_information_labelPrint(item,list_eip,suffix,sku,station,type,id,qty)
        dic_co = add_information_labelPrint(item,list_co,suffix,sku,station,type,id,qty)
        dic_label = add_information_labelPrint(item,list_label,suffix,sku,station,type,id,qty)
        dic_rp = add_information_labelPrint(item,list_rp,suffix,sku,station,type,id,qty)
        dic_car = add_information_labelPrint(item,list_car,suffix,sku,station,type,id,qty)
        list_combine=[dic_eip,dic_co,dic_label,dic_rp,dic_car]
        new_row = pd.DataFrame(list_combine)
        print(new_row)
        main_df = pd.concat([main_df , new_row], ignore_index=True)
        print(main_df)
    #Export file
    output_file = f'GetModelNameLoad ({datetime.now().strftime("%Y%m%d%H%M%S")}).xlsx'
    if not os.path.exists(os.path.join(strDirPath,'report')):
        os.makedirs(os.path.join(strDirPath,'report'))
    if not os.path.exists(os.path.join(strDirPath,'report',project)):
        os.makedirs(os.path.join(strDirPath,'report',project))
    if not os.path.exists(os.path.join(strDirPath,'report',project,'labelPrint')):
        os.makedirs(os.path.join(strDirPath,'report',project,'labelPrint'))
    output_file = os.path.join(os.path.join(strDirPath,'report',project,'labelPrint'),output_file)
    main_df.to_excel(output_file, index=False, sheet_name='Sheet1')
    return output_file,main_df
def packing_labelPrint_generate(project,sku_list,suffix,product):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    folder_path = os.path.join(strDirPath,"database")
    list_data_file = [os.path.join(folder_path,item) for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,item))]
    print(list_data_file) 
    # chk whether data file exists or not
    config_path = ''
    mapping_path = ''
    keyFile_path = ''
    for item in list_data_file:
        if project=='MT5':
            if 'VN MP Delivery Tracker' in os.path.basename(item):
                mapping_path = item
        elif project=='BZ5':
            if 'INT-VN-BZ5 MP POR' in os.path.basename(item):
                mapping_path = item  
        elif project=='FL5':
            if 'FL5 POR Packout' in os.path.basename(item):
                mapping_path = item 
        if 'config' in os.path.basename(item):
            config_path = item
        elif 'keyFile' in os.path.basename(item):
            keyFile_path = item
    if suffix != '':
        new_suffix = [it + '-' + suffix for it in sku_list]
    else:
        new_suffix = [it for it in sku_list]
    print(new_suffix)
    sku = get_header_title_label_print('sku','P25')[0][0]
    station = get_header_title_label_print('station','P25')[0][0]
    type = get_header_title_label_print('type','P25')[0][0]
    id = get_header_title_label_print('id','P25')[0][0]
    qty = get_header_title_label_print('qty','P25')[0][0]
    mapp_region = ''

    fixed_headers = [sku,type,station,id,qty]
    #tạo một frame rỗng với fixed_headers
    main_df = pd.DataFrame(columns=fixed_headers)

    for item in sku_list:
        if project == "MT5":
            pd_mapping = pd.read_excel(mapping_path,sheet_name='VN MP SKU Mapping Table',dtype={'EAN': str,'UPC碼' : str})
            print(pd_mapping)
            df_loc_sku = pd_mapping[pd_mapping.iloc[:,1] == item]
            #df_loc_sku.columns = df_loc_sku.columns.str.replace('\xa0', '', regex=False)
            print(df_loc_sku)
            mapp_region = df_loc_sku.iloc[0,20].strip()
        elif project == "FL5":
            pd_mapping = pd.read_excel(mapping_path,sheet_name='FL5_POR_包裝對照表 (Mapping Table)',header=10,dtype={'UPC Code-12': str,'EAN Code-13' : str})
            df_loc_mapping = pd_mapping[pd_mapping.iloc[:,4] == item]
            print(df_loc_mapping)
            #df_loc_mapping.columns = df_loc_mapping.columns.str.replace('\xa0', '', regex=False)
            mapp_region = df_loc_mapping.iloc[0,5].strip()    
        elif project == "BZ5":
            pd_mapping = pd.read_excel(mapping_path,sheet_name='BZ5 MP Control table_ VN',header=6,dtype={'UPC Code-12\n(except EMEA)': str,'EAN Code-13\n(EMEA only)' : str,'SKU ID (C-SKU for ATT only)': str})
            pd_des = pd.read_excel(mapping_path,sheet_name='POR Config List')
            df_loc_mapping = pd_mapping[pd_mapping.iloc[:,6] == item]
            #df_loc_mapping.columns = df_loc_mapping.columns.str.replace('\xa0', '', regex=False)
            mapp_region = df_loc_mapping.iloc[0,7].strip()
        region = region_convert(mapp_region)

        if project == 'MT5':
            tab_name = 'mt5Temp'
        elif project == 'BZ5':
            tab_name = 'bz5Temp'
        else:
            tab_name = 'fl5Temp'
        tempId_pl1 = get_temp_id(tab_name,'tempId','type','packing','station','pallet1','region','ROR','line','kit')[0][0]
        tempId_pl2 = get_temp_id(tab_name,'tempId','type','packing','station','pallet2','region','ROR','line','kit')[0][0]
        tempId_pl3 = get_temp_id(tab_name,'tempId','type','packing','station','pallet3','region','ROR','line','kit')[0][0]
        region_1 = region
        if 'CLNR' not in item:
            if  region not in ['TMO','VZW','EMEA']:
                region_1 = 'ROR'
            tempId_rp = get_temp_id(tab_name,'tempId','type','packing','station','repair-in','region','ROR','line','kit')[0][0]
            tempId_car = get_temp_id(tab_name,'tempId','type','packing','station','carton','region',region_1,'line','retail')[0][0]
            tempId_bts = get_temp_id(tab_name,'tempId','type','packing','station','ship','region',region_1,'line','retail')[0][0]
            list_pallet1 = ['PALLET','PALLET',tempId_pl1,1]
            list_pallet2 = ['PALLET','PALLET',tempId_pl2,1]
            list_pallet3 = ['PALLET','PALLET',tempId_pl3,1]
            list_repair = ['REPAIR_IN','REPAIR-IN',tempId_rp,1]
            qty_car = 1
            if region == 'JP':
                qty_car = 3
            list_carton = ['CARTON','ACP',tempId_car,qty_car]
            list_bts = ['SHIP','SHIP',tempId_bts,5]
            dic_pl1 = add_information_labelPrint(item,list_pallet1,suffix,sku,station,type,id,qty)
            dic_pl2 = add_information_labelPrint(item,list_pallet2,suffix,sku,station,type,id,qty)
            dic_pl3 = add_information_labelPrint(item,list_pallet3,suffix,sku,station,type,id,qty)
            dic_rp = add_information_labelPrint(item,list_repair,suffix,sku,station,type,id,qty)
            dic_ct = add_information_labelPrint(item,list_carton,suffix,sku,station,type,id,qty)
            dic_bts = add_information_labelPrint(item,list_bts,suffix,sku,station,type,id,qty)
            list_combine=[dic_pl1,dic_pl2,dic_pl3,dic_rp,dic_ct,dic_bts]
            new_row = pd.DataFrame(list_combine)
            print(new_row)
        else:
            if  region not in ['TMO','VZW','EMEA']:
                region_1 = 'ROR'
            tempId_car = get_temp_id(tab_name,'tempId','type','packing','station','carton','region',region_1,'line','fru')[0][0]
            tempId_bts = get_temp_id(tab_name,'tempId','type','packing','station','ship','region',region_1,'line','fru')[0][0]

            tempId_imei1 = get_temp_id(tab_name,'tempId','type','packing','station','devide','region',region,'line','CLNR')[0][0]
            tempId_imei2 = get_temp_id(tab_name,'tempId','type','packing','station','devide1','region',region,'line','CLNR')[0][0]
            
            list_pallet1 = ['PALLET','PALLET',tempId_pl1,1]
            list_pallet2 = ['PALLET','PALLET',tempId_pl2,1]
            list_pallet3 = ['PALLET','PALLET',tempId_pl3,1]
            list_carton = ['CARTON','ACP',tempId_car,1]
            list_bts = ['SHIP','SHIP',tempId_bts,5]
            list_imei1 = ['DEV','IMEI',tempId_imei1,1]
            list_imei2 = ['DEV2','IMEI1',tempId_imei2,1]

            dic_pl1 = add_information_labelPrint(item,list_pallet1,suffix,sku,station,type,id,qty)
            dic_pl2 = add_information_labelPrint(item,list_pallet2,suffix,sku,station,type,id,qty)
            dic_pl3 = add_information_labelPrint(item,list_pallet3,suffix,sku,station,type,id,qty)
            dic_ct = add_information_labelPrint(item,list_carton,suffix,sku,station,type,id,qty)
            dic_bts = add_information_labelPrint(item,list_bts,suffix,sku,station,type,id,qty)
            dic_imei1 = add_information_labelPrint(item,list_imei1,suffix,sku,station,type,id,qty)
            dic_imei2 = add_information_labelPrint(item,list_imei2,suffix,sku,station,type,id,qty)
            list_combine=[dic_pl1,dic_pl2,dic_pl3,dic_ct,dic_bts,dic_imei1,dic_imei2]
            new_row = pd.DataFrame(list_combine)
            print(new_row)
        main_df = pd.concat([main_df , new_row], ignore_index=True)
        print(main_df)
    #Export file
    output_file = f'GetModelNameLoad ({datetime.now().strftime("%Y%m%d%H%M%S")}).xlsx'
    if not os.path.exists(os.path.join(strDirPath,'report')):
        os.makedirs(os.path.join(strDirPath,'report'))
    if not os.path.exists(os.path.join(strDirPath,'report',project)):
        os.makedirs(os.path.join(strDirPath,'report',project))
    if not os.path.exists(os.path.join(strDirPath,'report',project,'labelPrint')):
        os.makedirs(os.path.join(strDirPath,'report',project,'labelPrint'))
    output_file = os.path.join(os.path.join(strDirPath,'report',project,'labelPrint'),output_file)
    main_df.to_excel(output_file, index=False, sheet_name='Sheet1')
    return output_file,main_df
def add_information_labelPrint(sku,list_mapp,suffix,sku_key,station_key,type_key,id_key,qty_key):
    result_list = dict()
    if suffix == '':
        result_list[sku_key] = sku 
    else:
        result_list[sku_key] = sku + '-' + suffix
    result_list[type_key] = list_mapp[0]
    result_list[station_key] = list_mapp[1]
    result_list[id_key] = list_mapp[2]
    result_list[qty_key] = list_mapp[3]
    return result_list
def main_generate(project,sku_list,suffix,product):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    chk_mandatory_folder(strAbsPath,strDirPath)
    # return list address of file
    folder_path = os.path.join(strDirPath,"database")
    list_data_file = [os.path.join(folder_path,item) for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,item))]
    print(list_data_file) 
    # chk whether data file exists or not
    config_path = ''
    mapping_path = ''
    keyFile_path = ''
    for item in list_data_file:
        if project=='MT5':
            if 'VN MP Delivery Tracker' in os.path.basename(item):
                mapping_path = item
        elif project=='BZ5':
            if 'INT-VN-BZ5 MP POR' in os.path.basename(item):
                mapping_path = item  
        elif project=='FL5':
            if 'FL5 POR Packout' in os.path.basename(item):
                mapping_path = item 
        if 'config' in os.path.basename(item):
            config_path = item
        elif 'keyFile' in os.path.basename(item):
            keyFile_path = item
    chk_mandatary_file(config_path,mapping_path,keyFile_path)
    if suffix != '':
        new_suffix = [it + '-' + suffix for it in sku_list]
    else:
        new_suffix = [it for it in sku_list]
    print(new_suffix)
    sku = get_header_title('sku','P25')[0][0]
    ver = get_header_title('version','P25')[0][0]
    type = get_header_title('type','P25')[0][0]
    name = get_header_title('name','P25')[0][0]
    des = get_header_title('des','P25')[0][0]
    value = get_header_title('value','P25')[0][0]
    if project == "MT5":
        pd_mapping = pd.read_excel(mapping_path,sheet_name='VN MP SKU Mapping Table',dtype={'EAN': str,'UPC碼' : str})
    elif project == "FL5":
        pd_mapping = pd.read_excel(mapping_path,sheet_name='FL5_POR_包裝對照表 (Mapping Table)',header=10,dtype={'UPC Code-12': str,'EAN Code-13' : str})
    elif project == "BZ5":
        pd_mapping = pd.read_excel(mapping_path,sheet_name='BZ5 MP Control table_ VN',header=6,dtype={'UPC Code-12\n(except EMEA)': str,'EAN Code-13\n(EMEA only)' : str,'SKU ID (C-SKU for ATT only)': str})
        pd_des = pd.read_excel(mapping_path,sheet_name='POR Config List')
    fixed_headers = [sku,ver,type,name,des,value]
    #tạo một frame rỗng với fixed_headers
    main_df = pd.DataFrame(columns=fixed_headers)
    for item in sku_list:
        arr_mapping = list()
        #Loc trong mapping de compare
        mapp_des = mapp_upc = map_bob = mapp_rap = mapp_brand = ''
        mapp_mrp=mapp_price=mapp_qr=''
        mapp_sap=mapp_carton_color = ''
        mapp_region = ''
        if project == "MT5":
            df_loc_sku = pd_mapping[pd_mapping.iloc[:,1] == item]
            df_loc_sku.columns = df_loc_sku.columns.str.replace('\xa0', '', regex=False)
            mapp_region = df_loc_sku.iloc[0,20].strip()
            mapp_des = df_loc_sku.iloc[0:5]
            arr_mapping = filter_mapping_config(mapp_region,df_loc_sku,item,config_path,project,product)
        elif project == 'FL5':
            df_loc_mapping = pd_mapping[pd_mapping.iloc[:,4] == item]
            print(df_loc_mapping)
            df_loc_mapping.columns = df_loc_mapping.columns.str.replace('\xa0', '', regex=False)
            mapp_region = df_loc_mapping.iloc[0,5].strip()
            mapp_des = df_loc_mapping.iloc[0,28]
            arr_mapping = filter_mapping_config_FL(mapp_region,df_loc_mapping,item,config_path,project,product)
        elif project == 'BZ5':
            df_loc_mapping = pd_mapping[pd_mapping.iloc[:,6] == item]
            df_loc_mapping.columns = df_loc_mapping.columns.str.replace('\xa0', '', regex=False)
            mapp_region = df_loc_mapping.iloc[0,7].strip()
            mapp_des = df_loc_mapping.iloc[0,26]
            arr_mapping = filter_mapping_config_BZ(mapp_region,df_loc_mapping,item,config_path,mapp_des,project,product)
        print(arr_mapping)
        #Add list infor into dictionary
        if 'CLNR' not in item:
            list_des = add_information(item,arr_mapping,'Description',suffix,sku,ver,type,name,des,value)
            list_brand = add_information(item,arr_mapping,'Brand',suffix,sku,ver,type,name,des,value)
            list_upc = add_information(item,arr_mapping,'UPC',suffix,sku,ver,type,name,des,value)
            list_rap = add_information(item,arr_mapping,'R-Label',suffix,sku,ver,type,name,des,value)
            list_bob = add_information(item,arr_mapping,'B-Label',suffix,sku,ver,type,name,des,value)
            list_combine=[list_des,list_brand,list_upc,list_rap,list_bob]
            new_row = pd.DataFrame(list_combine)
            print(new_row)
            if region_convert(mapp_region) == 'ATT' or region_convert(mapp_region) == 'TMO':
                list_sap = add_information(item,arr_mapping,'SAP',suffix,sku,ver,type,name,des,value)
                list_color = add_information(item,arr_mapping,'Carton_Color',suffix,sku,ver,type,name,des,value)
                list_att = [list_sap,list_color]
                new_row = pd.concat([new_row, pd.DataFrame(list_att)], ignore_index=True)
            elif region_convert(mapp_region) == 'IN':
                list_M = add_information(item,arr_mapping,'M-Label',suffix,sku,ver,type,name,des,value)
                list_Price = add_information(item,arr_mapping,'Price',suffix,sku,ver,type,name,des,value)
                list_Code = add_information(item,arr_mapping,'QR_CODE',suffix,sku,ver,type,name,des,value)
                list_att = [list_M,list_Price,list_Code]
                new_row = pd.concat([new_row, pd.DataFrame(list_att)], ignore_index=True)
            print(new_row)
        else:
            list_brand = add_information(item,arr_mapping,'Brand',suffix,sku,ver,type,name,des,value)
            list_upc = add_information(item,arr_mapping,'UPC',suffix,sku,ver,type,name,des,value)  
            list_combine=[list_brand,list_upc]
            new_row = pd.DataFrame(list_combine)         
        main_df = pd.concat([main_df , new_row], ignore_index=True)
        print(list_combine)
        print(new_row)
        print(main_df)
        #Export file
        output_file = f'Part No_{datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx'
        if not os.path.exists(os.path.join(strDirPath,'report')):
            os.makedirs(os.path.join(strDirPath,'report'))
        if not os.path.exists(os.path.join(strDirPath,'report',project,'keyConfig')):
            os.makedirs(os.path.join(strDirPath,'report',project,'keyConfig'))
        output_file = os.path.join(os.path.join(strDirPath,'report',project,'keyConfig'),output_file)
        main_df.to_excel(output_file, index=False, sheet_name='ACC')
    #os.startfile(output_file)
    return output_file,main_df
def filter_mapping_config_BZ(market,mapp_frame,sku,link_config,des,project,product):
    arr_std = list()
    df_loc_mapping = mapp_frame[mapp_frame.iloc[:,6] == sku]
    mapp_des = des
    mapp_brand = df_loc_mapping.iloc[0,14]
    mapp_sap = df_loc_mapping.iloc[0,16]
    mapp_color = df_loc_mapping.iloc[0,12]
    mapp_storage = df_loc_mapping.iloc[0,19]
    region = region_convert(market)
    if region == 'ATT' or region == 'TMO':
        mapp_rap = project +'_FIHVN_RAP' + '_' + region + '_' + mapp_storage + '_' + mapp_color + '_MP'
    elif region =='EMEA':
        mapp_rap = project + '_FIHVN_RAP' + '_' + region + '_MP'
    elif region == 'Gstore':
        mapp_rap = project + '_FIHVN_RAP' + '_' + region.upper() + '_MP'
    else:
        mapp_rap = project + '_FIHVN_RAP' + '_' + region + '_MP'
    if region == 'EMEA':
        mapp_upc = str(df_loc_mapping.iloc[0,18]) #str((df_loc_mapping['EAN'].iloc[0]))
    else:
        mapp_upc = str(df_loc_mapping.iloc[0,17])#str((df_loc_mapping['UPC碼'].iloc[0]))
    # trace BOB name BOB\nArtwork GPN & Rev\n
    #mapp_bob_code = df_loc_mapping.iloc[0,45]
    #mapp_bob_code = df_loc_mapping.iloc[0,45].split('\n')[0].strip()
   #mapp_bob_code = bob_convert(mapp_bob_code)
    rev_code = ''
    aaa = df_loc_mapping.iloc[0, 45]
    if pd.isna(aaa):
        aaa = ''
    if aaa != '':
        if len(df_loc_mapping.iloc[0,45].split('\n')) == 2:
            mapp_bob_code = df_loc_mapping.iloc[0,45].split('\n')[1].strip()
            mapp_bob_rev = df_loc_mapping.iloc[0,45].split('\n')[1].strip()
        else:
            mapp_bob_code = df_loc_mapping.iloc[0,45].split('\n')[0].strip()
            mapp_bob_rev = df_loc_mapping.iloc[0,45].split('\n')[0].strip()
    else:
        mapp_bob_code = ''
    if mapp_bob_code == 'No' or mapp_bob_code =='#VALUE!' or mapp_bob_code == '':
        mapp_bob_code = ''
    else:
        mapp_bob_code,rev_code = bob_convert(mapp_bob_code,mapp_bob_rev)
    if mapp_bob_code != '':
        mapp_bob_code = mapp_bob_code + '_rev' + rev_code
        fil = get_bob_list(mapp_bob_code,product)
        if len(fil) == 0:
            mapp_bob_fl = ''
        else:
            mapp_bob_fl = get_bob_list(mapp_bob_code,product)[0][0]
        #mapp_bob_fl = get_bob_list(mapp_bob_code,product)[0][0]
    else:
        mapp_bob_code = ''
        mapp_bob_fl = ''
    
    arr_std.append(mapp_des)
    arr_std.append(mapp_brand)
    arr_std.append(mapp_upc)
    arr_std.append(mapp_rap)
    arr_std.append(mapp_bob_fl)
    if region_convert(market) == 'ATT' or region_convert(market) == 'TMO':
        arr_std.append(mapp_sap)
        arr_std.append(mapp_color)
    elif region_convert(market) == 'IN':
        # doc file config.txt de lay price va Mlabel
        mapp_price = get_price_In(project)[0][0] #data.get('price')
        mapp_mLabel = project + " " + "MRP" #mLabel
        arr_std.append(mapp_price)
        arr_std.append(mapp_mLabel)
        arr_std.append(df_loc_mapping.iloc[0,47]) #IN MRP\nArtwork GPN & Rev\n
    return arr_std
def bob_convert(bob_code,rev_code):
    if len(bob_code) == 15:
        bob_code = bob_code[:-2]
        rev_code = rev_code[-1:]
    elif len(bob_code) == 16:
        bob_code = bob_code[:-3]
        rev_code = rev_code[-2:]
    elif len(bob_code) < 15:
        bob_code = bob_code
        rev_code = ''
    return bob_code,rev_code
def filter_mapping_config_FL(market,mapp_frame,sku,link_config,project,product):
    arr_std = list()
    df_loc_mapping = mapp_frame[mapp_frame.iloc[:,4] == sku]
    mapp_des = df_loc_mapping.iloc[0,28].strip()
    mapp_brand = df_loc_mapping.iloc[0,11].strip()
    mapp_sap = df_loc_mapping.iloc[0,48]
    mapp_color = df_loc_mapping.iloc[0,9].strip()
    mapp_storage = df_loc_mapping.iloc[0,44].strip()
    region = region_convert(market)
    if region == 'ATT' or region == 'TMO':
        mapp_rap = project +'_FIHVN_RAP' + '_' + region + '_' + mapp_color + '_' + mapp_storage + '_MP'
    elif region =='EMEA':
        mapp_rap = project + '_FIHVN_RAP' + '_' + region + '_MP'
    else:
        mapp_rap = project + '_FIHVN_RAP' + '_' + region + '_MP'
    if region == 'EMEA':
        mapp_upc = str(df_loc_mapping.iloc[0,50]).strip() #str((df_loc_mapping['EAN'].iloc[0]))
    else:
        mapp_upc = str(df_loc_mapping.iloc[0,49]).strip()#str((df_loc_mapping['UPC碼'].iloc[0]))
    # trace BOB name BOB\nArtwork GPN & Rev\n
    #mapp_bob_code = df_loc_mapping.iloc[0,55].split('\n')[0].strip()
    #mapp_bob_code = bob_convert(mapp_bob_code)
    aaa = df_loc_mapping.iloc[0, 55]
    if pd.isna(aaa):
        aaa = ''
    if aaa != '':
        if len(df_loc_mapping.iloc[0,55].split('\n')) == 2:
            mapp_bob_code = df_loc_mapping.iloc[0,55].split('\n')[1].strip()
            mapp_bob_rev = df_loc_mapping.iloc[0,55].split('\n')[1].strip()
        else:
            mapp_bob_code = df_loc_mapping.iloc[0,55].split('\n')[0].strip()
            mapp_bob_rev = df_loc_mapping.iloc[0,55].split('\n')[0].strip()
    else:
        mapp_bob_code = ''
    if mapp_bob_code == 'No'or mapp_bob_code =='#VALUE!' or mapp_bob_code == '':
        mapp_bob_code = ''
    else:
        mapp_bob_code,rev_code = bob_convert(mapp_bob_code,mapp_bob_rev)
    if mapp_bob_code != '':
        mapp_bob_code = mapp_bob_code + '_rev' + rev_code
        fil = get_bob_list(mapp_bob_code,product)
        if len(fil) == 0:
            mapp_bob_name = ''
        else:
            mapp_bob_name = get_bob_list(mapp_bob_code,product)[0][0]
    else:
        mapp_bob_code = ''
        mapp_bob_name = ''
    arr_std.append(mapp_des)
    arr_std.append(mapp_brand)
    arr_std.append(mapp_upc)
    arr_std.append(mapp_rap)
    arr_std.append(mapp_bob_name)
    if region == 'ATT' or region == 'TMO':
        arr_std.append(mapp_sap)
        arr_std.append(mapp_color)
    elif region == 'IN':
        # doc file config.txt de lay price va Mlabel
        mapp_price = get_price_In(project)[0][0] #data.get('price')
        mapp_mLabel = project + " " + "MRP" #mLabel
        arr_std.append(mapp_price)
        arr_std.append(mapp_mLabel)
        arr_std.append(str(df_loc_mapping.iloc[0,67])[:-2]) #IN MRP\nArtwork GPN & Rev\n
    return arr_std
def filter_mapping_config(market,mapp_frame,sku,link_config,project,product):
    arr_std = list()
    df_loc_mapping = mapp_frame[mapp_frame.iloc[:,1] == sku]
    mapp_des = df_loc_mapping.iloc[0,5].strip()
    mapp_brand = df_loc_mapping.iloc[0,7].strip()
    mapp_sap = df_loc_mapping.iloc[0,23]
    mapp_color = df_loc_mapping.iloc[0,18].strip()
    mapp_storage = df_loc_mapping.iloc[0,14].strip()
    region = region_convert(market)
    if region == 'ATT' or region == 'TMO':
        mapp_rap = project +'_FIHVN_RAP' + '_' + region + '_' + mapp_storage + '_' + mapp_color + '_MP'
    elif region =='EMEA':
        mapp_rap = project + '_FIHVN_RAP' + '_' + region + '_MP_45'
    else:
        mapp_rap = project + '_FIHVN_RAP' + '_' + region + '_MP'
    if region == 'EMEA':
        mapp_upc = df_loc_mapping.iloc[0,22].strip() #str((df_loc_mapping['EAN'].iloc[0]))
    else:
        mapp_upc = df_loc_mapping.iloc[0,21].strip()#str((df_loc_mapping['UPC碼'].iloc[0]))
    # trace BOB name BOB\nArtwork GPN & Rev\n
    aaa = df_loc_mapping.iloc[0, 40]
    if pd.isna(aaa):
        aaa = ''
    if aaa != '':
        if len(df_loc_mapping.iloc[0,40].split('\n')) == 2:
            mapp_bob_code = df_loc_mapping.iloc[0,40].split('\n')[1].strip()
            mapp_bob_rev = df_loc_mapping.iloc[0,40].split('\n')[1].strip()
        else:
            mapp_bob_code = df_loc_mapping.iloc[0,40].split('\n')[0].strip()
            mapp_bob_rev = df_loc_mapping.iloc[0,40].split('\n')[0].strip()
    else:
        mapp_bob_code = ''
    if mapp_bob_code == 'No'or mapp_bob_code =='#VALUE!' or mapp_bob_code == '':
        mapp_bob_code = ''
    else:
        mapp_bob_code,rev_code = bob_convert(mapp_bob_code,mapp_bob_rev)
    if mapp_bob_code != '':
        mapp_bob_code = mapp_bob_code + '_rev' + rev_code
        fil = get_bob_list(mapp_bob_code,product)
        if len(fil) == 0:
            mapp_bob_name = ''
        else:
            mapp_bob_name = get_bob_list(mapp_bob_code,product)[0][0]     
    else:
        mapp_bob_code = ''
        mapp_bob_name = ''        
    arr_std.append(mapp_des)
    arr_std.append(mapp_brand)
    arr_std.append(mapp_upc)
    arr_std.append(mapp_rap)
    arr_std.append(mapp_bob_name)
    if market == 'US - AT&T' or market == 'US-TMO':
        arr_std.append(mapp_sap)
        arr_std.append(mapp_color)
    elif market == 'IN':
        # doc file config.txt de lay price va Mlabel
        mapp_price = get_price_In(project)[0][0] #data.get('price')
        mapp_mLabel = project + " " + "MRP" #mLabel
        arr_std.append(mapp_price)
        arr_std.append(mapp_mLabel)
        arr_std.append(df_loc_mapping.iloc[0,42][:-2]) #IN MRP\nArtwork GPN & Rev\n
    return arr_std
def add_information(sku,list_mapp,type,suffix,sku_key,ver_key,type_key,name_key,des_key,value_key):
    result_list = dict()
    if suffix == '':
        result_list[sku_key] = sku 
    else:
        result_list[sku_key] = sku + '-' + suffix
    result_list[ver_key] = 'A'
    result_list[type_key] = 'GENRE_ID'
    result_list[name_key] = type
    item_mapp = ''
    match type:
        case 'Description':
            item_mapp = list_mapp[0]
        case 'Brand':
            item_mapp = list_mapp[1]
        case 'UPC':
            item_mapp = list_mapp[2]
        case 'R-Label':
            item_mapp = list_mapp[3]
        case 'B-Label':
            item_mapp = list_mapp[4]
        case 'SAP':
            item_mapp = list_mapp[5]
        case 'Carton_Color':
            item_mapp = list_mapp[6]
        case 'Price':
            item_mapp = list_mapp[5]
        case 'M-Label':
            item_mapp = list_mapp[6]
        case 'QR_CODE':
            if len(list_mapp[7]) == 15:
                item_mapp = list_mapp[7][:13]
            else: 
                item_mapp = list_mapp[7] 
    result_list[des_key] = item_mapp
    result_list[value_key] = item_mapp
    return result_list
def filter_standard_config(keyConfig_frame,sku,type_config):
    df_da_loc = keyConfig_frame[(keyConfig_frame['料號'] == sku) & (keyConfig_frame['key名稱'] == type_config)]
    print(df_da_loc)
    if df_da_loc.empty:
        des_value = ''
        des_confirm = ''
        des_keyname = ''
    else:
        des_value = df_da_loc['key描述'].iloc[0]
        des_confirm = df_da_loc['key值'].iloc[0]
        des_keyname = df_da_loc['key類型'].iloc[0]
    return des_value,des_confirm,des_keyname
def gen_dict_standard(region,list_infor,sku,type):
    result_list = dict()
    result_list['SKU'] = sku
    result_list['Type'] = type
    count = len(list_infor)
    if count == 0:
        match type:
            case 'Des':
                item_mapp = ''
            case 'Brand':
                item_mapp = ''
            case 'UPC':
                item_mapp = ''
            case 'Rap':
                item_mapp = ''
            case 'Bob':
                item_mapp = ''
            
        if region in ['ATT','TMO']:
            if type == 'sap':
                item_mapp = ''
            elif type == 'color':
                item_mapp = ''
        elif region in ['IN']:
            if type == 'price':
                item_mapp = ''
            elif type == 'mrp':
                item_mapp = ''
            elif type == 'qr-code':
                item_mapp = ''  
    else:
        match type:
            case 'Des':
                item_mapp = list_infor[0]
            case 'Brand':
                item_mapp = list_infor[1]
            case 'UPC':
                item_mapp = list_infor[2]
            case 'Rap':
                item_mapp = list_infor[3]
            case 'Bob':
                item_mapp = list_infor[4]
            
        if region in ['ATT','TMO']:
            if type == 'sap':
                item_mapp = list_infor[5]
            elif type == 'color':
                item_mapp = list_infor[6]
        elif region in ['IN']:
            if type == 'price':
                item_mapp = list_infor[5]
            elif type == 'mrp':
                item_mapp = list_infor[6]
            elif type == 'qr-code':
                item_mapp = list_infor[7]
                if len(list_infor[7]) == 15:
                    item_mapp = list_infor[7][:13]
                else:
                    item_mapp = list_infor[7]
    result_list['Value'] = item_mapp
    return result_list
def compare_keyConfig_mapping(sku,value,confirm,key,list_mapp,type):
    result_list = dict()
    result_list['SKU'] = sku
    result_list['Type'] = type
    item_mapp = ''
    match type:
        case 'Des':
            item_mapp = list_mapp[0]
        case 'Brand':
            item_mapp = list_mapp[1]
        case 'UPC':
            item_mapp = list_mapp[2]
        case 'Rap':
            item_mapp = list_mapp[3]
        case 'Bob':
            item_mapp = list_mapp[4]
        case 'sap':
            item_mapp = list_mapp[5]
        case 'color':
            item_mapp = list_mapp[6]
        case 'price':
            item_mapp = list_mapp[5]
        case 'mrp':
            item_mapp = list_mapp[6]
        case 'gpn':
            item_mapp = list_mapp[7]
            if len(list_mapp[7]) == 15:
                item_mapp = list_mapp[7][:13]
            else:
                item_mapp = list_mapp[7]
    if str(value) == str(item_mapp):
        result_list['Value'] = 'PASS'
    else:
        result_list['Value'] = '>fail<'       
    if str(confirm) == str(item_mapp):
        result_list['Confirm'] = 'PASS'
    else:
        result_list['Confirm'] = '>fail<' 
    if key == 'GENRE_ID':
        result_list['Key'] = 'PASS'
    else:
        result_list['Key'] = '>fail<' 
    return result_list
def region_convert(market):
    region = ''
    if market == 'US - AT&T' or market =='UTT' or market == 'AT&T, US' or market  == 'ATT, US':
        region = 'ATT'
    elif market == 'US-TMO' or market =='UTM' or market == 'US - Tmobile' or market == 'TMO, US':
        region = 'TMO'
    elif market == 'US Gstore' or market =='UGS' or market == 'US GStore'or market == 'GSTORE, US':
        region = 'Gstore'
    elif market == 'EU/UK' or market == 'UK/EU' or market =='EMA' or market == 'EU(GB, DE, IT, ES, IE, FR, NL, BE, AT, CH, PT, PL, CEE (RO, CZ, HU, SI, LV, LT, EE, FI), NO,SE,DK, SK)' or market == 'GB, DE, IT, ES, IE, FR, NL, BE, AT, CH, PT, PL, CZ, HU, RO, SI, LV, LT, EE, FI, NO, SE, DK, SK':
        region = 'EMEA'
    elif market == 'CA/TW/SG/AU/MY' or market =='NCA'or market =='CA/TW/SG/AU/MY/MX' or market == 'CA/TW/SG/MY/AU/MX':
        region = 'CA'
    elif market == 'JPN' or market =='AJP' or market =='JP':
        region = 'JP'
    elif market == 'US-VZW' or market =='UVZ' or market == 'VZW, US':
        region = 'VZW'
    else:
        region = 'IN'
    return region