string = str(input("Enter a sentence: "))
string = string.lower()

def counting(string):

    constonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    digits = "0123456789"
    
    VowelCount = 0
    SpaceCount = 0
    ConstonantCount = 0
    DigitCount = 0
    SpaceCount = string.count(" ")
    
    for letter in string:
        if letter in vowels:
            VowelCount += 1
        elif letter in constonants:
            ConstonantCount += 1
        elif letter in digits:
            DigitCount += 1

    return VowelCount, ConstonantCount, DigitCount, SpaceCount
VowelCount, ConstonantCount, DigitCount, SpaceCount = counting(string)
print(f" VowelCount: {VowelCount}\n ConstonantCount: {ConstonantCount}\n DigitCount: {DigitCount}\n SpaceCount: {SpaceCount}\n")
