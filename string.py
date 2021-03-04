# normal output
print("Hello")
print('Hello')

print()

#assign value
a = "Hello"
print(a)

print()

# multi line
a= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print()

# select alphabet
a = "Hello, World!"
print(a[1])

print()

# show many alphabet
for x in "banana":
    print(x)

# length
a = "Hello, World!"
print(len(a))

# check string in text
# exist
txt = "The best things in life are free!"
print("free" in txt)

# not exist
print("expensive" not in txt)

# if with string
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")
