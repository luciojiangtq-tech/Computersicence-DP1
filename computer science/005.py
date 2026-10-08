def validate(user):
    problem = True
    identities = ["T", "A", "S"]
    while problem:
        problem = False
        if len(user) <= 5:
            problem = True
        if not user[:2].isnumeric():
            problem = True
        if not user[2].isalpha() or user[2].lower() != user[2]:
            problem = True
        if user[-2] != "_":
            problem = True
        if not user[-1].isalpha() or user[-1] not in identities:
            problem = True
        elif user[:2] != "00" and user[-1] in ["A", "T"]:
            problem = True
        if not user[3:-2].isalpha() or user[3].upper() != user[3]:
            problem = True

        if problem:
            user = input("There was a problem. Please re enter username: ")

    return user

def validatename(ans, num):
    if num ==2:
        while len(ans.split()) != 2:
            ans = input("please write in correct format")
    elif num ==3:
        while len(ans.split()) != 3 or not ans.split()[2].isnumeric():
            ans = input("please write in correct format")

    return ans
    



def namesystem():
    quit = False
    while quit == False:
        print("Type 1 to create a username. \nType 2 to get your information based on your username. \nType 3 to validate a username. \nType 4 to quit.")
        choose = input()
        if choose == "1":
            print("Tell me your identity: T/A/S")
            identity = input().upper()
            if identity == "S":
                print("Tell me your name and year(firstname surname year)")
                answer = input()
                answer = validatename(answer, 3)
                firstname, surname, year = answer.split()
                surname = surname[0].upper() + surname[1:]
                year = year.strip("Y").strip("0")
                if int(year) < 10:
                    year = "0" + year
                firstname = firstname[0].lower()
                username = year + firstname + surname + "_" + "S"
            else:
                print("Tell me your name(firstname surname)")
                answer = input()
                answer = validatename(answer, 2)
                firstname, surname= answer.split()
                firstname = firstname[0].lower()
                surname = surname[0].upper() + surname[1:]
                username = "00" + firstname + surname + "_" + identity
            print(f"your username is {username}.")

        elif choose == "2":
            username = input("Tell me the username: \n")
            username = validate(username)
            year = "Y" + username[0:2].strip("0")
            firstname = username[2].upper()
            surname = username[3:username.find("_")]
            identity = username[-1]
            if identity == "T":
                identity = "teacher"
            elif identity == "A":
                identity = "admin"
            else:
                identity = "student"
            print(f"{firstname} {surname}, {identity}")

        elif choose == "3":
            username = input("Tell me the username: \n")
            username = validate(username)
            print(f"Your validated username is {username}.")

        elif choose == "4":
            quit = True
            print("Thank you for using, for any questions, please call 123456789")

        elif choose == "123456789":
            quit = True
            print("you can fix it by yourself, right? :D")

        else:
            print("Not a valid a choice.")

namesystem()