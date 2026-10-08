from random import randint, choice

def dicegame():
    player_score = 0
    comp_score = 0
    trun = 0
    comp = simplecomp
    print("Let's play agame! Rolling the dice to get score until you or the Evil Computer get 50 score!")
    mode = input("Choose the opponent you want to challenge. Easy or Difficult?").lower()
    while mode not in ["easy", "difficult"]:
        mode = input("You mast face that! Easy or Difficult?").lower()
    if mode == "difficult":
        comp = difficultcomp
        print("Good choice, warrior! Gook luck!")
    else:
        print("Good luck!")
    while  player_score < 50 and comp_score < 50:
        player_score = player(player_score)
        if player_score < 50:
            comp_score = comp(comp_score)
            print("Next turn!")
            trun += 1
    if player_score >= 50:
        print (f"Congratulations, you win! You have defeated the evil enemy!\nIn {comp} mode, you went through {trun} rounds, and get {player_score} score.")
    else:
        print ("Unfortunately, you lost in the darkness.")
    

def player(player_score = 0):
    choose = input("Roll the dice?").lower()
    while choose not in ["yes", "no"]:
        choose =input("You mast face that! yes or no?").lower()
    turn_score = 0

    while choose == "yes":
        player_roll = randint(1, 6)
        if player_roll != 1:
            turn_score += player_roll
            print(f"The number is {player_roll}!, Now your get {turn_score} score this turn.")
            if player_score + turn_score >= 50:
                print("You already get 50 score!")
            choose = input("Continue?").lower()
            while choose not in ["yes", "no"]:
                choose =input("You mast face that! yes or no?").lower()
        else:
            turn_score = 0
            print(f"What a pity! The number is {player_roll}!")
            break
    player_score += turn_score
    print(f"You got {turn_score} point this turn, your score is {player_score}!")
    return player_score

def simplecomp(comp_score = 0):
    comp_roll = 0
    turn_score = 0
    while turn_score < 15:
            comp_roll = randint(1, 6)
            print(f"The comp roll {comp_roll}!")
            if comp_roll != 1:
                turn_score += comp_roll
            else:
                turn_score = 0
                break
    comp_score += turn_score
    print(f"Computer score is {comp_score}.")
    return comp_score







def difficultcomp(comp_score = 0, player_score = 0):
    comp_roll = 0
    turn_score = 0
    loop = True
    choose = [True]
    while loop:
            comp_roll = randint(0, 6)
            if comp_roll == 0:
                comp_roll = 3
            if comp_roll != 1:
                turn_score += comp_roll
                if player_score - 50 < 9:
                    if turn_score >= 13 or comp_score + turn_score > player_score + 10  or comp_score + turn_score > 50:
                        choose.append(False)
                if comp_score + turn_score >=50:
                    choose = [False]
                print(f"The comp roll {comp_roll}!")
                loop = choice(choose)
            else:
                turn_score = 0
                break
    comp_score += turn_score
    print(f"Computer score is {comp_score}.")
    return comp_score





dicegame()