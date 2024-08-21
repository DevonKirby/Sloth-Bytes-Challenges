def nearest_vowel(char):
    CONST_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    CONST_VOWELS = 'aeiou'

    char_index = CONST_ALPHABET.find(char)
    
    left_vowel_index = CONST_ALPHABET.find('a')
    for i in reversed(range(char_index)):
        if CONST_ALPHABET[i] in CONST_VOWELS:
            left_vowel_index = i
            break
    
    right_vowel_index = CONST_ALPHABET.find('u')
    for i in range(char_index, len(CONST_ALPHABET)):
        if CONST_ALPHABET[i] in CONST_VOWELS:
            right_vowel_index = i
            break

    if (char_index - left_vowel_index) > (right_vowel_index - char_index):
        return CONST_ALPHABET[right_vowel_index]

    return CONST_ALPHABET[left_vowel_index] 

result = nearest_vowel('b')
print(result)

result = nearest_vowel('s')
print(result)

result = nearest_vowel('c')
print(result)

result = nearest_vowel('i')
print(result)
