# ---------------------------------------------------------
# Archivo base: calculadora.py
# Autor: Ian Bonilla Mena
# Rol: Líder / Aprobador
# Descripción:
#   Este archivo contiene la estructura base del programa.
#   Será modificado por los desarrolladores (Dev1 y Dev2)
#   durante el flujo de trabajo colaborativo en GitHub.
# ---------------------------------------------------------

def calcular_precio(precio):
    """
    Calcula el precio final de un producto.
    Actualmente solo retorna el precio original.
    Dev1 y Dev2 deberán modificar esta función.
    """
    return precio


if __name__ == "__main__":
    print("=== Calculadora de Precio Final ===")
    try:
        valor = float(input("Ingrese el precio del producto: "))
        total = calcular_precio(valor)
        print(f"El precio final es: {total}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")
