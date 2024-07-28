from IPython.display import clear_output


class Juego:
    def __init__(self, filas, columnas):
        # self._tablero = [['.'] * columnas] * filas #works on jupiter notebook but not pycharm
        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crear_tablero()

    def crear_tablero(self):
        tablero = [None] * self._filas
        for f in range(self._filas):
            tablero[f] = ['.'] * self._columnas
        return tablero

    def mostrar_tablero(self):
        for num in range(len(self._columnas)):
            print(num, end=" ")
        for fila in self._tablero:
            print("")
            for celda in fila:
                print(celda, end=" ")

    def introducir_ficha(self, columna, color):
        if len(self._columnas) > columna >= 0:
            for fila in reversed(range(len(self._tablero))):
                if self._tablero[fila][columna] == '.':
                    self._tablero[fila][columna] = color
                    break
            else:
                print("Columna llena")
        else:
            print("Columna invalida")

    def revisar_filas(self, color):
        for fila in range(len(self._tablero)):
            contador = 0
            for celda in self._tablero[fila]:
                if celda == color:
                    contador += 1
                else:
                    contador = 0
                if contador >= 4:
                    return True
        return False

    def revisar_columnas(self, color):
        for columna in range(len(self._columnas)):
            contador = 0
            for celda in range(len(self._tablero)):
                if self._tablero[celda][columna] == color:
                    contador += 1
                else:
                    contador = 0
                if contador >= 4:
                    return True
        return False

    def revisar_diagonal_derecha(self, color):
        for fi in range(len(self._tablero) - 3):
            for col in range(3, len(self._columnas)):
                if (self._tablero[fi][col] == self._tablero[fi + 1][col - 1] == self._tablero[fi + 2][col - 2] ==
                        self._tablero[fi + 3][col - 3] == color):
                    return True
        return False

    def revisar_diagonal_izquierda(self, color):
        for fi in range(len(self._tablero) - 3):
            for col in range(0, len(self._columnas) - 3):
                if (self._tablero[fi][col] == self._tablero[fi + 1][col + 1] == self._tablero[fi + 2][col + 2] ==
                        self._tablero[fi + 3][col + 3] == color):
                    return True
        return False

    def comprobar_ganador(self, color):
        if (self.revisar_filas(color) or self.revisar_columnas(color) or
                self.revisar_diagonal_derecha(color) or self.revisar_diagonal_izquierda(color)):
            return True
        return False

    def jugar(self):
        turnos = ['R', 'A']
        contador = 0
        input_text = {"R": "Turno del rojo: ", "A": "Turno del amarillo: "}
        while True:
            contador += 1
            turno = turnos[contador % 2]
            self.mostrar_tablero()
            columna = int(input(input_text[turno]))
            self.introducir_ficha(columna, turno)
            clear_output(wait=False)
            if self.comprobar_ganador(turno):
                print("Ganador el jugador ", turno, "\n\n")
                self.mostrar_tablero()
                break


juego1 = Juego(6, 7)
juego1.jugar()
