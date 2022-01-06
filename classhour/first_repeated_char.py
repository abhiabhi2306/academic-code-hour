tc = int(input())
flag=False
for i in range(tc):
    flag=False
    arr = input()
    arr2 = list(arr)
    for letter in arr2:
        if arr2.count(letter)>1:
            print(letter)
            flag=True
            break
    if flag==False:
        print("-1")
    
