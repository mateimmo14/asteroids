import sys

import pygame

import constants
from circleshape import CircleShape
from shoot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.minigun_timer = 0
        # in the Player class
        self.minigun_timer_on = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if constants.ACTIVATE_LASER == True:
           # Start at the player's position
           start_pos = self.position

           # End 720 pixels in front of the player
           end_pos = self.position + forward * 720


           pygame.draw.line(screen, "red", start_pos, end_pos, 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

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

            # -------- MINIGUN LOGIC --------
            # Press O to activate minigun if it's not already active
            # -------- MINIGUN LOGIC (15s on, 15s cooldown) --------

            # 1. Press O → activate minigun ONLY if ready
        if keys[pygame.K_o] and self.minigun_timer_on <= 0 and self.minigun_timer <= 0:
            self.minigun_timer_on = constants.PLAYER_MINIGUN_SECONDS  # active for 15s

            self.minigun_timer = 15  # cooldown after it ends

            # 2. Minigun ACTIVE
        if self.minigun_timer_on > 0:
            self.minigun_timer_on -= dt
            constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0   # full auto

            # 3. Minigun on cooldown

        elif self.minigun_timer > 0:
            self.minigun_timer -= dt
            constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3  # normal shooting

            # 4. Fully ready again
        else:
            constants.PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3

            # -------- END MINIGUN LOGIC --------

        if keys[pygame.K_n]:
            constants.PLAYER_SPEED += 10
            constants.PLAYER_TURN_SPEED += 10
        if keys[pygame.K_m]:
            constants.PLAYER_SPEED -= 10
            constants.PLAYER_TURN_SPEED -= 10
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_l]:
            constants.ACTIVATE_LASER = True

        self.shoot_timer -= dt
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_r]:
            constants.restart_program()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_timer > 0:
            pass
        else:
            self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS

            shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation)
            ) * constants.PLAYER_SHOOT_SPEED
