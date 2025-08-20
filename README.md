# Snake-Game
A snake game written in Python using Pygame

## Description
This is a simple Snake game implementation featuring:
- Arrow key controls (↑↓←→)
- Boundary collision detection
- Real-time gameplay at 30 FPS
- Clean, minimal interface

## Requirements
- Python 3.6+
- pygame 2.0+

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game:
   ```bash
   python snake_game.py
   ```

## Controls
- **Arrow Keys**: Move the snake
- **Close Window**: Exit the game

## Testing
The game includes comprehensive test suites to ensure functionality:

### Quick Validation
```bash
python run_tests.py
```
This runs basic validation tests including syntax, imports, initialization, game logic, and file structure.

### Full Test Suite  
```bash
python test_snake_game.py
```
This runs detailed unit tests and integration tests covering:
- Pygame initialization
- Display creation and drawing
- Movement mechanics
- Boundary collision detection
- Key event handling
- Game loop components

### What's Tested
- ✅ Syntax validation
- ✅ Pygame compatibility
- ✅ Game initialization
- ✅ Movement logic
- ✅ Boundary checking
- ✅ Key input handling
- ✅ Display rendering
- ✅ Clock timing

## Game Features
- **Boundary Detection**: Game ends when snake hits the wall
- **Smooth Movement**: 10-pixel increments at 30 FPS
- **Responsive Controls**: Immediate direction changes
- **Clean Exit**: Proper pygame cleanup
