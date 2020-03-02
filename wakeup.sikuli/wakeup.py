from nas_info import *
from library import *
import sys

Settings.OcrTextSearch = True
Settings.OcrTextRead = True
import sys
nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]
target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)
print("Target is: " + target["name"])

def qfinder_wakeup():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    wait(1)
    click("1557738314329.png")
    print("Click wake up button in main")
    click("1557738402951.png")
    print("Click wake up button in window")
    wait(2)
    if exists("1557738424305.png"):
        print("Show wake up dia")
        msg_region = Region(Region(422,263,437,153))
        msg_region.click("1557738454499.png")
        msg_region = Region(Region(408,71,464,537))
        msg_region.click("1557738921336.png")
        print("close wake up window")
        print("start to wakeup")
        flag = "True"
    else:
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
    print("--- End " + fun_name + " ---")

if __name__ == "__main__":
    qfinder_wakeup()

    
                
    
