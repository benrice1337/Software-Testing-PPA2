import datetime

def bmi(feet: int, inches: int, pounds: int) -> str:
    #BMI function. Also do DB stuff here, probably.
    return ''


def bmi_calculator(feet: int, inches: int, pounds: int) -> int:
    #BMI calculator.
    return 0;


def distance(x1: double, x2: double, y1: double, y2: double) -> str:
    #Distance function. Also do DB stuff here, probably.
    return ''


#Other functions too.

def log_bmi(feet: int, inches: int, pounds: int, result: double) -> None:
    with open('bmi.log', 'a') as log:
        print(feet, inches, pounds, result, str(datetime.datetime.now()), file=log, sep='|')


def log_distance(x1: double, x2: double, y1: double, y2: double, result: double) -> None:
    with open('distance.log', 'a') as log:
        print(x1, x2, y1, y2, result, str(datetime.datetime.now()), file=log, sep='|')
