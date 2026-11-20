import pygame


class Player:
    """Represents the player avatar with jumping physics and gravity."""

    def __init__(self, x, ground_y, width=30, height=40):
        self.start_x = x
        self.ground_y = ground_y
        self.width = width
        self.height = height

        self.x = x
        self.y = ground_y - height
        self.vy = 0
        self.gravity = 0.8
        self.jump_strength = -15
        self.on_ground = True

    def jump(self):
        """Trigger jump impulse if currently grounded."""
        if self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False
            return True
        return False

    def update(self):
        """Apply gravity and update vertical position."""
        self.vy += self.gravity
        self.y += self.vy

        ground_level = self.ground_y - self.height
        if self.y >= ground_level:
            self.y = ground_level
            self.vy = 0
            self.on_ground = True

    def reset(self):
        """Reset player state back to starting conditions."""
        self.x = self.start_x
        self.y = self.ground_y - self.height
        self.vy = 0
        self.on_ground = True

    def rect(self):
        """Current bounding hitbox for the player."""
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)
