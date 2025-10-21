import os,sys
from log import *
import pandas as pd
from sqliteProcess import *


'''def get_sys_path(strFolder):
    strMainPath = os.path.abspath(sys.argv[0])
    strCrrPath = os.path.dirname(strMainPath)
    return os.path.join(strCrrPath,strFolder);'''
def check_mandatory_folder_exists(folder_name):
    strAbsPath = os.path.abspath(sys.argv[0])
    strCrrPath = os.path.dirname(strAbsPath)
    if not os.path.isdir(os.path.join(strCrrPath,folder_name)):
        raise FileNotFoundError(f"Folder {os.path.join(strCrrPath,folder_name)} is not Exists!!!")
def list_file_in_folder(folderName):
    strMainPath = os.path.abspath(sys.argv[0])
    strCrrPath = os.path.dirname(strMainPath)
    data_path = os.path.join(strCrrPath,"database")
    #data_path = get_sys_path("database")
    list_file = [os.path.join(data_path,item) for item in os.listdir(data_path) if os.path.isfile(os.path.join(data_path,item))]
    return list_file
def get_file_path(crr_project,list_file_path):
    mapping_path = ''
    for item in list_file_path:
        if crr_project=='MT5':
            if 'VN MP Delivery Tracker' in os.path.basename(item):
                mapping_path = item
        elif crr_project=='BZ5':
            if 'INT-VN-BZ5 MP POR' in os.path.basename(item):
                mapping_path = item  
        elif crr_project=='FL5':
            if 'FL5 POR Packout' in os.path.basename(item):
                mapping_path = item  
    print(mapping_path)
    return mapping_path
def region_convert(market):
    region = ''
    if (market == 'US - AT&T' or market =='UTT' or market == 'AT&T, US' or market == 'US -AT&T' or
        market == 'ATT, US' or market =='ATT'):
        region = 'ATT'
    elif (market == 'US-TMO' or market =='UTM' or market == 'US - Tmobile' or market == 'TMO, US' or 
          market =='US-Tmobile' or market == 'TMO'):
        region = 'TMO'
    elif market == 'US Gstore' or market =='UGS' or market == 'US GStore'or market == 'GSTORE, US':
        region = 'Gstore'
    elif (market == 'EU/UK' or market == 'UK/EU' or market =='EMA' or 
    market == 'EU(GB, DE, IT, ES, IE, FR, NL, BE, AT, CH, PT, PL, CEE (RO, CZ, HU, SI, LV, LT, EE, FI), NO,SE,DK, SK)' or 
    market == 'GB, DE, IT, ES, IE, FR, NL, BE, AT, CH, PT, PL, CZ, HU, RO, SI, LV, LT, EE, FI, NO, SE, DK, SK' or 
    market == 'GB, DE, IT, ES, IE, FR, NL, BE, AT, CH, PT, PL, CEE ( CZ, HU, RO, SI, LV, LT, EE, FI), NO,SE,DK, SK, CA/TW/SG/AU/MY/MX'):
        region = 'EMEA'
    elif market == 'CA/TW/SG/AU/MY' or market =='NCA'or market =='CA/TW/SG/AU/MY/MX' or market == 'CA/TW/SG/MY/AU/MX':
        region = 'CA'
    elif market == 'JPN' or market =='AJP' or market =='JP':
        region = 'JP'
    elif (market == 'US-VZW' or market =='UVZ' or market == 'VZW, US' or market == 'VZW'):
        region = 'VZW'
    elif (market == 'IN'):
        region = 'IN'
    return region
def region_convert_pack(crr_region):
    if crr_region in ['ATT','TMO','Gstore','CA','VZW','IN']:
        return 'US'
    elif crr_region in ['JP']:
        return 'JP'
    elif crr_region in ['EMEA']:
        return 'GB'
