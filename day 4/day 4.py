OddWords = []
EvenWords = []
def count_vowels():
    Words = []
    TempWord = input("Enter words separated by spaces: ")
    Words = TempWord.split()
    for word in Words:
        VowelCount = 0
        for char in word.lower():
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                VowelCount = VowelCount + 1
        if VowelCount % 2 == 1:
            OddWords.append(word)
        else:
            EvenWords.append(word)
    print(f"✅ Odd vowels: {OddWords}")
    print(f"🚫 Even vowels: {EvenWords}")
def custom_rule():
    Words = []
    TempWord = input("Enter words separated by spaces: ")
    Words = TempWord.split()
    Rule = input("Enter rule (e.g., length > 4): ")
    Filtered = []
    NotFiltered = []
    for word in Words:
        length = len(word)
        if eval(Rule):
            Filtered.append(word)
        else:
            NotFiltered.append(word)
    print(f"✅ Matches rule: {Filtered}")
    print(f"🚫 Does not match: {NotFiltered}")
while True:
    while True:
        Decision = int(input("Odd vowels filter (1), Custom rule (2), Exit (3): "))
        if Decision ==  1 or Decision == 2 or Decision ==3:
            break
        else:
            print("invalid option try again")
    if Decision == 3:
        print("bye")
        break
    elif Decision == 1:
        count_vowels()
    else:
        custom_rule()
