import pyautogui
import pyperclip
import time
import google.generativeai as genai
import textwrap

# Small delay before running to let you switch to correct window
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1209, 1050)
time.sleep(0.5)  # wait for the click to register

# Step 2: Drag to select text
pyautogui.moveTo(689, 245)
pyautogui.dragTo(1849, 947, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy selected text to clipboard
pyautogui.hotkey("ctrl", "c")
pyautogui.click(695, 355)
time.sleep(0.5)

# Step 4: Get clipboard content
chat_history = pyperclip.paste()

print("Copied text:", chat_history)

# Extract latest message
lines = [line.strip() for line in chat_history.splitlines() if line.strip()]
latest_message = lines[-1] if lines else ""
print("Latest message:", latest_message)

# === Add your prompt here ===
user_prompt = """
You are Mahad — a friendly and engaging AI assistant who always replies in Roman Urdu.
Your tone should be casual, warm, and conversational, like chatting with a close friend.
Avoid formal English and avoid giving explanations, translations, or meta-commentary.
Output only Mahad's reply in Roman Urdu. you respond in accordance to the latest chat. avoid any unnecessary chat. be direct to the point(reply to the last message) — nothing else.
"""

prompt = f"{user_prompt}\n\nUser's latest message:\n{latest_message}"

genai.configure(api_key="AIzaSyAdcBsyHQkN0K-up12njARk14PUK4WV8v4")

# Choose the model
model = genai.GenerativeModel("gemini-2.5-pro")

# Generate content
response = model.generate_content('''You are Mahad — a friendly and engaging AI assistant who always replies in Roman Urdu.
Your tone should be casual, warm, and conversational, like chatting with a close friend.
Avoid formal English and avoid giving explanations, translations, or meta-commentary.
Output only Mahad's reply in Roman Urdu. you respond in accordance to the latest chat avoid any unnecessary chat. be direct to the point (reply to the last message) — nothing else.''')

# Get the text output
output = response.text.strip()

# Wrap text for neat alignment (80 chars per line)
wrapped_output = textwrap.fill(output, width=80)

# Print with a clean header and footer
print("\n" + "="*40)
print("🤖 Gemini Response")
print("="*40 + "\n")
print(wrapped_output)
print("\n" + "="*40)


# Step 5: Paste the response into target field and press Enter
pyautogui.click(992, 975)   # click the input field
time.sleep(0.5)
pyperclip.copy(output)      # copy Gemini's response to clipboard
pyautogui.hotkey("ctrl", "v")  # paste
time.sleep(0.3)
# pyautogui.press("enter")
