import pyautogui
import time
import pyperclip

# Wait a few seconds before starting (to give you time to open window)
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(1639, 1412)
time.sleep(1)  # small delay

# Step 2: Drag to select text
pyautogui.moveTo(626, 238)
pyautogui.dragTo(1199, 944, duration=1, button='left')

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1199, 944) # click to remove selection
time.sleep(0.5)

# Step 4: Get copied text from clipboard
copied_text = pyperclip.paste()

print("✅ Copied Text:\n")
print(copied_text)
