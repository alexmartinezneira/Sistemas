def Trama(n):
    binario=(str(bin(n)))                                   #Se convierte el numero en binario y en cadena de texto
    caracter=(binario.split('0b'))                          #Se separa la conversion en un arreglo de 2 valores,
                                                            #en la posicion 0 va estar '0b' y en la posicion 1 la conversion a binario

    trama=caracter[1]                                       #Se seleciona la posicion 1 del arreglo 
    array=([0]*len(trama))                                  #Se crea un arreglo del tamaño de la conversion binaria
    
    for i in range(len(trama)):                             #Ciclo for el cual sirve para rellenar el arreglo array
        array[i]=int(trama[i])                              #en el cual se guardara cada bit de la conversion a binario 

    def Data(array):                                        #Funcion para encontrar valor del Dato de la conversion 
        data=0
        array.reverse()
        for i in range(len(array)):
            if(i>=2 and i<=9):
                if((array[i]!=0)):
                    data+=pow(2,i-2)
                    
        return (hex(data))                                       #retorna el dato de forma decimal 

    def Direccion(array):                                   #Funcion para ver en que direccion de memoria se va a escribir o leer el data
        data=0
        array.reverse()
        for i in range(len(array)):
            if(i>=10 and i<=17):
                if((array[i]!=0)):
                    data+=pow(2,i-10)
                    
        return hex(data)                                       #retorna el dato de forma decimal 
    
    def Operacion(array):                                   #Funcion para obtener la operacion que se va a realizar 0 para Leer 1 para Escribir
    
       array.reverse()
       data=array[18]
       return hex(data)
    
    def Device(array):                                      #Funcion para ver que dispositivo se va a utilizar 
        data=0
        array.reverse()
        for i in range(len(array)):
            if(i>=19 and i<=21):
                if((array[i]!=0)):
                    data+=pow(2,i-19)
        return hex(data)
    
    return Data(array),Direccion(array),Operacion(array),Device(array)      #Retorna todas las funciones anidadas 
    

n=[179900835,177765503,179570763,177904163]             #Se ingresa el numero en su  forma decimal 

for i in range(len(n)):
    
    print("+---------------------------------------------------+")
    print("|   El resultado del numero: "+str(n[i])+'              |')
    print('|   El valor del dato es: '+str(Trama(n[i])[0])+'                      |')                            #Se manda a llamar a la Funcion Trama y devuelve la funcion Anidada Data 
    print('|   El valor de la direccion de memoria es: '+str(Trama(n[i])[1])+'    |')          #Se manda a llamar a la Funcion Trama y devuelve la funcion Anidada Direccion 
    print('|   El valor de la operacion  es: '+str(Trama(n[i])[2])+'               |')                    #Se manda a llamar a la Funcion Trama y devuelve la funcion Anidada Operacion 
    print('|   El valor del dispositivo  es: '+str(Trama(n[i])[3])+'               |')                    ##Se manda a llamar a la Funcion Trama y devuelve la funcion Anidada Device
print('+---------------------------------------------------+')

    
    
