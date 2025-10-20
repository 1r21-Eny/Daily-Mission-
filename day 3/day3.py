Ans = None

def addition():
    Nums = []
    while True:
        TempNum = input("Enter number to add or (EXIT) to stop adding numbers: ")
        if TempNum == "EXIT":
            break
        else:
            TempNum = int(TempNum)
            Nums.append(TempNum)
    Ans = sum(Nums)
    print(f"sum of: {Nums} is: {Ans}")
while True:
    while True:
        Decision = int(input("Addition (1), Subtraction (2), Multiplication (3), Division (4), Exit (5): "))
        if Decision ==  1 or Decision == 2 or Decision == 3 or Decision == 4 or Decision ==5:
            break
        else:
            print("invalid option try again")
    if Decision == 5:
        print("bye")
        break
    else:
        addition()
