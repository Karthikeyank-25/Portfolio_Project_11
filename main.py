# IMPORTING PACKAGES :
import pyautogui
import time
from PIL import ImageGrab, ImageOps
from selenium import webdriver

# KEEPING CHROME PAGE OPEN :
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# AUTOMATING PROCESS :
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/t-rex/")

# FOR FINDING MOUSE LOCATION :
# while True:
#     pos = pyautogui.position()
#     print("Mouse is at:", pos)
#     time.sleep(0.2)

# OBJECT LOCATION :
box = (245,590,338,675)

# FUNCTION :
def detect_obstacle(obstacle):
    # GETTING THE OBJECT IMAGE FROM POSITION :
    cap = ImageGrab.grab(obstacle)
    # CONVERTING THAT IMAGE INTO BLACK AND WHITE PIXELS :
    gray_cap = ImageOps.grayscale(cap)
    # SUM THE PIXELS OF THE IMAGE :
    pixel_sum = sum(gray_cap.getdata())
    # RETURNING PIXELS TOTAL :
    return pixel_sum

print("Starting in 3 seconds... Switch to Chrome!")
time.sleep(3)
pyautogui.press('space')
# IMAGE PIXEL'S TOTAL SUM -1 :
baseline_sum = detect_obstacle(box)
while True:
    # IMAGES PIXEL'S TOTAL SUM - 2 :
    current_sum = detect_obstacle(box)
    # IF IMAGE TOTAL SUM - 1 IS 100 LOWER THAN IMAGE SUM - 2 :
    if current_sum < baseline_sum - 100:
        # PRESS 'SPACE' KEY :
        pyautogui.press('space')
        print("JUMP!")
        time.sleep(0.2)