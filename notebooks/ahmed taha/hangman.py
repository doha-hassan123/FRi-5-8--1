import random
someWords = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
someWords = someWords.split()

secret_word = random.choice(someWords)
text = []
for e in secret_word:
    text.append("-")
trys = 0
while True:
    if trys >= len(secret_word) + 2:
        print("sorry you lost")
        print(f"the word was {secret_word}")
        break
    trial = input("Enter letter: ")
    if len(trial) > 1:
        print("please only write one letter")
        continue
    try:
        int(trial)
        print("Please only use letters")
        continue
    except:
        pass
    found_a_letter = False
    for e in range(len(secret_word)):
        if secret_word[e] == trial:
            text[e] = trial
            found_a_letter = True
    if found_a_letter:
        print("congrats you found a letter in the game")
        print("".join(text))
        if "".join(text) == secret_word:
            print("you won congrats")
            break
    else:
        trys += 1
        print(f"you lost a try, you now have {trys}/{len(secret_word) + 2} trys")