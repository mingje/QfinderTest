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

def qfinder_network_driver():
    # open qfinder
    open_qfinder()
    click("1557739083182.png")
    print("click refresh button")
    wait_please(loop=10, time=10)
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    wait(1)

    click("1557391119673.png")
    print("click network drivers button")
    wait(10)
    if exists("1557390582065.png"):
        type(target["ac"])
        type(Key.TAB)
        type(target["pwd"])
        type(Key.ENTER)
        wait(5)
    else:
        pass
    
    if exists(Pattern("1557390790842.png").similar(0.80)):
        click(Pattern("1557390790842.png").similar(0.80))
        print("max window")
        wait(2)
        a = Region(Region(95,1,83,17))
        t = a.text()
        if t == target["lanip1"]:
            print("open network drivers PASS")        
            flag = "True"
        else:
            flag = "False"
        click(Pattern("1562739261310.png").similar(0.80))
        
    elif exists("1557473815093.png"):
        print("open network drivers FAIL")
        flag = "False"
    else:
        flag = "False"
    
    with open("result.txt", "w") as fp:
       fp.write(flag) 

if __name__ == "__main__":
    qfinder_network_driver() 
