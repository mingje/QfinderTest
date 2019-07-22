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

def qfinder_myQNAP_sort():
    # open qfinder
    open_qfinder()
    click("1557906681939.png")
    wait(1)
    
    s = Region(Region(565,283,134,371))
    myqnap_str = s.text()
    myqnap_list = myqnap_str.splitlines()
    print(myqnap_list)
    # rm space, exchange"l","S"
    myqnaplist = []
    for i in myqnap_list:
        i = i.split("(")
        i = i[0]
        q = i.replace(']','')
        q = q.replace('|','l')
        q = q.replace('}','')
        q = q.replace('t3','ts')
        q = q.replace('<:','c')
        q = q.replace('Iu','lu')
        q = q.replace(' ','')
        q = q.replace('2S3','253')
        q = q.replace('alorna','aloma')
        myqnaplist.append(q)
    print(myqnaplist)
    a = sorted(myqnaplist,key=str.lower)
    b = sorted(myqnaplist, reverse=True, key=str.upper)
    print(a)
    print(b)
    if myqnaplist == []:
        print("list fail")
        flag = "False"
    elif myqnaplist == a or myqnaplist == b:
        print("pass")
        flag = "True"
    else:
        print("FAIL")
        flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
       
if __name__ == "__main__":
    qfinder_myQNAP_sort()