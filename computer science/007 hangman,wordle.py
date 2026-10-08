from random import choice

def body():
    input("Some dangerous criminals are on the run.\nGreat Detective, The police need your help!(Type any key to continue)")
    input("Deciphering the deceased's last word to help them identify the murderer!(Type any key to continue)")
    answer = input("Choose the mode you prefer!\n 1 is a minor case.\n 2 is a complex case.\n 3 is a huge case.")
    while answer not in ["1", "2", "3"]:
        answer = input("We need your help!\n 1 is a minor case.\n 2 is a complex case.\n 3 is a huge case.")
    ending = choosemode(answer)
    if ending[0] :
        input(f"After {ending[3]} chances, you find the answer.The last word is {ending[2]}.\nBased on the clues you provided, the police have launched an investigation...(Type any key to continue)")
        if ending[1] > 3:
            print("Because you solved the case so quickly, the murderer was apprehended within hours.\nThe police are very grateful for your contribution; you have completed this mission perfectly!")
        else:
            print("Because of your help, the murderer was apprehended within days.\nThe police are grateful for your contribution; you have completed this mission!")
    else:
        print(f"The last word is {ending[2]}.\nYou missed it, the police investigation was unsuccessful, the murderer escaped.\nThe police are still very grateful to you and hope for a smooth cooperation next time!")




def choosemode(mode):
    word = ""
    if mode == "1":
        kind = choice([1, 2])
        if kind == 1:
            print("The deceased's last word is about THE POISONED FOOD!")
            wordlist = ["beef", "vitamin", "clam", "cabbage", "papaya", "walnut", "almond", "lasagna", "pomegranate", "asparagus", "zucchini", "raspberry", "Stargazypie"]
            word = choice(wordlist).lower()
        elif kind == 2:
            print("The deceased's last word is about THE MURDER WEAPON!")
            wordlist = ["knife", "rope", "hammer", "lamp", "ashtray", "bottle", "scissors", "vase", "chair", "bat", "pan", "candelabrum", "paperweight"]
            word = choice(wordlist).lower()
        print(f"The word length is {len(word)}!")
        Countdown = 11 + len(word) // 4
        ending = lettergame(word, Countdown)
    elif mode == "2":
        wordlist = ["abhor", "acute", "adorn", "aloof", "amass", "ample", "bleak", "blunt", "brash", "caste", "cater", "civic", "clash", "crave", "crypt", "cynic", "defer", "deity", "dense", "deter", "dogma", "elude", "evoke", "exalt", "facet"]
        word = choice(wordlist).lower()
        print(f"The word length is {len(word)}!")
        Countdown = 7
        ending = wordlegame(word, Countdown)
    elif mode == "3":
        wordlist = ["abhor", "acute", "adorn", "aloof", "amass", "ample", "bleak", "blunt", "brash", "caste", "cater", "civic", "clash", "crave", "crypt", "cynic", "defer", "deity", "dense", "deter", "dogma", "elude", "evoke", "exalt", "facet"]
        word = choice(wordlist).lower()
        Countdown = 7
        ending = modethree(word, Countdown)
    return ending



def lettergame(word, Countdown):
    knownlist = []
    checkedlist = []
    usecountdown = 0
    for i in range(len(word)):
        knownlist.append("*")
    while Countdown > 0:
        letter = input(f"Guess a letter and see if it is in there. Hurry up! The murderer will escape after {Countdown} chances!").lower()
        while len(letter) != 1 or not letter.isalpha() or letter in checkedlist:
            if letter in checkedlist:
                letter = input("You've already check that! Please choose another one letter!")
            else:
                letter = input("Please enter only one letter!")
        checkedlist.append(letter)
        place = word.find(letter)
        if place != -1:
            for i in range(len(word)):
                if word[i] == letter:
                    knownlist[i] = letter
                    print(f"Find {letter} at the {i + 1} place!")
        else:
            print(f"You find that {letter} isn't in last word!")
        input(f"Now the known word is {''.join(knownlist)}.(Type any key to continue)")
        Countdown -= 1
        usecountdown += 1
        if "*" not in knownlist:
            print("A flash of inspiration, and you've discovered the truth!!")
            return [True, Countdown, word, usecountdown]
    else:
        print("It's too late!")
        return [False, Countdown, word, usecountdown]

    

