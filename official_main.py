
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


dt = 0
game_surface = pygame.Surface(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
dt = clock.tick(60) / 1000
def main(difficulty, minigun=False, tank=False):

    pygame.init()
    if getattr(sys, 'frozen', False):
        base_font_path = sys._MEIPASS
    else:
        base_font_path = os.path.dirname(__file__)
    font_path = os.path.join(base_font_path, "assets", "pixel.ttf")
    font = pygame.font.Font(font_path, 36)  # None = default font, 36 = size

    if minigun:
        constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0
    elif tank:
        constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 2
        constants.SHOT_RADIUS = 10
        constants.ASTEROID_SPAWN_RATE_SECONDS = 0.7

    if difficulty:
        constants.ASTEROID_KINDS = 5
        constants.ASTEROID_MIN_RADIUS = 30
        constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3

    game_over = False
    score = 0

    title_font = pygame.font.Font(None, 100)
    score_font = pygame.font.Font(None, 50)

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    window = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
        pygame.RESIZABLE
    )
    background_path = os.path.join(base_path, "assets", "Background.png")
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.smoothscale(
        background,
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )





    dt = 0

    while True:
        constants.menu_open = False
        if constants.PAUSED:
            while True:

                if not constants.menu_open:
                    launcher.main()
                    constants.menu_open = True
                for obj in drawable:
                    obj.draw(game_surface)
                clock.tick(60)

                if not constants.PAUSED:
                    break
            constants.menu_open = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_l]:
                    if constants.ACTIVATE_LASER:
                        constants.ACTIVATE_LASER = False
                    elif not constants.ACTIVATE_LASER:

                        constants.ACTIVATE_LASER = True

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    constants.restart_program()

            if event.type == pygame.VIDEORESIZE
                window = pygame.display.set_mode(
                    (event.w, event.h),
                    pygame.RESIZABLE
                )

        if not game_over:
            updatable.update(dt)

        if constants.PAUSED:
            constants.PLAYER_SPEED = 0
            constants.PLAYER_TURN_SPEED = 0
        else:
            constants.PLAYER_TURN_SPEED = 300
            constants.PLAYER_SPEED = 200

        # ===== COLLISIONS =====
        for aster in asteroids:
            if aster.collides_with(player):
                game_over = True

                game_over_surf = title_font.render(
                    "GAME OVER", True, (255, 255, 255)
                )
                score_surf = score_font.render(
                    f"Your score is {score}. Press R to go back to the main menu",
                    True,
                    (255, 255, 255)
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

            for shot in shots:
                if aster.collides_with(shot):
                    if tank:
                        aster.kill()
                    else:
                        shot.kill()
                        aster.split(tank)
                    score += 1

        # ===== RENDERING =====
        game_surface.fill((0, 0, 0))
        game_surface.blit(background, (0, 0))
        if tank:
            score_text = font.render(f"Score: {score * 1.5}", True, (255, 255, 255))
        elif difficulty:
            score_text = font.render(f"Score: {score * 2}", True, (255, 255, 255))

        else:
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        if game_over:
            game_surface.blit(game_over_surf, game_over_rect)
            game_surface.blit(score_surf, score_rect)
            if not minigun:
                high_score(score, tank, difficulty)
        else:
            for obj in drawable:
                obj.draw(game_surface)


        scaled_surface = pygame.transform.smoothscale(
            game_surface,
            window.get_size()
        )

        window.blit(scaled_surface, (0, 0))
        window.blit(score_text, (10, 10))
        pygame.display.flip()

        dt = clock.tick(60) / 1000
