# access with index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# access from the end of list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# range from the end of list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# check exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
