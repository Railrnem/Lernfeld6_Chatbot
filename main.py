from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re

chatbot = ChatBot("Chatbot")
FILE = "chat.txt"

# Read training file
def prepareFile():  
    with open(FILE, "r") as training_file:
        content = training_file.read()
    return tuple(content.split("\n"))

# Train the bot
prepared_file = prepareFile()
trainer = ListTrainer(chatbot)
trainer.train(prepared_file)

# Main loop
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Bot: {chatbot.get_response(query)}")