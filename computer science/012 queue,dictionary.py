import random

item_list = {
    "apple": 325,
    "peach": 799
}
Quantities_Sold_list = dict.fromkeys(item_list, 0)

def add_list(item, price):
    item_list[item] = price
    Quantities_Sold_list[item] = 0
    

def Quantities_Sold(list):
    invalid_list = []
    for i in list:
        if i in Quantities_Sold_list:
            Quantities_Sold_list[i] += 1
        else:
            invalid_list.append(i)
    print(f"invalid item:", ", ".join(invalid_list))

def print_list():
    print("Todays Quantities_Sold_list is", ", ".join(f"{k}: {v}" for k, v in Quantities_Sold_list.items()))
        

Quantities_Sold(["apple", "bb"])
print_list()

teamname_list = {
    "apple": [0, 0],
    "peach": [0, 0],
    "banana": [0, 0]
}

def creat_team(*teamname):
    for i in list(teamname):
        teamname_list[i] = [0, 0]

def update_table(team, result):
    if result:
        teamname_list[team] += 1

def print_table():
    table = sorted(teamname_list.items(), key=lambda i: i[1], reverse=True)
    print(", ".join(f"{k}- Session:{v[0]}, score:{v[1]}" for k, v in table))

def simulate_match(team1, team2):
    choose1 = random.choice([1, 2, 3, 4])
    choose2 = random.choice([1, 2, 3, 4])
    teamname_list[team1][0] += 1 
    teamname_list[team2][0] += 1 
    if choose1 > choose2:
        teamname_list[team1][1] += 1 
    elif choose2 > choose1:
        teamname_list[team2][1] += 1 

def run_match():
    for t in teamname_list:
        teamname_list[t] = [0, 0]
    for i in teamname_list:
        for a in teamname_list:
            if teamname_list[a][0] < len(teamname_list) - 1 and a!= i:
                simulate_match(a, i)
    print_table()

run_match()