# if only
a,b = 33, 200

if b > a:
    print("b is greater than a")

print()

# else if
a, b = 33, 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

print()

# else
a, b = 200, 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
