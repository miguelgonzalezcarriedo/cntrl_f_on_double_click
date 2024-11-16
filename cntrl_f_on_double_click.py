from pynput import mouse, keyboard
import time

# Create keyboard controller
keyboard_controller = keyboard.Controller()

def on_double_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        current_time = time.time()
        
        # Check if this is the second click
        if hasattr(on_double_click, 'last_click_time'):
            if current_time - on_double_click.last_click_time < 0.5:  # 500ms for double click
                # Simulate Ctrl+F
                with keyboard_controller.pressed(keyboard.Key.ctrl):
                    keyboard_controller.press('f')
                    keyboard_controller.release('f')
                on_double_click.last_click_time = 0  # Reset timer
                return
        
        on_double_click.last_click_time = current_time

# Create and start the listener
with mouse.Listener(on_click=on_double_click) as listener:
    listener.join()