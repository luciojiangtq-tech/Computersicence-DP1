price = [5, 12, 19, 25]
add_price = [i+10 for i in price]
print(add_price)

number = [12, 5, 8, 21, 30, 7, 14]
even_number = [i for i in number if i % 2 == 0]
print(even_number)

str_number = ["10", "20", "30", "40"]
int_number = [int(i) for i in str_number]
print(int_number)

names = ["John", "Alice", "Bob", "Diana"]
first_letter = [i[0] for i in names]
print(first_letter)

grades = [60, 56, 45, 34, 23, 56, 68, 92, 56, 23, 40]
pass_list = ["pass" if i >40 else "fail" for i in grades]
print(pass_list)

item = ["apple", "banana", "cherry"]
item_position = [f"{i}:{x}" for i,x in enumerate(item)]
print(item_position)