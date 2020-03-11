import random
m=int(input("enter number of rows="))
n=int(input("enter number of columns="))
a=[[random.random()for row in range(n)]for col in range(m)]
count = 1

for i in range(m):
    l = m-1
    for j in range(n):
        if i%2==0:
            a[i][j]=count
        elif i%2!=0 and l == (m-1):
            a[i][l] = count
            l = l-1
        if l == 0:
            break

        count=count+1
        print(a[i][j], end="\t")
    print("")
