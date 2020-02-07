import mysql.connector
import time
import datetime
import paramiko
import os
import socket
from stat import S_ISDIR as isdir


host_ip = "10.64.101.252"
nas_username = "admin"
nas_password = "qtp321"
username = "root"
password = "admin"

dqv_dashboard_db = mysql.connector.connect(
    host=host_ip,
    user=username,
    passwd=password,
    database="AutoTools_TestResult"
)


def add_mission_to_db(mission_name, record_count, start_time, server_name, server_ip, engineer, result_path):

    # Add New Mission to Mission Table
    mycursor = dqv_dashboard_db.cursor()
    db_add_new_mission = "INSERT INTO Mission (MissionName, ToolID, isDailyMission, NASCount, StartTime, " \
                         "EndTime, ServerName, ServerIP, Engineer, ResultPath) " \
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mission_info = (mission_name, 16, 0, record_count, start_time, "0000-00-00 00:00:00", server_name, server_ip,
                    engineer, result_path)
    mycursor.execute(db_add_new_mission, mission_info)
    mission_id = mycursor.lastrowid
    print("插入的Mission ID:", mission_id)
    dqv_dashboard_db.commit()
    mycursor.close()
    return mission_id


def add_record_to_db(mission_id, device_id, app_id, app_version, qpkg_name, qpkg_version,
                     nas_model, nas_firmware, classification, case_summary, description, result_path):

    # Add New Record to MobileTestRecords Table
    mycursor = dqv_dashboard_db.cursor()
    db_add_new_record = "INSERT INTO MobileTestRecords (MissionID, DeviceID, AppID, AppVersion, QpkgName," \
                        "QpkgVersion, NASModel, NASFirmware, Classification, " \
                        "CaseSummary, Result, Description, ResultPath) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    record_info = (mission_id, device_id, app_id, app_version, qpkg_name, qpkg_version, nas_model,
                   nas_firmware, classification, case_summary, "Waiting", description, result_path)
    mycursor.execute(db_add_new_record, record_info)
    record_id = mycursor.lastrowid
    print("插入的Record ID:", record_id)
    dqv_dashboard_db.commit()
    mycursor.close()
    return record_id


def update_record_to_db(record_id, result, description):

    # Update Result to exist record
    mycursor = dqv_dashboard_db.cursor()
    db_update_record = "UPDATE MobileTestRecords SET Result=%s, Description=%s WHERE RecordID=%s;"
    record_update = (result, description, record_id)
    mycursor.execute(db_update_record, record_update)
    dqv_dashboard_db.commit()


def update_record_nasinfo_to_db(record_id, nas_model, nas_fw):

    # Update NAS Info to exist record
    mycursor = dqv_dashboard_db.cursor()
    db_update_end_record = "UPDATE MobileTestRecords SET NASModel=%s, NASFirmware=%s WHERE RecordID=%s;"
    record_update_nasinfo = (nas_model, nas_fw, record_id)
    mycursor.execute(db_update_end_record, record_update_nasinfo)
    dqv_dashboard_db.commit()


def update_record_starttime_to_db(record_id, start_time):

    # Update start time to exist record
    mycursor = dqv_dashboard_db.cursor()
    db_update_start_record = "UPDATE MobileTestRecords SET StartTime=%s WHERE RecordID=%s;"
    record_update_start = (start_time, record_id)
    mycursor.execute(db_update_start_record, record_update_start)
    dqv_dashboard_db.commit()


def update_record_endtime_to_db(record_id, end_time):

    # Update End time to exist record
    mycursor = dqv_dashboard_db.cursor()
    db_update_end_record = "UPDATE MobileTestRecords SET EndTime=%s WHERE RecordID=%s;"
    record_update_end = (end_time, record_id)
    mycursor.execute(db_update_end_record, record_update_end)
    dqv_dashboard_db.commit()


def update_mission_endtime_to_db(mission_id, end_time):

    # Update End time to exist mission
    mycursor = dqv_dashboard_db.cursor()
    db_update_end_mission = "UPDATE Mission SET EndTime=%s WHERE MissionID=%s;"
    mission_update_end = (end_time, mission_id)
    mycursor.execute(db_update_end_mission, mission_update_end)
    dqv_dashboard_db.commit()



def count_time(start_time, elapsed_time):

    # Count End time
    tick_start = time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))
    print(tick_start)
    tick_end = tick_start + float(elapsed_time)
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tick_end))
    return end_time


def getdeviceinfo(devicename):

    # Get device id from database
    mycursor = dqv_dashboard_db.cursor()
    db_getdeviceinfo = "SELECT * FROM MobileDeviceInfo WHERE ModelName=%s;"
    mycursor.execute(db_getdeviceinfo, (devicename, ))
    result = mycursor.fetchall()

    try:
        device_info = result[0]  # Check if the list is empty
        return device_info
    except IndexError as error_msg:
        print("Can not find [" + devicename + "] in database")
        print(error_msg)
        pass


