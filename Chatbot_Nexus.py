responses = {
    "hello": "Hello!welcome to chatbot.",
    "thank you": " How can I assist you?",
    "how are you?": "I'm just a simple bot, but I'm doing great!",
    "who created you?":"I was created by a developer who loves Python",
    "can you recommend a good book to read?":" I don't read books, but I hear 'atomic habits' is a good one!",
    "what are the best practices for staying productive?":"set clear goals, prioritize tasks,eliminate distractions are some of the best practices for staying productive",
    "thank you!":"Your Welcome! if you have any questions feel free to ask",

}


def get_response(user_input):
    user_input = user_input.lower()
    #error handling line if chatbot doesn't understand the question
    return responses.get(user_input, "I'm sorry, I don't understand that.")

# Main loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
 
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot: " + response)


if __name__ == "__main__":
    chat()
