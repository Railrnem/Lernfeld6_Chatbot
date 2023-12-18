from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re

chatbot = ChatBot("Chatbot",
                logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand. If you want to escalte to 2nd level support please type: "I want to talk to a human"',
                    'maximum_similarity_threshold': 0.90
                }
                ],
                read_only=True)

# Read training file
def prepareFile(file: str):  
    with open(file, "r") as training_file:
        content = training_file.read()
    return tuple(content.split("\n"))

# Train the bot
trainer = ListTrainer(chatbot)
files = ["training_1.txt", "training_2.txt", "training_3.txt", "training_4.txt", "training_5.txt"]
for file in files:
    prepared_file = prepareFile(file)
    trainer.train(prepared_file)

# Main loop
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Bot: {chatbot.get_response(query)}")