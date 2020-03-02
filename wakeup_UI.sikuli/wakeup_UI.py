from nas_info import *
from library import *

Settings.OcrTextSearch = True
Settings.OcrTextRead = True
import sys
nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]
target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)
print("Target is: " + target["name"])

def qfinder_wakeup_UI():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    for i in range(6):
        wait(60)
        click("1557739083182.png")
        print("click refresh button")
        wait_please(loop=10, time=10)
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    # login to open web page
    if login_open_web() == "True":
        print("wake up PASS")
        flag = "True"
    else:
        print("wake up FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
        fp.write(flag) 
    print("--- End " + fun_name + " ---")
    
if __name__ == "__main__":
    qfinder_wakeup_UI()