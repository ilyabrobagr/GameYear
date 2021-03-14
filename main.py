import pygame

class Object(pygame.sprite.Sprite):
    def ___init___(self, img, x, y, speed):
        pygame.sprite.Sprite.___init___(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра года")


bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (800, 600))

run = True

while run:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    pygame.display.update()