# Documentación de tablero.py

*Mini-juego «Hundir la flota» (versión de 1 barco de tamaño 1)*

## 1. Descripción general

`tablero.py` es un juego de consola en Python inspirado en «Hundir la flota». El programa esconde **un único barco de tamaño 1** en un tablero de **10 filas x 15 columnas** y el jugador debe adivinar su posición introduciendo coordenadas (por ejemplo `A5` o `J15`). El juego termina cuando el jugador acierta o cuando se rinde con `Ctrl+C`.

## 2. Requisitos y ejecución

- Python 3.6 o superior (usa f-strings).
- Solo utiliza la biblioteca estándar (`random`); no requiere instalar nada.

```bash
python tablero.py
```

## 3. Constantes y variables globales

| Nombre | Tipo | Descripción |
|---|---|---|
| `FILAS` | int | Número de filas del tablero (10). |
| `COLS` | int | Número de columnas del tablero (15). |
| `LETRAS` | str | Letras `"ABCDEFGHIJ"` que identifican las filas; el índice de cada letra es el índice de fila. |
| `oculto` | list[list[str]] | Tablero secreto que contiene la posición real del barco. |
| `jugador` | list[list[str]] | Tablero visible que se va actualizando con los disparos del jugador. |
| `f`, `c` | int | Fila y columna (base 0) elegidas al azar para el barco. |

## 4. Símbolos del tablero

| Símbolo | Significado | Aparece en |
|---|---|---|
| `~` | Casilla sin descubrir (agua desconocida). | `oculto` y `jugador` |
| `B` | Barco (solo visible al rendirse). | `oculto` |
| `X` | Disparo acertado. | `jugador` |
| `O` | Disparo fallado (agua). Es la letra O, no el cero. | `jugador` |

## 5. Inicialización

Ambos tableros se crean con una comprensión de listas, de modo que cada fila es una lista independiente (evitando el error típico de duplicar la misma referencia):

```python
oculto = [["~"] * COLS for _ in range(FILAS)]
jugador = [["~"] * COLS for _ in range(FILAS)]
```

A continuación se sortea la posición del barco con `random.randint` y se marca con `"B"` en `oculto`.

## 6. Funciones

**`mostrar(tablero)`** - Imprime un tablero por consola con la cabecera de columnas (1-15) y la letra de cada fila.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `tablero` | list[list[str]] | Matriz de FILAS x COLS con los símbolos a imprimir. |

No devuelve nada (`None`); solo escribe en la salida estándar.

```python
def mostrar(tablero):
    """Muestra el tablero con coordenadas."""
    print("   " + " ".join(f"{i:2}" for i in range(1, COLS + 1)))
    for i, fila in enumerate(tablero):
        print(f"{LETRAS[i]}  " + " ".join(fila))
```

## 7. Flujo del programa

- Se muestra el mensaje de bienvenida y las instrucciones.
- Bucle `while True`: se imprime el tablero del jugador y se pide una casilla; la entrada se limpia con `strip()` y `upper()`, por lo que `a5` y `A5` son equivalentes.
- Se valida el formato y el rango (ver sección 8).
- Si la casilla ya contiene `X` u `O`, se avisa de que ya se disparó ahí y no se penaliza.
- Si coincide con el barco, se marca `X`, se muestra el tablero y se termina el juego con `break` (victoria).
- Si no, se marca `O` y se muestra «Agua. Sigue intentándolo.».
- Si el usuario pulsa `Ctrl+C`, se captura `KeyboardInterrupt`, se informa de la rendición y se imprime el tablero `oculto` para revelar el barco.

## 8. Validación de la entrada

La entrada se comprueba en dos pasos: primero el formato (letra + número) y después el rango de la columna.

```python
if len(coord) < 2 or coord[0] not in LETRAS or not coord[1:].isdigit():
    print("Formato incorrecto o fila inválida. Ejemplo: A5")
    continue

fila_idx = LETRAS.index(coord[0])
col_idx = int(coord[1:]) - 1

if not (0 <= col_idx < COLS):
    print("Esa columna está fuera del tablero.")
    continue
```

| Entrada | Resultado |
|---|---|
| `A5`, `a5`, `J15` | Válida. |
| `A`, `5`, `` (vacío) | «Formato incorrecto o fila inválida». |
| `K3`, `Z1` | Fila inválida (solo A-J). |
| `A0`, `A16`, `C20` | «Esa columna está fuera del tablero». |
| `A5B`, `A-1` | «Formato incorrecto». |

## 9. Ejemplo de sesión

```text
Introduce la casilla: a5
Agua. Sigue intentándolo.

Introduce la casilla: K3
Formato incorrecto o fila inválida. Ejemplo: A5

Introduce la casilla: C20
Esa columna está fuera del tablero.

Introduce la casilla: A5
Ya has disparado aquí antes. Prueba otra.
```

## 10. Observaciones y posibles mejoras

- **Alineación de la cabecera:** los números de columna se imprimen con ancho 2 (`{i:2}`), mientras que las celdas ocupan 1 carácter, por lo que la cabecera queda desalineada respecto a las filas. Se soluciona usando el mismo ancho en ambos (por ejemplo, `" ".join(f"{c:>2}" for c in fila)`).
- **Entrada con dígitos Unicode:** `isdigit()` acepta caracteres como `²`, para los que `int()` lanza `ValueError` y el programa se cierra. Usar `isdecimal()` o capturar `ValueError` lo evita.
- **Fin de entrada (`Ctrl+D` / `Ctrl+Z`):** provoca `EOFError`, que no está capturada.
- **Sin límite de intentos ni contador:** se podría añadir un máximo de disparos o mostrar cuántos ha hecho el jugador.
- **Ampliaciones:** varios barcos, barcos de distinto tamaño o un modo de dos jugadores.
- **Estructura:** convertir el código en funciones (`crear_tablero`, `pedir_coordenada`, `jugar`) y usar `if __name__ == "__main__":` facilitaría las pruebas y su reutilización.
