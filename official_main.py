import sys
import time
import pygame
import os
import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
import launcher
from player import *
from shoot import Shot
from high_score import high_score, get_high_score_path
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
menu_open = False

def main(difficulty, minigun=False, tank=False):
    playtime = 0
    pygame.init()
    if minigun:
        constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0
    elif tank:
        constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 2
        constants.SHOT_RADIUS = 10
        constants.ASTEROID_SPAWN_RATE_SECONDS=0.7


    if difficulty:
        constants.ASTEROID_KINDS = 5
        constants.ASTEROID_MIN_RADIUS = 30
        constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
    game_over = False
    score = 0


    title_font = pygame.font.Font(None, 100)
    score_font = pygame.font.Font(None, 50)
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller executable
        base_path = sys._MEIPASS
    else:
        # Running as a script
        base_path = os.path.dirname(__file__)

    background_path = os.path.join(base_path, "assets","Background.png")
    background = pygame.image.load(background_path)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),pygame.RESIZABLE)






    dt = 0

    while True:
        global menu_open


        if constants.PAUSED and not menu_open:
            menu_open = True
            launcher.main()
            menu_open = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    constants.restart_program()







        if not game_over:

            updatable.update(dt)
        if constants.PAUSED:
            constants.PLAYER_SPEED = 0
            constants.PLAYER_TURN_SPEED = 0

        if not constants.PAUSED:
            constants.PLAYER_TURN_SPEED = 300
            constants.PLAYER_SPEED = 200
        for aster in asteroids:
            if aster.collides_with(player):

                game_over = True

                # Draw Game Over text


                game_over_surf = title_font.render("GAME OVER", True, (255, 255, 255))
                score_surf = score_font.render(
                    f"Your score is {score}. Press R to go back to the main menu", True, (255, 255, 255)

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

                pygame.display.flip()

                # Wait 10 seconds

            for shot in shots:
                if aster.collides_with(shot):
                    if tank:
                        aster.kill()
                    if not tank:
                        shot.kill()
                        aster.split(tank)
                    score += 1
            screen.blit(background, (0, 0))  # draw the background

            if game_over:
                screen.blit(game_over_surf, game_over_rect)
                screen.blit(score_surf, score_rect)
                if not minigun:
                    high_score(score,tank,difficulty)

            else:
                for obj in drawable:
                    obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



