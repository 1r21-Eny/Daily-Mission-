Ans = None
def addition():
    global Ans
    Nums = []
    while True:
        TempNum = input("Enter number to add or (EXIT) to stop adding numbers: ")
        if TempNum == "EXIT":
            break
        else:
            if TempNum == "ans":
                if Ans is None:
                    print("No previous answer")
                    continue
                TempNum = Ans
            try:
                TempNum = float(TempNum)
                Nums.append(TempNum)
            except:
                print("invalid input")
    Ans = sum(Nums)
    print(f"sum of: {Nums} is: {Ans}")
def subtraction():
    global Ans
    Nums = []
    while True:
        TempNum = input("Enter number to subtract or (EXIT) to stop adding numbers: ")
        if TempNum == "EXIT":
            break
        else:
            if TempNum == "ans":
                if Ans is None:
                    print("No previous answer")
                    continue
                TempNum = Ans
            try:
                TempNum = float(TempNum)
                Nums.append(TempNum)
            except:
                print("invalid input")
    Ans = Nums[0]
    for i in range(1, len(Nums)):
        Ans = Ans - Nums[i]
    print(f"result of: {Nums} is: {Ans}")
def multiplication():
    global Ans
    Nums = []
    while True:
        TempNum = input("Enter number to multiply or (EXIT) to stop adding numbers: ")
        if TempNum == "EXIT":
            break
        else:
            if TempNum == "ans":
                if Ans is None:
                    print("No previous answer")
                    continue
                TempNum = Ans
            try:
                TempNum = float(TempNum)
                Nums.append(TempNum)
            except:
                print("invalid input")
    Ans = 1
    for num in Nums:
        Ans = Ans * num
    print(f"product of: {Nums} is: {Ans}")
def division():
    global Ans
    Nums = []
    while True:
        TempNum = input("Enter number to divide or (EXIT) to stop adding numbers: ")
        if TempNum == "EXIT":
            break
        else:
            if TempNum == "ans":
                if Ans is None:
                    print("No previous answer")
                    continue
                TempNum = Ans
            try:
                TempNum = float(TempNum)
                Nums.append(TempNum)
            except:
                print("invalid input")
    Ans = Nums[0]
    for i in range(1, len(Nums)):
        if Nums[i] == 0:
            print("division by zero error")
            return
        Ans = Ans / Nums[i]
    print(f"result of: {Nums} is: {Ans}")
while True:
    while True:
        try:
            Decision = int(input("Addition (1), Subtraction (2), Multiplication (3), Division (4), Exit (5): "))
            if Decision ==  1 or Decision == 2 or Decision == 3 or Decision == 4 or Decision ==5:
                break
            else:
                print("invalid option try again")
        except:
            print("invalid option try again")
    if Decision == 5:
        print("bye")
        break
    elif Decision == 1:
        addition()
    elif Decision == 2:
        subtraction()
    elif Decision == 3:
        multiplication()
    elif Decision == 4:
        division()
