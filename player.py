import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
)
from shoot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

        # in the Player class

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(dt - (dt * 2))
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt - (dt * 2))
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shoot_timer -= dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_timer > 0:
            pass
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation)
            ) * PLAYER_SHOOT_SPEED
