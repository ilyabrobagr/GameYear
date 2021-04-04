import pygame
from time import sleep

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
pygame.display.set_caption("Игра года")

#точка спавна игрока
start_x = 150
start_y = 150

# изображения
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1280, 720))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (40, 40))

wall_h = pygame.transform.scale(pygame.image.load("images/wall_h.png"), (64, 32))
wall_v = pygame.transform.scale(pygame.image.load("images/wall_v.png"), (32, 64))

enemy_1_img = pygame.transform.scale(pygame.image.load("images/enemy1.png"), (40, 40))
enemy_2_img = pygame.transform.scale(pygame.image.load("images/enemy2.png"), (40, 40))
enemy_3_img = pygame.transform.scale(pygame.image.load("images/enemy3.png"), (40, 40))

# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# создание объектов
player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player)

#враг
enemy1_x = 378
enemy1_y = 185
enemy1 = Object(enemy_1_img, enemy1_x, enemy1_y, 2)
enemies.add(enemy1)
all_sprites.add(enemy1)

enemy2_x = 150
enemy2_y = 350
enemy2 = Object(enemy_2_img, enemy2_x, enemy2_y, 2)
enemies.add(enemy2)
all_sprites.add(enemy2)

enemy3_x = 1000
enemy3_y = 500
enemy3 = Object(enemy_3_img, enemy3_x, enemy3_y, 2)
enemies.add(enemy3)
all_sprites.add(enemy3)

