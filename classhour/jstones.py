
tcase = int(input())

def find(a,b):
    keymap = {}
    flagvar = 0
    for item in a:
        if item in keymap:
            keymap[item]+=1
        else:
            keymap[item]=1
            
    for character in b:
        if character in keymap:
            flagvar+=keymap[character]
    return flagvar
    
    

for i in range(tcase):
    a,b = input().split(" ")
    print(find(a,b))
