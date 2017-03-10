import math
bits = 3
irreduciblePoly= 13


cosa = int(math.pow(2, bits))

#Tabla de Adicion
for i in range(cosa):
    for j in range(cosa):
        result = i ^ j
        result = '{0:03b}'.format(result)
        print result," ",
    print(" ")

print("---------------------------------------------")

#Tabla de multiplicacion
suma = []
for i in range(cosa):
    for j in range(cosa):

        multiplicador =  '{0:03b}'.format(j)
        for z in range(bits):
            suma[i] = '{0:03b}'.format(multiplicador[i]*j)
        for z in range(bits):
            if z>0:
                reminder = suma[z-1] ^ suma[z]
                #
                #
                #
        producto = i*j
        result = producto % irreduciblePoly
        result = '{0:03b}'.format(result)
        print result," ",
    print(" ")







