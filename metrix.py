import random
n = int(input("Enter row for metrix ="))
m = int(input("Enter col for metrix ="))
mylist = []
a=[[random.random() for row in range(m)]for col in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())

print("Enter Your seat:")
print("Enter row:")
row = int(input(">"))
print("Enter col:")
col = int(input(">"))
# print("Your metrix is=")
for i in range(n):
    for j in range(m):
        # count = count+ a[i][j]
        # if i==j or i+j==(m-1):
        #     print(a[i][j], end="\t")
        # a[i][j] = mylist[count]
        # count = count+1
        # print(a[i][j])
        # if i-j == 1 or j-i == 1 :
        #     mylist.append(a[i][j])
        i = row
        j = col
        if i <= n-1 and j <= m-1:
            if a[i][j] == 0:
                print("Seat is empty!")
                book = int(input("Press 1 for book this seat>"))
                print("Your seat is booked!")
                exit()
            elif a[i][j]  == 1:
                print("Seat is booked, choose some another seat!")
                break
        else:
            print("Invalid seat no!")


    # print("")
# print(mylist)
# for i in range(n):
#     for j in range(m):
        # print(a[i][j])
# print(count)
