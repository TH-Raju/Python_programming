n = 8
for i in range(0, 8):
    for j in range(0, n):
        print(end=" ")
    n = n-1
    for j in range(0, i+1):
        print("*",end='')
    print()

n = 7
for i in range(0, 5):
    for j in range(0, n):
        print(end=" ")
    n = n-1
    for j in range(0, i+1):
        print("*", end=" ")
    print()
    
n = 8
for i in range(n+1):
    print(i*"*")

m = 7
for i in range(m):
    for j in range(m):
        print(end=" ")
    m = m -1
    for x in range(i):
        print("x",end=" ")
    print(" ")