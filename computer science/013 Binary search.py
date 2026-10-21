
def found(list, search_key):
    aim = list
    fin_index = 0
    while True:
        index = len(aim)//2
        mid = aim[index]
        fin_index += index
        if search_key > mid:
            aim = aim[index:]
        elif mid > search_key:
            aim = aim[:index]
            fin_index -= index
        elif mid == search_key:
            print(f"It at {fin_index + 1}")
            break

def megafound(list, search_key):
    up = len(list) - 1
    low = 0
    while True:
        mid = low + (up - low)//2
        if list[mid] > search_key:
            up -= (up - low)//2
        elif list[mid] < search_key:
            low += (up - low)//2
        elif list[mid] == search_key:
            low += (up - low)//2
            print(f"It at {mid}")
            break


megafound(["a", "b", "c", "d", "e", "f", "g"], "c")