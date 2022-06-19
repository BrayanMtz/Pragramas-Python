#Variables de los datos establecidos
estado = "Sinaloa"
superficie_km2 = 52365
localizacion = "noroeste del pais"
clima = "cálido, subhúmedo, seco y semiseco"
temperatura_media_anual = 25.45
precipitacion_anual = 790.1
poblacion_mujeres = 1532128
poblacion_hombres = 1494815
procentaje_habitante_Culiacan = 33.15
procentaje_habitante_Mazatlan = 16.57

#Nuevas variables

#La poblacion total entre hombres y mujeres.
poblacion_total = poblacion_hombres + poblacion_mujeres
print( f"La poblacion total es: {poblacion_total}" )

#El porcentaje total de la población entre Culiacán y Mazathán.
porcentaje_total_poblacion = procentaje_habitante_Culiacan + procentaje_habitante_Mazatlan
print( f"El porcentaje total de la poblacion es: {porcentaje_total_poblacion}%" )

#La temperatura media anual y los tipos de clima
temperatura_clima = str(temperatura_media_anual) + " °C y los tipos de clima: "+ clima
print( f"Temperatura anual : {temperatura_clima}" )
