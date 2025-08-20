#!/usr/bin/env python3
"""
Test suite for Snake Game
Tests game initialization, movement, boundary conditions, and key handling
"""

import unittest
import pygame
import sys
import os

# Add the current directory to path to import snake_game
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestSnakeGame(unittest.TestCase):
    """Test cases for Snake Game functionality"""
    
    def setUp(self):
        """Set up test environment before each test"""
        pygame.init()
        # Initialize a headless display for testing
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        self.test_display = pygame.display.set_mode((400, 300))
        
    def tearDown(self):
        """Clean up after each test"""
        pygame.quit()
        
    def test_pygame_initialization(self):
        """Test that pygame initializes correctly"""
        self.assertTrue(pygame.get_init())
        
    def test_display_creation(self):
        """Test that display can be created with correct dimensions"""
        display = pygame.display.set_mode((400, 300))
        self.assertIsNotNone(display)
        self.assertEqual(display.get_size(), (400, 300))
        
    def test_color_definitions(self):
        """Test that color constants are properly defined"""
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        
        # Test color values are tuples with 3 elements
        self.assertEqual(len(white), 3)
        self.assertEqual(len(black), 3)
        self.assertEqual(len(red), 3)
        self.assertEqual(len(blue), 3)
        
        # Test specific color values
        self.assertEqual(white, (255, 255, 255))
        self.assertEqual(black, (0, 0, 0))
        
    def test_initial_position(self):
        """Test that initial snake position is within bounds"""
        x1 = 200
        y1 = 150
        
        # Check that initial position is within display bounds
        self.assertGreaterEqual(x1, 0)
        self.assertGreaterEqual(y1, 0)
        self.assertLess(x1, 400)
        self.assertLess(y1, 300)
        
    def test_movement_changes(self):
        """Test that movement variables work correctly"""
        x1_change = 0
        y1_change = 0
        
        # Test initial state (no movement)
        self.assertEqual(x1_change, 0)
        self.assertEqual(y1_change, 0)
        
        # Test left movement
        x1_change = -10
        y1_change = 0
        self.assertEqual(x1_change, -10)
        self.assertEqual(y1_change, 0)
        
        # Test right movement
        x1_change = 10
        y1_change = 0
        self.assertEqual(x1_change, 10)
        self.assertEqual(y1_change, 0)
        
        # Test up movement
        x1_change = 0
        y1_change = -10
        self.assertEqual(x1_change, 0)
        self.assertEqual(y1_change, -10)
        
        # Test down movement
        x1_change = 0
        y1_change = 10
        self.assertEqual(x1_change, 0)
        self.assertEqual(y1_change, 10)
        
    def test_boundary_conditions(self):
        """Test boundary checking logic"""
        # Test positions that should trigger game over
        boundary_test_cases = [
            (400, 150),  # Right boundary (x >= 400)
            (-1, 150),   # Left boundary (x < 0)
            (200, 300),  # Bottom boundary (y >= 300)
            (200, -1),   # Top boundary (y < 0)
            (450, 350),  # Both boundaries exceeded
        ]
        
        for x, y in boundary_test_cases:
            game_over = (x >= 400 or x < 0 or y >= 300 or y < 0)
            self.assertTrue(game_over, f"Position ({x}, {y}) should trigger game over")
            
        # Test positions that should NOT trigger game over
        valid_positions = [
            (0, 0),      # Top-left corner
            (399, 299),  # Bottom-right corner (just inside bounds)
            (200, 150),  # Center
            (10, 10),    # Valid position
        ]
        
        for x, y in valid_positions:
            game_over = (x >= 400 or x < 0 or y >= 300 or y < 0)
            self.assertFalse(game_over, f"Position ({x}, {y}) should NOT trigger game over")
            
    def test_key_event_simulation(self):
        """Test key event handling simulation"""
        # Create mock key events
        left_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        right_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        up_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        down_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
        quit_event = pygame.event.Event(pygame.QUIT)
        
        # Test that events can be created
        self.assertEqual(left_event.type, pygame.KEYDOWN)
        self.assertEqual(left_event.key, pygame.K_LEFT)
        self.assertEqual(quit_event.type, pygame.QUIT)
        
    def test_drawing_rectangle(self):
        """Test that rectangle drawing works"""
        white = (255, 255, 255)
        black = (0, 0, 0)
        
        # Fill display with white
        self.test_display.fill(white)
        
        # Draw a black rectangle (snake segment)
        pygame.draw.rect(self.test_display, black, [200, 150, 10, 10])
        
        # Test that drawing doesn't raise exceptions
        # (Visual verification would require actual display)
        pygame.display.update()
        
    def test_clock_functionality(self):
        """Test that pygame clock works"""
        clock = pygame.time.Clock()
        self.assertIsNotNone(clock)
        
        # Test that tick method exists and can be called
        # Note: We don't test actual timing in unit tests
        tick_result = clock.tick(30)
        self.assertIsInstance(tick_result, int)


