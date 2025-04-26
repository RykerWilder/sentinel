from pynput import keyboard

class KeyboardHandler:
    def __init__(self):
        self.should_exit = False
    
    def on_press_exit(self, key):
        if key == keyboard.Key.esc:
            self.should_exit = True
            return False  # Ferma il listener