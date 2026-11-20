import pygame


class Obstacle:
    """Represents a scrolling obstacle on the running track."""

    def __init__(self, x, ground_y, speed, width=25, height=40):
        self.x = float(x)
        self.prev_x = float(x)
        self.width = width
        self.height = height
        self.y = ground_y - height
        self.speed = speed
        self.scored = False

    def move(self):
        """Move the obstacle leftwards and record previous position for CCD."""
        self.prev_x = self.x
        self.x -= self.speed

    def off_screen(self):
        """Check if obstacle has completely moved past the left screen edge."""
        return self.x + self.width < 0

    def rect(self):
        """Instantaneous hitbox for the obstacle at current position."""
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def swept_rect(self):
        """Continuous Collision Detection (CCD) swept hitbox across the frame.

        Covers horizontal span from current x to prev_x + width, preventing
        fast-moving obstacles from skipping through the player hitbox (tunneling).
        """
        min_x = min(self.x, self.prev_x)
        span_width = int(max(self.x, self.prev_x) - min_x + self.width)
        return pygame.Rect(int(min_x), int(self.y), span_width, self.height)
