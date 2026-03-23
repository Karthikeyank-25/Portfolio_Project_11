# 🦖 Chrome Dino Game Bot

This project is a Python automation bot that plays the Chrome Dino (T-Rex) game automatically. It detects obstacles on the screen using image processing and makes the dinosaur jump at the right time.

The bot uses Selenium to open the game, PyAutoGUI to control keyboard actions, and PIL for screen analysis.

---

## 🚀 Features

* 🤖 Fully automated gameplay
* 👀 Real-time obstacle detection using screen capture
* ⌨️ Simulates keyboard input (jump action)
* 🌐 Automatically opens the game in Chrome
* ⚡ Fast and lightweight script

---

## 🛠️ Technologies Used

* Python 🐍
* Selenium 🌐
* PyAutoGUI ⌨️
* PIL (Pillow) 🖼️

---

## 📂 Project Structure

```id="f9s2kj"
project-folder/
│
├── main.py
└── README.md
```

---

## ⚙️ How It Works

1. Opens the Chrome Dino game using Selenium:

   ```
   https://elgoog.im/t-rex/
   ```

2. Captures a specific screen area where obstacles appear

3. Converts the captured image into grayscale

4. Calculates pixel intensity values

5. Compares:

   * Baseline (no obstacle)
   * Current frame

6. If a difference is detected → Bot presses **SPACE** to jump

---

## ▶️ How to Run

### 1. Clone the repository

```bash id="7c1vbn"
git clone https://github.com/your-username/dino-game-bot.git
cd dino-game-bot
```

### 2. Install dependencies

```bash id="i5q2mn"
pip install pyautogui pillow selenium
```

### 3. Run the script

```bash id="p9d2lm"
python main.py
```

---

## ⚠️ Important Notes

* 🖥️ Screen resolution and zoom must match your setup
* 🎯 The detection box coordinates may need adjustment:

  ```python
  box = (245,590,338,675)
  ```
* ⏱️ Switch to the Chrome window quickly after starting the script
* 🔑 ChromeDriver must be installed and configured

---

## 🧠 How Detection Works

* Takes a screenshot of the obstacle area
* Converts it to grayscale
* Sums pixel values
* Detects changes in brightness when an obstacle appears

---

## 🚀 Future Improvements

* Add ducking for flying obstacles 🦅
* Dynamic speed adjustment
* Auto calibration for different screen sizes
* Add GUI for configuration
* Improve detection accuracy using OpenCV

---

## 👨‍💻 Author

Karthikeyan

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
