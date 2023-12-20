import pygame, misc

def main():
   Minesweeper = misc.Minesweeper 
   while True:
    Minesweeper.new()
    Minesweeper.run()

if __name__ == '__main__':
    main()