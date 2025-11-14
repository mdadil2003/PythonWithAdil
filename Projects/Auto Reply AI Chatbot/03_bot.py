import pyautogui 
import time 
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="YOUR_API_KEY",
)

# Wait a few seconds before starting (to give you time to open window)
time.sleep(3)

# Click on the icon
pyautogui.click(1639, 1412)
time.sleep(1)  # small delay

# Drag to select text
pyautogui.moveTo(744, 123)
pyautogui.dragTo(1820, 990, duration=1, button='left')


pyautogui.hotkey('ctrl', 'c')
time.sleep(1) # small delay to ensure clipboard is updated
pyautogui.click(866, 1035) # click to remove selection

# Get copied text from clipboard
chat_history = pyperclip.paste()

print(chat_history)


completion = client.chat.completions.create(
   model= "gpt-3.5-turbo",
   messages=[
       {"role": "system", "content": "You are a person named Emine Sahin who speaks as well as english. You are from India and you are a Engineer. You analyze chat history and respond like Emine Sahin. Output should be the next reply as Emine Sahin."},
       {"role": "user", "content": chat_history}
   ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)


#  Click at coordinates 
pyautogui.click(866, 1035)
time.sleep(1) # Wait for 1 second to ensure the click is registered
# Paste the text
pyautogui.hotkey( 'ctrl', 'v')
time.sleep(2) # Wait for 2 seconds to ensure the paste command is completed
#  Press Enter 1
pyautogui.press('enter')
