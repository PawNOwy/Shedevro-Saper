import pygame, os

# Тут ишачий конфиг
TILESIZE = 40
ROWS = 10
COLS = 10
AMOUNT_MINES = 10
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60
TITLE = "Сапёрдёрпер 🤓"

# Отсюда идут важные штучки

tile_numbers = [] # Получает соседов (мины) и добавляет в список
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

# Переменные для спрайтов
tile_discovered = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Tile.png")), (TILESIZE, TILESIZE))
tile_bomb = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileBomb.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileFlag.png")), (TILESIZE, TILESIZE))
tile_undiscovered = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileUndiscovered.png")), (TILESIZE, TILESIZE))
tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "TileEmpty.png")), (TILESIZE, TILESIZE))