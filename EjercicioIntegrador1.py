venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
venta_dia = 0
descuento = 0
for i in range(10):
	if venta_productos[i]:
		venta_dia += venta_productos[i][1]
	

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
	venta = (venta_dia+cajas_vender) > 1500
	if venta:
		descuento = (cajas_vender*precio) * 0.20

	precio_total = round((cajas_vender * precio) - descuento,2)

	if cajas_vender <= 100:
	 	precio_total += 1500
	 	
	print("\nSalida:")
	print( f"El producto es: {nombre_producto}" )
	print( f"El precio por caja es: {precio}" )
	print( f"Aplica descuento del 20%: {venta}" )
	print( f"El costo total a pagar: {precio_total}" )
