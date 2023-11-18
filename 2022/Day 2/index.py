# A -> Rock, B -> Paper, C -> Scissors
# X -> Rock, Y -> Paper, Z -> Scissors

def who_wins(a, b):
    if (a == 'A'):
        if (b == 'Y'): return 6+2
        elif (b == 'Z'): return 0+3  
        else: return 3+1

    elif (a == 'B'):
        if (b == 'Z'): return 6+3 
        elif (b == 'X'): return 0+1
        else: return 3+2

    elif (a == 'C'):
        if (b == 'X'): return 6+1
        elif (b == 'Y'): return 0+2 
        else: return 3+3

    return 0;


with open('input.txt', 'r') as f:
    lines = f.readlines()
    suma = 0

    for line in lines:
        if line.strip() != "":
            lista = line.split(" ")
            suma += who_wins(lista[0], lista[1].rstrip())

    print(suma)

