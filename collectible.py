import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 0))  # Żółty kolor dla obiektu do zbierania
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self, offset):
        self.rect.x += offset.x
        self.rect.y += offset.y
