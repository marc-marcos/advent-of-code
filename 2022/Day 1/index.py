with open('input.txt', 'r') as f:
    lines = f.readlines()

    maximum_1 = 0
    maximum_2 = 0
    maximum_3 = 0
    current = 0

    for line in lines:
        if line.strip() == "":
            print(f"1. {maximum_1}")
            print(f"2. {maximum_2}")
            print(f"3. {maximum_3}")
            print(f"Current. {current }")
            print()
            if (current >= maximum_1): 
                maximum_3 = maximum_2
                maximum_2 = maximum_1
                maximum_1 = current 

            elif (current >= maximum_2):
                maximum_3 = maximum_2
                maxium_2 = current

            elif (current >= maximum_3):
                maximum_3 = current

            current = 0

        else:
            current += int(line)

    print(maximum_1 + maximum_2 + maximum_3)
