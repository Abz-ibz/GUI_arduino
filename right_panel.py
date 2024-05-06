from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.properties import NumericProperty, BooleanProperty

import global_state

class CompartmentButton(Button):
    is_open = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original_pos = (1500, 150)
        self.size_hint = (None, None)
        self.size = (250, 400)
        self.pos = self.original_pos
        self.background_color = (0,0,0,0)
        self.arrow = None 
        self.is_open = False
        self.draw()
        self.bind(on_press=self.toggle_compartment)

    def draw(self, open=False):
        self.canvas.before.clear()
        pos_y = self.original_pos[1] - 200 if open else self.original_pos[1]
        
        with self.canvas.before:
            Color(0, 0, 0, 0.5)  # Shadow color
            RoundedRectangle(pos=(1495, pos_y - 5), size=(260, 410), radius=[10])
            Color(0.8, 0.8, 0.8, 1)  # Compartment color
            RoundedRectangle(size=(250, 400), radius=[10], pos=(1500,pos_y))
        
        if self.arrow:
            self.remove_widget(self.arrow)
        self.arrow = Image(source='right_panel_pictures/arrows.png', size_hint=(None, None), size=(80, 80), pos=(self.original_pos[0] + 75, pos_y + 60))
        self.add_widget(self.arrow)
    

    def toggle_compartment(self, instance):
        self.is_open = not self.is_open
        self.draw(open=self.is_open)
        if self.is_open:
            self.parent.move_rod_open()
        else:
            self.parent.move_rod_close()

class RightPanel(Widget):
    def __init__(self, pos, size, **kwargs):
        super().__init__(**kwargs)
        self.pos = pos
        self.size = size
        self.draw_panel()
  
        # Initialize led_status and led_flash dictionaries here
        self.led_status = {'green': False, 'orange': False, 'red': False}
        self.led_flash = {'green': False, 'orange': False, 'red': False}

        self.add_widgets()
        Clock.schedule_interval(self.update_leds, 0.5)  # Schedule the LED updates

    def add_widgets(self):
        # Manually set positions
        led_positions = {
            'green': (1600, 800),
            'orange': (1600, 700),
            'red': (1600, 600)
        }

        # Create and add LED images
        self.green_led = Image(source='right_panel_pictures/green_off.png', size_hint=(None, None), size=(80, 80), pos=led_positions['green'])
        self.orange_led = Image(source='right_panel_pictures/orange_off.png', size_hint=(None, None), size=(80, 80), pos=led_positions['orange'])
        self.red_led = Image(source='right_panel_pictures/red_off.png', size_hint=(None, None), size=(80, 80), pos=led_positions['red'])

        self.add_widget(self.green_led)
        self.add_widget(self.orange_led)
        self.add_widget(self.red_led)
        self.compartment_button = CompartmentButton()
        self.add_widget(self.compartment_button)
        self.draw_inset_box()
        self.draw_rod()
        
    def draw_panel(self):
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Shadow color
            RoundedRectangle(pos=(self.pos[0], self.pos[1] - 10), size=self.size, radius=[10])
            Color(0.8, 0.8, 0.8, 1)  # Panel color
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

    def draw_rod(self):
        with self.canvas:
            self.rod_color = Color(0.8, 0.8, 0.8, 0)  # Initially fully transparent
            self.rod = RoundedRectangle(size=(8, 100), pos = (300, 500), color = (0.8, 0.8, 0.8, 1)  # Fully opaque
)

    def move_rod_open(self):
        # Update the rod to the open position and make it visible
        self.rod.pos = (300, 500)
        self.rod_color.rgba = (0.4, 0.4, 0.4, 1)  # Fully opaque

    def move_rod_close(self):
        self.rod_color.rgba = (0.8, 0.8, 0.8, 0)  # Make it fully transparent again for hiding


    def draw_inset_box(self):
        # Ensure the inset box is drawn with a visible color
        with self.canvas.before:
            Color(0, 0, 0, 0.2)  # Inset box shadow color, ensure alpha is not 0
            self.inset_box = RoundedRectangle(pos=(1500, 150), size=(250, 400), radius=[12])

    def set_led(self, led_widget, color, on):
        # Set the LED to on or off state
        led_widget.source = f'right_panel_pictures/{color}_{"on" if on else "off"}.png'

    def flash_led(self, led_widget, color):
        if self.led_flash[color]:
            # Toggle the LED to create a flashing effect
            led_widget.source = f"right_panel_pictures/{color}_{'off' if 'on' in led_widget.source else 'on'}.png"
        else:
            # Ensure the LED is in the correct steady state
            self.set_led(led_widget, color, self.led_status[color])

    def update_leds(self, dt):
    # Update the green LED status
        if global_state.system == 1 and not global_state.arm:
            self.led_flash['green'] = True  # Green flashes if system is on and no arm
        else:
            self.led_flash['green'] = False  # Green does not flash otherwise
            self.led_status['green'] = global_state.arm  # Green is on if armed, off otherwise

    # Update the orange LED status
        if global_state.face_id:
            self.led_flash['orange'] = True  # Orange flashes if faceID is true
        else:
            self.led_flash['orange'] = False  # Orange does not flash otherwise
            self.led_status['orange'] = global_state.recording  # Orange is on if recording

    # Update the red LED status
            self.led_flash['red'] = global_state.alarm  # Red flashes if alarm is active

    # Apply the updated statuses and flashing states
        for color, led_widget in [('green', self.green_led), ('orange', self.orange_led), ('red', self.red_led)]:
            if self.led_flash[color]:
                self.flash_led(led_widget, color)
            else:
                self.set_led(led_widget, color, self.led_status[color])

