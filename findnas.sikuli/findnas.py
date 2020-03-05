
a = [1,2,3]
b = [4,5,6]
c = []
d = [a,b,c]
x = 0
for i in d:
    x = x + len(i)
    print(x)


    

"""
def search_target(find_screenshot):
    findall_list = []
    try:
        all_list = findAll(Pattern(find_screenshot).similar(0.80)
        for i in all_list:
            finall_list.append(i)
    except:
        print("Not find target")
    return findall_list

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
        if d == targrt['name']:
            print("ok")
            flag = 1
            break
        else:
            print("fail")
            flag = 0
    return flag

if len(search_target()) != 0:
    w_list = search_target()
    confirm_target(w_list)
else:
    print("nono")

       
print(target["icon"])
click(Pattern(target['icon']).similar(0.80))
flag = 1
print("find target icon")
break

   
def search_target():
    b = []
    try:
        a = findAll("1583378114002.png")
        for i in a:
            b.append(i)
    except:
        print("Not find target")
    return b

b = []
for i in a:
    b.append(i)
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
    print(d)
    
print(len(b))
"""