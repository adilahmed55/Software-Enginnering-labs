# Lab 4: VibeCoding — Prompts, Iterations, and Pair-Programming Chat History

**Student Name:** N. Adil Ahmed  
**SRN:** PES1UG24CS285  
**Assigned Project:** `SETAPESU26/39_endless-runner`  
**Tool Used:** Antigravity (Google DeepMind Gemini 3.8)  

---

## Overview

In this VibeCoding lab, an LLM pair-programming partner was used to diagnose, fix, and extend a Pygame-based endless runner game. The development was conducted iteratively across four distinct tasks:
1. **Task 1:** Resolving the collision tunneling bug and capping speed for fair gameplay.
2. **Task 2:** Implementing a graphical Game Over overlay displaying the final score.
3. **Task 3:** Providing a replay mechanism with selectable difficulty presets (Easy, Medium, Hard).
4. **Task 4:** Integrating dynamic audio feedback for jump, scoring chime, and game over.

---

## Iterative Prompt Transcript

### Round 1: Diagnosing Collision Tunneling & Speed Runaway
**User Prompt:**
> "I'm running the endless runner in `main.py` and `game/game_engine.py`. The obstacles speed up continuously without an upper bound. Once the speed exceeds roughly 20-25 pixels per frame, obstacles pass directly through the player's white box without registering any collision. Why is this happening and how can we implement continuous collision detection (CCD) and a fair speed cap?"

**AI Response / Fix Explanation:**
> The issue is a classic game physics problem known as **discrete collision tunneling**:
> 1. In `update()`, the obstacle moves by `self.speed` pixels in a single frame *before* `colliderect()` is evaluated.
> 2. When `speed > player.width` (the player is 30px wide), an obstacle located at `x = 100` might jump to `x = 65` in one tick. If the player sits at `x = 80` with a width of 30 (range `[80, 110]`), the obstacle's instantaneous hitbox was never inside `[80, 110]` at either frame tick, completely bypassing collision.
> 3. **Fix Implemented:**
>    - In `Obstacle`, record `self.prev_x = self.x` before moving.
>    - Create `swept_rect()` that spans `[min(x, prev_x), max(x, prev_x) + width]`.
>    - Check `obstacle.swept_rect().colliderect(self.player.rect())`.
>    - Enforce a maximum speed cap (`max_speed = 13.5`) in `GameEngine.update()` so reaction times remain humanly playable.

---

### Round 2: Implementing the Game Over Screen
**User Prompt:**
> "Currently, when game over occurs, it only prints 'Game over! Final score: X' to the console and halts physics while the window remains blank or frozen. Please implement an in-game graphical Game Over screen that renders a dark translucent overlay, displays 'GAME OVER' in bold red, presents the final score and session high score, and prompts the user for replay or quit."

**AI Response / Fix Explanation:**
> **Changes Made to `game_engine.py`:**
> 1. Added a high score tracking attribute `self.high_score`.
> 2. In `render(screen)`, if `self.game_over` is `True`:
>    - Render a semi-transparent dark banner overlay (`pygame.Surface` with alpha `(15, 20, 30, 210)`).
>    - Center-align "GAME OVER" title in 52pt bold accent red.
>    - Render "Final Score: X | Best: Y" in gold text.
>    - Render user guidance: "Press [1] Easy [2] Medium [3] Hard | Press [SPACE/R] Restart | Press [Q] Quit".
> 3. In `main.py`, added `if engine.should_quit: running = False` to allow graceful termination when pressing 'Q' or 'Escape'.

---

### Round 3: Adding Interactive Replay with Difficulty Modes
**User Prompt:**
> "Now let's implement Task 3: allow the user to immediately restart from the Game Over screen by choosing a difficulty preset: Easy, Medium, or Hard. Each should adjust starting speed, spawn interval, and speed acceleration."

**AI Response / Fix Explanation:**
> **Implemented `DIFFICULTY_PRESETS` in `game_engine.py`:**
> - **Easy:** Starting speed = 5.0, obstacle spawn interval = 85 frames, speed ramp = 0.0015, max speed = 10.0.
> - **Medium:** Starting speed = 7.0, obstacle spawn interval = 70 frames, speed ramp = 0.0025, max speed = 13.5.
> - **Hard:** Starting speed = 9.5, obstacle spawn interval = 52 frames, speed ramp = 0.0040, max speed = 16.5.
> 
> In `handle_event(event)`:
> - Keys `1`, `2`, `3` reconfigure the engine parameters and call `reset_game()`.
> - Key `R` or `SPACE` restarts on the current difficulty setting.
> - `player.reset()` resets avatar velocity and returns it to ground level.

---

### Round 4: Procedural 8-Bit Audio Feedback (Zero External Dependencies)
**User Prompt:**
> "Task 4 asks for sound effects on jump, passing an obstacle, and game over. However, committing large external .wav or .mp3 files can cause missing file errors if someone clones the repo without assets. Can we synthesize retro sound effects in pure Python memory?"

**AI Response / Fix Explanation:**
> **Implemented `SoundManager` in `game/sound_manager.py`:**
> - Uses Python's standard `math` and `struct` libraries with `pygame.mixer.Sound(buffer=bytes(...))` to generate pure waveforms on demand:
>   - **Jump Sound:** Upward frequency sweep (320 Hz $\to$ 640 Hz over 120 ms) with linear decay.
>   - **Score Sound:** 3-note ascending arpeggio (C5: 523 Hz $\to$ E5: 659 Hz $\to$ G5: 784 Hz) giving a retro arcade coin chime.
>   - **Game Over Sound:** Downward low-frequency buzz (280 Hz $\to$ 70 Hz over 450 ms).
> - Wrapped initialization in graceful exception handling so headless or audio-disabled environments do not fail.

---

## Verification & Summary of Improvements

| Component | Initial Status | VibeCoding Final Status |
|:---|:---|:---|
| **Collision Detection** | Point-in-time `colliderect`; misses fast obstacles | **Continuous Swept Rect (CCD)**; zero tunneling |
| **Speed Progression** | Unbounded acceleration to $\infty$ | **Bounded ramp** capped at difficulty ceiling |
| **Game Over UI** | Console print statement only | **Polished in-game graphical UI** with high score |
| **Replay System** | Requires restarting Python script | **Instant in-game restart** with [1/2/3/R/Q] keys |
| **Audio Feedback** | None | **Procedural 8-bit sound effects** for all events |
