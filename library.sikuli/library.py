from sikuli import *
from nas_info import *
import sys

Settings.OcrTextSearch = True
Settings.OcrTextRead = True
def move_to(type):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    if type == "top":
        if exists("1557993168704.png"):
            dragDrop("1557993168704.png", "1557993187173.png")
        else:
            pass
    else:
        if exists("1557993168704.png"):
            dragDrop("1557993168704.png", "1558066322938.png")
        else:
            pass
    print("--- End " + fun_name + " ---")

# open qfinder
def open_qfinder():
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    Qfinder = "C:\Program Files (x86)\QNAP\Qfinder\QfinderPro.exe"
    openApp(Qfinder)
    wait_please(loop=50, time=2)
    wait(10)
    click("1581651434184.png")
    print("click refresh button in main")
    wait_please(loop=50, time=2)
    wait(10)
    if exists ("1557215006398.png"):
        click("1557215006398.png")
        print("Open Qfinder success")
        flag = 1
    else:
        flag = 0
    assert flag == 1, "Open Qfinder FAIL"
    click(Pattern("1562128466510.png").similar(0.80))
    print("Max Qfinder UI")
    wait(1)
    print("--- End " + fun_name + " ---")
    return flag

def search_target(screens):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    b_list = []
    try:
        all_list = findAll(Pattern(screens).similar(0.70))
        for i in all_list:
            hover(i)
            b_list.append(i)
    except:
        print("Not find target")
    print("--- End " + fun_name + " ---")
    return b_list

def confirm_target(ta_list):
    flag = 0
    for i in ta_list:
        click(i)
        wait(1)
        click("1583378173145.png")
        wait(1)
        type("a", KeyModifier.CTRL)
        wait(1)
        type("c", KeyModifier.CTRL)
        wait(1)
        region_text = Env.getClipboard().strip()
        print(region_text)
        region_text = region_text.split("(")
        s = region_text[0]
        print(region_text[0])
        d = s[:-1]
        click("1583391115643.png")
        wait(1)
        if d == targrt['name']:
            print("ok")
            flag = 1
            break
        else:
            print("fail")
            flag = 0
    return flag      



def confirm_target3(nas_picture, lanip1, qid):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    click(nas_picture)
    print("click target")
    wait(1)
    click("1583407685337-1.png")    
    print("click login button in main")
    wait(3)
    reg1 = Region(429,35,670,33)
    reg1.click("1583407764208-1.png")
    type("a", KeyModifier.CTRL)
    wait(1)
    type("c", KeyModifier.CTRL)
    wait(1)
    region_text = Env.getClipboard().strip()
    print(region_text)
    aa = region_text.split("/")
    print(aa)
    ss = aa[2]
    qq = ss.split(":")
    print(qq)
    ff = qq[0]
    if ff == lanip1 or ff == qid:
        print("ip match, get target")
        flag = 1
    else:
        print("ip not match")
        flag = 0
    try:
        closeApp("chrome")
        print("close chrome")
    except:
        pass  
    print("--- End " + fun_name + " ---")   
    return flag


def check_target(screenpath, lanip1, qid):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    w_list = search_target(screenpath)
    print(w_list)
    flag = 0
    if len(w_list) != 0:
        for i in w_list:    
            if confirm_target3(i,lanip1,qid) == 1:
                flag = 1
                print("find target icon")
                break
            else:
                flag = 0
    else:
        print("No item in list")
        flag = 0
    return flag   

def find_target_nas(**kwargs):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    target = nas_detail(**kwargs)
    print("Target is: " + str(target["name"]) + str(target['lanip1']))
    print(target)
    move_to(type='top')
    for i in range(200):
        if check_target(target['icon'],target['lanip1'],target['qid']) == 1:
            flag = 1
            break
        elif check_target(target['icon_1'],target['lanip1'],target['qid']) == 1:
            flag = 1
            break
        elif check_target(target['icon_g'],target['lanip1'],target['qid']) == 1:
            flag = 1
            break
        elif check_target(target['icon_highlight'],target['lanip1'],target['qid']) == 1:
            flag = 1
            break
        elif check_target(target['icon_gh'],target['lanip1'],target['qid']) == 1:
            flag = 1
            break
        else:
            print("next page ")
            last_name_current = Region(Region(49,632,95,20))
            last_name_current = last_name_current.text()
            if exists(Pattern("1557215418598.png").similar(0.80)):
                for i in range(14):
                    click(Pattern("1557215418598.png").similar(0.80))
                last_name = Region(Region(49,632,95,20))
                last_name = last_name.text()
                if last_name_current == last_name:
                    print("Not find target")
                    flag = 0
                    break
                else:
                    pass
            else:
                print("Not find target")
                flag = 0
                break
    assert flag == 1, "Find target FAIL" 
    wait(2)
    print("--- End " + fun_name + " ---")
    return flag


def enter_config(ac, pwd):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    wait(1)
    click("1557300544512.png")
    print("click config button in main")
    wait(5)
    if exists("1557375692116.png"):
        print("open login window")
        flag = 1
    else:
        flag = 0
    assert flag == 1, "open login window FAIL"
    type(ac)
    wait(1)
    type(Key.TAB)
    wait(1)
    print(pwd)
    type(pwd)
    wait(1)
    type(Key.ENTER)
    wait(5)
    print("input ac & pwd")
    wait_please(loop=50, time=2)
    if exists("1557302801616.png"):
        print("open config UI")
        flag = 1
    else:
        print("open config UI fail")
        flag = 0
    print("--- End " + fun_name + " ---")
    assert flag == 1, "Open config error"
    

