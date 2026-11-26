"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación
Problema 3: Control de inventario y reabastecimiento

El programa identifica los artículos cuyo stock actual está por debajo
del stock mínimo requerido y calcula cuántas unidades se deben pedir.
"""

def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """Retorna la cantidad necesaria para alcanzar el stock mínimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_reporte(inventario):
    """Muestra el nombre de cada artículo y la cantidad que debe pedirse."""
    print("\nREPORTE DE REABASTECIMIENTO")
    print("-" * 55)
    print(f"{'Artículo':<22}{'Stock actual':>14}{'Cantidad a pedir':>19}")
    print("-" * 55)

    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        cantidad = calcular_cantidad_pedir(stock_actual, stock_minimo)
        print(f"{nombre:<22}{stock_actual:>14}{cantidad:>19}")

    print("-" * 55)


def main():
    # Matriz: [código, nombre, stock actual, stock mínimo requerido]
    inventario = [
        [101, "Cuaderno", 12, 20],
        [102, "Lapicero", 35, 25],
        [103, "Borrador", 8, 15],
        [104, "Regla", 10, 10],
        [105, "Marcador", 4, 12]
    ]

    mostrar_reporte(inventario)


if __name__ == "__main__":
    main()
