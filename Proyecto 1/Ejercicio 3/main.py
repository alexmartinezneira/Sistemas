def Pregunta_1(byte,Vdd):
    b=byte
    vdd=Vdd
    def Resolucion(b):
        
        resolucion=(8*b)-2
        
        
        return resolucion

    def Maximo(vdd):
        return 'hola'

    def Minimo(b):
        voltaje=vdd
        b=Resolucion(b)
        cap=pow(2,b)

        minimo=(voltaje/cap)*1000
        d=str(minimo).split('3')
        return d[0]

    return Resolucion(b),Maximo(b),Minimo(b)

def Pregunta_2(Vref,Vin):
    ref=Vref
    vin=Vin

    Adres=pow(2,14)*((vin-0)/(ref-0))
    binario=bin(int(Adres))

    return binario

def Pregunta_3(Adres):
    lsb=23

    
    
    return lsb

    
byte=2
Vdd=9
Adres=0b0011000
Vref=23
Vin=3

#print('El maximo de resolucion del Convertidor es: '+str(Pregunta_1(byte,Vdd)[2])+' bits')
#print('El minimo voltaje que puede analizar el  Convertidor es: '+str(Pregunta_1(byte,Vdd)[2])+' mV')

#print('El valor que hay en Adres es: '+str(Pregunta_2(Vref,Vin))+' bits')
print('El valor que hay en Adres es: '+str(Pregunta_3(Adres))+' bits')


