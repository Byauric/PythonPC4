import requests
import sqlite3
from datetime import datetime

def obtener_tipo_cambio_desde_api():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"Error al obtener datos de la API: {e}")
        return None

def actualizar_tipo_cambio():
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()
    datos_api = obtener_tipo_cambio_desde_api()

    if datos_api:
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO tipo_cambio (moneda_origen, moneda_destino, tasa_cambio, fecha_actualizacion)
            VALUES (?, ?, ?, ?)
        ''', (*datos_api, fecha_hora_actual))

        print("Tipo de cambio actualizado con éxito.")
        conexion.commit()
        conexion.close()
actualizar_tipo_cambio()