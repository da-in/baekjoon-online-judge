import sys
n = int(sys.stdin.readline())

for i in range(1, n+1):
    if(i%3==0):
        continue
    elif(i!=n):
        print(f'{i} ', end="")
    else:
        print(f'{i}', end="")