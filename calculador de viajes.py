import sys
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad):
    """Obtiene las coordenadas de una ciudad usando geopy."""
    # Definimos un user_agent para identificarnos ante la API gratuita de OpenStreetMap
    geolocator = Nominatim(user_agent="calculador_viajes_cl_ar")
    try:
        location = geolocator.geocode(ciudad)
        if location:
            return (location.latitude, location.longitude), location.address
        return None, None
    except Exception:
        return None, None

def calcular_viaje():
    print("==================================================")
    print(" CALULADOR DE VIAJES:  ")
    print("==================================================")
    print("Nota: Puedes presionar la letra 's' en cualquier momento para salir.\n")

    while True:
        # 1. Solicitar Ciudad de Origen
        origen = input("Ingrese la Ciudad de Origen: ").strip()
        if origen.lower() == 's':
            break
            
        # 2. Solicitar Ciudad de Destino
        destino = input("Ingrese la Ciudad de Destino: ").strip()
        if destino.lower() == 's':
            break

        # 3. Elegir medio de transporte
        print("\nSeleccione el medio de transporte a utilizar:")
        print("1. Auto (Velocidad prom: 90 km/h)")
        print("2. Autobús (Velocidad prom: 70 km/h)")
        print("3. Avión (Velocidad prom: 800 km/h)")
        opcion = input("Elija una opción (1-3) o 's' para salir: ").strip()

        if opcion.lower() == 's':
            break

        medios = {
            "1": {"nombre": "Auto", "velocidad": 90},
            "2": {"nombre": "Autobús", "velocidad": 70},
            "3": {"nombre": "Avión", "velocidad": 800}
        }

        if opcion not in medios:
            print(" Opción no válida. Volviendo a empezar.\n")
            continue

        transporte = medios[opcion]

        print("\nBuscando ubicaciones en el mapa... 🔄")
        coord_origen, dir_completa_origen = obtener_coordenadas(origen)
        coord_destino, dir_completa_destino = obtener_coordenadas(destino)

        if not coord_origen or not coord_destino:
            print(" No se pudo encontrar alguna de las ciudades. Intenta ser más específico (ej: 'Santiago, Chile' o 'Mendoza, Argentina').\n")
            continue

        # 4. Calcular distancias
        # Calculamos la distancia en línea recta (geodésica)
        distancia_km = geodesic(coord_origen, coord_destino).kilometers
        distancia_mi = distancia_km * 0.621371

        # 5. Calcular duración del viaje
        duracion_horas = distancia_km / transporte["velocidad"]
        horas = int(duracion_horas)
        minutos = int((duracion_horas - horas) * 60)

        # 6. Mostrar resultados en pantalla
        print("\n" + "="*50)
        print(" RESUMEN DEL VIAJE")
        print("="*50)
        print(f" Origen: {dir_completa_origen}")
        print(f" Destino: {dir_completa_destino}")
        print(f" Transporte: {transporte['nombre']}")
        print(f" Distancia en Kilómetros: {distancia_km:.2f} km")
        print(f" Distancia en Millas: {distancia_mi:.2f} mi")
        print(f" Duración aproximada: {horas} horas y {minutos} minutos")
        print("-" * 50)
        
        # 7. Mostrar la narrativa del viaje
        narrativa = (
            f"Tu aventura comenzará saliendo desde {dir_completa_origen.split(',')[0]}, con un viaje planificado "
            f"hacia {dir_completa_destino.split(',')[0]}. Para cruzar las fronteras y llegar a tu destino, "
            f"has seleccionado viajar en {transporte['nombre'].lower()}. "
            f"El trayecto implica recorrer una distancia aproximada de {distancia_km:.2f} km "
            f"({distancia_mi:.2f} millas). Si las condiciones de la ruta son ideales y mantienes "
            f"una velocidad promedio constante, estarás llegando a tu destino en aproximadamente "
            f"{horas} horas y {minutos} minutos. ¡Disfruta el viaje!"
        )
        print(" NARRATIVA:")
        print(narrativa)
        print("="*50 + "\n")

    print("\n ¡Gracias! Programa finalizado.")

if __name__ == "__main__":
    calcular_viaje()
