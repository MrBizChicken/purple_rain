from constants import *
import pygame
import rain



clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

rain = rain.Rain()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()


        draw()
        update()

    pygame.quit()


def draw():
    surface.fill((0, 0, 0))
    rain.draw(surface)


    pygame.display.flip()


def update():
    rain.update()






if __name__ == "__main__":
    main()
