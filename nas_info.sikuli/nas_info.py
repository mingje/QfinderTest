from sikuli import *
import os
import sys

current_path = sys.path[0]
current_path1 = current_path.split("\\")
del current_path1[-1]
delimiter = "\\"
path = delimiter.join(current_path1) + "\\screenshot\\"

def nas_detail(**kwargs):
    nas = {}
    nas["name"] = kwargs.get("name")
    nas["icon"] = path + kwargs.get("name") + "\\" + kwargs.get("name") + ".png"
    nas["icon_1"] = path + kwargs.get("name") + "\\" + kwargs.get("name") + "_1.png"
    nas["icon_highlight"] = path + kwargs.get("name") + "\\" + kwargs.get("name") + "_highlight.png"
    nas["icon_g"] = path + kwargs.get("name") + "\\" + kwargs.get("name") + "_g.png"
    nas["icon_gh"] = path + kwargs.get("name") + "\\" + kwargs.get("name") + "_gh.png"    
    nas["lanip1"] = kwargs.get("lanip1")   
    nas["lanip1P"] = path + "xx.png"
    nas["lanip2"] = kwargs.get("lanip2")
    nas["ac"] = kwargs.get("ac")
    nas["pwd"] = kwargs.get("pwd")
    check_page = path + kwargs.get("name") + "\\detail_check\\"
    detail_list = os.listdir(check_page)
    check_list = []
    for i in detail_list:
        check_list.append(check_page + i)
    nas["detail_check"] = check_list
    return nas

