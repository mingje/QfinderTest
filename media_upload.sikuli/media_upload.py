from nas_info import *
from library import *
import os

Settings.OcrTextSearch = True
Settings.OcrTextRead = True
import sys
nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]
target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)
print(target)

def qfinder_media_upload():
    # open qfinder
    open_qfinder()
    
    #  find target NAS
    find_target_nas(name = target["name"], lanip1 = target["lanip1"])
    
    
    click("1560414427699.png")
    for i in range(3):
        wait(3)
        if exists("1557375692116.png"):
            print("open login window")
            flag = 1
            break
        else:
            flag = 0
    assert flag == 1, "open login window FAIL"
    type("admin")
    type(Key.TAB)
    type("dqvts231p2")
    type(Key.ENTER)
    for i in range(3):
        wait(10)
        if exists("1560414599541.png"):
            flag = 1
            print("Open media upload pass")
            break
        else:
            flag = 0
    assert flag == 1, "Open media upload error"
    
    result_list = []
    if upload_action(uploadfile = "C:\UtilityAuto\Qfinder_test\qfinderupload\qfinderuploadfile.MP3", up_policy = "skip") == 1:
        result_list.append("P")
    else:
        result_list.append("F")
    if upload_action(uploadfile = "C:\UtilityAuto\Qfinder_test\qfinderupload\qfinderuploadfile.MP3", up_policy = "rename") == 1:
        result_list.append("P")
    else:
        result_list.append("F")
    if "F" in result_list:
        print("upload FAIL")
        flag = "False"       
    else:
        flag = "True"
        print("upload PASS")
    with open("result.txt", "w") as fp:
       fp.write(flag) 
    os.system("taskkill /f /im QfinderUpload.exe")
    
if __name__ == "__main__":
    qfinder_media_upload() 