def wait_please(loop,time):
    wait(5)
    for i in range(loop):
        try:
            waitVanish("1557302307072-1.png",time)
            wait(1)
            if not exists("1557302307072-1.png"):
                print("wait disappear")
                break
            else:
                pass
        except:
            pass
    if exists("1557302307072-1.png"):
        flag = 0
    else:
        flag = 1
    assert flag == 1, "Still wait..over time"
    wait(1)

def get_region_text(x,y,w,h):
    a = Region(x,y,w,h)
    dragDrop(Location(x, y), a)
    type("c", KeyModifier.CTRL)
    wait(1)
    b = Env.getClipboard().strip()
    return b

def login_open_web():      
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    click("1557309643274.png")
    print("click login button in main")
    wait(10)
    if exists("1557309257444-1.png"):
        print("Min window")
        click("1557309257444-1.png")
    elif exists("1557309306602-1.png"):
        print("Max window")
    else:
        print("not find browser window")
    
    wait(5)
    if exists("1557310210160-1.png"):
       print("Open web page1")
       flag = "True"
    elif exists("1557310336279-1.png"):
       print("Open web page2")
       flag = "True"
    elif exists("1562579603836-1.png"):
       print("Open web page3")
       flag = "True"
    elif exists("1581325742321.png"):
       print("Open web page4")
       flag = "True"
    elif exists("1562561186884-1.png"):
       print("Open web page5")
       flag = "True"
    elif exists("1557798873195-1.png"):
            
       msg_region = Region(Region(413,247,453,186))
       msg_region.click("1557798940520-1.png")
       print("Open web page FAIL1")
       flag = "False"
    else:   
       print("Open web page FAIL2")
       flag = "False"
    print(flag)
    
    try:
        closeApp("chrome")
        print("close chrome")
    except:
        pass
    print("--- End " + fun_name + " ---")
    return flag

def replace_str(replacestr, *args):
    k = 0
    for i in range(len(args)/2):
        replacestr = replacestr.replace(args[k],args[k+1])
        k = k + 2
    return replacestr

def bookmark(target):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    print(target)
    #  find target NAS
    if find_target_nas(name = target["name"],lanip1 = target['lanip1']) == 1:
        bookmark_target = target['icon_highlight']
    else:
        print("FAIL")
    click("1581307703276.png")
    print("bookmark button in main")
    picture = find(bookmark_target)
    picture_x = picture.getX()
    print(picture_x)
    picture_y = picture.getY()
    print(picture_y)
    bookmark_region = Region(picture_x-45,picture_y+1,42,25)
    lo = Location(picture_x-45,picture_y+1)
    hover(lo)
    if bookmark_region.exists(Pattern("1557832935307.png").exact()):   
        print("Bookmark PASS")
        flag = 1
    else:
        print("FAIL")
        flag = 0
    print("--- End " + fun_name + " ---")
    return flag

def check_bookmark(target_list,type):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    if type == "top":
        move_to(type = "top")
    else:
        move_to(type = "end")
    wait(1)
    u = len(target_list)
    if type == "top":
        b = Region(Region(5,284,41,20))
    else:
        b = Region(Region(5,628,42,25))
    x = b.x
    y = b.y
    w = b.w
    h = b.h
    print(x)
    print(y)
    for i in range(u + 1):
        if i < u:
            if b.exists("1557996053481.png") or b.exists("1557996987049.png"):
                print("mark")
                flag = 1
            else:
                print("not mark")
                flag = 0
                break
        else:  
            if b.exists("1557996053481.png") or b.exists("1557996987049.png"):
                print("mark")
                flag = 0
            else:
                print("not mark")
                flag = 1     
        if type == "top":
            b = Region(x,y+26,w,h)
        else:
            b = Region(x,y-26,w,h)
        x = b.x
        y = b.y
        w = b.w
        h = b.h
        print(x)
        print(y)
    if flag == 1:
        print('PASS bookmark')
    else:
        print('FAIL bookmark')
    print("--- End " + fun_name + " ---")
    return flag 

def upload_action(uploadfile, up_policy):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    click("1560414599541-1.png")
    print("click create upload job button")
    wait(5)
    click(Pattern("1560481192508.png").similar(0.90))
    print("click add file button")
    wait(3)
    type(uploadfile)
    type(Key.ENTER)
    click("1560481294073.png")
    print("click change destination button")
    for i in range(15):
        wait(2)
        if exists("1560481327682.png"):
            print("wait..")
        else:
            break
    click(Pattern("1560481565253.png").similar(0.90))
    type("qfinderupload")
    click(Pattern("1560485763485.png").similar(0.90))
    for i in range(15):
        wait(2)
        if exists("1560481327682.png"):
            print("wait..")
        else:
            break
    click(Pattern("1560483192785.png").similar(0.90))
    wait(1)
    click(Pattern("1560482334036.png").similar(0.90))
    wait(1)
    for i in range(2):
        type(Key.PAGE_UP)
    if up_policy == "skip":
        pass
    elif up_policy == "overwrite":
        type(Key.PAGE_DOWN)
    else:
        for j in range(2):
            type(Key.PAGE_DOWN)
    type(Key.ENTER)
    wait(1)
    click("1560486267746.png")
    print("click start upload button")
    flag = 0
    for i in range(20):
        wait(5)
        if exists("1560483041869.png"):
            print("UI upload pass")
            flag = 1
            break
        else:
            flag = 0
    print("--- End " + fun_name + " ---")
    return flag
#find_target_nas(name = "Steven-TS551", lanip1 = "10.20.241.196")


def b():
    xx = "abc"
    if xx == c(xx):
        print("ok")
def c(datt):
    return datt