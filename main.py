import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from oclock import Countdown
from datetime import date
from matplotlib import image as mpimg

print("******************************")
print("----PLANNATE WELCOMES YOU!----")
print("******************************")
print("Do you wish to LOGIN / SIGNUP?")
ls = input()

def emoji():
    global img
    global titl
    print(img,img,img,img,img,img,img,img,img)
    print(titl)
    print(img,img,img,img,img,img,img,img,img)

def analyze_weaknesses():
    cursor = mydb.cursor()
    subjects = ['chemistry', 'maths', 'physics']
    time_avg = {}
    speed_avg = {}

    for subject in subjects:
        # Analyzing Time Management
        time_query = "SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM {} WHERE subject = '{}'".format('JEE_TIME', subject)
        cursor.execute(time_query)
        time_data = cursor.fetchone()
        time_avg[subject] = sum(time_data) / 7

        # Analyzing Speed
        speed_query = "SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM {} WHERE subject = '{}'".format('JEE_SPEED', subject)
        cursor.execute(speed_query)
        speed_data = cursor.fetchone()
        speed_avg[subject] = sum(speed_data) / 7

    min_time_subject = min(time_avg, key = time_avg.get)
    min_speed_subject = min(speed_avg, key = speed_avg.get)

    if min_time_subject == 'chemistry':
        print("Revise the THEORY and FORMULAS in CHEMISTRY.")
    elif min_time_subject == 'physics':
        print("Revise and memorize the FORMULAS and DERIVARIONS in PHYSICS.")
    elif min_time_subject == 'maths':
        print("Revisit the RULES and FORMULAS in MATHS.")

    if min_speed_subject == 'chemistry':
        print("Try to think of questions more SWIFTLY in CHEMISTRY.")
    elif min_speed_subject == 'physics':
        print("Try increasing your PACE in PHYSICS.")
    elif min_speed_subject == 'maths':
        print("Practice and work on your SPEED in MATHS.")

    menu()
