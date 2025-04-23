def frequency(s):
    words = s.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    return dict(sorted(freq_dict.items()))

string = input("Enter a string: ")
result = frequency(string)
print("Word frequencies:", result)