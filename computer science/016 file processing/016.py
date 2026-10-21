import random

def random_numb_list():
    numb_list = [random.randint(1, 70) for i in range(100)]
    with open("/Users/tianqijiang/汇总/computer science/016 file processing/numb.text", "w") as f:
        for i in numb_list:
            f.write(f"{i}\n")