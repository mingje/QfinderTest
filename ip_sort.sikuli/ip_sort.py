from nas_info import *
from library import *
from socket import inet_aton, inet_ntoa
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


def qfinder_ip_sort():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    # open qfinder
    open_qfinder()
    click("1557892638363.png")
    print("click IP address field")
    wait(2)
    
    s = Region(Region(409,283,102,370))
    ip_str = s.text()
    ip_list = ip_str.splitlines()
    print("Initial list: " + str(ip_list))
    # rm space
    iplist_a = []
    for i in ip_list:
        i = i.split("(")
        i = i[0]
        q = i.replace(' ','')
        q = q.replace('l','1')
        q = q.replace('S','5')
        q = q.replace('2045','204.5')
        iplist_a.append(q)
    iplist_b = []
    for i in iplist_a:
        if i.count('.') == 3:
            iplist_b.append(i)
    iplist_c = []
    for j in iplist_b:
        k = list(j)
        flag = 0
        for f in k:
            if f.isalpha() == True:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            iplist_c.append(j)

    iplist_d = []
    for u in iplist_c:
        d = u.split(".")
        for r in d:
            if r.isdigit() == False or len(r) > 3:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            iplist_d.append(u)
    print("Switch list: " + str(iplist_d))
    print("Sorting...")
    lot = map(inet_aton, iplist_d)
    print("Sort lot")
    lot1 = map(inet_aton, iplist_d)
    print("Sort lot1")
    lot.sort()
    lot1.sort(reverse=True)
    iplist1 = map(inet_ntoa, lot)
    iplist2 = map(inet_ntoa, lot1)
    print("Sorted list: " + str(iplist1))
    print("Sorted list: " + str(iplist2))
    if iplist_d == []:
        print("list fail")
        flag = "False"
    elif iplist_d == iplist1 or iplist == iplist2:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
    print("--- End " + fun_name + " ---")

if __name__ == "__main__":
    qfinder_ip_sort()
