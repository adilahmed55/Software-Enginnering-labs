# Project: Real-Time Endless Runner Game (VibeCoding)

- **Student Name:** N. Adil Ahmed
- **SRN:** PES1UG24CS285
- **Assigned Repository:** `SETAPESU26/39_endless-runner`
- **Course:** Software Engineering Lab — Lab 4

---

## Overview

This project is a real-time endless runner built using **Pygame**. Using an LLM pair-programming workflow (VibeCoding), the codebase was analyzed, debugged, and enhanced with four major features.

---

## Implemented Features

### Task 1: Refined Continuous Collision Detection (CCD) & Speed Capping
- Implemented **Swept Bounding Box** detection (`swept_rect()`) in `obstacle.py` to prevent tunneling when obstacles move fast.
- Enforced maximum speed ceilings according to selected difficulty to maintain fair gameplay.

### Task 2: Graceful In-Game Game Over Screen
- Added semi-transparent overlay showing:
  - Big bold **GAME OVER** title.
  - Final Run Score & Session High Score.
  - User action prompts.

### Task 3: Interactive Replay & Difficulty Selection
- Instant restart without quitting the game:
  - Press `[1]`: **Easy Mode** (Base speed: 5.0, spawn interval: 85 frames)
  - Press `[2]`: **Medium Mode** (Base speed: 7.0, spawn interval: 70 frames)
  - Press `[3]`: **Hard Mode** (Base speed: 9.5, spawn interval: 52 frames)
  - Press `[R]` or `[SPACE]`: Restart on current difficulty
  - Press `[Q]` or `[ESC]`: Gracefully exit the game

### Task 4: Procedural 8-Bit Audio Feedback
- Implemented `game/sound_manager.py` which dynamically synthesizes retro sound effects:
  - **Jump Sound:** Rising sweep tone
  - **Scoring Chime:** Ascending arcade arpeggio
  - **Game Over:** Descending crash tone
- Pure Python synthesis: zero external `.wav` files required!

---

## How to Run

```bash
# 1. Install dependencies
pip install pygame

# 2. Run the game
python main.py
```

### Controls
- **Jump:** `SPACE`, `UP ARROW`, or `W`
- **On Game Over Screen:**
  - `1`: Play on Easy
  - `2`: Play on Medium
  - `3`: Play on Hard
  - `R` or `SPACE`: Replay current mode
  - `Q` or `ESC`: Quit

---

## Submission Checklist & Deliverables

- [x] **Updated and Refactored Code**: `main.py`, `game/`
- [x] **LLM Prompt History**: Complete pair-programming chat transcript documented in [PROMPTS_AND_CHAT_HISTORY.md](PROMPTS_AND_CHAT_HISTORY.md)
- [ ] **10-Second Gameplay Videos**:
  - `video_before.mp4`: 10-second recording showing the original buggy behavior (obstacle tunneling / console game over)
  - `video_after.mp4`: 10-second recording showing the new features (jump sounds, score sounds, continuous collision detection, Game Over screen, and difficulty replay)
