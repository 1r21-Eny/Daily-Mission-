string = str(input("Enter a sentence: "))
string = string.lower()

def counting(string):

    constonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    digits = "0123456789"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    VowelCount = 0
    SpaceCount = 0
    ConstonantCount = 0
    DigitCount = 0
    SpaceCount = string.count(" ")
    IsPangram = True
    
    for letter in string:
        if letter in vowels:
            VowelCount += 1
        elif letter in constonants:
            ConstonantCount += 1
        elif letter in digits:
            DigitCount += 1

    for letter in alphabet:
        if letter not in string:
            IsPangram = False
            break
        
    return VowelCount, ConstonantCount, DigitCount, SpaceCount, IsPangram
VowelCount, ConstonantCount, DigitCount, SpaceCount, IsPangram = counting(string)
print(f" VowelCount: {VowelCount}")
print(f"ConstonantCount: {ConstonantCount}")
print(f"DigitCount: {DigitCount}")
print(f"SpaceCount: {SpaceCount}")
print(F"Is a pangram: {IsPangram}")
