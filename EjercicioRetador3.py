peso_maximo = 3254
peso_minimo = 3254/2
peso_costal_semento = 40
peso_costal_yeso = 30

print("Entrada:")
pedido_cemento = int( input("Número de costales de cemento (kg): ") )
pedido_yeso = int( input("Número de costales de yeso (kg): ") )

peso_total = (pedido_cemento*peso_costal_semento) + (pedido_yeso*peso_costal_yeso)
puede_eviarse = peso_total <= peso_maximo and peso_total >= peso_minimo

print( "\nSalida:" )
print( f"El peso total en kg es: {peso_total}" )
print( f"¿Se puede realizar el envio?: {puede_eviarse}" )
