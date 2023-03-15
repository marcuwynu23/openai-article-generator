
import openai
import os


# Set up the OpenAI API key
openai.api_key ="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"

# Create a completion function to generate text from GPT-3
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Initialize the prompt and response variables
prompt = ""
response = ""

# Start the while loop
while prompt != "exit":
    prompt = input("\033[32m" + "describe article: " + "\033[0m")
    if prompt == "exit":
        break
    text = f'write me a article about {prompt} with title include and filename in md.'
    response = generate_text(text)
    print(response)
