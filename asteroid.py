import random

import pygame
import math
import constants
from circleshape import CircleShape



class Asteroid(CircleShape):
    def generate_polygon(self):
        if constants.PAUSED:
            return
        points = []
        vertex_count = random.randint(8, 14)

        for i in range(vertex_count):
            angle = (2 * math.pi / vertex_count) * i
            distance = random.uniform(0.6, 1.0) * self.radius

            x = math.cos(angle) * distance
            y = math.sin(angle) * distance

            points.append(pygame.Vector2(x, y))

        return points
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-40, 40)
        self.visual_scale = 1.50  # 10–20% is ideal

        self.shape = self.generate_polygon()

    def draw(self, screen):

            transformed_points = [
            point.rotate(self.rotation) * self.visual_scale + self.position
            for point in self.shape
        ]

            pygame.draw.polygon(screen, (65, 65, 65), transformed_points)
            pygame.draw.polygon(screen, (20, 20, 20), transformed_points, 3)

    def update(self, dt):

        if constants.PAUSED:
            return
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt

    def split(self, tank=False):
        if constants.PAUSED:
            return
        self.kill()
        if not tank:

            if self.radius <= constants.ASTEROID_MIN_RADIUS:
                return

            angle = random.uniform(20, 50)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2

