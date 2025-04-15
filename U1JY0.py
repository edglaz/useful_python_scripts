#!/usr/bin/env python3
import random
import time

class ASCIIArtGenerator:
    def __init__(self):
        # Seed with current time for more randomness
        random.seed(time.time())
        
        # Select a random shape to draw
        self.shapes = ["box", "triangle", "diamond", "random_pattern"]
        self.selected_shape = random.choice(self.shapes)
        
        # Random size between 5 and 15
        self.size = random.randint(5, 15)
        
        # Random character selection
        self.chars = ["*", "#", "@", "$", "%", "&", "+", "=", "~", "■", "●", "◆"]
        self.main_char = random.choice(self.chars)
        self.secondary_char = random.choice([c for c in self.chars if c != self.main_char])
    
    def draw_box(self):
        """Draw a box"""
        result = []
        for i in range(self.size):
            if i == 0 or i == self.size - 1:
                result.append(self.main_char * self.size)
            else:
                result.append(self.main_char + self.secondary_char * (self.size - 2) + self.main_char)
        return result
    
    def draw_triangle(self):
        """Draw a triangle"""
        result = []
        for i in range(self.size):
            spaces = " " * (self.size - i - 1)
            if i == self.size - 1:
                result.append(self.main_char * (2 * i + 1))
            else:
                inner_spaces = self.secondary_char * (2 * i - 1) if i > 0 else ""
                if i == 0:
                    result.append(spaces + self.main_char)
                else:
                    result.append(spaces + self.main_char + inner_spaces + self.main_char)
        return result
    
    def draw_diamond(self):
        """Draw a diamond"""
        result = []
        # Top half (including middle)
        for i in range(self.size // 2 + 1):
            spaces = " " * (self.size // 2 - i)
            if i == 0:
                result.append(spaces + self.main_char)
            else:
                inner_spaces = self.secondary_char * (2 * i - 1)
                result.append(spaces + self.main_char + inner_spaces + self.main_char)
        
        # Bottom half
        for i in range(self.size // 2 - 1, -1, -1):
            spaces = " " * (self.size // 2 - i)
            if i == 0:
                result.append(spaces + self.main_char)
            else:
                inner_spaces = self.secondary_char * (2 * i - 1)
                result.append(spaces + self.main_char + inner_spaces + self.main_char)
        
        return result
    
    def draw_random_pattern(self):
        """Draw a random pattern"""
        result = []
        for _ in range(self.size):
            line = ""
            for _ in range(self.size):
                # 70% chance for main character, 30% for secondary
                if random.random() < 0.7:
                    line += self.main_char
                else:
                    line += self.secondary_char
            result.append(line)
        return result
    
    def generate(self):
        """Generate the selected ASCII art"""
        if self.selected_shape == "box":
            return self.draw_box()
        elif self.selected_shape == "triangle":
            return self.draw_triangle()
        elif self.selected_shape == "diamond":
            return self.draw_diamond()
        else:
            return self.draw_random_pattern()

if __name__ == "__main__":
    generator = ASCIIArtGenerator()
    
    print(f"Shape: {generator.selected_shape}")
    print(f"Characters: Primary='{generator.main_char}', Secondary='{generator.secondary_char}'")
    print(f"Size: {generator.size}")
    print("-" * 40)
    
    art = generator.generate()
    for line in art:
        print(line)
