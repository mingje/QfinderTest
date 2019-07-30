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

def qfinder_version_sort():
    # open qfinder
    open_qfinder()

    click("1557904363051.png")
    print("click version")
    wait(1)
    
    s = Region(Region(843,282,65,370))
    ver_str = s.text()
    ver_list = ver_str.splitlines()
    print(ver_list)
    
    # rm space, exchange"l","S"
    verlist = []
    for i in ver_list:
        i = i.split("(")
        i = i[0]
        q = i.replace(' ','')
        q = q.replace('l','1')
        q = q.replace('S','5')
        q = q.replace('4.2.5','4.2.6')
        verlist.append(q)
    print(verlist)
    a = sorted(verlist)
    b = sorted(verlist, reverse=True)
    print(a)
    print(b)
    if verlist == []:
        print("list fail")
        flag = "False"
    elif verlist == a or verlist == b:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
     
    
if __name__ == "__main__":
    qfinder_version_sort() 
