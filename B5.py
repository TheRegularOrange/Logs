import random

class Chatbot:
    def __init__(self):
        self.responses = {
            'greetings': ['hi', 'hello', 'hey', 'howdy', 'hi there'],
            'farewells': ['bye', 'goodbye', 'see you later', 'take care'],
            'insults': ['stupid', 'dumb', 'useless'],
            'location': 'We are located at 123 Main Street, Cityville.',
            'hours': 'Our store hours are Monday to Friday, 9 AM to 6 PM.',
            'contact': 'You can contact us at 555-1234 or email support@store.com.',
            'insult_reply': 'That I am. HEHEH.'
        }

    def respond(self, text):
        text = text.lower()
        if any(w in text for w in self.responses['greetings']):
            return random.choice(['Hello! How can I assist you today?', 'Hi there! How can I help you?'])
        if any(w in text for w in self.responses['farewells']):
            return random.choice(['Goodbye! Have a great day!', 'See you later! Take care!'])
        if any(w in text for w in self.responses['insults']):
            return self.responses['insult_reply']
        for key in ['location', 'hours', 'contact']:
            if key in text:
                return self.responses[key]
        return "I'm sorry, I didn't quite understand that. Can you ask something else?"

def chat():
    bot = Chatbot()
    print("Welcome to the customer support chatbot! How can I help you today?")
    while True:
        user = input("You: ").strip()
        reply = bot.respond(user)
        print("Bot:", reply)
        if any(w in user.lower() for w in bot.responses['farewells']):
            break

if __name__ == "__main__":
    chat()
