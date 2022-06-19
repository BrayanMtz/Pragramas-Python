print("Entrada:")
cajas_vender = int(input("Número de cajas a vener: "))
id_producto = int(input("ID del producto: "))

if id_producto == 1:
	nombre_producto = "Maíz grano"
	precio = 285.55
elif id_producto == 2:
	nombre_producto = "Pepino"
	precio = 334.72
elif id_producto == 3:
	nombre_producto = "Tomate verde"
	precio = 129
else:
	id_producto = 4
	print("ID no encontrado!!")

if id_producto != 4:	
	precio_total = round( (cajas_vender * precio), 2 )
	
	if cajas_vender <= 100:
	 	precio_total += 1500

	print( "\nSalida:" )
	print( f"El producto es: {nombre_producto}" )
	print( f"El precio por caja es: {precio}" )
	print( f"El costo total a pagar: {precio_total}" )