def getappid(appname):

    # Get app id from database
    mycursor = dqv_dashboard_db.cursor()
    db_getappid = "SELECT AppID FROM MobileAppInfo WHERE AppName=%s;"
    mycursor.execute(db_getappid, (appname, ))
    result = mycursor.fetchall()

    try:
        app_id = result[0][0] # Check if the list is empty
        return app_id
    except IndexError as error_msg:
        print("Can not find [" + appname + "] in database")
        print(error_msg)
        pass

def getserverip():
    sever_name = socket.gethostname()
    server_ip = socket.gethostbyname_ex(sever_name)

    for item in server_ip[2]:
        if item.find('10.20') == False:
            return item
    print("Not Found Correct Server IP")
    return server_ip[2][0]


#-----------------File Management-----------------------

def upload_from_local(hostname, username, password, port, local_dir, remote_dir):

    if local_dir == 'de':
        current_path = os.getcwd()
        current_path = current_path + '/' + 'ATtest/'
        local_dir = current_path
    else:
        local_dir = local_dir
    try:
        t = paramiko.Transport(hostname, port)
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print ('upload file start %s' % datetime.datetime.now())
        for root, dirs, files in os.walk(local_dir):
            for filespath in files:
                local_file = os.path.join(root, filespath)
                a = local_file.replace(local_dir, '')
                remote_file = os.path.join(remote_dir, a)
                try:
                    sftp.put(local_file, remote_file)
                except Exception:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                print ("upload %s to remote %s" % (local_file, remote_file))
            for name in dirs:
                local_path = os.path.join(root, name)
                a = local_path.replace(local_dir, '')
                remote_path = os.path.join(remote_dir, a)
                try:
                    sftp.mkdir(remote_path)
                    print ("mkdir path %s" % remote_path)
                except Exception:
                    print("Exist")
        print('upload file success %s ' % datetime.datetime.now())
        t.close()
        flag = 1
    except Exception:
        print("error")
        flag = 0
    assert flag == 1, 'Upload fail'


def upload_from_local_file(hostname, username, password, port, local_dir, remote_dir):

    # upload_from_local_file
    try:
        t = paramiko.Transport(hostname, port)
        t.connect(username=username, password=password)
    except ConnectionError as error_connect:
        print("Fail to establish connection with" + hostname)
        print(error_connect)

    sftp = paramiko.SFTPClient.from_transport(t)
    path1 = remote_dir.split('/')
    del path1[-1]
    a = ''
    for i in path1:
        if i == '':
            pass
        else:
            i = '/' + i
            a = a + i
            try:
                sftp.listdir(a)
            except:
                sftp.mkdir(a)
    sftp.put(local_dir, remote_dir)


def down_from_remote(host_name, user_name, password, port, remote_dir_name, local_dir_name):
    if local_dir_name == 'de':
        current_path = os.getcwd()
        current_path = current_path + '/' + 'ATtest/'
        local_dir_name = current_path
    else:
        local_dir_name = local_dir_name
    """遠程下載文件"""
    t = paramiko.Transport(host_name, port)
    t.connect(username=user_name, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    remote_file = sftp.stat(remote_dir_name)
    if isdir(remote_file.st_mode):
        # 文件夾，不能直接下載，需要繼續循環
        check_local_dir(local_dir_name)
        print('開始下載資料夾1：' + remote_dir_name)
        for remote_file_name in sftp.listdir(remote_dir_name):
            sub_remote = os.path.join(remote_dir_name, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            sub_local = os.path.join(local_dir_name, remote_file_name)
            sub_local = sub_local.replace('\\', '/')
            down_from_remote(host_name, user_name, password, port, sub_remote, sub_local)
    else:
        # 文件，直接下載
        print('開始下載文件2：' + remote_dir_name)
        sftp.get(remote_dir_name, local_dir_name)
    t.close()


def check_local_dir(local_dir_name):
    """本地文件是否存在，不在則創建"""
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)

#-----------------File Path Related-----------------------

def convert_month(number_month):

    # Convert Numbers to Month Name
    if number_month == '01':
        month_name = 'Jan'
    elif number_month == '02':
        month_name = 'Feb'
    elif number_month == '03':
        month_name = 'Mar'
    elif number_month == '04':
        month_name = 'Apr'
    elif number_month == '05':
        month_name = 'May'
    elif number_month == '06':
        month_name = 'Jun'
    elif number_month == '07':
        month_name = 'Jul'
    elif number_month == '08':
        month_name = 'Aug'
    elif number_month == '09':
        month_name = 'Sep'
    elif number_month == '10':
        month_name = 'Oct'
    elif number_month == '11':
        month_name = 'Nov'
    elif number_month == '12':
        month_name = 'Dec'
    else:
        month_name = 'Error Month Input'

    return month_name
