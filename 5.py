num = 19399380
lst = [i for i in range(2,20)]
while True:
    flag = True
    for i in lst:
        if num%i!=0:
            flag = False
            break
    if flag:
        print("Found: ", num)
        break
    num+=19399380
    
