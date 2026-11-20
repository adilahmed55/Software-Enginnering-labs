"""Synthetic Sound Manager for Endless Runner.

Generates retro 8-bit sound effects procedurally without requiring
external audio files.
"""

import math
import struct
import pygame


class SoundManager:
    """Manages procedural sound effects for jump, score, and game over."""

    def __init__(self):
        self.enabled = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
            self.enabled = True
            self.jump_sound = self._create_sweep_tone(
                start_freq=320, end_freq=640, duration=0.12, volume=0.25
            )
            self.score_sound = self._create_arpeggio(
                frequencies=[523, 659, 784], duration=0.06, volume=0.20
            )
            self.game_over_sound = self._create_sweep_tone(
                start_freq=280, end_freq=70, duration=0.45, volume=0.35
            )
        except Exception as exc:  # pylint: disable=broad-exception-caught
            print(f"[SoundManager] Audio disabled ({exc})")
            self.enabled = False

    def _create_sweep_tone(self, start_freq, end_freq, duration, volume=0.25, sample_rate=22050):
        """Synthesize a frequency sweep tone with exponential decay."""
        n_samples = int(sample_rate * duration)
        buf = bytearray()
        for i in range(n_samples):
            t = float(i) / sample_rate
            progress = float(i) / n_samples
            current_freq = start_freq + (end_freq - start_freq) * progress
            decay = max(0.0, 1.0 - progress)
            sample_val = int(32767.0 * volume * decay * math.sin(2.0 * math.pi * current_freq * t))
            buf.extend(struct.pack("<h", max(-32768, min(32767, sample_val))))
        return pygame.mixer.Sound(buffer=bytes(buf))

    def _create_arpeggio(self, frequencies, duration, volume=0.20, sample_rate=22050):
        """Synthesize a cheerful ascending arpeggio chime for scoring."""
        buf = bytearray()
        samples_per_tone = int(sample_rate * duration)
        for freq in frequencies:
            for i in range(samples_per_tone):
                t = float(i) / sample_rate
                decay = max(0.0, 1.0 - (float(i) / samples_per_tone))
                sample_val = int(32767.0 * volume * decay * math.sin(2.0 * math.pi * freq * t))
                buf.extend(struct.pack("<h", max(-32768, min(32767, sample_val))))
        return pygame.mixer.Sound(buffer=bytes(buf))

    def play_jump(self):
        """Play jump sound effect."""
        if self.enabled and hasattr(self, "jump_sound"):
            self.jump_sound.play()

    def play_score(self):
        """Play point scoring sound effect."""
        if self.enabled and hasattr(self, "score_sound"):
            self.score_sound.play()

    def play_game_over(self):
        """Play game over sound effect."""
        if self.enabled and hasattr(self, "game_over_sound"):
            self.game_over_sound.play()
