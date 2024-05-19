import pygame
import numpy as np
from box import Box
from board_game_map import BoardTile
from board_map import *
from player import Player
from enemy import Enemy

WIDTH, HEIGHT = 800, 650
FPS = 60

pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

run = True

def draw_window(win, board_group, player, enemies_group):
    win.fill((30,30,30))
    board_group.draw(win)
    enemies_group.draw(win)
    win.blit(player.image, player.rect)
    pygame.display.update()

def check_collision(player, enemies):
    collison = pygame.sprite.spritecollide(player, enemies, False)
    if len(collison) > 0:
        print(collison[0].behavior)



maps = BoardMap()

board_wall = pygame.sprite.Group()
cell, row = board_map.shape
for r in range(row):
    for c in range(cell):
        if board_map[c,r] != 0:
            board_wall.add(BoardTile(board_map[c,r], r, c))

player = Player(45,45)
all_enemies = pygame.sprite.Group()
all_enemies.add(Enemy(player, 4,5))
all_enemies.add(Enemy(player, 9,8))

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_cursor_pos = pygame.mouse.get_pos() - player.global_offset
                row, cell, _ = maps.get_element_from_table(pygame.math.Vector2(current_cursor_pos))
                player.move(row, cell)
                # print(pygame.mouse.get_pos())
                # move = True
            if event.button == 3:
                print(pygame.mouse.get_pos()[0])

    check_collision(player, all_enemies)
    offset = maps.determine_offset(pygame.mouse.get_pos(), WIDTH, HEIGHT)
    player.global_offset += offset
    board_wall.update(offset)
    player.update(offset)
    all_enemies.update(offset)

    draw_window(win, board_wall, player, all_enemies)

pygame.quit()
    