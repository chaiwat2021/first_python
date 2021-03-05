# append to the end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert with index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# extend list with values from another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
