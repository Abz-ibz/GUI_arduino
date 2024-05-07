from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.button import Button

import global_state
from screen_reader import translations
from face_id.authentication import authenticate

class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Make the button's background completely transparent
        self.color = (0.26, 0.26, 0.26, 1)  # Dark grey text
        self.font_size = global_state.font_size
        self.size_hint = (None, None)
        self.size = (80, 60)
        
        with self.canvas.before:
            Color(0, 0, 0, .5)  # Shadow color
            self.shadow = RoundedRectangle(size=(self.width - 5, self.height - 5), pos=(self.x + 5, self.y - 5), radius=[10])
            Color(0.9, 0.9, 0.9, 1)  # Button color
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])

        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_size)

    def update_graphics_pos(self, instance, value):
        self.rect.pos = instance.pos
        self.shadow.pos = (instance.x + 3, instance.y - 3)

    def update_graphics_size(self, instance, value):
        self.rect.size = instance.size
        self.shadow.size = (instance.size[0] - 5, instance.size[1] - 5)

    def on_press(self):
        self.shadow.pos = (self.x + 2, self.y - 2)
        self.rect.pos = (self.x + 1, self.y - 1)

    def on_release(self):
        self.shadow.pos = (self.x + 3, self.y - 3)
        self.rect.pos = self.pos

class PlusMinusButton(CustomButton):
    def __init__(self, **kwargs):
        super(PlusMinusButton, self).__init__(**kwargs)
        self.font_size = '30sp'

from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle

class CenterPanel(Widget):
    def __init__(self, pos, size, **kwargs):
        super(CenterPanel, self).__init__(**kwargs)
        self.pos = pos
        self.size = size
        self.pin_code = ""
        self.display_width = 830  # Width of the display area
        self.display_height = 400  # Height of the display area
        self.display_x = 545       # X position of the display area
        self.display_y = 500       # Y position of the display area
        self.setup_panel()
        self.add_custom_keypad()
        self.add_display_screen()
        self.check_system_status()

    def setup_panel(self):
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Shadow color
            RoundedRectangle(pos=(self.pos[0], self.pos[1] - 10), size=self.size, radius=[10])
            Color(0.8, 0.8, 0.8, 1)  # Panel color
            RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

    def add_display_screen(self):
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Set the background color to light grey
            self.bg_rect = RoundedRectangle(pos=(self.display_x, self.display_y),
                                           size=(self.display_width, self.display_height))
        self.display_label = Label(pos=(self.display_x, self.display_y + self.display_height - 70),
                                   size=(self.display_width, 40),
                                   color=(0, 0, 0, 1),
                                   halign='center',
                                   valign='middle',
                                   text_size=(self.display_width, None),
                                   font_size='20sp')
        self.add_widget(self.display_label)

    def update_display_message(self, message):
        self.display_label.text = message

    
    def add_custom_keypad(self):
<<<<<<< HEAD
        keypad_x, keypad_y = 770, 430
        button_spacing = 93
=======
        keypad_x, keypad_y = 770, 480
        button_spacing = 95
>>>>>>> refs/remotes/origin/main
        keypad_layout = [
            ('1', '2', '3'),
            ('4', '5', '6'),
            ('7', '8', '9'),
            ('C', '0', 'Enter')
        ]

        for i, row in enumerate(keypad_layout):
            for j, text in enumerate(row):
                btn = CustomButton(text=text, size=(80, 60), pos=(keypad_x + j * button_spacing, keypad_y - i * button_spacing))
                btn.bind(on_press=self.on_keypad_press)
                self.add_widget(btn)

        # Adding Plus and Minus buttons
        plus_button = PlusMinusButton(text='+', pos=(keypad_x + 3 * button_spacing, keypad_y - 3 * button_spacing))
        minus_button = PlusMinusButton(text='-', pos=(keypad_x + 3 * button_spacing, keypad_y - 2 * button_spacing))
        self.add_widget(plus_button)
        self.add_widget(minus_button)


    def check_system_status(self):
        if global_state.system == 1 and global_state.arm == 1 and global_state.alarm_triggered ==1:
            self.authenticate_user()

    def authenticate_user(self):
        authenticate(self.face_recognition_callback)

    def face_recognition_callback(self, is_recognised):
        language = global_state.get_language()
        if is_recognised:
            message = translations[language].get('user_recognised', "Translation not found")
        else:
            message = translations[language].get('user_not_recognised', "Translation not found")
        self.update_display_message(message)
        Clock.schedule_once(lambda dt: self.prompt_for_pin(), 2)

    def on_keypad_press(self, instance):
        if instance.text == 'C':
            self.pin_code = ""
            self.update_display_message("")
        elif instance.text == 'Enter':
            self.verify_pin()
        else:
            self.pin_code += instance.text
            self.update_display_message(self.pin_code)

    def verify_pin(self):
        if self.pin_code == "20731":  # Assume "20731" is the correct PIN
            global_state.set_alarm(0)  # Disarm the system
            message = global_state.get_translation(global_state.language, 'pin_correct')
            self.update_display_message(message)
            self.pin_attempts = 0  # Reset attempts after correct PIN
        else:
            self.pin_attempts += 1
            if self.pin_attempts >= 3:
                global_state.set_alarm(1)  # Activate the alarm after 3 failed attempts
                message = global_state.get_translation(global_state.language, 'alarm_active')
            else:
                message = global_state.get_translation(global_state.language, 'pin_incorrect')
            self.update_display_message(message)
        self.pin_code = ""  # Reset PIN code after each attempt
    