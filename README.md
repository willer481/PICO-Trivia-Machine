# OLED Trivia Game for Raspberry Pi Pico

This is a simple trivia game built for the Raspberry Pi Pico using physical buttons, LEDs, and an I2C OLED screen. It's designed to be fun, educational, and extendable.

## 🧠 Features

- YES and NO button inputs
- Green LED for correct answers ✅
- Red LED for wrong answers ❌
- OLED display (128x32 SSD1306) for question display
- Randomly selected trivia questions
- Ready for hardware or mock mode (for testing without OLED)

## 🛠 Hardware Required

- Raspberry Pi Pico (or Pico W)
- 0.91" 128x32 I2C OLED Display (SSD1306)
- 2x Push Buttons (for YES/NO)
- 1x Red LED (wrong answer)
- 1x Green LED (correct answer)
- 220Ω resistors for LEDs
- Jumper wires and breadboard

## 🧾 Wiring (GPIO Mapping)

| Component      | Pico Pin |
|----------------|----------|
| YES Button     | GP15     |
| NO Button      | GP14     |
| Green LED      | GP13     |
| Red LED        | GP12     |
| OLED SDA       | GP6      |
| OLED SCL       | GP7      |
| OLED VCC       | 3.3V     |
| OLED GND       | GND      |

> You can customize these in the code.

## 🚀 Getting Started

1. Flash your Pico with the [MicroPython UF2 firmware](https://micropython.org/download/rp2-pico/).
2. Open [Thonny](https://thonny.org/) or your preferred MicroPython IDE.
3. Upload the following files:
   - `trivia_game.py` – main game script
   - `ssd1306.py` – OLED driver (optional if screen is connected)
4. Run `trivia_game.py`.

If you **don't have the OLED connected**, the code still runs using a `MockOLED` that prints questions to the console.

## 📂 File Descriptions

- `trivia_game.py` – Main script with game logic and button/LED control
- `ssd1306.py` – MicroPython driver for SSD1306 OLED (128x32 or 128x64)
- `README.md` – This file

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 👤 Author

**[willer481](https://github.com/willer481)**

---

Feel free to contribute, fork, or remix this project!

## 🙏 Acknowledgments

This project was created with the help of [ChatGPT](https://openai.com/chatgpt) by OpenAI.

