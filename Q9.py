def count_alpha_digits(s):
    
    counts = {'alphabets': 0, 'digits': 0}
    
    
    for char in s:
        if char.isalpha():  
            counts['alphabets'] += 1
        elif char.isdigit():  
            counts['digits'] += 1
    
    return counts


string = input("Enter a string: ")
result = count_alpha_digits(string)
print("Counts:", result)