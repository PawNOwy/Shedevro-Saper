import pygame, sys
from config import *
from pygame_sprites import *


class Minesweeper:      #Сапёрпёрдпер
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self):      #Новая игра
        self.grid = Grid()
        self.grid.display_grid()

    def run(self):      #Запуск
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()

    def draw(self):     #Создание ишачьего поля 🤓🤓🤓
        self.screen.fill((40, 40, 40))
        self.grid.draw(self.screen)
        pygame.display.flip()

    def check_win(self): #Это вообще зачем 😭
        for row in self.grid.grid_list:
            for tile in row:
                if tile.type != "Bomb" and not tile.revealed:
                    return False
        return True

    def events(self):       # Ивентикииии (мышка по туториалу, т.к. не знал)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.grid.grid_list[mx][my].flagged:
                        # dig and check if exploded
                        if not self.grid.dig(mx, my):
                            # explode
                            for row in self.grid.grid_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "Bomb":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_discovered
                                    elif tile.type == "Bomb":
                                        tile.revealed = True
                            self.playing = False

                if event.button == 3:
                    if not self.grid.grid_list[mx][my].revealed:
                        self.grid.grid_list[mx][my].flagged = not self.grid.grid_list[mx][my].flagged

                if self.check_win():
                    self.win = True
                    self.playing = False
                    for row in self.grid.grid_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True

    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return


game = Minesweeper()
while True:
    game.new()
    game.run()