def label_infor_return(mapping,compare_value,sku_col,bob_col,des_col,rap_col,brand_col,color_col,
                       qr_col,storage_col,region_col,project,ver_col,start_imei_col,end_imei_col,
                       sap_col,upc_col,ean_col,product):
    condition = mapping.iloc[:, sku_col] == compare_value
    print(mapping.loc[condition, mapping.columns[bob_col]])
    if len(mapping.loc[condition, mapping.columns[bob_col]]) >1:
        BOB_code = str(mapping.loc[condition, mapping.columns[bob_col]].iloc[0])
    else:
        BOB_code = str(mapping.loc[condition, mapping.columns[bob_col]].item())
    if BOB_code == 'nan':
        BOB_code = ''
    else:
        BOB_code = BOB_code.strip()   
        if len(BOB_code) >2 :
            if '\n' in BOB_code:
                BOB_code =  BOB_code.split('\n')[-1][:-2]
            else:
                if len(BOB_code) == 16:
                    BOB_code =  BOB_code[:-3]
                elif len(BOB_code) == 15:
                    BOB_code = BOB_code[:-2]
        elif len(BOB_code)<3:
            BOB_code=BOB_code
    print(BOB_code)  
    bob_list = get_bob_list(BOB_code,product)
    if bob_list:
        BOB_code=(bob_list[0][0])
    else:
        BOB_code = ('')
    if len(mapping.loc[condition, mapping.columns[des_col]])>1:
        Des_code = mapping.loc[condition, mapping.columns[des_col]].iloc[0]
    else:
        Des_code = mapping.loc[condition, mapping.columns[des_col]].item()
    if len(mapping.loc[condition, mapping.columns[rap_col]])>1:
        rap_code = mapping.loc[condition, mapping.columns[rap_col]].iloc[0] 
    else:
        rap_code = mapping.loc[condition, mapping.columns[rap_col]].item()   
    if len(mapping.loc[condition, mapping.columns[brand_col]])>1:
        brand_code = mapping.loc[condition, mapping.columns[brand_col]].iloc[0]
    else:       
        brand_code = mapping.loc[condition, mapping.columns[brand_col]].item() 
    if len(mapping.loc[condition, mapping.columns[color_col]]) > 1: 
        color_code = mapping.loc[condition, mapping.columns[color_col]].iloc[0]
    else:       
        color_code = mapping.loc[condition, mapping.columns[color_col]].item()
    if len(mapping.loc[condition, mapping.columns[qr_col]])>1:
        qr_code = mapping.loc[condition, mapping.columns[qr_col]].iloc[0]
    else:
        qr_code = mapping.loc[condition, mapping.columns[qr_col]].item()
    #a = upc_code.item()
    if len(mapping.loc[condition, mapping.columns[storage_col]])>1:
        storage_code = mapping.loc[condition, mapping.columns[storage_col]].iloc[0]
    else:
        storage_code = mapping.loc[condition, mapping.columns[storage_col]].item()
    price_code = get_price_In(project)[0][0]
    m_code = project + ' MRP'
    if len(mapping.loc[condition, mapping.columns[region_col]])>1:
        region_code = region_convert(mapping.loc[condition, mapping.columns[region_col]].iloc[0])
    else:
        region_code = region_convert(mapping.loc[condition, mapping.columns[region_col]].item())
    sw_ver = mapping.loc[condition, mapping.columns[ver_col]]#.item()
    sw_ver = sw_ver.fillna("None")
    if len(sw_ver)>1:
        sw_ver = sw_ver.iloc[0]
    else:
        sw_ver = sw_ver.item()
    print(sw_ver)
    if len(mapping.loc[condition, mapping.columns[start_imei_col]])>1:
        start_IMEI = mapping.loc[condition, mapping.columns[start_imei_col]].iloc[0]
    else:
        start_IMEI = mapping.loc[condition, mapping.columns[start_imei_col]].item()
    if len(mapping.loc[condition, mapping.columns[end_imei_col]])>1:
        end_IMEI = mapping.loc[condition, mapping.columns[end_imei_col]].iloc[0]
    else:
        end_IMEI = mapping.loc[condition, mapping.columns[end_imei_col]].item() 
    mapp_rap=''
    sap_code=''
    if region_code == 'ATT' or region_code == 'TMO':
        sap_code = mapping.loc[condition, mapping.columns[sap_col]].item()
        mapp_rap = project +'_FIHVN_RAP' + '_' + region_code + '_' + storage_code + '_' + color_code + '_MP'
        if len(mapping.loc[condition, mapping.columns[upc_col]])>1:
            upc_code = mapping.loc[condition, mapping.columns[upc_col]].iloc[0]
        else:
            upc_code = mapping.loc[condition, mapping.columns[upc_col]].item()
        m_code = ''
        qr_code = ''
        price_code =''
    elif region_code == 'IN': 
        mapp_rap = project +'_FIHVN_RAP' + '_' + region_code + '_' +  'MP'
        if len(mapping.loc[condition, mapping.columns[upc_col]])>1:
            upc_code = mapping.loc[condition, mapping.columns[upc_col]].iloc[0]
        else:
            upc_code = mapping.loc[condition, mapping.columns[upc_col]].item()

        sap_code =''
        color_code = ''
    elif region_code == 'EMEA':
        mapp_rap = project +'_FIHVN_RAP' + '_' + region_code + '_' +  'MP'
        if len(mapping.loc[condition, mapping.columns[ean_col]])>1:
            upc_code = mapping.loc[condition, mapping.columns[ean_col]].iloc[0]
        else:
            upc_code = mapping.loc[condition, mapping.columns[ean_col]].item()
        sap_code =''
        color_code = ''
        m_code = ''
        qr_code = ''
        price_code =''
    else:
        mapp_rap = project +'_FIHVN_RAP' + '_' + region_code + '_' +  'MP'
        if len(mapping.loc[condition, mapping.columns[upc_col]])>1:
            upc_code = mapping.loc[condition, mapping.columns[upc_col]].iloc[0]
        else:
            upc_code = mapping.loc[condition, mapping.columns[upc_col]].item()

        sap_code =''
        color_code = ''
        m_code = ''
        qr_code = ''
        price_code =''
    return (BOB_code,Des_code,rap_code,brand_code,color_code,qr_code,storage_code,price_code,m_code,
            sw_ver,start_IMEI,end_IMEI,sap_code,mapp_rap,upc_code,region_code)
