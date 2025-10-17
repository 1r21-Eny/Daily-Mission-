CodedString = []
DecodedString = []
NewString = None

String = input("Enter string you want coded: ")
StringList = list(String)

delimiter = " "


def Coding():
    for letter in StringList:
        LetterNumber = ord(letter)
        LetterNumber += CeaserShift
        NewCharacter = chr(LetterNumber)
        CodedString.append(NewCharacter)
    NewString = delimiter.join(CodedString)
    print(f"Coded string is: {NewString}")

def Decoding():
    for letter in CodedString:
        LetterNumber = ord(letter)
        LetterNumber -= CeaserShift
        NewCharacter = chr(LetterNumber)
        DecodedString.append(NewCharacter)
    NewString = delimiter.join(DecodedString)
    print(f"Decoded string is: {NewString}")
    
while True:
    
    while True:
        try:
            Choice = int(input("Code a string (1) or Decodestring (2) or exit (3): "))
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
        print("invalid choice selected please choose 1-3 restarting program")
        continue


