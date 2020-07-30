import pygame
from Ship import *
from Asteroid import *

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (30, 0, 30)

player = Ship()
#a class is a blueprint
obstacle = Asteroid()

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    player.update()
    screen.blit(player.image, player.rect)
    screen.blit(obstacle.image, obstacle.rect)
    pygame.display.flip()
    
    
if __name__ == '__main__':
  main()
