limite= int(input("Escoja un valor: "))
#Esta funcion suma iterativametne los numeros 
def sumaIterativa (n):
    resultado=0
    for i in range(1,n+1):
        #print(resultado,"y",i)
        #resultado=resultado+i
        resultado+=i
    return resultado

suma=sum(range(1,limite+1))
print("Resultado funcion propia= ",sumaIterativa(limite))
print("Resultado segunda opción= ",suma)