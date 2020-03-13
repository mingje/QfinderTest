from nas_info import *
from library import *

Settings.OcrTextSearch = True
Settings.OcrTextRead = True

import sys

nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]
nas_qid = sys.argv[5]
"""
nas_name = "AT-TVS473"
nas_lanip1 = "10.20.241.197"
nas_ac = "admin"
nas_pwd = "dqvtvs473"
nas_qid = "jj932.myqnapcloud.com"
"""
target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd, qid = nas_qid)
print("Target is: " + target["name"])

def qfinder_config():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()
    for i in range(2):
        wait(5)
        click("1557739083182.png")
        wait_please(loop=10, time=10)
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"], qid = target["qid"])
    
    # enter config page
    enter_config(ac = target["ac"], pwd = target["pwd"])
    
    
    # get text
    #region_text = get_region_text(438,161,264,17)
    wait(1)
    click(Pattern("1560505851866.png").similar(0.90).targetOffset(-23,0))
    wait(1)
    type("a", KeyModifier.CTRL)
    type("c", KeyModifier.CTRL)
    wait(1)
    region_text = Env.getClipboard().strip()
    print(region_text)
    assert region_text == "TARGETNAS", "device name display error"
    
    type("ATtest")
    wait(1)
    click("1560507514764.png")
    wait(1)
    click("1560504550140.png")
    wait(1)
    click("1560504580263.png")
    wait(1)
    
    s = Region(444,245,96,15)
    ee = s.text()
    print(ee)
    cc = ee.split("/")
    print(cc)
    kk = []
    for i in range(3):
        d = cc[i]
        d = d.replace(' ','')
        print(d)
        kk.append(d)
    delimiter = "/"
    file_title = delimiter.join(kk)
    print(file_title)
    wait(1)
    
    click("1560739387095.png")
    wait(1)
    click(Pattern("1560739454769.png").targetOffset(99,0))
    type(target["pwd"])
    for i in range(2):
        wait(1)
        type(Key.TAB)
        wait(1)
        type("ATtest")
    wait(1)
    
    click("1557313968028.png")
    for i in range(10):
        try:    
            wait_please(loop = 50,time = 2)
            find("1561631482832.png")
            click("1557314077398.png")
            wait(3)
            find("1557314046874.png")
            click("1557314077398.png")
            flag = 1
            break
        except:
            flag = 0
    assert flag == 1, "Change config FAIL"
    wait(1)
    # refresh list
    for i in range(2):
        click("1557314271456.png")
        wait_please(loop=50, time=2)
    click("1557376974013.png")
    
    #  find target NAS
    find_target_nas(name = "ATtest", lanip1 = target["lanip1"], qid = target["qid"])
    # enter config page
    enter_config(ac = target["ac"], pwd = "ATtest")
    
    # get text
    wait(1)
    click(Pattern("1560505851866.png").similar(0.90).targetOffset(-23,0))
    wait(1)
    type("a", KeyModifier.CTRL)
    type("c", KeyModifier.CTRL)
    wait(1)
    region_text = Env.getClipboard().strip()
    print(region_text)
    assert region_text == "ATtest", "device name display error"
    
    type("TARGETNAS")
    wait(1)
    click("1560739387095.png")
    wait(1)
    click(Pattern("1560739454769.png").targetOffset(99,0))
    type("ATtest")
    for i in range(2):
        wait(1)
        type(Key.TAB)
        type(target["pwd"])
    wait(1)
    click("1557313968028.png")
    flag = "False"
    for j in range(10):
        try:    
            wait_please(loop = 50,time = 2)
            find("1561631482832.png")
            click("1557314077398.png")
            wait(3)
            find("1557314046874.png")
            click("1557314077398.png")
            flag = "True"
            break
        except:
            flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
    print("--- End " + fun_name + " ---")

    """
    # refresh list
    click("1557314271456.png")
    wait_please(loop = 10,time = 10)
    """

if __name__ == "__main__":
    qfinder_config()
