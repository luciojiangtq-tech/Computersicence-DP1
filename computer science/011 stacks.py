
def reverse_a_string(string):
    stringlist = list(string)
    reverselist = [stringlist.pop() for i in range(len(stringlist))]
    print(''.join(reverselist))


def code_check():
    code = list(input())
    bracket = [i for i in code if i == "(" or i == ")"]
    number = [1 if bracket.pop()=="(" else -1 for i in range(len(bracket))]
    if sum(number) == 0:
        print("It work")
    else:
        print("Those brackets are not balance")

def code_checktwo():
    try:
        code = list(input())
    except KeyboardInterrupt:
        print("Invalid input")
        exit()
    bracket = []
    for i in code:
        if i == "{":
            bracket.append(i)
        elif i == "}":
            try:
                bracket.pop(-1)
            except ValueError:
                return False
    if not bracket:
        return True
    else:
        return False


def code_checkthree():
    open_bracket = ["(", "[", "{"]
    close_bracket = [")", "]", "}"]
    try:
        code = list(input())
    except KeyboardInterrupt:
        print("Invalid input")
        exit()
    bracket = []
    for i in code:
        if i in open_bracket:
            bracket.append(i)
        elif i in close_bracket:
            try:
                type = bracket.pop(-1)
                if close_bracket.index(i) != open_bracket.index(type):
                    return False
            except:
                return False
    if not bracket:
        return True
    else:
        return False

if code_checkthree():
    print("Yes!")
else:
    print("No!")