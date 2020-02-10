from nas_info import *
from library import *
Settings.OcrTextSearch = True
Settings.OcrTextRead = True


import sys
"""
target_list = []
for i in range(len(sys.argv)):
    if i < 1:
        pass
    else:
        targetx = nas_detail(name = sys.argv[i])
        target_list.append(targetx)
print(target_list)
"""

nas_name = "AT-TS231P2"
nas_name1 = "AT-TVS473"
target1 = nas_detail(name = nas_name)
target2 = nas_detail(name = nas_name1)
target_list = [target1,target2]
print(target_list)

def qfinder_bookmark_sort():
    # open qfinder
    open_qfinder()
    wait(1)
    move_to(type = "top")
    wait(1)
    click(Location(1200, 500))
    wait(1)
    s = Region(1,280,44,373)
    r = Region(Region(1260,606,20,53))
    
    # clean bookmark
    for i in range(10):
        # clean bookmark on current page
        for j in range(14):
            if s.exists(Pattern("1557990451641.png").similar(0.90)):
                click(Pattern("1557990451641.png").similar(0.90))     
            elif s.exists(Pattern("1581041647863.png").exact()):
                click(Pattern("1557996053481.png").exact()) 
            else:
                print("clean current page")
                break
            wait(1)
            """
            click("1581040306938.png")
            """
            wait(1)
        l = Region(Region(51,628,122,26))
        last_device = l.text()
        if r.exists("1557990701693.png"):
            for i in range(14):
                r.click("1557990701693.png")
            k = Region(Region(51,628,122,26))
            last_device_current = k.text()
            if last_device == last_device_current:
                print("last page")
                break
            else:
                pass
        else:
            print("search end")
            break
    move_to(type = "top")
    wait(1)
    for target in target_list:
        click(Location(1200, 500))
        wait(1)
        bookmark(target=target)
    
    click(Pattern("1557995822824.png").similar(0.90))
    wait(1)
    click(Location(1200, 500))
    wait(1)
    flag = "False"
    for i in range(1):
        if check_bookmark(target_list = target_list, type='top') == 1:
            print("bookmark sort pass_top")
            flag = "True"
            break
        elif check_bookmark(target_list = target_list, type='end') == 1:
            print("bookmark sort pass_end")
            flag = "True"
            break
        else:
            print("bookmark sort fail")
            flag = "False"
    with open("result.txt", "w") as fp:
       fp.write(flag) 
          

if __name__ == "__main__":
    qfinder_bookmark_sort() 