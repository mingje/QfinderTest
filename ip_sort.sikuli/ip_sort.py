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
target = nas_detail(name = nas_name, lanip1 = nas_lanip1, ac = nas_ac, pwd = nas_pwd)
print(target)

def qfinder_ip_sort():
    # open qfinder
    open_qfinder()
    click("1557892638363.png")
    wait(1)
    
    s = Region(Region(409,283,102,370))
    ip_str = s.text()
    ip_list = ip_str.splitlines()
    print(ip_list)
    # rm space
    iplist = []
    for i in ip_list:
        i = i.split("(")
        i = i[0]
        q = i.replace(' ','')
        q = q.replace('l','1')
        q = q.replace('S','5')
        iplist.append(q)
    print(iplist)
    lot = map(inet_aton, iplist)
    lot1 = map(inet_aton, iplist)
    lot.sort()
    lot1.sort(reverse=True)
    iplist1 = map(inet_ntoa, lot)
    iplist2 = map(inet_ntoa, lot1)
    print(iplist1)
    print(iplist2)
    if iplist == []:
        print("list fail")
        flag = "False"
    elif iplist == iplist1 or iplist == iplist2:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 


if __name__ == "__main__":
    qfinder_ip_sort()
