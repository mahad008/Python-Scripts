import google.generativeai as genai
import textwrap

# Configure with your API key
genai.configure(api_key="AIzaSyAdcBsyHQkN0K-up12njARk14PUK4WV8v4")

# Choose the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content
response = model.generate_content("What is coding and Python? make it absolutely breif.")

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


