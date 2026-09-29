"""
Módulo de juego: Hundir la Flota (Battleship)
==============================================
Este módulo contiene la lógica principal para inicializar un tablero de juego,
posicionar de forma aleatoria un barco y gestionar la interacción por consola 
con el usuario hasta que encuentre el objetivo o se rinda.

Autores: Iván Guijarro Verbo
Versión: 1.0.0
"""

import random

# ==========================================
# CONSTANTES Y CONFIGURACIÓN DEL TABLERO
# ==========================================

FILAS: int = 10
"""int: Número de filas del tablero de juego."""

COLS: int = 15
"""int: Número de columnas del tablero de juego."""

LETRAS: str = "ABCDEFGHIJ"
"""str: Cadena con las letras correspondientes a los índices de las filas (A-J)."""

# ==========================================
# INICIALIZACIÓN DE TABLEROS
# ==========================================

oculto: list[list[str]] = [["~"] * COLS for _ in range(FILAS)]
"""list[list[str]]: Tablero interno que contiene la posición real del barco ('B') y agua ('~')."""

jugador: list[list[str]] = [["~"] * COLS for _ in range(FILAS)]
"""list[list[str]]: Tablero visible para el usuario con sus disparos previas ('X' para tocado, 'O' para agua)."""

# Colocar 1 barco de tamaño 1 de manera aleatoria
f: int = random.randint(0, FILAS - 1)
c: int = random.randint(0, COLS - 1)
oculto[f][c] = "B"


def mostrar(tablero: list[list[str]]) -> None:
    """Imprime por consola el tablero formateado con sus coordenadas.

    Muestra una cabecera superior con los números de columna (1 a COLS)
    y una columna izquierda con las letras de fila (A a J).

    Args:
        tablero (list[list[str]]): Matriz bidimensional que representa el 
            tablero a imprimir (ya sea el visible o el oculto).

    Example:
        >>> mostrar(jugador)
           1  2  3  4 ...
        A  ~  ~  ~  ~ ...
        B  ~  ~  ~  ~ ...
    """
    print("   " + " ".join(f"{i:2}" for i in range(1, COLS + 1)))
    for i, fila in enumerate(tablero):
        print(f"{LETRAS[i]}  " + " ".join(fila))


def jugar() -> None:
    """Ejecuta el bucle principal del juego Hundir la flota.

    Solicita coordenadas al usuario por consola (ej. 'A5'), valida la entrada,
    actualiza el tablero e indica si ha habido impacto o agua.
    El juego finaliza cuando el usuario acierta la posición o interrumpe la
    ejecución mediante Ctrl+C.
    """
    print("¡Bienvenido a Hundir la flota! (Pulsa Ctrl+C en cualquier momento para rendirte)")
    print("Adivina dónde está el barco. Introduce una coordenada (ej. A5 o J15).")

    try:
        while True:
            mostrar(jugador)
            coord: str = input("\nIntroduce la casilla: ").strip().upper()
            
            # Validación de formato aglutinada
            if len(coord) < 2 or coord[0] not in LETRAS or not coord[1:].isdigit():
                print("Formato incorrecto o fila inválida. Ejemplo: A5")
                continue
                
            fila_idx: int = LETRAS.index(coord[0])
            col_idx: int = int(coord[1:]) - 1

            if not (0 <= col_idx < COLS):
                print("Esa columna está fuera del tablero.")
                continue

            if jugador[fila_idx][col_idx] in ("X", "O"):
                print("Ya has disparado aquí antes. Prueba otra.")
            elif oculto[fila_idx][col_idx] == "B":
                jugador[fila_idx][col_idx] = "X"
                mostrar(jugador)
                print("\n¡HAS ACERTADO! Has encontrado el barco. ¡Ganaste!")
                break
            else:
                jugador[fila_idx][col_idx] = "O"
                print("Agua. Sigue intentándolo.")

    except KeyboardInterrupt:
        # Se ejecuta si el usuario cancela el programa (Ctrl + C)
        print("\n\nJuego terminado. Te has rendido.")
        print("Aquí es donde estaba escondido el barco:")
        mostrar(oculto)


if __name__ == "__main__":
    jugar()