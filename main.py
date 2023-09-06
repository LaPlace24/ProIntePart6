import readchar
import random
import os
from functools import reduce

WALL_CHAR = "#"
PATH_CHAR = "."
PLAYER_CHAR = "P"

class Juego:
    def __init__(self, maze_string, start, end):
        self.maze_matrix = self.convert_to_matrix(maze_string)
        self.start = start
        self.end = end

    def convert_to_matrix(self, maze_string):
        return list(map(list, maze_string.split("\n")))

    def print_maze(self):
        for row in self.maze_matrix:
            print("".join(row))

    def main_loop(self):
        px, py = self.start
        self.maze_matrix[py][px] = PLAYER_CHAR
        self.print_maze()
        while (px, py) != self.end:
            key = readchar.readkey()
            if key == readchar.key.UP and py > 0 and self.maze_matrix[py - 1][px] != WALL_CHAR:
                self.maze_matrix[py][px] = PATH_CHAR
                py -= 1
            elif key == readchar.key.DOWN and py < len(self.maze_matrix) - 1 and self.maze_matrix[py + 1][px] != WALL_CHAR:
                self.maze_matrix[py][px] = PATH_CHAR
                py += 1
            elif key == readchar.key.RIGHT and px < len(self.maze_matrix[py]) - 1 and self.maze_matrix[py][px + 1] != WALL_CHAR:
                self.maze_matrix[py][px] = PATH_CHAR
                px += 1
            elif key == readchar.key.LEFT and px > 0 and self.maze_matrix[py][px - 1] != WALL_CHAR:
                self.maze_matrix[py][px] = PATH_CHAR
                px -= 1
            self.maze_matrix[py][px] = PLAYER_CHAR
            print("\033[H\033[J")  # Clear the terminal
            self.print_maze()

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        archivo = random.choice(os.listdir(path_a_mapas))
        archivo_completo = os.path.join(path_a_mapas, archivo)
        mapa_datos = self.leer_mapa_archivo(archivo_completo)
        super().__init__(*mapa_datos)

    def leer_mapa_archivo(self, archivo):
        with open(archivo, "r") as f:
            lineas = f.read().splitlines()
            start = tuple(map(int, lineas[0].strip().split(",")))
            end = tuple(map(int, lineas[1].strip().split(",")))
            maze_string = "\n".join(lineas[2:]).strip()
            return maze_string, start, end


def main():
    path_a_mapas = "mapas"
    juego = JuegoArchivo(path_a_mapas)
    juego.main_loop()

if __name__ == "__main__":
    main()
