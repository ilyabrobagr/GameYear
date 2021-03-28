import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Игра года")

#точка спавна игрока
start_x = 100
start_y = 120

# изображения
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1000, 800))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (40, 40))

wall_h = pygame.transform.scale(pygame.image.load("images/wall_h.png"), (64, 32))
wall_v = pygame.transform.scale(pygame.image.load("images/wall_v.png"), (32, 64))

# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()

# создание объектов
player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player)

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

run = True

while run:
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

    all_sprites.draw(window)
    all_sprites.update()
    pygame.display.update()