#создание стен(картинка, х, у, скорость)
wall1 = Object(wall_v, 100, 100, 0)
walls.add(wall1)
all_sprites.add(wall1)
wall2 = Object(wall_h, 100, 100, 0)
walls.add(wall2)
all_sprites.add(wall2)
wall3 = Object(wall_v, 100, 164, 0)
walls.add(wall3)
all_sprites.add(wall3)
wall4 = Object(wall_h, 100, 228, 0)
walls.add(wall4)
all_sprites.add(wall4)
wall5 = Object(wall_h, 164, 100, 0)
walls.add(wall5)
all_sprites.add(wall5)
wall6 = Object(wall_h, 228, 100, 0)
walls.add(wall6)
all_sprites.add(wall6)
wall7 = Object(wall_h, 292, 100, 0)
walls.add(wall7)
all_sprites.add(wall7)
wall8 = Object(wall_h, 356, 100, 0)
walls.add(wall8)
all_sprites.add(wall8)
wall9 = Object(wall_h, 420, 100, 0)
walls.add(wall9)
all_sprites.add(wall9)
wall10 = Object(wall_h, 484, 100, 0)
walls.add(wall10)
all_sprites.add(wall10)
wall11 = Object(wall_h, 548, 100, 0)
walls.add(wall11)
all_sprites.add(wall11)
wall12 = Object(wall_h, 612, 100, 0)
walls.add(wall12)
all_sprites.add(wall12)
wall13 = Object(wall_h, 676, 100, 0)
walls.add(wall13)
all_sprites.add(wall13)
wall14 = Object(wall_h, 740, 100, 0)
walls.add(wall14)
all_sprites.add(wall14)
wall15 = Object(wall_h, 804, 100, 0)
walls.add(wall15)
all_sprites.add(wall15)
wall16 = Object(wall_h, 164, 228, 0)
walls.add(wall16)
all_sprites.add(wall16)
wall17 = Object(wall_h, 228, 228, 0)
walls.add(wall17)
all_sprites.add(wall17)
wall18 = Object(wall_h, 292, 228, 0)
walls.add(wall18)
all_sprites.add(wall18)
wall19 = Object(wall_v, 228, 180, 0)
walls.add(wall19)
all_sprites.add(wall19)
wall20 = Object(wall_v, 228, 260, 0)
walls.add(wall20)
all_sprites.add(wall20)
wall21 = Object(wall_v, 228, 324, 0)
walls.add(wall21)
all_sprites.add(wall21)
wall22 = Object(wall_v, 228, 388, 0)
walls.add(wall22)
all_sprites.add(wall22)
wall23 = Object(wall_v, 228, 452, 0)
walls.add(wall23)
all_sprites.add(wall23)
wall24 = Object(wall_h, 100, 516, 0)
walls.add(wall24)
all_sprites.add(wall24)
wall25 = Object(wall_h, 164, 516, 0)
walls.add(wall25)
all_sprites.add(wall25)
wall26 = Object(wall_v, 228, 516, 0)
walls.add(wall26)
all_sprites.add(wall26)
wall26 = Object(wall_v, 100, 548, 0)
walls.add(wall26)
all_sprites.add(wall26)
wall27 = Object(wall_v, 100, 602, 0)
walls.add(wall27)
all_sprites.add(wall27)
wall28 = Object(wall_h, 100, 666, 0)
walls.add(wall28)
all_sprites.add(wall28)
wall29 = Object(wall_h, 164, 666, 0)
walls.add(wall29)
all_sprites.add(wall29)
wall30 = Object(wall_h, 228, 666, 0)
walls.add(wall30)
all_sprites.add(wall30)
wall31 = Object(wall_h, 272, 666, 0)
walls.add(wall31)
all_sprites.add(wall31)
wall32 = Object(wall_v, 336, 516, 0)
walls.add(wall32)
all_sprites.add(wall32)
wall33 = Object(wall_v, 336, 580, 0)
walls.add(wall33)
all_sprites.add(wall33)
wall34 = Object(wall_v, 336, 644, 0)
walls.add(wall34)
all_sprites.add(wall34)
wall35 = Object(wall_v, 336, 708, 0)
walls.add(wall35)
all_sprites.add(wall35)
wall36 = Object(wall_h, 336, 740, 0)
walls.add(wall36)
all_sprites.add(wall36)
wall37 = Object(wall_h, 400, 740, 0)
walls.add(wall37)
all_sprites.add(wall37)
wall38 = Object(wall_v, 432, 708, 0)
walls.add(wall38)
all_sprites.add(wall38)
wall39 = Object(wall_v, 432, 644, 0)
walls.add(wall39)
all_sprites.add(wall39)
wall40 = Object(wall_v, 432, 580, 0)
walls.add(wall40)
all_sprites.add(wall40)
wall41 = Object(wall_v, 432, 516, 0)
walls.add(wall41)
all_sprites.add(wall41)
wall42 = Object(wall_v, 432, 452, 0)
walls.add(wall42)
all_sprites.add(wall42)
wall43 = Object(wall_v, 432, 388, 0)
walls.add(wall43)
all_sprites.add(wall43)
wall44 = Object(wall_h, 336, 388, 0)
walls.add(wall44)
all_sprites.add(wall44)
wall45 = Object(wall_h, 400, 388, 0)
walls.add(wall45)
all_sprites.add(wall45)
wall46 = Object(wall_h, 432, 484, 0)
walls.add(wall46)
all_sprites.add(wall46)
wall47 = Object(wall_h, 496, 484, 0)
walls.add(wall47)
all_sprites.add(wall47)
wall48 = Object(wall_h, 560, 484, 0)
walls.add(wall48)
all_sprites.add(wall48)
wall49 = Object(wall_h, 624, 484, 0)
walls.add(wall49)
all_sprites.add(wall49)
wall52 = Object(wall_h, 624, 388, 0)
walls.add(wall52)
all_sprites.add(wall52)
wall53 = Object(wall_h, 560, 388, 0)
walls.add(wall53)
all_sprites.add(wall53)
wall54 = Object(wall_v, 560, 356, 0)
walls.add(wall54)
all_sprites.add(wall54)
wall55 = Object(wall_v, 560, 292, 0)
walls.add(wall55)
all_sprites.add(wall55)
wall56 = Object(wall_h, 528, 292, 0)
walls.add(wall56)
all_sprites.add(wall56)
wall57 = Object(wall_h, 464, 292, 0)
walls.add(wall57)
all_sprites.add(wall57)
wall58 = Object(wall_v, 560, 228, 0)
walls.add(wall58)
all_sprites.add(wall58)
wall59 = Object(wall_h, 560, 228, 0)
walls.add(wall59)
all_sprites.add(wall59)
wall60 = Object(wall_h, 624, 228, 0)
walls.add(wall60)
all_sprites.add(wall60)
wall61 = Object(wall_v, 656, 228, 0)
walls.add(wall61)
all_sprites.add(wall61)
wall62 = Object(wall_v, 656, 292, 0)
walls.add(wall62)
all_sprites.add(wall62)
wall63 = Object(wall_h, 656, 324, 0)
walls.add(wall63)
all_sprites.add(wall63)
wall64 = Object(wall_h, 720, 324, 0)
walls.add(wall64)
all_sprites.add(wall64)
wall65 = Object(wall_h, 784, 324, 0)
walls.add(wall65)
all_sprites.add(wall65)
wall66 = Object(wall_v, 848, 292, 0)
walls.add(wall66)
all_sprites.add(wall66)
wall67 = Object(wall_v, 848, 228, 0)
walls.add(wall67)
all_sprites.add(wall67)
wall68 = Object(wall_v, 848, 164, 0)
walls.add(wall68)
all_sprites.add(wall68)
wall69 = Object(wall_v, 848, 100, 0)
walls.add(wall69)
all_sprites.add(wall69)
wall70 = Object(wall_v, 750, 100, 0)
walls.add(wall70)
all_sprites.add(wall70)
wall71 = Object(wall_v, 750, 164, 0)
walls.add(wall71)
all_sprites.add(wall71)
wall72 = Object(wall_h, 688, 388, 0)
walls.add(wall72)
all_sprites.add(wall72)
wall73 = Object(wall_h, 752, 388, 0)
walls.add(wall73)
all_sprites.add(wall73)
wall74 = Object(wall_h, 816, 388, 0)
walls.add(wall74)
all_sprites.add(wall74)
wall75 = Object(wall_h, 880, 388, 0)
walls.add(wall75)
all_sprites.add(wall75)
wall76 = Object(wall_v, 944, 100, 0)
walls.add(wall76)
all_sprites.add(wall76)
wall77 = Object(wall_v, 944, 164, 0)
walls.add(wall77)
all_sprites.add(wall77)
wall78 = Object(wall_v, 944, 228, 0)
walls.add(wall78)
all_sprites.add(wall78)
wall79 = Object(wall_v, 944, 292, 0)
walls.add(wall79)
all_sprites.add(wall79)
wall80 = Object(wall_v, 944, 356, 0)
walls.add(wall80)
all_sprites.add(wall80)








