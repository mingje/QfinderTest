#獨立測試案例, 每個def 都是一個獨立的案例需要重新建立session
import unittest
import time
import os
from BeautifulReport import BeautifulReport
import subprocess
from PIL import ImageGrab
import sys
import library, library_db
import socket

# Declare Input Argument
Product_flag = "Qfinder"
# ProductVer_flag = "6.6.7.0613"
ProductVer_flag = sys.argv[1]
Device_flag = "Windows_PC"
DeviceOS_flag = "Win10"
DeviceOSVer_flag = "Win10_Home"
#case_list = [9]


# Mission Data
Mission_name = "RegressionTest_" + Product_flag
Sever_name = socket.gethostname()
Server_ip = library_db.getserverip()
Engineer = "StevenHsu"
Result_path = "Path"

# Record Data
device_id = 10 #"AT-VM-C1"
app_id = 14 #"Qfinder_Windows"
qpkg_name = ""
qpkg_version = ""
nas_model = ""
nas_firmware = ""


# declare report info
current_path = os.getcwd()
print(current_path)
report = os.path.join(current_path, "Report")
if not os.path.exists(report):
    os.makedirs('Report')
logfile = os.path.join(current_path, "logfile")
if not os.path.exists(logfile):
    os.makedirs('logfile')
logfile = logfile + "\\"

now = time.strftime("%Y-%m-%d~%H.%M.%S", time.localtime(time.time()))
d_path = now.split('~')
d_path_time = d_path[0]
path_time = d_path_time.split("-")
path_month = library_db.convert_month(number_month=path_time[1])
report_title = Product_flag + DeviceOS_flag + ProductVer_flag + "_" + now + ".html"
report_path1 = Product_flag + "_" + now + "/"
des = Device_flag + "_" + str(DeviceOSVer_flag)
dashboard_show_path = '/Web/MobileTest/RegressionTest/' + DeviceOS_flag + '/' + Product_flag + '/' + \
                      path_time[0] + '/' + path_month + '/' + path_time[2] + '/' + report_path1 + report_title
img_path = 'img'
image_path = os.path.join(current_path, img_path)
if not os.path.exists(image_path):
    os.makedirs('img')

# NAS info
"""
target_info_name = "AT-TS231P2"
target_info_lanip = "10.20.241.192"
target_info_ac = "admin"
target_info_pwd = "dqvts231p2"
"""
target_info_name = sys.argv[2]
target_info_lanip = sys.argv[3]
target_info_ac = sys.argv[4]
target_info_pwd = sys.argv[5]

