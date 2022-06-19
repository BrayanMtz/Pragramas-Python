lista_minicipio = []
lista_habitantes = []
total_habitantes = 0

print( "Entrada:" )
for i in range(3):
	lista_minicipio.append( input( f"Ingresa el municipio {i+1}: ") )
	lista_habitantes.append( input( f"Ingrese el numero de habitantes de {lista_minicipio[i]}: ") ) 
	total_habitantes += int(lista_habitantes[i])


print( "\nSalida:" )
print( f"El total de habitantes es: {total_habitantes}" )
promedio = round( (total_habitantes/3) , 2 )
print( f"El promedio de habitantes es: {promedio}" ) 

