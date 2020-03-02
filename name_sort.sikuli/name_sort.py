from nas_info import *
from library import *
Settings.OcrTextSearch = True
Settings.OcrTextRead = True
import sys

nas_name = sys.argv[1]
nas_lanip1 = sys.argv[2]
nas_ac = sys.argv[3]
nas_pwd = sys.argv[4]
"""
nas_name = "AT-TVS473"
nas_lanip1 = "10.20.241.197"
nas_ac = "admin"
nas_pwd = "dqvtvs473"
"""
target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)

device_list = ['Aloma-TVS682T','Aloma-TVS871t1','Andy-TS253B','Andy-TS453A','Andy-TVS463',
        'AT-TS231P2','AT-TS253BE','AT-TS432XU','AT-TVS473','AT-TS453BT3','AT-TS677-A', 
        'AT-TS677-B','Chehung1277','Chehung431XU','Chehung453A','Chehung671','Chehung-8080', 
        'Chehung-963X','DQVServer','Erin-131p','Erin-451A','ERIN-871T','ERIN-882ST','ERIN-1282T3'
        'Erin-Q451','Erin-TS253B','XS62-QVR-Pro','XS62-Pfsense','TS253B-Kira','Roy-TS451',
        'Roy-TS431X2','Roy-TS332X','Roy-TS253B','Roy-TBS453A','RoyHsu-QWU100-2','RoyHsu-QWU100-1',
        'RoyHsu-882ST','RoyHsu682T',"RexTS831X",'Rex-TS431','Rex-TS253Pro','Rex-TS253B-02', 
        'Rex-TS253B','RexTS228A','RoyHsu-670PRO','Rex-VM2TS1277','Rex-TS832X','rexTS470',
        'AT-Hero473','ATQsyncTS1277','ATQsyncTs253b','ATQsyncTVS871T','ATQsyncTVS882','TS451',
        'Roy-QWU01','Roy-QNE3','Roy-QNE1','RoyHsu-NC-Auto','RoyHsu-670Pro','Roy-682T','RexTVS871T']

def qfinder_name_sort():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()
    
    click("1557885931619.png")
    print("click name field")
    wait(1)
    name_region = Region(Region(51,282,232,372))
    name_str = name_region.text()
    current_name_list = name_str.splitlines()
    print("Initial list: " + str(current_name_list))
    # rm space
    d = []
    for i in current_name_list:
        q = i.replace(' ','')
        d.append(q)
    print(d)
    correct_list = []
    for a in d:
        b = a.replace('l','1')
        c = a.replace('T5','TS')
        if a in device_list:
            q = a.replace('-','')
            correct_list.append(q)
        elif b in device_list:
            q = b.replace('-','')
            correct_list.append(q)
        elif c in device_list:
            q = c.replace('-','')
            correct_list.append(q)
        else:
            print("not in list")
    print("Switch list: " + str(correct_list))
    a = sorted(correct_list,key=str.lower)
    b = sorted(correct_list, reverse=True, key=str.upper)
    print("Sorted list: " + str(a))
    print("Sorted list: " + str(b))
    if a == [] or correct_list == []:
        print("list fail")
        flag = "False"
    elif correct_list == a or correct_list == b:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
    print("--- End " + fun_name + " ---")

if __name__ == "__main__":
     qfinder_name_sort()