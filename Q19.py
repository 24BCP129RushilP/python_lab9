def string_length(s):
    if not s:
        return 0
    return 1 + string_length(s[1:])


string = input("Enter a string: ")
print("Length of the string:", string_length(string))