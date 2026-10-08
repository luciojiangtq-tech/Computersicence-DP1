

age = 17
name = "tianqi" 
print(age, name)

price = 9.9999
integer = int(price)
print(price, integer)

global_count = 0
def increment_count():
    global global_count
    global_count += 1

increment_count()
increment_count()
print(global_count)

school_name = "St George's School"

def show_user_info():
    user_name = "Bruno"
    user_age = 16
    is_student = True

    print(user_name)
    print(user_age)
    print(is_student)
    print(school_name)

show_user_info()

#1  0.20  none  none  none
#7  0.20  100   none  none
#3  0.20  100   none  none
#4  0.20  100   20.0  none
#5  0.20  100   20.0  20.0
#6  0.25  100   20.0  none
#8  0.25  200   none  none
#3  0.25  200   none  none
#4  0.25  200   50.0  none
#5  0.25  200   50.0  50.0
#6  0.25  200   50.0  none



