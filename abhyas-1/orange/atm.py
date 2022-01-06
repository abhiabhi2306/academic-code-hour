wth,bal = input().split()

wth=float(wth)
bal=float(bal)

if wth+0.50<=bal:
    if (wth%5==0):
        bal=bal-wth
        bal=bal-0.50
        print("{:.2f}".format(bal))
    else:
        print("{:.2f}".format(bal))
else:
    print("{:.2f}".format(bal))
