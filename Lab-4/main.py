"""Main entrypoint for Real-Time Endless Runner Game.

Lab 4: VibeCoding
Student: N. Adil Ahmed (PES1UG24CS285)
"""

import pygame
from game.game_engine import GameEngine


def main():
    """Initialize display and execute real-time game loop."""
    pygame.init()

    width, height = 800, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Endless Runner - VibeCoding Edition")

    sky_color = (200, 220, 240)
    clock = pygame.time.Clock()
    fps = 60

    engine = GameEngine(width, height)
    running = True

    while running:
        screen.fill(sky_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            engine.handle_event(event)

        if engine.should_quit:
            running = False

        engine.handle_input()
        engine.update()
        engine.render(screen)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
