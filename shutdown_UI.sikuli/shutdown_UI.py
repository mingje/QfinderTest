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

def qfinder_shutdown_UI():    
    for i in range(6):
        wait(60)
        click("1557799685522.png")
        wait_please(loop=10, time=10)
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    wait(1)
    click("1557737668421.png")
    wait(10)
    if exists("1557737704530.png"):
        print("shutdown PASS")
        flag = "True"
    else:
        print("shutdown FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 


if __name__ == "__main__":
    qfinder_shutdown_UI() 
