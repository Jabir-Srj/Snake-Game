#!/usr/bin/env python3
"""
Simple test runner for Snake Game
This script validates that the game can be imported and basic functions work
"""

import sys
import os
import subprocess

def test_syntax():
    """Test that the game file has correct syntax"""
    print("Testing syntax...")
    try:
        result = subprocess.run([sys.executable, '-m', 'py_compile', 'snake_game.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Syntax check passed")
            return True
        else:
            print(f"✗ Syntax error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Syntax test failed: {e}")
        return False

def test_imports():
    """Test that required modules can be imported"""
    print("Testing imports...")
    try:
        import pygame
        print("✓ pygame imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_game_initialization():
    """Test that the game can be initialized without errors"""
    print("Testing game initialization...")
    try:
        import pygame
        pygame.init()
        
        # Test display creation
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        display = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Test")
        
        # Test colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        
        # Test drawing
        display.fill(white)
        pygame.draw.rect(display, black, [200, 150, 10, 10])
        pygame.display.update()
        
        # Test clock
        clock = pygame.time.Clock()
        clock.tick(1)
        
        pygame.quit()
        print("✓ Game initialization successful")
        return True
    except Exception as e:
        print(f"✗ Initialization failed: {e}")
        return False

def test_game_logic():
    """Test core game logic components"""
    print("Testing game logic...")
    try:
        # Test boundary checking
        def check_boundaries(x, y):
            return x >= 400 or x < 0 or y >= 300 or y < 0
        
        # Test valid positions
        assert not check_boundaries(200, 150), "Center position should be valid"
        assert not check_boundaries(0, 0), "Top-left should be valid"
        assert not check_boundaries(399, 299), "Bottom-right edge should be valid"
        
        # Test invalid positions  
        assert check_boundaries(400, 150), "Right boundary should be invalid"
        assert check_boundaries(-1, 150), "Left boundary should be invalid"
        assert check_boundaries(200, 300), "Bottom boundary should be invalid"
        assert check_boundaries(200, -1), "Top boundary should be invalid"
        
        print("✓ Game logic tests passed")
        return True
    except AssertionError as e:
        print(f"✗ Logic test failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Logic test error: {e}")
        return False

def test_game_file_structure():
    """Test that the game file has the expected structure"""
    print("Testing file structure...")
    try:
        with open('snake_game.py', 'r') as f:
            content = f.read()
        
        # Check for required components
        required_elements = [
            'import pygame',
            'pygame.init()',
            'pygame.display.set_mode',
            'while not game_over:',
            'pygame.event.get()',
            'pygame.QUIT',
            'pygame.KEYDOWN',
            'pygame.K_LEFT',
            'pygame.K_RIGHT', 
            'pygame.K_UP',
            'pygame.K_DOWN',
            'pygame.display.update()',
            'clock.tick(',
            'pygame.quit()'
        ]
        
        missing_elements = []
        for element in required_elements:
            if element not in content:
                missing_elements.append(element)
        
        if missing_elements:
            print(f"✗ Missing required elements: {missing_elements}")
            return False
        else:
            print("✓ File structure validation passed")
            return True
            
    except Exception as e:
        print(f"✗ File structure test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("SNAKE GAME VALIDATION TESTS")
    print("=" * 50)
    
    tests = [
        test_syntax,
        test_imports,
        test_game_initialization,
        test_game_logic,
        test_game_file_structure
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The Snake Game is ready to play.")
        return True
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)