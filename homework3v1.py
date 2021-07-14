a = 6
for i in range(a):
    for n in range(i):
        print("*", end="")
    print("")
for i in range(a, 0, -1):
    for n in range(i):
        print("*", end="")
    print("")