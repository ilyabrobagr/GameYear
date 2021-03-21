import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра года")

#точка спавна игрока
start_x = 100
start_y = 120

# изображения
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (800, 600))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (40, 40))

# создание групп объектов
all_sprites = pygame.sprite.Group()

# создание объектов
player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player)

run = True

while run:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w]:
            player.rect.y -= player.speed

        if keys[pygame.K_s]:
            player.rect.y += player.speed

        if keys[pygame.K_a]:
            player.rect.x -= player.speed
        if keys[pygame.K_d]:
            player.rect.x += player.speed

    all_sprites.draw(window)
    all_sprites.update()
    pygame.display.update()