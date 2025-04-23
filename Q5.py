def ispangram(sentence, alphaset=None, index=0):
    
    if alphaset is None:
        alphaset = set('abcdefghijklmnopqrstuvwxyz')
    
   
    sentence_set = set(char.lower() for char in sentence if char.isalpha())
    
   
    if index >= len(alphaset):
        return alphaset <= sentence_set
    
    
    if alphaset <= sentence_set:
        return True
    
    
    return ispangram(sentence, alphaset, index + 1)


test1 = "The quick brown fox jumps over the lazy dog"
test2 = "Crazy Fredrick bought many very exquisite opal jewels"

print(f"'{test1}' is a pangram: {ispangram(test1)}")
print(f"'{test2}' is a pangram: {ispangram(test2)}")