import random

def setup():
    # Open the file in read mode
    with open("TypingWords.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))


        paragraph = ""
        for x in range(30):
            paragraph + " " + ((random.choice(words)))

        print(paragraph)
    
setup()