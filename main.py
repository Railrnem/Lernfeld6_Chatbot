from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re

chatbot = ChatBot("Chatbot",
                logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold': 0.90
                }
                ],
                read_only=True)
FILE1 = "training_1.txt"
FILE2 = "training_2.txt"

# Read training file
def prepareFile(FILE: str):  
    with open(FILE, "r") as training_file:
        content = training_file.read()
    return tuple(content.split("\n"))

# Train the bot
trainer = ListTrainer(chatbot)
prepared_file = prepareFile(FILE1)
trainer.train(prepared_file)
prepared_file = prepareFile(FILE2)
trainer.train(prepared_file)

# Main loop
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Bot: {chatbot.get_response(query)}")