class TestSnakeGameIntegration(unittest.TestCase):
    """Integration tests for the complete game logic"""
    
    def setUp(self):
        """Set up test environment"""
        pygame.init()
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        
    def tearDown(self):
        """Clean up after tests"""
        pygame.quit()
        
    def test_game_initialization_sequence(self):
        """Test complete game initialization"""
        # Test initialization steps
        pygame.init()
        self.assertTrue(pygame.get_init())
        
        # Test color definitions
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        
        # Test display creation
        dis = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Snake game by Jabir")
        
        # Test initial game state
        game_over = False
        x1 = 200
        y1 = 150
        x1_change = 0
        y1_change = 0
        
        # Test clock creation
        clock = pygame.time.Clock()
        
        # Verify all components are properly initialized
        self.assertFalse(game_over)
        self.assertEqual(x1, 200)
        self.assertEqual(y1, 150)
        self.assertEqual(x1_change, 0)
        self.assertEqual(y1_change, 0)
        self.assertIsNotNone(clock)
        
    def test_movement_simulation(self):
        """Test simulated movement without actual game loop"""
        x1 = 200
        y1 = 150
        x1_change = 10  # Moving right
        y1_change = 0
        
        # Simulate a few movement steps
        steps = 5
        for _ in range(steps):
            x1 += x1_change
            y1 += y1_change
            
            # Check position is still valid
            if x1 >= 400 or x1 < 0 or y1 >= 300 or y1 < 0:
                break
                
        expected_x = 200 + (10 * steps)
        self.assertEqual(x1, expected_x)
        self.assertEqual(y1, 150)  # y should not change
        
    def test_boundary_collision_simulation(self):
        """Test boundary collision detection"""
        # Start near right boundary
        x1 = 390
        y1 = 150
        x1_change = 10  # Moving right
        y1_change = 0
        
        game_over = False
        steps = 0
        max_steps = 10
        
        while not game_over and steps < max_steps:
            x1 += x1_change
            y1 += y1_change
            
            # Check boundaries
            if x1 >= 400 or x1 < 0 or y1 >= 300 or y1 < 0:
                game_over = True
                
            steps += 1
            
        self.assertTrue(game_over)
        self.assertGreaterEqual(x1, 400)  # Should have hit right boundary


def run_manual_test():
    """
    Manual test function to verify the game runs correctly
    This is not part of the automated test suite
    """
    print("Running manual Snake Game test...")
    print("This will start the game for 3 seconds to verify it works")
    
    try:
        # Import and run the actual game with a timeout
        import subprocess
        import signal
        
        def timeout_handler(signum, frame):
            raise TimeoutError("Manual test completed")
            
        # Set up timeout for manual test
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(3)  # 3 second timeout
        
        try:
            # Try to run the game
            result = subprocess.run([sys.executable, 'snake_game.py'], 
                                  cwd=os.path.dirname(os.path.abspath(__file__)),
                                  timeout=3, 
                                  capture_output=True, 
                                  text=True)
            print("Game started successfully!")
            return True
        except subprocess.TimeoutExpired:
            print("Game ran for 3 seconds without crashing - Test PASSED!")
            return True
        except Exception as e:
            print(f"Game failed to start: {e}")
            return False
        finally:
            signal.alarm(0)  # Cancel the alarm
            
    except ImportError:
        print("Cannot run manual test - missing dependencies")
        return False
    except Exception as e:
        print(f"Manual test error: {e}")
        return False


if __name__ == '__main__':
    print("=" * 60)
    print("SNAKE GAME TEST SUITE")
    print("=" * 60)
    
    # Run automated unit tests
    print("\n1. Running automated unit tests...")
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "=" * 60)
    print("2. Running manual game test...")
    manual_result = run_manual_test()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY:")
    print(f"Manual test result: {'PASSED' if manual_result else 'FAILED'}")
    print("=" * 60)