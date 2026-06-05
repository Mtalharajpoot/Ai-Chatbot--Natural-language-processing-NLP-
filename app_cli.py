from chatbot import Chatbot

def main():
    print("=" * 50)
    print("  TalhaBot — AI Chatbot (type 'quit' to exit)")
    print("=" * 50)
    bot = Chatbot()

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye! Have a great day!")
            break
        response = bot.respond(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
