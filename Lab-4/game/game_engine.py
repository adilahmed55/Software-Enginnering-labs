"""Enhanced Game Engine for Real-Time Endless Runner.

Implements:
- Task 1: Continuous Collision Detection (CCD) and Speed Capping
- Task 2: Interactive Game Over screen with score metrics
- Task 3: Replay functionality with selectable difficulty presets
- Task 4: Dynamic audio feedback (jump, score, game over)
"""

import pygame
from .player import Player
from .obstacle import Obstacle
from .sound_manager import SoundManager

# Palette
WHITE = (255, 255, 255)
BLACK = (20, 20, 25)
BROWN = (120, 80, 40)
DARK_GREEN = (35, 120, 35)
ACCENT_RED = (220, 50, 50)
GOLD = (235, 185, 40)
OVERLAY_COLOR = (15, 20, 30, 210)

# Difficulty Presets
DIFFICULTY_PRESETS = {
    "Easy": {"base_speed": 5.0, "spawn_interval": 85, "speed_ramp": 0.0015, "max_speed": 10.0},
    "Medium": {"base_speed": 7.0, "spawn_interval": 70, "speed_ramp": 0.0025, "max_speed": 13.5},
    "Hard": {"base_speed": 9.5, "spawn_interval": 52, "speed_ramp": 0.0040, "max_speed": 16.5},
}


class GameEngine:
    """Manages gameplay physics, collision detection, game state, and rendering."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_y = height - 40

        self.player = Player(80, self.ground_y)
        self.sound_manager = SoundManager()

        # Fonts
        self.font = pygame.font.SysFont("Arial", 26, bold=True)
        self.title_font = pygame.font.SysFont("Arial", 52, bold=True)
        self.sub_font = pygame.font.SysFont("Arial", 22)

        # Game state & High Score tracking
        self.high_score = 0
        self.difficulty_name = "Medium"
        self.should_quit = False
        self.game_over = False
        self._game_over_sound_played = False

        self._apply_difficulty(self.difficulty_name)
        self.reset_game()

    def _apply_difficulty(self, name):
        """Configure gameplay parameters according to chosen difficulty preset."""
        preset = DIFFICULTY_PRESETS.get(name, DIFFICULTY_PRESETS["Medium"])
        self.difficulty_name = name
        self.base_speed = preset["base_speed"]
        self.spawn_interval = preset["spawn_interval"]
        self.speed_increase_per_frame = preset["speed_ramp"]
        self.max_speed = preset["max_speed"]

    def reset_game(self):
        """Reset runner parameters for a fresh gameplay attempt."""
        self.speed = self.base_speed
        self._spawn_timer = 0
        self.obstacles = []
        self.distance = 0
        self.score = 0
        self.game_over = False
        self._game_over_sound_played = False
        self.player.reset()

    def handle_event(self, event):
        """Process keyboard interactions during gameplay and on the Game Over screen."""
        if event.type != pygame.KEYDOWN:
            return

        if self.game_over:
            # Replay options on Game Over screen
            if event.key in (pygame.K_1, pygame.K_KP1):
                self._apply_difficulty("Easy")
                self.reset_game()
            elif event.key in (pygame.K_2, pygame.K_KP2):
                self._apply_difficulty("Medium")
                self.reset_game()
            elif event.key in (pygame.K_3, pygame.K_KP3):
                self._apply_difficulty("Hard")
                self.reset_game()
            elif event.key in (pygame.K_r, pygame.K_SPACE):
                # Quick restart on same difficulty
                self.reset_game()
            elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                self.should_quit = True
        else:
            # Jump controls during active gameplay
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                if self.player.jump():
                    self.sound_manager.play_jump()

    def handle_input(self):
        """Reserved for continuous polling if required."""

    def update(self):
        """Update game physics, obstacle movement, and evaluate collisions."""
        if self.game_over:
            return

        # Task 1 Fix: Ramp speed gradually up to a designated fair ceiling
        if self.speed < self.max_speed:
            self.speed += self.speed_increase_per_frame

        self.player.update()

        # Spawning obstacles
        self._spawn_timer += 1
        if self._spawn_timer >= self.spawn_interval:
            self._spawn_timer = 0
            self.obstacles.append(Obstacle(self.width, self.ground_y, self.speed))

        # Move obstacles
        for obstacle in self.obstacles:
            obstacle.move()
            obstacle.speed = self.speed

        # Task 1 Fix: Continuous Collision Detection (CCD) via swept bounding boxes
        player_hitbox = self.player.rect()
        for obstacle in self.obstacles:
            # Check swept rect to prevent tunneling at high speeds
            if obstacle.swept_rect().colliderect(player_hitbox):
                self.game_over = True
                if self.score > self.high_score:
                    self.high_score = self.score
                if not self._game_over_sound_played:
                    self.sound_manager.play_game_over()
                    self._game_over_sound_played = True
                return

        # Scoring: award point when player successfully clears obstacle
        for obstacle in self.obstacles:
            if not obstacle.scored and (obstacle.x + obstacle.width < self.player.x):
                obstacle.scored = True
                self.score += 1
                self.sound_manager.play_score()

        # Prune offscreen obstacles
        self.obstacles = [o for o in self.obstacles if not o.off_screen()]
        self.distance += self.speed

    def render(self, screen):
        """Draw running track, player, obstacles, HUD, and Game Over screen."""
        # Draw track
        pygame.draw.line(screen, BROWN, (0, self.ground_y), (self.width, self.ground_y), 4)

        # Draw player & obstacles
        pygame.draw.rect(screen, WHITE, self.player.rect(), border_radius=3)
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, DARK_GREEN, obstacle.rect(), border_radius=2)

        # Heads-Up Display (HUD)
        score_surf = self.font.render(f"Score: {self.score}", True, BLACK)
        mode_surf = self.sub_font.render(f"Mode: {self.difficulty_name} | Speed: {self.speed:.1f}", True, BLACK)
        screen.blit(score_surf, (15, 12))
        screen.blit(mode_surf, (15, 42))

        # Task 2 & 3: Render Graceful Game Over Screen
        if self.game_over:
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill(OVERLAY_COLOR)
            screen.blit(overlay, (0, 0))

            # Game Over Title
            go_text = self.title_font.render("GAME OVER", True, ACCENT_RED)
            go_rect = go_text.get_rect(center=(self.width // 2, self.height // 2 - 80))
            screen.blit(go_text, go_rect)

            # Score Summary
            summary_str = f"Final Score: {self.score}   |   Best: {self.high_score}"
            sum_text = self.font.render(summary_str, True, GOLD)
            sum_rect = sum_text.get_rect(center=(self.width // 2, self.height // 2 - 20))
            screen.blit(sum_text, sum_rect)

            # Replay and Difficulty Prompt
            options_str = "Press [1] Easy   [2] Medium   [3] Hard"
            opt_text = self.font.render(options_str, True, WHITE)
            opt_rect = opt_text.get_rect(center=(self.width // 2, self.height // 2 + 35))
            screen.blit(opt_text, opt_rect)

            sub_str = "Press [SPACE / R] Restart   |   Press [Q] Quit"
            sub_text = self.sub_font.render(sub_str, True, (200, 210, 225))
            sub_rect = sub_text.get_rect(center=(self.width // 2, self.height // 2 + 75))
            screen.blit(sub_text, sub_rect)
