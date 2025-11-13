import pyautogui
import time
import pyperclip

# Wait a few seconds before starting (to give you time to open window)
time.sleep(3)

# Click on the icon
pyautogui.click(1639, 1412)
time.sleep(1)  # small delay

# Drag to select text
pyautogui.moveTo(684, 311)
pyautogui.dragTo(1823, 967, duration=1, button='left')


pyautogui.hotkey('ctrl', 'c')
time.sleep(1) # small delay to ensure clipboard is updated
pyautogui.click(1793, 235) # click to remove selection

# Get copied text from clipboard
copied_text = pyperclip.paste()

print("✅ Copied Text:\n")
print(copied_text)