def wordlegame(word, Countdown):
    knownlist = []
    checkedlist = []
    usecountdown = 0
    unsurelist = []
    for i in range(len(word)):
        knownlist.append("*")
    input("The last word become more difficult to identify, maybe you should overall judgment...(Type any key to continue)")
    while Countdown > 0:
        letter = input(f"Guess a word and see if it is fit. Hurry up! The murderer will escape after {Countdown} chances!").lower()
        while len(letter) != len(word) or not letter.isalpha() or letter in checkedlist:
            if letter in checkedlist:
                letter = input("You've already check that! Please choose another word!")
            else:
                letter = input("Please enter a word in same length!")
        checkedlist.append(letter)
        Countdown -= 1
        usecountdown += 1
        for a in range(len(word)):
            if letter[a] == word[a]:
                knownlist[a] = letter[a]
                if letter[a] in unsurelist:
                    check = True
                    for b in range(len(word)):
                        if word[b] == letter[a] and knownlist[b] != letter[a]:
                            check = False
                    if check:
                        unsurelist.remove(letter[a])
            elif  word.find(letter[a]) != -1 and letter[a] not in unsurelist:
                unsurelist.append(letter[a])
        if not unsurelist:
            input(f"After confirmation, now the known word is {''.join(knownlist)}.(Type any key to continue)")
        else:
            input(f"After confirmation, now the known word is {''.join(knownlist)}. And {', '.join(unsurelist)} is in this word but wrong place.(Type any key to continue)")
        if "*" not in knownlist:
            print("A flash of inspiration, and you've discovered the truth!!")
            return [True, Countdown, word, usecountdown]
    else:
        print("It's too late!")
        return [False, Countdown, word, usecountdown]

def modethree(word, Countdown):
    clue = ["length", "firstword", "lastword", "none", "twoletter", "oneletter", "oneletter"]
    knownlist = []
    checkedlist = []
    usecountdown = 0
    input("The last word becomes more difficult to identify, you have to research clue by yourself and overall judgment...(Type any key to continue)")
    while Countdown > 0:
        answer = input(f"You can choose to research or guess a word! Hurry up! The murderer will escape after {Countdown} chances!").lower()
        while answer != "research" and answer in checkedlist:
            answer = input("You've already checked that! Please choose another word, it's to deduced!").lower()
        while answer == "research" and not clue:
            answer = input("You've cannot find any information any more!")
        checkedlist.append(answer)
        Countdown -=1
        usecountdown += 1
        if answer == "research":
            clue_get = choice(clue)
            knownlist.append(research(clue_get, word))
            clue.remove(clue_get)
            print(f"Now you know that {knownlist}")
        elif answer == word:
            print("A flash of inspiration, and you've discovered the truth!!")
            return [True, Countdown, word, usecountdown]
        else:
            print("It not seems to be the right one...")
    else:
        print("It's too late!")
        return [False, Countdown, word, usecountdown]


def research(choose, word):
    if choose == "none":
        print("You failed to find any clues...")
        return
    elif choose == "length":
        print(f"You find that the word length is {len(word)}...")
        result = f"word length is {len(word)}"
    elif choose == "firstword":
        print(f"You find that the first letter is {word[0]}...")
        result = f"first letter is {word[0]}"
    elif choose == "lastword":
        print(f"You find that the last letter is {word[-1]}...")
        result = f"last letter is {word[-1]}"
    elif choose == "oneletter":
        letter = choice(list(word))
        positions = []
        for i in range(len(word)):
            if word[i] == letter:
                positions.append(i + 1)
        print(f"You find that {letter} is it and appear at {positions}...")
        result = f"{letter} is it and appear at {positions}"
    elif choose == "twoletter":
        position1 = choice(range(1, len(word)-1))
        lettera = word[position1]
        letterb = word[position1+1]
        print(f"You find that the {position1 + 1} and {position1 + 2} letter is {lettera} and {letterb}...")
        result = f"{position1 + 1} and {position1 + 2} letter is {lettera} and {letterb}"
    return result



body()
        