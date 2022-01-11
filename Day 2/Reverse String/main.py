# Method 1
def reverse1(string):
    str = ""
    for i in string:
        str = i + str
    return str


testString1 = "Hello, World!"
print(reverse1(testString1))

# Method 2

testString2 = "Hello, World from the Method 2!"
print(testString2[::-1])
