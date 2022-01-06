n = int(input())

startpoint = 0

for i in range(n):
    b = int(input())
    arr = input().split()
    arr = list(arr)
    arsize = len(arr)
    for j in range(startpoint, arsize,1):
        for k in range(j,arsize,1):
            for m in range(j,k+1,1):
                print(arr[m],end=' ')
            print("",end='\n')

            
