def convert(s):
    
    unique_sorted_words = sorted(set(s.split()))
    
    return ' '.join(unique_sorted_words)


string = input("Enter a sequence of whitespace-separated words: ")
result = convert(string)
print("Result:", result)