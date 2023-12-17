# EJERCICIO 2

# 2.1.
import os
from pyfiglet import Figlet
Figlet = Figlet()
import random

ruta_main_py = '/workspaces/PythonPC4/main.py'
fuentes_disponibles = Figlet.getFonts()
fuente_seleccionada = random.choice(fuentes_disponibles)
figlet = Figlet.setFont(font=fuente_seleccionada)

texto_imprimir = "Bienvenidos a store DatuxTec"

print(figlet.renderText(texto_imprimir))

comando_ejecucion = f'python {ruta_main_py}'
os.system(comando_ejecucion)