class QfinderTest(unittest.TestCase):

    # @classmethod
    def setUp(self):
        print("start")

        start_time_list.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if result.result_list:
            library_db.update_record_starttime_to_db(record_id_list[0], start_time_list.pop(0))

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        im = ImageGrab.grab()
        im.save('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img('test001_Version_sort')
    def test001_Version_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\Version_sort.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test002_device_sort')
    def test002_device_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\device_sort.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test003_ip_sort')
    def test003_ip_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\ip_sort.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test004_mac_sort')
    def test004_mac_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\mac_sort.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test005_myqnapcloud_sort')
    def test005_myqnapcloud_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\myqnapcloud_sort.sikuli -f " + logfile\
                         + fun_name + ".txt --args "+ target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test006_name_sort')
    def test006_name_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\name_sort.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
    
    @BeautifulReport.add_test_img('test007_bookmark_sort')
    def test007_bookmark_sort(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\bookmark_sort.sikuli -d -f " + logfile\
                         + fun_name + ".txt --args " + "AT-TS231P2 AT-TVS473"
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
    
    @BeautifulReport.add_test_img('test008_detail_check')
    def test008_detail_check(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\detail_check.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
    
    @BeautifulReport.add_test_img('test009_onlineNAS_avarage')
    def test009_onlineNAS_avarage(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\onlineNAS_avarage.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test010_media_upload')
    def test010_media_upload(self):
        library.folder_clean(hostname=target_info_lanip, port=22, username=target_info_ac, password=target_info_pwd)
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\media_upload.sikuli -d -f " + logfile\
                        + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + \
                            target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
        library.folder_check(hostname=target_info_lanip, port=22, username=target_info_ac, password=target_info_pwd,
                                path="/share/Multimedia/qfinderupload/", filename="qfinderuploadfile.MP3")
    
    @BeautifulReport.add_test_img('test011_login')
    def test011_login(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\login.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test012_network_drivers')
    def test012_network_drivers(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\network_drivers.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
    
    @BeautifulReport.add_test_img('test013_shutdown')
    def test013_shutdown(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\shutdown.sikuli -d -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + \
                         target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
        library.shutdown_check(hostname=target_info_lanip, port=22, username=target_info_ac, password=target_info_pwd)
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\shutdown_UI.sikuli -d -f " + logfile + "shutdown_UI.txt --args " \
                         + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + \
                         target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test014_wakeup')
    def test014_wakeup(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\wakeup.sikuli -d -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + \
                         target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
        library.alive_check(hostname=target_info_lanip, port=22, username=target_info_ac, password=target_info_pwd)
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\wakeup_UI.sikuli -d -f " + logfile + "wakeup_UI.txt --args " \
                         + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + \
                         target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    @BeautifulReport.add_test_img('test016_reboot')
    def test016_reboot(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\reboot.sikuli -d -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + \
                         target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"
        library.reboot_check(hostname=target_info_lanip, port=22, username=target_info_ac, password=target_info_pwd)

    @BeautifulReport.add_test_img('test015_config')
    def test015_config(self):
        fun_name = sys._getframe().f_code.co_name
        sikuli_runcase = "C:\\sikuli\\runsikulix -r " + current_path + "\\config.sikuli -f " + logfile\
                         + fun_name + ".txt --args " + target_info_name + " " + target_info_lanip + " " + target_info_ac + " " + target_info_pwd
        subprocess.run(sikuli_runcase, shell=True)
        with open("result.txt", "r") as fp:
            flag = fp.read()
            print(flag)
        os.remove("result.txt")
        assert flag == "True", fun_name + " case fail"

    def tearDown(self):
        try:
            os.system("taskkill /f /im QfinderPro.exe")
        except:
            pass

        end_time_list.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        tc_index = len(result.result_list)
        if result.result_list:
            print(tc_index)
            print(result.result_list[tc_index - 1][4])
            library_db.update_record_endtime_to_db(record_id_list[0], end_time_list.pop(0))
            #library_db.update_record_nasinfo_to_db(record_id_list[0], nas_info_list.pop(0), nas_fw_list.pop(0))
            library_db.update_record_to_db(record_id_list.pop(0), result.result_list[tc_index - 1][4],
                                           result.result_list[tc_index - 1][2])

        print("close")







if __name__ == '__main__':
    suite = unittest.TestSuite()
    """
    tests = [Lan_DePortNAS_Login]  # Lan_DePortNAS_Login, Lan_NonDePortNAS_Login, tutk_DePortNAS_Login, tutk_NonDePortNAS_Login,
                                       # China_DePortNAS_Login, China_NonDePortNAS_Login, Global_DePortNAS_Login, Global_NonDePortNAS_Login
    
    tests = []
    tests_login = [Lan_DePortNAS_Login, Lan_NonDePortNAS_Login, tutk_DePortNAS_Login, tutk_NonDePortNAS_Login,
                   China_DePortNAS_Login, China_NonDePortNAS_Login, Global_DePortNAS_Login, Global_NonDePortNAS_Login,
                   Regression_Login_GlobalA, Regression_Login_GlobalB, Regression_Login_ChinaA, Regression_Login_ChinaB]
    for j in library_login.case_list:
        tests.append(tests_login[j-1])
    """

    suite.addTests(unittest.makeSuite(QfinderTest))
        #suite.addTests(unittest.makeSuite(Login2))

        #suite.addTests(unittest.makeSuite(testadd))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(yu))
    #suite = unittest.TestSuite(map(yu, tests))

    # suite.addTests(suite1)
    print(suite)
    print(suite.countTestCases())


    # 創建Mission並新增至DB
    record_count = suite.countTestCases()
    mission_id = library_db.add_mission_to_db(Mission_name, record_count, now,
                                              Sever_name, Server_ip, Engineer,
                                              Result_path)
    print("此次所新增的Mission ID 為" + str(mission_id))

    # 處理TC的用例說明及分類
    tpsuite = tuple(suite)
    list_test_case_name = []
    list_test_case_class = []
    for i in range(len(tpsuite)):
        test_case_info = str(tpsuite[i])
        test_case_name_index = test_case_info.find("(")  # test case的名稱在str內的結尾位置
        test_case_class_index_start = test_case_info.find(".")  # test case的分類在str內的開始位置
        test_case_class_index_end = test_case_info.find(")")  # test case的分類在str內的結尾位置
        list_test_case_name.insert(i, test_case_info[0:test_case_name_index - 1])
        list_test_case_class.insert(i, test_case_info[test_case_class_index_start + 1:test_case_class_index_end])

    # 先建立所有的Record，並將RecordID存入record_id_list
    description = ""
    record_id_list = []
    start_time_list = []
    end_time_list = []
    nas_info_list = []
    nas_fw_list = []
    for i in range(record_count):
        print("這是第" + str(i + 1) + "個Record")
        record_id = library_db.add_record_to_db(mission_id, device_id, app_id,
                                                ProductVer_flag, qpkg_name, qpkg_version,
                                                nas_model, nas_firmware, list_test_case_class[i],
                                                list_test_case_name[i], description, dashboard_show_path)
        record_id_list.insert(i, record_id)

    # 執行所有的Test Case
    result = BeautifulReport(suite)
    result.report(description=des, filename=report_title, log_path=report)

    # 補插入最後一筆資料
    if record_id_list:
        tc_index = len(result.result_list)
        library_db.update_mission_endtime_to_db(mission_id, end_time_list[0])
        library_db.update_record_starttime_to_db(record_id_list[0], start_time_list.pop(0))
        library_db.update_record_endtime_to_db(record_id_list[0], end_time_list.pop(0))
        library_db.update_record_to_db(record_id_list.pop(0), result.result_list[tc_index - 1][4],
                                       result.result_list[tc_index - 1][2])

        #  Path Report to Server
        report_path = current_path + '/Report/' + report_title
        dqvserver_path = '/share/Document/ATReport/RegressionTest/' + DeviceOS_flag + '/' + Product_flag + '/' + \
                         path_time[0] + '/' + path_month + '/' + path_time[2] + '/' + report_path1 + '/' + report_title
        dashboard_path = '/share/TestedResult/MobileTest/RegressionTest/' + DeviceOS_flag + '/' + Product_flag + '/' + \
                         path_time[0] + '/' + path_month + '/' + path_time[2] + '/' + report_path1 + '/' + report_title
        dashboard_web_path = '/share/Web/MobileTest/RegressionTest/' + DeviceOS_flag + '/' + Product_flag + '/' + \
                             path_time[0] + '/' + path_month + '/' + path_time[
                                 2] + '/' + report_path1 + '/' + report_title
        #  Upload DQV server
        try:
            library_db.upload_from_local_file('10.20.241.100', 'admin', 'qwerty543', 22, report_path, dqvserver_path)
        except ConnectionError as error_upload_dqv_fail:
            print("Fail to upload to DQV server")
            print(error_upload_dqv_fail)

        """
        #  Upload Dashboard server
        try:
            library_db.upload_from_local_file(library_db.host_ip, library_db.nas_username, library_db.nas_password, 22,
                                              report_path,dashboard_path)
            library_db.upload_from_local_file(library_db.host_ip, library_db.nas_username, library_db.nas_password, 22,
                                              report_path, dashboard_web_path)
        except ConnectionError as error_upload_dashboard_fail:
            print("Fail to upload to dashboard server")
            print(error_upload_dashboard_fail)
        """

    """
    result = BeautifulReport(suite)
    result.report(description=des, filename=report_title, log_path=report)

    
    #print(result.start_time)
    print(type(float(result.start_time)))
    startttime = float(result.start_time)
    print(float(result.start_time))
    #total_time = time.strftime("%H:%M:%S", time.localtime(float(result.end_time)))
    ee = result.end_time[:-2]
    ee2 = startttime + float(ee)
    print(result.begin_time)
    print(ee2)
    print(time.localtime(ee2))
    print(time.localtime())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ee2)))
    #total_time = starttime + result.end_time
    #print(total_time)
    """