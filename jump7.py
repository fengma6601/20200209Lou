
for num in range(1,101):
    flag=False
    if num % 7==0:
        pass
    else:
        tmp=num
        while tmp!=0:
            if tmp %10 ==7:
                break
            else:
                tmp=tmp //10
        if tmp==0:
            flag=True
    if flag:
        print(num)
            
