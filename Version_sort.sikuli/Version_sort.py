from nas_info import *
from library import *
import sys

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

def qfinder_version_sort():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()

    click("1557904363051.png")
    print("click version field")
    wait(1)
    s = Region(Region(909,283,78,372))
    ver_str = s.text()
    ver_list = ver_str.splitlines()
    print("Initial list: " + str(ver_list))
    
    # rm space, exchange"l","S"
    verlist = []
    for i in ver_list:
        i = i.split("(")
        i = i[0]
        q = i.replace(' ','')
        q = q.replace('l','1')
        q = q.replace('S','5')
        q = q.replace('4.2.5','4.2.6')
        q = q.replace('1.o.1','1.0.1')
        q = q.replace('o.o.1','0.0.1')
        q = q.replace('0175','q175')
        q = q.replace('q175I','q175')
        q = q.replace('0193I','q193')
        verlist.append(q)
    print("Switch list: " + str(verlist))
    a = sorted(verlist)
    b = sorted(verlist, reverse=True)
    print("Sorted list: " + str(a))
    print("Sorted list: " + str(b))
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
    print("--- End " + fun_name + " ---")
     
    
if __name__ == "__main__":
    qfinder_version_sort() 
