from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class PinEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.center_panel = CenterPanel(pos=self.pos, size=self.size)
        self.add_widget(self.center_panel)

    def on_enter(self):
        # You might want to set focus to the input or reset it each time the screen is shown
        pass
def handle_key_input(self, instance, keyboard, keycode, text, modifiers):
    # Handle different keycodes or text input
    if text.isdigit():
        # Update the display screen
        self.center_panel.update_display(text)
    elif keycode == 13:  # Enter key
        # You might want to validate the PIN or transition to another screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'next_screen_name'
