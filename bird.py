import pygame


class Bird():
    def __init__(self):
        self.x = 130
        self.y = 200
        self.flap = False
        self.gravityIncrement = 0.1
        self.gravity = 1
        self.sprite = pygame.transform.scale(
            pygame.image.load(r'bird.png'), (100, 100))
        self.rotation = 0

        self.hitbox = pygame.Rect(self.x+30, self.y+30, 45, 45)

    def update(self):
        """Update the bird's position based on the current state of the game. To Be called every frame"""
        if self.flap:  # If the bird is flapping
            self.gravityIncrement = -10
            self.flap = False
            self.rotation = 10
        else:
            if(self.y < 480):
                self.y += self.gravityIncrement
                if(self.gravityIncrement < 10):
                    self.gravityIncrement += self.gravity

        # set the bird's rotation based on the gravity
        if(not self.flap and self.gravityIncrement > 2):
            if self.rotation > -90:
                self.rotation -= 5

        self.hitbox = pygame.Rect(self.x+30, self.y+30, 45, 45)

    def blitRotateCenter(self, surf):
        topleft = (self.x, self.y)
        rotated_image = pygame.transform.rotate(self.sprite, self.rotation)
        new_rect = rotated_image.get_rect(
            center=self.sprite.get_rect(topleft=topleft).center)

        surf.blit(rotated_image, new_rect)


if __name__ == '__main__':
    bird = Bird()
    for i in range(50):
        bird.update()
        print(bird.y)
