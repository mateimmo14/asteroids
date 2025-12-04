import sys

import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event, log_state
from player import *
from shoot import Shot


def main():
    playtime = 0
    score = 0
    pygame.init()
    title_font = pygame.font.SysFont(None, 100)  # Big text
    score_font = pygame.font.SysFont(None, 50)  # Smaller text
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        updatable.update(dt)

        for aster in asteroids:
            if aster.collides_with(player):
                log_event("player_hit")

                # Draw Game Over text
                title_font = pygame.font.SysFont(None, 100)
                score_font = pygame.font.SysFont(None, 50)

                game_over_surf = title_font.render("GAME OVER", True, (255, 255, 255))
                score_surf = score_font.render(
                    f"Your score is {score}. Restarting game...", True, (255, 255, 255)
                )

                game_over_rect = game_over_surf.get_rect(
                    center=(
                        constants.SCREEN_WIDTH // 2,
                        constants.SCREEN_HEIGHT // 2 - 40,
                    )
                )
                score_rect = score_surf.get_rect(
                    center=(
                        constants.SCREEN_WIDTH // 2,
                        constants.SCREEN_HEIGHT // 2 + 40,
                    )
                )

                # Fill and draw
                screen.fill("black")
                screen.blit(game_over_surf, game_over_rect)
                screen.blit(score_surf, score_rect)

                pygame.display.flip()

                # Wait 10 seconds
                pygame.time.wait(5000)

                constants.restart_program()
            for shot in shots:
                if aster.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    aster.split()
                    score += 1
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
