import math
import datetime

def bmi(feet: int, inches: int, pounds: int) -> str:
    if not isinstance(feet, int) or not isinstance(inches, int) or not isinstance(pounds, int):
        return "Invalid input"
    if feet < 0 or inches < 0 or pounds < 0:
        return "Invalid input"
    if feet == 0 and inches == 0:
        return "Invalid input"
    if pounds == 0:
        return "Invalid input"
    bmi = bmi_calculator(feet, inches, pounds)
    appraisal = "Obese"
    if bmi < 18.5:
        appraisal = "Underweight"
    elif bmi < 25:
        appraisal = "Normal"
    elif bmi < 30:
        appraisal = "Overweight"
    return 'Your BMI is ' + str(bmi) + ', making you ' + appraisal


def bmi_calculator(feet: int, inches: int, pounds: int) -> int:
    kilos = pounds * 0.45
    meters = ((feet * 12) + inches) * 0.025
    meters = meters * meters
    bmi = kilos / meters
    return bmi


def retirement(age: int, salary: int, save: int, goal: int) -> str:
    if not isinstance(age, int) or not isinstance(salary, int) or not isinstance(save, int) or not isinstance(goal, int):
        return 'Invalid input'
    if age >= 100:
        return 'Invalid input'
    if age <= 0 or salary <= 0 or save <= 0 or goal <= 0:
        return 'Invalid input'
    goal_age = ret_calculator(age, salary, save, goal)
    if goal_age >= 100:
        return "You'll be dead before you reach your goal!"
    return "You'll reach your goal at age " + str(goal_age)


def ret_calculator(age: int, salary: int, save: int, goal: int) -> int:
    percent = save * 1.35 / 100
    savings = 0
    goal_age = age
    while savings < goal:
        savings += salary * percent
        goal_age += 1
    return goal_age


def distance(x1: float, x2: float, y1: float, y2: float) -> str:
    if not isinstance(x1, float) or not isinstance(x2, float) or not isinstance(y1, float) or not isinstance(y2, float):
        return 'Invalid input'
    #Distance function. Also do DB stuff here, probably.
    distance = distance_calculator(x1, x2, y1, y2)
    return 'The distance is ' + str(distance)


def distance_calculator(x1: float, x2: float, y1: float, y2: float) -> float:
    return math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))


def split_tip(guests: int, bill: float) -> str:
    if not isinstance(guests, int) or not isinstance(bill, float):
        return 'Invalid input'
    guest_pay = ''
    if guests > 50:
        guest_pay = 'Invalid input'
        return guest_pay
    guest_dist = []
    split = splitter(guests, bill)
    bill = round(bill*1.15, 2)
    difference = bill - (guests * split)
    difference = (math.floor(100*difference))/100
    for i in range(guests):
        guest_dist.append(split)
    j = 0
    while difference > 0:
        guest_dist[j] += 0.01
        guest_dist[j] = math.ceil(100*guest_dist[j])/100
        if j < guests:
            j += 1
        else:
            j = 0
        difference -= 0.01
    for i in range(guests):
        guest_pay += ('guest' + str(i+1) + "-$" + str(guest_dist[i]) + "\n")
    return guest_pay


def splitter(guests: int, bill: float) -> float:
    split = math.floor(100*((bill*1.15)/guests))
    split /= 100
    return split


def log_bmi(feet: int, inches: int, pounds: int, result: float) -> None:
    with open('bmi.log', 'a') as log:
        print(feet, inches, pounds, result, str(datetime.datetime.now()), file=log, sep='|')


def log_distance(x1: float, x2: float, y1: float, y2: float, result: float) -> None:
    with open('distance.log', 'a') as log:
        print(x1, x2, y1, y2, result, str(datetime.datetime.now()), file=log, sep='|')


def main_loop():
    while true:
        print("Pick a function:")
        print("1. Body Mass Index")
        print("2. Retirement")
        print("3. Shortest Distance")
        print("4. Split the Tip")
        print("5. Exit")
        choice = input("Integer, please: ")

        if choice == 1:
            print("How many feet tall are you (integer only)?")
            feet = input("> ")
            print("And how many inches (integer only)?")
            inches = input("> ")
            print("How many pounds do you weight (integer only)?")
            pounds = input("> ")
            print(bmi(feet, inches, pounds))
        elif choice == 2:
            print("How old are you (integer only)?")
            age = input("> ")
            print("What is your salary (integer only)?")
            salary = input("> ")
            print("What percentage of that do you save (integer only)?")
            save = input("> ")
            print("What is your goal (integer only)?")
            goal = input("> ")
            print(retirement(age, salary, save, goal))
        elif choice == 3:
            print("X1 coordinate:")
            x1 = input("> ")
            print("Y1 coordinate:")
            y1 = input("> ")
            print("X2 coordinate:")
            x2 = input("> ")
            print("Y2 coordinate:")
            y2 = input("> ")
            print(distance(x1, x2, y1, y2))
        elif choice == 4:
            print("How many guests are there (integer only)?")
            guests = input("> ")
            print("What is the bill, excluding tax?")
            bill = round(input("> "), 3)
            print(split_tip(guests, bill))
        elif choice == 5:
            print("Bye!")
            return
        else:
            print("Not a valid choice. Try again.")


if __name__ == "__main__":
    main_loop()
