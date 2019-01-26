# -*- coding: utf-8 -*-
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os

#google_drive認証処理
def Authentication():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

# google_drive_一覧表示 
def display(brive):
    display = []
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    for f in file_list:
        display.append('title: %s, id: %s' % (f['title'], f['id']))
    return display

#ローカルにあるcsvファイルをgoogle_drive上にアップロード
def upload(drive):
    csv_file = []
    path = os.getcwd()
    os.chdir(path)
    csv = glob.glob(path+"/*.csv")
    for csv_data in csv:
        csv_file.append(csv_data.strip(path))
    print (csv_file)
    for dt in csv_file:
        file2 = drive.CreateFile()
        file2.SetContentFile(dt)
        file2.Upload()
    return 'upload_complete'

#google_drive上にあるcsvファイルの削除
def delete(drive):
    T_data = []
    I_data = []
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    for f in file_list:
        T_data.append('%s' % (f['title']))
        I_data.append('%s' % (f['id']))
        print('title: %s, id: %s' % (f['title'], f['id']))
    print('T_data', T_data)
    print('I_data', I_data)
    for df in I_data:
        # リストに格納されたCSVファイルIDを使用してGoogle_driveのファイルを削除
        delete_object = df
        file_delete = drive.CreateFile({'id': delete_object})
        file_delete.Delete()
    return 'delete_complete'

# 指定したIDのデータをダウンロード
def download(drive):
    T_data = []
    I_data = []
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    for f in file_list:
        T_data.append('%s' % (f['title']))
        I_data.append('%s' % (f['id']))
        print('title: %s, id: %s' % (f['title'], f['id']))
    print('T_data', T_data)
    print('I_data', I_data)
    
    for If in range(len(T_data)):
        # リストに格納されたCSVファイルIDを使用してGoogle_driveのファイルを削除
        Import_object = I_data[If]
        file_import = drive.CreateFile({'id': Import_object})
        file_import.GetContentFile(T_data[If])
    return 'import_complete'

def data():
    drive = Authentication()
    status = delete(drive)
    print(status)
    status = upload(drive)
    print(status)


if __name__ == '__main__':
    drive = Authentication()
    #p = upload(drive)
    #p = test(drive)
    p = data()
    print (p)