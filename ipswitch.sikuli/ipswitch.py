list_a = ['10.20.204.1','10.20.204','10.20.dsjj','10.20.204.saa','10.20.204.198','10.2000.204.122',
        '10..204.128', '10. .205.198']
print(list_a)
list_b = []
for i in list_a:
    if i.count('.') == 3:
        list_b.append(i)

print(list_b)

list_c = []
for j in list_b:
    k = list(j)
    flag = 0
    for f in k:
        if f.isalpha() == True:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        list_c.append(j)
print(list_c)

list_d = []
for u in list_c:
    d = u.split(".")
    for r in d:
        if r.isdigit() == False or len(r) > 3:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        list_d.append(u)
print(list_d)

        
    