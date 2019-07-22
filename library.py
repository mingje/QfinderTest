import mysql.connector
import time
import datetime
import paramiko
import os
from stat import S_ISDIR as isdir


class Parameter:
    def __init__(self, product, product_ver, device):
        self.Product_flag = product
        self.ProductVer_flag = product_ver
        self.Device_flag = device

def shutdown_check(hostname, port, username, password):
    flag = 0
    for i in range(10):
        time.sleep(30)
        try:
            t = paramiko.Transport(hostname, port)
            t.connect(username, password)
            sftp = paramiko.SFTPClient.from_transport(t)
            t.close()
            print("NAS alive")
            flag = 0
        except:
            print("NAS disconnect")
            flag = 1
            break
    assert flag == 1, "NAS shutdown fail"


def alive_check(hostname, port, username, password):
    flag = 0
    for i in range(20):
        time.sleep(30)
        try:
            t = paramiko.Transport(hostname, port)
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            t.close()
            print("NAS alive")
            flag = 1
            break
        except:
            print("NAS disconnect")
            flag = 0
    assert flag == 1, "NAS power on fail"

def reboot_check(hostname, port, username, password):
    flag = 0
    for i in range(10):
        time.sleep(30)
        try:
            t = paramiko.Transport(hostname, port)
            t.connect(username, password)
            sftp = paramiko.SFTPClient.from_transport(t)
            t.close()
            print("NAS alive")
            flag = 0
        except:
            print("NAS disconnect")
            flag = 1
            break
    assert flag == 1, "NAS shutdown fail"

    flag = 0
    for i in range(20):
        time.sleep(30)
        try:
            t = paramiko.Transport(hostname, port)
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            t.close()
            print("NAS alive")
            flag = 1
            break
        except:
            print("NAS disconnect")
            flag = 0
    assert flag == 1, "NAS power on fail"

def folder_clean(hostname, port, username, password):
    t = paramiko.Transport(hostname, port)
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    po = "/share/Multimedia/qfinderupload/"
    po1 = "/share/Multimedia/qfinderupload/.@__thumb/"
    po2 = "/share/Multimedia/qfinderupload/.@__thumb/transcode/"
    po_list = [po2, po1, po]
    for i in po_list:
        try:
            a = sftp.listdir(i)
            for j in a:
                rr = i + j
                try:
                    sftp.remove(rr)
                except:
                    pass
            sftp.rmdir(i)
        except:
            pass
    try:
        sftp.listdir(po)
        flag = 0
    except:
        flag = 1
    t.close()
    assert flag == 1, "clean folder fail"
"""
hostname = "10.20.241.192"
port = 22
username = "admin"
password = "dqvts231p2"

t = paramiko.Transport(hostname, port)
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
po = "/share/Multimedia/qfinderupload/"
po1 = "/share/Multimedia/qfinderupload/.@__thumb/"
po2 = "/share/Multimedia/qfinderupload/.@__thumb/transcode/"
po_list = [po2, po1, po]
for i in po_list:
    try:
        a = sftp.listdir(i)
        for j in a:
            rr = i + j
            try:
                sftp.remove(rr)
            except:
                pass
        sftp.rmdir(i)
    except:
        pass
hh = sftp.listdir("/share/Multimedia/qfinderupload/")
print(hh)
t.close()
"""
#folder_clean(hostname="10.20.241.192", port=22, username="admin", password="dqvts231p2", path="/share/Multimedia/qfinderupload/")

"""
# command line
# date +%Y/%m/%d 查詢日期
# /bin/hostname 查詢 device name
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允許連線不在know_hosts檔案中的主機
ssh.connect(hostname=hostname,port=port,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command("/bin/hostname") #遠端執行shell命令
print(stdout.readlines()) #輸出回顯結果

ssh.close()

hostname = "10.20.241.192"
port = 22
username = "admin"
password = "dqvts231p2"
"/share/Multimedia/qfinderupload/"
"bb.png"
"""


def folder_check(hostname, port, username, password, path, filename):
    t = paramiko.Transport(hostname, port)
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    a = sftp.listdir(path=path)
    print(a)
    data_full = filename
    data_name = data_full.split(".")
    data_type = data_name[-1]
    del data_name[-1]
    delimiter = "."
    file_title = delimiter.join(data_name)
    file_name_list = [data_full]
    for j in range(2):
        file_name = file_title + " (" + str(j+1) + ")." + data_type
        file_name_list.append(file_name)
    print(file_name_list)
    # file_name2 = x + " (2).MP3"
    check_list = []
    for i in file_name_list:
        if i in a:
            check_list.append("P")
        else:
            check_list.append("F")
    print(check_list)
    if check_list == ["P", "P", "F"]:
        print("Files check pass")
        flag = 1
    else:
        print("Files check fail")
        flag = 0
    t.close()
    assert flag == 1, "Files check fail"
