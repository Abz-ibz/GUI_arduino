import serial
import serial.tools.list_ports
from face_id.authentication import authenticate
from screen_reader import translations

# Initialize global state variables
language = 'English'
font_size = 20
system = 1
arm = 1
alarm_triggered = 1
alarm = 0
alarm_start_time = 0
face_id = 0
recording = 0

# setup serial connection
#def setup_arduino():
 #   ports = serial.tools.list_ports.comports()
  #  com_port = None
   ## for port in ports:
     #   if "Arduino" in port.description:  # This line might need to be adjusted based on your Arduino's port description
      #      com_port = port.device
       #     break
    
    #if com_port:
     #   try:
      #      return serial.Serial(com_port, 9600, timeout=1)
       # except serial.SerialException as e:
        #    print("Failed to connect to Arduino:", e)
   # else:
    #    print("Arduino not found")
   # return None
# Initialize Arduino connection
#arduino = setup_arduino()

#def send_command(serial_inst, command):
 #   if serial_inst:
  #      print(f"Sending command: {command}")
   #     serial_inst.write(command.encode('utf-8'))
        
    #else:
     #   print("Serial instance not available.")

#def handle_incoming_data(incoming):
 #   print(f"Arduino says: {incoming}")
  #  global system, arm, alarm_triggered, door, window

   # if incoming == "SYSTEM ON":
    #    system = 1
   # elif incoming == "SYSTEM OFF":
    #    system = 0
     #   arm = 0  # Typically, turning the system off would also disarm it.
    # elif incoming == "MOTION BOTH":
     #   alarm_triggered = 1
      #  door = 1
       # window = 1
    #elif incoming == "MOTION AT DOOR":
     #   alarm_triggered = 1
      #  door = 1
    #elif incoming == "MOTION AT WINDOW":
     #   alarm_triggered = 1
      #  window = 1



    # Read and handle incoming data from Arduino
  #  if serialInst.in_waiting > 0:
   #     incoming = serialInst.readline().decode('utf-8').strip()
    #    print(f"Arduino says: {incoming}")

# Function to set the current language
def set_language(new_language):
    global language
    language = new_language
    # Here you can add code to save this setting to a file or database if needed

# Function to get the current language
def get_language():
    return language

def get_translation(language, key):
    # Fetch the dictionary for the current language and retrieve the key
    return translations.get(language, {}).get(key, "Translation not found")

def set_alarm(state):
    global alarm
    alarm = state

def get_alarm():
    return alarm
