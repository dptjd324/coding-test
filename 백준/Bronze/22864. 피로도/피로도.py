a,b,c,m = map(int,input().split())
stress = 0
work = 0
hours=24

while hours !=0:
    if a > m:
        break
    elif stress+a > m:
        stress -=c
        hours -=1
        if stress <0:
            stress=0
    else:
        stress +=a
        work +=b
        hours -=1
print(work)