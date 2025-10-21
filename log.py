import os
import sys
from datetime import datetime
from log import *
import traceback
def testLog():
    a= 5
    b= 0
    return a/b
    print(e)
def get_details_error(loi):
    tb =  traceback.extract_tb(loi.__traceback__)
    if tb:
        frame = tb[-1]
        file = frame.filename
        line = frame.lineno
        func = frame.name
        return file,func,line
    return None, None, None
def getRelativePath():
    #c = os.path.abspath(__file__)
    strAbsPath = os.path.abspath(sys.argv[0])
    strCurrPath = os.path.dirname(strAbsPath)
    strLogPath = os.path.join(strCurrPath,"log")
    if not os.path.exists(strLogPath):
        os.makedirs(strLogPath)
        return strLogPath
    else:
        return strLogPath
def logExport(ex):
    strLogPath = getRelativePath()
    strFilePath = strLogPath + r"\log_"  +  datetime.now().strftime("%Y%m%d") +".txt"
    strContents = "[{}] {}".format( datetime.now().strftime("%Y/%m/%d %H:%M:%S"),ex)
    if not os.path.exists(strFilePath):
        
        logFile = open(strFilePath,"x")
        logFile.writelines("\n")
        logFile.writelines(strContents)
        logFile.close()
    else:
        logFile = open(strFilePath,"a")
        logFile.writelines("\n")
        logFile.writelines(strContents)
        logFile.close()    