with open('input_2.txt', 'r') as f:
    lines = f.readlines()
    suma = 0

    for line in lines:
        a, b = line.split(",") 
        b = b.rstrip()

        print(f"{a} y {b}.")

        a1, a2 = a.split("-")
        b1, b2 = b.split("-")

        if ((int(a2) - int(a1)) >= (int(b2) - int(b1))):
            if (a1 <= b1 and a2 >= b2): 
                suma += 1

        else:
            if (b1 <= a1 and b2 >= a2): 
                suma += 1
        

    print(suma)
