import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH


class Shot(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius)
        pygame.draw.circle(screen, "red", self.position, self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt
