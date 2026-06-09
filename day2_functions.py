
def add(num1,num2):
    return num1+num2
    
print(add(2,3))

x = 10

def my_func():
    global x
    x = 99  
    print(x)

my_func()
print(x)


# day2_functions.py

def calculate_grade(score):
    try:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "F"
    except:
        return "Invalid"


# Test cases
print("Score: 95 -> Grade:", calculate_grade(95))
print("Score: 84 -> Grade:", calculate_grade(84))
print("Score: 73 -> Grade:", calculate_grade(73))
print("Score: 62 -> Grade:", calculate_grade("excellent"))



passed_grades = [calculate_grade(score) for score in scores if score >= 70]

print(passed_grades)
