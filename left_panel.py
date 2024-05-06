from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.clock import Clock
import global_state

class CustomImageButton(ButtonBehavior, Widget):
    def __init__(self, image_normal, image_down, pos, size, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = size
        self.pos = pos
        self.background_normal = image_normal
        self.background_down = image_down or image_normal

        with self.canvas.before:
            Color(0, 0, 0, 0.5)  # Shadow color
            self.shadow = Ellipse(size=(self.size[0] - 5, self.size[1] - 5), pos=(self.pos[0] + 5, self.pos[1] - 5))
        
        with self.canvas:
            # Initially set the button color to transparent
            Color(1, 1, 1, 0)  # Transparent
            self.rect = Ellipse(size=self.size, pos=self.pos, radius=[10])
            self.image = Image(source=self.background_normal, pos=self.pos, size=self.size, allow_stretch=True)

        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_size, state=self.update_graphics_state)

    def update_graphics_pos(self, instance, value):
        # Update the position of the shadow, rectangle, and the image
        self.shadow.pos = (instance.pos[0] + 5, instance.pos[1] - 5)
        self.rect.pos = instance.pos
        self.image.pos = instance.pos

    def update_graphics_size(self, instance, value):
        # Update the size of the shadow, rectangle, and the image
        self.shadow.size = (instance.size[0] - 5, instance.size[1] - 5)
        self.rect.size = instance.size
        self.image.size = instance.size

    def update_graphics_state(self, instance, value):
        # Adjust the image based on the button state
        self.image.source = self.background_down if instance.state == 'down' else self.background_normal
    # Existing CustomImageButton code unchanged, assuming it includes all methods correctly.

class LeftPanel(Widget):
    def __init__(self, pos, size, **kwargs):
        super().__init__(**kwargs)
        self.pos = pos
        self.size = size
        self.draw_panel()
        self.add_components()

    def draw_panel(self):
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Shadow color
            RoundedRectangle(pos=(self.pos[0], self.pos[1] - 10), size=self.size, radius=[10])
            Color(0.8, 0.8, 0.8, 1)  # Panel color
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

    def add_components(self):
        button_size = (150, 150)
        button_pos = (220, 250)
        self.power_button = CustomImageButton(
            image_normal='left_panel_pictures/power_button.png',
            image_down='left_panel_pictures/power_button_pressed.png',
            pos=button_pos,
            size=button_size
        )
        self.power_button.bind(on_press=self.handle_power_button)
        self.add_widget(self.power_button)

        # Buzzer image and animation setup
        buzzer_pos = (160, 700)
        buzzer_size = (250, 250)
        self.buzzer_img = Image(
            source='left_panel_pictures/buzzer.png',
            pos=buzzer_pos,
            size=buzzer_size,
            size_hint=(None, None)
        )
        self.add_widget(self.buzzer_img)

        # Small dark grey hole
        hole_pos = (300, 500)
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            Ellipse(pos=hole_pos, size=(10, 10))

        # Start checking the alarm state periodically
        Clock.schedule_interval(self.check_alarm, 0.5)

    def handle_power_button(self, instance):
        if global_state.system == 0:
            global_state.system = 1
            global_state.arm = 1
        elif global_state.system == 1 and global_state.arm == 0:
            global_state.system = 0
            global_state.set_alarm(0)
        elif global_state.system == 1 and global_state.arm == 1:
            global_state.alarm_start_time += 5

    def check_alarm(self, dt):
        if global_state.get_alarm() == 1:
            self.start_buzzer_vibration()
        else:
            self.stop_buzzer_vibration()

    def start_buzzer_vibration(self):
        if not hasattr(self, 'buzzer_animation'):
            self.buzzer_animation = Animation(x=self.buzzer_img.x + 5, duration=0.05) + Animation(x=self.buzzer_img.x - 5, duration=0.05)
            self.buzzer_animation.repeat = True
        self.buzzer_animation.start(self.buzzer_img)

    def stop_buzzer_vibration(self):
        if hasattr(self, 'buzzer_animation'):
            self.buzzer_animation.cancel(self.buzzer_img)

# Ensure to update global_state.py as required for new attributes.
