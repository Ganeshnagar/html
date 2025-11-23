import random
def simple_chatbot():
    print("Heyy, I'm jusr simple chatbot")

    while True:
         user_input = input("You:")

         if user_input.lower() == 'exit':
             print("Goodbye")
             break

         if "hello" in user_input.lower():
            print("Hii..")
         elif "How are" in user_input.lower():
            print("I'm just a simple chat bot.,im fine ")
         elif "Your name" in user_input.lower():
            print("Simple charbot")
         else:
            responses = ["interesting" , "Tell me more", "whatt"]
            random_response = random.choice(responses)
            print(f"Chatbot : {random_response}" )
if __name__ == "__main__":
    simple_chatbot()
