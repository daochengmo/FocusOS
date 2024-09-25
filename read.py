import openai
openai.api_key = "YOUR_API_KEY"

# Read the file
with open("file.txt", "r") as file:
    text = file.read()

# Pass the text to GPT for processing
prompt = "Complete the following sentence:\n\n" + text + "\n\nThe completed sentence is:"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.5,
    max_tokens=100
)

# Print the completed sentence
print(response.choices[0].text)
