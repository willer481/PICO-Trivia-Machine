from machine import Pin, I2C
import time
import random

# === TRY to import the SSD1306 OLED ===
try:
    from ssd1306 import SSD1306_I2C
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    oled = SSD1306_I2C(128, 32, i2c)
    has_oled = True
except:
    # Use a mock OLED if display not connected
    class MockOLED:
        def fill(self, x): pass
        def text(self, text, x, y, color=1): print("OLED:", text)
        def show(self): pass
    oled = MockOLED()
    has_oled = False

# === Buttons and LEDs ===
yes_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
no_button = Pin(14, Pin.IN, Pin.PULL_DOWN)
green_led = Pin(13, Pin.OUT)
red_led = Pin(12, Pin.OUT)

# === Questions ===
questions = [
    {"question": "Is Python a language?", "answer": True},
    {"question": "Is 2+2 = 5?", "answer": False},
    {"question": "Is Earth a planet?", "answer": True},
    {"question": "Is the sun cold?", "answer": False},
]

# === Display Function ===
def display_text(text):
    oled.fill(0)
    oled.text(text[:16], 0, 0)
    if len(text) > 16:
        oled.text(text[16:32], 0, 10)
    oled.show()

# === Game Feedback ===
def feedback(correct):
    if correct:
        green_led.value(1)
    else:
        red_led.value(1)
    time.sleep(1)
    green_led.value(0)
    red_led.value(0)

# === Game Loop ===
while True:
    q = random.choice(questions)
    display_text(q["question"])

    while True:
        if yes_button.value():
            user_answer = True
            break
        elif no_button.value():
            user_answer = False
            break
        time.sleep(0.1)

    correct = (user_answer == q["answer"])
    feedback(correct)
    display_text("Correct!" if correct else "Wrong!")
    time.sleep(2)
