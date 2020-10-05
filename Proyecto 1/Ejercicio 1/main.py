




MSB= [0xB0,0x92,0x21]



def Convertir_MSB(MSB):
    a=str(bin(MSB))
    c=a.split('0b')
    
    d=c[1]

    return int(str(d),2)

for i in range(len(MSB)):    
    variable=(Convertir_MSB(MSB[i]))
    print (variable)
    
