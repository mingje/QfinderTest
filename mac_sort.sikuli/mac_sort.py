from nas_info import *
from library import *

Settings.OcrTextSearch = True
Settings.OcrTextRead = True
import sys
"""
nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]
"""
nas_name = "AT-TVS473"
nas_lanip1 = "10.20.241.197"
nas_ac = "admin"
nas_pwd = "dqvtvs473"

target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)
print(target)

def qfinder_mac_sort():
    # open qfinder
    open_qfinder()
    click("1557911466975.png")
    wait(1)
    
    s = Region(Region(1030,282,132,373))
    mac_str = s.text()
    mac_list = mac_str.splitlines()
    print(mac_list)
    # rm space, exchange"l","S"
    maclist = []
    for i in mac_list:
        i = i.split("(")
        i = i[0]
        q = replace_str(i,'O0','00','SE','5E','OB','0B','OE','0E','O8','08','OA','0A',
                'U4','04','O7','07','DA','0A','D0','00','ZA','2A','OF','0F','S','5',
                'OC','0C','O4','04','O2','02','~','-',' ','','98','9B','O3','07','OD','0D')
        if len(q) == 17 and q.count('-') == 5:
            maclist.append(q)
        else:
            print("drop item")
    print(maclist)
    a = sorted(maclist,key=str.lower)
    b = sorted(maclist, reverse=True, key=str.upper)
    print(a)
    print(b)
    if maclist == []:
        print("list fail")
        flag = "False"
    elif maclist == a or maclist == b:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 


if __name__ == "__main__":
    qfinder_mac_sort() 