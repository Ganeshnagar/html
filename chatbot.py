import random
def simple_chatbot():
    
    print("Hello! I am a simple chatbot. Let's have a conversation. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        if "hello" in user_input.lower():
            print("Chatbot: Hi there!")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a program, but I'm doing well, thanks for asking!")
        elif "your name" in user_input.lower():
            print("Chatbot: My name is Chatbot. Nice to meet you!")
        else:
            responses = ["Interesting!", "Tell me more.", "I'm not sure I understand.",
                         "How does that make you feel?"]
            random_response = random.choice(responses)
            print(f"Chatbot: {random_response}")


if __name__ == "__main__":
    simple_chatbot()






