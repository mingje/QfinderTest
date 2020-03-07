def confirm_target2(ta_list, lanip1):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    flag = 0
    print(ta_list)
    for i in ta_list:
        click(i)
        print("click target")
        wait(1)
        click("1583407685337-1.png")    
        print("click login button in main")
        wait(3)
        reg1 = Region(429,35,670,33)
        reg1.click("1583510293595.png")
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
        if ff == lanip1:
            print("ip match, get target")
            flag = 1
            try:
                closeApp("chrome")
                print("close chrome")
            except:
                pass  
            break
        else:
            print("ip not match")
            flag = 0
        try:
            closeApp("chrome")
            print("close chrome")
        except:
            pass  
    print("--- End " + fun_name + " ---")   
    return flagdef confirm_target2(ta_list, lanip1):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    flag = 0
    print(ta_list)
    for i in ta_list:
        click(i)
        print("click target")
        wait(1)
        click("1583407685337-2.png")    
        print("click login button in main")
        wait(3)
        reg1 = Region(429,35,670,33)
        reg1.click("1583510293595-1.png")
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
        if ff == lanip1:
            print("ip match, get target")
            flag = 1
            try:
                closeApp("chrome")
                print("close chrome")
            except:
                pass  
            break
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

def find_target_nas_1(**kwargs):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    target = nas_detail(**kwargs)
    print("Target is: " + str(target["name"]) + str(target['lanip1']))
    print(target)
    move_to(type='top')
    for i in range(200):
        w_list = search_target(target['icon'])
        print(w_list)
        w_list1 = search_target(target['icon_1'])
        print(w_list1)
        w_list2 = search_target(target['icon_g'])
        print(w_list2)
        w_list3 = search_target(target['icon_highlight'])
        print(w_list3)
        w_list4 = search_target(target['icon_gh'])
        print(w_list4)
        total_list = [w_list, w_list1, w_list2, w_list3, w_list4]
        k = 0
        for t in total_list:
            k = k + len(t)
        if k != 0:
            for i in total_list:
                if len(i) != 0:      
                    if confirm_target2(i,lanip1 = target["lanip1"]) == 1:
                        print(target["icon"]) 
                        flag = 1
                        print("find target icon")
                        break
                else:
                    pass
        
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
    """
    assert flag == 1, "Find target FAIL"
    """
    wait(2)
    print("--- End " + fun_name + " ---")
    return flag



# find target NAS
def find_target_nas_original(**kwargs):
    fun_name = sys._getframe().f_code.co_name
    print("*** Start to " + fun_name + " ***")
    target = nas_detail(**kwargs)
    print("Target is: " + str(target["name"]))
    move_to(type='top')
    for i in range(200):
        if exists (Pattern(target['icon']).similar(0.80)):
            print(target["icon"])
            click(Pattern(target['icon']).similar(0.80))
            flag = 1
            print("find target icon")
            break
        elif exists (Pattern(target['icon_1']).similar(0.80)):
            print(target["icon_1"])
            click(Pattern(target['icon_1']).similar(0.80))
            flag = 1
            print("find target icon_1")
            break
        elif exists (Pattern(target['icon_g']).similar(0.80)):
            print(target["icon_g"])
            click(Pattern(target['icon_g']).similar(0.80))
            flag = 1
            print("find target icon_g")
            break
        elif exists (Pattern(target['icon_highlight']).similar(0.80)):
            print(target["icon_highlight"])
            click(Pattern(target['icon_highlight']).similar(0.80))
            flag = 1
            print("find target icon_highlight")
            break
        elif exists (Pattern(target['icon_gh']).similar(0.80)):
            print(target["icon_gh"])
            click(Pattern(target['icon_gh']).similar(0.80))
            flag = 1
            print("find target icon_gh")
            break
        else:
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
