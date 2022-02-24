from lxml import etree
import sys
metro = etree.parse(sys.argv[1])


coordenadas = metro.xpath('//Document/Folder[1]/Placemark/LineString/coordinates')  #guardamoos las coordenadas y linea del metro asociada
linea =  metro.xpath('//Document/Folder[1]/Placemark/name')

linea_cord = {}                                                          #hacemos un diccionario para juntarlos y asociarlos 
for i in range (len(coordenadas)):
    linea_cord[linea[i].text]= coordenadas[i].text


estacion= metro.xpath('//Document/Folder[2]/Placemark/name')                    # guardamos y asociamos en un diccionario  la estacion y su ubicacion
ubicacion = metro.xpath('//Document/Folder[2]/Placemark/Point/coordinates')  
estacion_ubi = {}
for c in range (len(estacion)): 
    estacion_ubi[estacion[c].text] =  ubicacion[c].text 


metro_lineas= {}                                                                 # hacemos otro diccionario que asocia Linea y estacion
for key, value in linea_cord.items():
    for key_estacion_ubi, value_estacion_ubi in estacion_ubi.items():
        if value_estacion_ubi in value:
            metro_lineas.update( {key:[key_estacion_ubi] } )

for key, value in linea_cord.items():                                           # en este for hacemos append a las estaciones
    for key_estacion_ubi, value_estacion_ubi in estacion_ubi.items():
        if value_estacion_ubi in value:
            metro_lineas[key].append(key_estacion_ubi)


for key,value in metro_lineas.items():                                      # Imprimimos los valores de nuestro diccionario
    print(f"""
        {key} tiene las estaciones:
        {value}
    """)
                    