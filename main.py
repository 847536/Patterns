for x in range(0,2):
    for y in range(0,3,2):
        for z in range(0,y+1):
            print(f'{"*"*(z+1):^8}')
        print("\r")
for j in range(0,5):
    print("*", end="")
for i in range(0,9,2):
    for p in range(0,i-1):
        print("*",end="")
    print("\r")


