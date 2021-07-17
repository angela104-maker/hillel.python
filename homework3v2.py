a = int(input("enter number: "))
b = int(input("unter second number: "))
if a<b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)