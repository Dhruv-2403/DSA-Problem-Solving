for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]>=3:
            print(i)
            break
    else:
        print(-1)
