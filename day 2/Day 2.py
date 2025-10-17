CodedString = []
DecodedString = []
NewString = None

String = input("Enter string you want coded: ")
StringList = list(String)

delimiter = ""


def Coding():
    global NewString
    CodedString.clear()
    for letter in StringList:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            NewCharacter = chr((ord(letter) - base + CeaserShift) % 26 + base)
        else:
            NewCharacter = letter
        CodedString.append(NewCharacter)
    NewString = delimiter.join(CodedString)
    print(f"Coded string is: {NewString}")


def Decoding():
    global NewString
    DecodedString.clear()
    for letter in CodedString:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            NewCharacter = chr((ord(letter) - base - CeaserShift) % 26 + base)
        else:
            NewCharacter = letter
        DecodedString.append(NewCharacter)
    NewString = delimiter.join(DecodedString)
    print(f"Decoded string is: {NewString}")


while True:
    while True:
        try:
            Choice = int(input("Code a string (1) or Decode string (2) or exit (3): "))
            break
        except ValueError:
            print("Please enter an integer")

    if Choice == 3:
        print("Exiting...")
        break

    while True:
        try:
            CeaserShift = int(input("Enter how much you want to shift by: "))
            break
        except ValueError:
            print("Please enter an integer")

    if Choice == 1:
        Coding()
    elif Choice == 2:
        Decoding()
    else:
        print("Invalid choice selected, please choose 1-3. Restarting program.")
        continue