run = True

while run:
    sleep(0.01)
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# Упровление
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_UP]:
            player.rect.y -= player.speed

        if keys[pygame.K_DOWN]:
            player.rect.y += player.speed

        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        if keys[pygame.K_RIGHT]:
            player.rect.x += player.speed

        if keys[pygame.K_ESCAPE]:
            run = False

     #чудики решили ходить и биться головой об стенки
    enemy1.rect.x += enemy1.speed
    enemy2.rect.x += enemy2.speed
    enemy3.rect.y += enemy3.speed
    if len(pygame.sprite.spritecollide(enemy1, walls, False)) > 0:
        enemy1.speed *= -1
    if len(pygame.sprite.spritecollide(enemy2, walls, False)) > 0:
        enemy2.speed *= -1
    if len(pygame.sprite.spritecollide(enemy3, walls, False)) > 0:
        enemy3.speed *= -1


    
    # встреча со стеной
    if len(pygame.sprite.spritecollide(player, walls, False)) > 0:
        player.rect.x = start_x
        player.rect.y = start_y

    # встреча с чудиком
    if len(pygame.sprite.spritecollide(player, enemies, False)) > 0:
        player.rect.x = start_x
        player.rect.y = start_y

    all_sprites.draw(window)
    all_sprites.update()
    pygame.display.update()
