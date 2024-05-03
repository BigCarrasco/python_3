def count_vowels(sentence):
    vowels = "aeiou"  # Define our vowels  
    count = 0  # Initialize the count variable
    
    for char in sentence.lower(): # Get the character count of this sentence
        if char in vowels: #verify if the character is a vowel
            count += 1 # if is a vowel, increment

    return count # return the count variable

print(count_vowels("adacadabra")) # test the count variable 1
print(count_vowels("hola")) # test the count variable 2
print(count_vowels("miguelito carrasco")) # test the count variable 3