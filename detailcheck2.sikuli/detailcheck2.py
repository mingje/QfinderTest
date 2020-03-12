"""
    
    detail_window = Region(Region(403,163,471,347))
    for i in range(3):
        detail_window.click("1557400195347.png")
    check_result = []
    for i in target["detail_check"]:
        if detail_window.exists(Pattern(i).similar(0.90)):
            print("detail check PASS")
            check_result.append("P")
        else:
            print("detail check FAIL")
            check_result.append("F")
        if detail_window.exists(Pattern("1557482984281.png").similar(0.90)):
            print("Find end")
            break
        else:
            for j in range(11):
                detail_window.click("1557400195347.png")
            wait(1)
    print(check_result)
    if "F" in check_result:
        print("detail FAIL")
        flag = "False"       
    else:
        flag = "True"
        print("detail PASS")
"""