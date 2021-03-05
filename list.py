# case1
mylist = ["apple", "banana", "cherry"]
print(mylist)

# case2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# lenngth
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# pure data_type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# mix data_type
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# check_type
mylist = ["abc", 34, True, 40, "male"]
print(type(mylist))
print(type(mylist[0]))
print(type(mylist[1]))
print(type(mylist[2]))

# constructor
# use double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)