from google.oauth2.service_account import Credentials
from datetime import datetime, timezone,timedelta
import gspread
def get_timer():
    # Khai báo scope chỉ đọc metadata của Drive
    SCOPES = ['https://www.googleapis.com/auth/drive']
    # Đọc credentials
    creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    # Tạo service Drive API
    gc = gspread.authorize(creds)
    # ID của file Google Sheet từ link
    file_ids = '15BVZr_7D8mwvqgqC88pq1pN9WOjqz4Bn61U7wWO4J_s'
    # Mở bảng tính theo ID
    sh = gc.open_by_key(file_ids)
    # Chọn sheet "log"
    worksheet = sh.worksheet("log")
    # Đọc các ô A1, A2, A3
    mt = worksheet.acell('A1').value
    bz = worksheet.acell('A2').value
    fl = worksheet.acell('A3').value
    print("A1:", mt)
    print("A2:", bz)
    print("A3:", fl)
    return mt,bz,fl