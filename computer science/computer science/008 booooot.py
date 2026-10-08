from random import choice
lexicon = ["abhor", "acute", "adorn", "aloof", "amass", "ample", "bleak", "blunt", "brash", "caste", "cater", "civic", "clash", "crave", "crypt", "cynic", "defer", "deity", "dense", "deter", "dogma", "elude", "evoke", "exalt", "facet", "guess", "hasty", "ivory", "kneel", "lapse","mirth", "noble", "overt", "plume", "prone", "realm", "scorn", "shrew","stark", "throb", "vivid", "glyph", "nymph", "fjord", "quack", "vexed", "waltz", "crypt", "jazzy", "proxy", "knurl", "crwth", "blitz", "jazzy", "quiff", "nymph", "fjord", "vexes", "glyph", "wryly", "queue", "xylem", "zesty", "quirk", "vivid", "pluck", "wince", "braze", "cynic", "ghoul", "cwmfy", "epoxy", "jumpy", "quill", "wrung", "zonal", "brisk", "chasm", "flint", "gawky", "crypt", "glyph", "nymph", "fjord", "quirk", "vexed", "waltz", "xylem", "knurl", "blitz", "epoxy", "jumpy", "quill", "wrung", "zonal", "brisk", "chasm", "flint", "gawky", "cynic", "ghoul", "proxy", "jazzy", "vivid", "pluck", "wince", "braze", "zesty", "queue", "axiom", "bleak", "crisp", "dwarf", "eerie", "frail", "gruff", "hasty", "ivory", "joust", "karma", "lurid", "mirth", "naive", "ozone", "pique", "rhyme", "scorn", "throb", "ulcer", "vague", "whirl", "yacht", "zebra", "brawl", "clamp", "dizzy", "evoke", "fable", "glint", "haunt", "inert", "jaunt", "kneel", "lapse", "mourn", "niche", "orbit", "prism", "raven", "sleek", "truce", "usher", "venom", "wreak", "yield", "zippy"]
answer = ""

def check_answer(guess):
    feedback = [0, 0, 0, 0, 0]
    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = 2
        elif answer.find(guess[i]) != -1:
            feedback[i] = 1
    return feedback


def Baseline_Bot():
    time = 1
    guess = "guess"
    need_check_list = lexicon.copy()
    feedback = [0, 0, 0, 0, 0]
    remove_list = []
    while answer != guess:
        feedback = check_answer(guess)
        position = 0
        for i in feedback:
            if i == 2:
                for n in need_check_list:
                    if n[position] != guess[position]:
                        remove_list.append(n)
            elif i == 1:
                for n in need_check_list:
                    if  n.find(guess[position]) == -1 or n[position] == guess[position]:
                        remove_list.append(n)
            elif i == 0:
                for n in need_check_list:
                    if n.find(guess[position]) != -1:
                        remove_list.append(n)
            position += 1
        time += 1
        for i in remove_list:
            if i in need_check_list:
                need_check_list.remove(i)
        guess = choice(need_check_list)
    return time
        

def frequency_weighted_bot():
    time = 1
    guess = "guess"
    need_check_list = lexicon.copy()
    feedback = [0, 0, 0, 0, 0]
    remove_list = []
    while answer != guess:
        feedback = check_answer(guess)
        position = 0
        for i in feedback:
            if i == 2:
                for n in need_check_list:
                    if n[position] != guess[position]:
                        remove_list.append(n)
            elif i == 1:
                for n in need_check_list:
                    if  n.find(guess[position]) == -1 or n[position] == guess[position]:
                        remove_list.append(n)
            elif i == 0:
                for n in need_check_list:
                    if n.find(guess[position]) != -1:
                        remove_list.append(n)
            position += 1
        time += 1
        frequency_weighted = 0
        for i in remove_list:
            if i in need_check_list:
                need_check_list.remove(i)
        for i in need_check_list:
            new_requency_weighted = 0
            for n in set(i):
                for w in need_check_list:
                    if n in w:
                        new_requency_weighted += 1 
            if new_requency_weighted > frequency_weighted:
                guess = i
                frequency_weighted = new_requency_weighted
    return time

def information_bot():
    time = 1
    guess = "guess"
    need_check_list = dict.fromkeys(lexicon, 0)
    left_check_list = lexicon.copy()
    feedback = [0, 0, 0, 0, 0]
    while answer != guess:
        feedback = check_answer(guess)
        position = 0
        for i in feedback:
            if i == 2:
                for n in need_check_list:
                    if n[position] != guess[position]:
                        need_check_list[n] -= 4
                        if n in left_check_list:
                            left_check_list.remove(n)
            elif i == 1:
                for n in need_check_list:
                    if  n.find(guess[position]) == -1 or n[position] == guess[position]:
                        need_check_list[n] -= 4
                        if n in left_check_list:
                            left_check_list.remove(n)
            elif i == 0:
                for n in need_check_list:
                    if n.find(guess[position]) != -1:
                        need_check_list[n] -= 4
                        if n in left_check_list:
                            left_check_list.remove(n)
            position += 1
        time += 1
        for i in left_check_list:
            for n in set(i):
                for w in need_check_list:
                    if n in w:
                        need_check_list[i] += 1 
        guess = max(need_check_list, key=need_check_list.get)
    return time







def contest(time, bot1, bot2):
    global answer
    Bot1_score = 0
    Bot2_score = 0
    bot1_total = 0
    bot2_total = 0
    for i in range(time):
            answer = choice(lexicon)
            bot1_time = bot1()
            bot2_time = bot2()
            bot1_total += bot1_time
            bot2_total += bot2_time
            print(f"{bot1_time}/{bot2_time}")
            if bot1_time < bot2_time:
                Bot1_score += 1
            elif bot1_time > bot2_time:
                Bot2_score += 1
    if Bot1_score > Bot2_score:
        print(f"{bot1.__name__.replace("_", " ")} win!")
    elif Bot1_score < Bot2_score:
        print(f"{bot2.__name__.replace("_", " ")} win!")
    else:
        print(f"Draw!")
    print(f"{bot1.__name__.replace("_", " ")} average time is {bot1_total // time}! \n{bot2.__name__.replace("_", " ")} average time is {bot2_total // time}!")


contest(50, frequency_weighted_bot, information_bot)
