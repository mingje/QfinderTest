from nas_info import *
from library import *

Settings.OcrTextSearch = True
Settings.OcrTextRead = True
import sys
"""
nas_name = "AT-TVS473"
nas_lanip1 = "10.20.241.197"
nas_ac = "admin"
nas_pwd = "dqvtvs473"
"""
nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]

target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)

def qfinder_device_sort():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()
    click("1557978035944.png")
    print("click device type field")
    wait(1)
    
    s = Region(Region(786,280,119,373))
    device_str = s.text()
    device_list = device_str.splitlines()
    print("Initial list: " + str(device_list))
    check_list = ['TS','TVS','D2 Pro','ES1640dc','HS','Mustang','QGenie','QWU',
            'TBS','TES','TDS','QuCPE','NAS','vQTS','QSW','QGD']
    # rm space
    devicelist = []
    for i in device_list:
        q = replace_str(i,'l','1','SS1','551','4S3','453','T5','TS','TV5',
                'TVS','IVS','TVS','"','',' ','','Pro',' Pro','~','-',
                'QuCPE-3010\xe2\x80\x94IPT','QUCPE-3010-IPT')
        g = q.split("-")
        g = g[0]
        if g in check_list:
            devicelist.append(q)
        else:
            print("drop item")
    print("Switch list: " + str(devicelist))
    a = sorted(devicelist,key=str.lower)
    b = sorted(devicelist, reverse=True, key=str.upper)
    print("Sorted list: " + str(a))
    print("Sorted list: " + str(b))
    if devicelist == []:
        print("list fail")
        flag = "False"
    elif devicelist == a or devicelist == b:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
    print("--- End " + fun_name + " ---")
    
if __name__ == "__main__":
    qfinder_device_sort()