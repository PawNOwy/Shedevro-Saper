import random, pygame
from config import *

class Tile:     #Какие-то там клеточкиэээ
    def __init__(self, x, y, image, type, revealed=False, flagged=False): # Инитиализатион 🤣
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def draw(self, grid_surface):       # Рисаватъ па паверхнастиээ
        if not self.flagged and self.revealed:
            grid_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            grid_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            grid_surface.blit(tile_undiscovered, (self.x, self.y))


class Grid:
    def __init__(self):
        self.grid_surface = pygame.Surface((WIDTH, HEIGHT))
        self.grid_list = [[Tile(col, row, tile_empty, "Empty") for row in range(ROWS)] for col in range(COLS)]
        self.place_mines()
        self.place_clues()
        self.dug = []

    def place_mines(self):
        for _ in range(AMOUNT_MINES):
            while True:
                x = random.randint(0, ROWS-1)
                y = random.randint(0, COLS-1)

                if self.grid_list[x][y].type == "Empty":
                    self.grid_list[x][y].image = tile_undiscovered
                    self.grid_list[x][y].type = "Bomb"
                    break

    def place_clues(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.grid_list[x][y].type != "Bomb":
                    total_mines = self.check_neighbours(x, y)
                    if total_mines > 0:
                        self.grid_list[x][y].image = tile_numbers[total_mines-1]
                        self.grid_list[x][y].type = "Clue"


    @staticmethod
    def is_inside(x, y):
        return 0 <= x < ROWS and 0 <= y < COLS

    def check_neighbours(self, x, y):
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                neighbour_x = x + x_offset
                neighbour_y = y + y_offset
                if self.is_inside(neighbour_x, neighbour_y) and self.grid_list[neighbour_x][neighbour_y].type == "Bomb":
                    total_mines += 1

        return total_mines

    def draw(self, screen):
        for row in self.grid_list:
            for tile in row:
                tile.draw(self.grid_surface)
        screen.blit(self.grid_surface, (0, 0))

    def dig(self, x, y):
        self.dug.append((x, y))
        if self.grid_list[x][y].type == "Bomb":
            self.grid_list[x][y].revealed = True
            self.grid_list[x][y].image = tile_bomb
            return False
        elif self.grid_list[x][y].type == "Clue":
            self.grid_list[x][y].revealed = True
            return True

        self.grid_list[x][y].revealed = True

        for row in range(max(0, x-1), min(ROWS-1, x+1) + 1):
            for col in range(max(0, y-1), min(COLS-1, y+1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def display_grid(self):
        for row in self.grid_list:
            pass
