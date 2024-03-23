import pandas as pd
from joblib import load

# Función para cargar el modelo entrenado
def cargar_modelo_entrenado(ruta_al_modelo):
    modelo_cargado = load(ruta_al_modelo)
    return modelo_cargado

# Función para realizar predicciones
def hacer_predicciones(datos_entrada, modelo):
    predicciones = modelo.predict(datos_entrada)
    pd.DataFrame(predicciones, columns=['Predicción']).to_csv('src/data/predictions/predicciones.csv', index=False)
    print("Predicciones realizadas con éxito y guardadas en 'src/data/predictions/predicciones.csv'.")
    datos_salida = pd.read_csv('src/data/predictions/predicciones.csv')
    print(datos_salida.head())

# Cargar modelo
ruta_modelo = 'src/model/mejor_modelo.joblib'
modelo = cargar_modelo_entrenado(ruta_modelo)

variables = ['height(cm)', 'weight(kg)', 'waist(cm)', 'hemoglobin', 'ALT', 'Gtp', 'serum creatinine', 'dental caries', 'Lipid_Component']

metodo_entrada = input("Escribe 'cargar' para cargar un archivo CSV o 'manual' para ingresar datos manualmente: ").strip().lower()

if metodo_entrada == 'cargar':
    ruta_archivo = input("Introduce la ruta completa al archivo CSV: ")
    datos_entrada = pd.read_csv(ruta_archivo)
    datos_entrada = datos_entrada[variables]
    hacer_predicciones(datos_entrada, modelo)
elif metodo_entrada == 'manual':
    
    datos_manuales = {}
    
    for var in variables:
        dato_valido = False
        while not dato_valido:
            try:
                dato = float(input(f"Ingrese el valor de {var}: "))
                datos_manuales[var] = dato
                dato_valido = True
            except ValueError:
                print("Por favor, ingresa un número válido.")
    

    datos_entrada_manual = pd.DataFrame([datos_manuales])
    hacer_predicciones(datos_entrada_manual, modelo)
else:
    print("Entrada no reconocida. Por favor, escribe 'cargar' o 'manual'.")
