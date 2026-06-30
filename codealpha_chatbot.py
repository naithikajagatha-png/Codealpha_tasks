print("================================")
print("      BASIC CHATBOT PROJECT")
print("================================")

print("\nAvailable Commands:")
print("hello")
print("how are you")
print("what is your name")
print("who created you")
print("thank you")
print("bye")

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good Morning! Have a great day.")

    elif user == "good night":
        print("Bot: Good Night! Take care.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")