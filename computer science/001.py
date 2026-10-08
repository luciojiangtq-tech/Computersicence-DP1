s = ["chose one"]
num = [1, 25, 99]

def chosenumber():
    answer = int(input(f"{s}:{num}"))
    if answer in num:
        print(answer)
        print("good gob!")
    elif len(s) < 36 :
        s.extend(s)
        chosenumber()
    else:
        print("you make a BAD choose :(")
        print("i will FIND you")

chosenumber()
