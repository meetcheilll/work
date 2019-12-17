a = int(input("число A"))
b = int(input("число B"))
c = int(input("число С"))
if a > b and a > c:
    print("a-max")
elif b > a and b > c:
    print("b>max")
else:
    print("c-max")
