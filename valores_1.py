base_maior = float(5.0)
base_menor = float(2.0)
altura = float(3.5)

def area(a):
    global base_menor
    global base_maior
    global altura

    area = (((base_maior * base_menor) * altura) /2)
    return area