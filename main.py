# Flappy Bird in python
# By Soumyadeep Saha
import pygame
from bird import Bird
from pipe import Pipe

# main function


def main():
    pygame.init()

    top_pipe = pygame.image.load(r"pipe.png")
    bottom_pipe = pygame.transform.rotate(top_pipe, 180)
    score = 0

    hit = False
    death_sound_played = False
    screen = pygame.display.set_mode((460, 480))
    pygame.display.set_caption("Flappy Bird")
    icon = pygame.image.load("icon.webp")
    pygame.display.set_icon(icon)

    font = pygame.font.Font(r"Flappy Bird Regular.ttf", 128)
    wing_sound = pygame.mixer.Sound("sounds/sfx_wing.mp3")
    point_sound = pygame.mixer.Sound("sounds/sfx_point.mp3")
    die_sound = pygame.mixer.Sound("sounds/sfx_die.mp3")

    bird = Bird()
    pipe = Pipe()
    # Run until the user asks to quit
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not hit:
                        pygame.mixer.Sound.play(wing_sound)
                        bird.flap = True
                    if hit:
                        hit = False
                        pipe.reset()
                        bird.flap == False
                        bird.x = 130
                        bird.y = 200
                        bird.rotation = 0
                        score = 0
                        death_sound_played = False

        # Fill the background with white
        screen.fill((155, 155, 255))
        if hit:
            score = 0
        text = font.render(str(score), True, (255, 255, 255))
        screen.blit(text, (230, 20))
        # update each pipe
        pipe.update(hit)
        # draw the pipes
        screen.blit(top_pipe, [pipe.x, pipe.top])
        screen.blit(bottom_pipe, [pipe.x, pipe.bottom])

        if pipe.x == 130 and (not hit):
            score += 1
            pygame.mixer.Sound.play(point_sound)
            print("Score: " + str(score))

        # Update the bird
        bird.update()

        # Draw the bird
        bird.blitRotateCenter(screen)
        # Check for collisions
        if (
            bird.hitbox.colliderect(pipe.top_hitbox)
            or bird.hitbox.colliderect(pipe.bottom_hitbox)
            or bird.y > 460
        ):
            hit = True
            if not death_sound_played:
                pygame.mixer.Sound.play(die_sound)
            death_sound_played = True

        if hit:
            text = font.render("You died.", True, (255, 0, 0))
            screen.blit(text, (20, 230))
        # Flip the display
        pygame.display.update()

        pygame.time.Clock().tick(30)
    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
