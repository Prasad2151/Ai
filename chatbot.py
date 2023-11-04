import openai
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

from config import apikey
openai.api_key = apikey
def generate_response(user_input):
    prompt = f"You: {user_input}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3hhi.5 engine
        prompt=prompt,
        max_tokens=50  # Adjust based on desired response length
    )
    return response.choices[0].text.strip()


def chat():
    print("Chatbot: Hi! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        bot_response = generate_response(user_input)
        print("Chatbot:", bot_response)
        #say(bot_response)


if __name__ == "__main__":
    chat()