string= str(input("enter a string : "))

def count_UPPER_lower(s):
    lower_count=0
    UPPER_count=0
    for letter in s:
        if ord('a')<=ord(letter)<=ord('z'):
            lower_count = lower_count + 1
        elif ord('A')<=ord(letter)<=ord('Z'):
            UPPER_count = UPPER_count + 1
        else:
            continue
    
    return dict({"UPPER count":UPPER_count,"lower count":lower_count})

print("UPPER AND LOWER COUNTS : ",count_UPPER_lower(string))

# can be done by isupper and islower