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
print(target)

def qfinder_shutdown():
    # open qfinder
    open_qfinder()
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    wait(1)
    click("1557736549093.png")
    for i in range(4):
        type(Key.DOWN)
    type(Key.ENTER)
    wait(1)
    if exists("1557375692116.png"):
        print("open login window")
    else:       
        print("open login window FAIL") 
    type(target["ac"])
    type(Key.TAB)
    type(target["pwd"])
    type(Key.ENTER)
    wait(3)
    if exists("1557743664241.png"):
        print("start to shutdown")
        flag = "True"
        msg_region = Region(Region(481,270,320,138))
        msg_region.click("1557743776764.png")
    else:
        print("Fail to start shutdown")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 

if __name__ == "__main__":
    qfinder_shutdown() 
    


