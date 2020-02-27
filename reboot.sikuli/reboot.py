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
print(target["name"])

def qfinder_reboot():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()
    # find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    wait(1)
    click("1562724193568.png")
    print("click tools")
    wait(1)
    for i in range(3):
        type(Key.DOWN)
    type(Key.ENTER)
    wait(10)
    if exists("1557375692116.png"):
        print("open login window")
        flag = 1
    else:
        flag = 0
    assert flag == 1, "open login window FAIL"
    type(target["ac"])
    type(Key.TAB)
    type(target["pwd"])
    type(Key.ENTER)
    wait(5)
    if exists("1562724575751.png"):
        print("start to reboot")
        flag = "True"
    else:
        print("reboot fail")
        flag = "False"
    with open("result.txt", "w") as fp:
           fp.write(flag) 
    print("--- End " + fun_name + " ---")
    
if __name__ == "__main__":
    qfinder_reboot() 
