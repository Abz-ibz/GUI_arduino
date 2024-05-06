from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.label import Label

from global_state import font_size
from left_panel import LeftPanel
from right_panel import RightPanel
from center_panel import CenterPanel

Window.fullscreen = 'auto'

class AlarmSystemUI(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set background and window settings, and initialize the panels
        with self.canvas.before:
            Color(0.7, 0.7, 0.7, 1)  # RGB for #e5e5e5
            self.outer_rect = Rectangle(size=(2000,2000), pos=(0,0))

        # Set the inner rectangle color and position, with shadow
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Shadow color for inner rectangle
            self.shadow_rect = Rectangle(size=(1700, 750),
                                         pos=(self.x + 110, self.y + 90))  # Shadow position
            Color(0.45, 0.45, 0.45, 1)  # Inner rectangle color
            self.inner_rect = Rectangle(size=(1720, 850),
                                         pos=(self.x + 100, self.y + 100))

        self.setup_ui()


    def setup_ui(self):
        
        # Panels positioning and sizes
        left_panel_pos = (120, 120)
        left_panel_size = (350, 800)
        center_panel_pos = (535, 120)
        center_panel_size = (850, 800)
        right_panel_pos = (1450, 120)
        right_panel_size = (350, 800)

        # Draw panels
        self.add_widget(LeftPanel(pos=left_panel_pos, size=left_panel_size))
        self.add_widget(CenterPanel(pos=center_panel_pos, size=center_panel_size))
        self.add_widget(RightPanel(pos=right_panel_pos, size=right_panel_size))
        # Other UI components
        self.add_widget(Label(text='Press ESC to exit the application', font_size=font_size, size_hint=(None, None), size=(Window.width, 30), pos=(-300, 1000), color=(0, 0, 0, 1)))
         # Update webcam position
        webcam_size = 120
        webcam_pos = (870, 
                      900)
        self.draw_webcam(webcam_pos, webcam_size)

    def draw_webcam(self, pos, size):
        with self.canvas:
            # Shadow for the outermost circle of the webcam
            Color(0.15, 0.15, 0.15, 1)
            Ellipse(pos=(pos[0], pos[1] - 10), size=(size, size))  # Offset shadow
            # Dark grey outer circle
            Color(0.30, 0.30, 0.30, 1)
            Ellipse(pos=(pos[0], pos[1]), size=(size, size))
            # Black inner circle (lens)
            Color(0, 0, 0, 1)
            Ellipse(pos=(pos[0] + size * 0.2, pos[1] + size * 0.2), size=(size * 0.6, size * 0.6))
            # White reflection on the lens
            Color(1, 1, 1, 1)
            Ellipse(pos=(pos[0] + size * 0.45, pos[1] + size * 0.45), size=(size * 0.1, size * 0.1))

class AlarmApp(App):
    def build(self):
        ui = AlarmSystemUI()
        return ui

if __name__ == "__main__":
    AlarmApp().run()
    