import pygame
import os
from classes import *
import time
import random
from pygame import key
pygame.font.init()
pygame.init()

run = True
pygame.display.set_caption("Rodents Rebooted")

window = WIDTH, HEIGHT = 750, 750
screen = pygame.display.set_mode(window)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rodents Rebooted")




wood = [WOOD_1, WOOD_2, WOOD_3, WOOD_4]
#wood = WOOD_1
LEFT_COLLIDE = 0
RIGHT_COLLIDE = 1
TOP_COLLIDE = 2
BOTTOM_COLLIDE = 3


  # def update(self):
  #      self.image = pygame.transform.rotate(self.rat_img, self.angle)
  #      self.angle += 1 % 360
  #      x, y = self.rect
  #      self.rect = self.rat_img_rect()
  #      self.rect.center = (x.y)

def main():
    run = True
    FPS = 60
    hits = 3
    level = 0
    hits_font = pygame.font.SysFont("comicsans", 30)
    level_font = pygame.font.SysFont("comicsans", 30)
    player_vel = 7
    clock = pygame.time.Clock()
    player = Rat(WIDTH/2, HEIGHT/2)
    wood = Block(WIDTH/4,HEIGHT/4)
    clock_font= pygame.font.SysFont("impact", 20)
    player_pos = (player.x, player. y)

    def redraw_window():
        #Since the window is the thing drawing everything, fill it blank before every redraw to avoid
        #   that pesky issue where colored rects stay drawn in black/background corners.
        WIN.fill(0)
        WIN.blit(BG, (0,0))
        player.draw(WIN)
        wood.draw(WIN)
        #draw_grid(wood)
        #pygame.draw.rect(WIN, pygame.color.Color(200, 0, 0), player.rect)
        hits_label = hits_font.render(f"Hits: {hits}", 1, (149,11,9))
        level_label = level_font.render(f"Level: {level}", 1, (149,11,9))
        clock_label = clock_font.render(f"FPS: {clock}", 1, (149,11, 9))

        WIN.blit(hits_label, (20,20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        WIN.blit(clock_label, ( 20,HEIGHT - clock_label.get_height() - 20,))
        #WIN.blit(player.rect)
        #screen.blit(RAT, (WIDTH/2, HEIGHT/2))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        clock.tick(FPS)
        #pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        collision = collide(player, wood)
        if collision == True:
            if player.y > wood.y + wood.get_height()/2 - 10 and wood.y > 0:
                wood.move(0, -player_vel)
            elif player.y < wood.y - wood.get_height()/2 + 10 and  wood.y + wood.get_height() < HEIGHT:
                wood.move(0, player_vel)
            elif player.x > wood.x + wood.get_width()/2 + 10 and wood.x > 0:
                wood.move(-player_vel, 0)
            elif player.x < wood.x - wood.get_width()/2 - 10 and wood.x + wood.get_width() < WIDTH:
                wood.move(player_vel, 0)



#changing if to elif constrains to one direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            Rat.rotate(player, 90)
            player.move(-player_vel, 0)
            if player.collide_dir(wood.rect) == LEFT_COLLIDE and wood.x <= 0:
                player.move(player_vel, 0)
        elif keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:
            Rat.rotate(player, 270)
            player.move(player_vel, 0)
            if player.collide_dir(wood.rect) == RIGHT_COLLIDE and wood.x + wood.get_width() >= WIDTH:
                player.move(-player_vel, 0)
        elif keys[pygame.K_w] and player.y - player_vel > 0:
            Rat.rotate(player, 0)
            player.move(0, -player_vel)
            if player.collide_dir(wood.rect) == TOP_COLLIDE and wood.y <= 0:
                player.move(0, player_vel)
        elif keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
            Rat.rotate(player, 180)
            player.move(0, player_vel)
            if player.collide_dir(wood.rect) == BOTTOM_COLLIDE and wood.y + wood.get_height() >= HEIGHT:
                player.move(0, -player_vel)

        pygame.display.update()


main()

pygame.quit()

