min = input("tell me your remaining lifetim")
min = 60
hour = int(min) // 60
minute = int(min) % 60
if hour > 24:
    day = hour // 24
    hour = hour % 24
    print(f"Your remaining lifetime is {day} day and {hour} hours")
else:
    print(f"Your remaining lifetime is {hour} hour(s) and {minute} minute(s).")
