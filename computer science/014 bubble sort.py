
def bubble(listt):
    corn = True
    while corn:
        corn = False
        for i in range(len(listt)-1):
            if listt[i] > listt[i+1]:
                move = listt[i]
                listt[i] = list[i+1]
                listt[i+1] = move
                corn = True
    return list

print(bubble([1, 5, 3, 4]))


