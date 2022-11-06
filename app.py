""" 要件
1. googleの新しいタブを立ち上げ、そこに自動で平泉町 観光と入力し、検索
2. 開いたページのスクリーンショットを撮って、保存
"""
import pyautogui
import time
import webbrowser


# while True:
#     x, y = pyautogui.position()
#     positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#     print(positionStr, end="")
#     print("\b" * len(positionStr), end="", flush=True)


# Prepare GoogleURL
url = "https://www.google.com/"


def screenShot():
    """Conduct screenShot
    Take a image after 5s
    """
    time.sleep(5)
    pyautogui.screenshot("Images/rpa_result.png")


# Browser open
webbrowser.open(url)

# Move searchBox
pyautogui.moveTo(800, 470, 1)

# Move searchBox
pyautogui.click()

# Write Word
pyautogui.write("hiraizumi kannkou")

# conduct enter command
pyautogui.press("enter")

# Conduct screenShot
screenShot()
