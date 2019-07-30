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

def login_open_web():     
    # open qfinder
    open_qfinder()
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    wait(1)
    click("1557309643274.png")
    print("click login button")
    wait(10)
    if exists("1557309257444.png"):
        print("Min window")
        click("1557309257444.png")
    elif exists("1557309306602.png"):
        print("Max window")
    else:
        pass
    
    wait(5)
    if exists("1557310210160.png"):
       print("Open web page1")
       flag = "True"
    elif exists("1557310336279.png"):
       print("Open web page2")
       flag = "True"
    elif exists("1562579603836.png"):
       print("Open web page3")
       flag = "True"
    elif exists("1562561110248.png"):
       print("Open web page4")
       flag = "True"
    elif exists("1562561186884.png"):
       print("Open web page5")
       flag = "True"
    elif exists("1557798873195.png"):
            
       msg_region = Region(Region(413,247,453,186))
       msg_region.click("1557798940520.png")
       print("Open web page FAIL1")
       flag = "False"
    else:   
       print("Open web page FAIL2")
       flag = "False"
    print(flag)
    """
    if flag == 1:
        region_text = get_region_text(200, 36, 214, 69)
        print(region_text)
        region_text = region_text.split("/")
        region_text = region_text[2]
        region_text = region_text.split(":")
        print(region_text[0])
        if region_text[0] == target["lanip1"]:
            rflag = "True"
        else:
            rflag = "False"
    else:
        rflag = "False"
    """
    try:
        closeApp("chrome")
        print("close chrome")
    except:
        pass
    with open("result.txt", "w") as fp:
        fp.write(flag)

if __name__ == "__main__":
    login_open_web() 