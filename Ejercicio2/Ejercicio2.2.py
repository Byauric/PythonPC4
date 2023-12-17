# 2.2. 
import sqlite3

def config():
    conexion = sqlite3.connect('modulos.db')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tipo_cambio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moneda_origen TEXT,
            moneda_destino TEXT,
            tasa_cambio REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            email TEXT
        )
    ''')
    cursor = conexion.cursor() 
    conexion.commit()
    conexion.close()
    print(cursor)

    
