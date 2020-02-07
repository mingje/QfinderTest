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

def qfinder_bookmark():
    # open qfinder
    open_qfinder()
    #  find target NAS
    if find_target_nas(name = target["name"], lanip1 = target["lanip1"]) == 1:
        bookmark_target = target['icon_highlight']
    else:
        print("Find NAS FAIL")
    picture = find(bookmark_target)
    picture_x = picture.getX()
    print(picture_x)
    picture_y = picture.getY()
    print(picture_y)
    bookmark_region = Region(picture_x-45,picture_y-5,45,28)
    lo = Location(picture_x-45,picture_y-5)
    hover(lo)
    if bookmark_region.exists("1557832935307.png"):   
        print("Bookmark PASS")
        flag = "True"
    else:
        print("Bookmark FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 

if __name__ == "__main__":
    qfinder_bookmark() 


