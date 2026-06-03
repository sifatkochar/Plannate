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


def generate_time_graph():
    global img
    global titl
    cursor = mydb.cursor()

    chem_time_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_TIME WHERE subject = "chemistry"'''
    cursor.execute(chem_time_query)
    chemistry_time = cursor.fetchall()

    physics_time_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_TIME WHERE subject = "physics"'''
    cursor.execute(physics_time_query)
    physics_time = cursor.fetchall()

    maths_time_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_TIME WHERE subject = "maths"'''
    cursor.execute(maths_time_query)
    maths_time = cursor.fetchall()

    tdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    chem_time_values = []
    physics_time_values = []
    maths_time_values = []

    for row in chemistry_time:
        chem_time_values.extend(row)
    for row in physics_time:
        physics_time_values.extend(row)
    for row in maths_time:
        maths_time_values.extend(row)

    total_time_values = chem_time_values + physics_time_values + maths_time_values
    avg_total_time = sum(total_time_values) / len(total_time_values)

    if avg_total_time < 7:
        titl = "You need to IMPROVE your STUDY HOURS!"
        img = "\U0001F61E"
        emoji()
    elif avg_total_time >= 11:
        titl = "AMAZING WORK! KEEP GOING."
        img = "\U0001F603"
        emoji()
    else:
        titl = "PERFECT!"
        img = "\U0001F60A"
        emoji()

    barWidth = 0.3
    xc_axis = np.arange(len(chem_time_values))
    xp_axis = [x+barWidth for x in xc_axis]
    xm_axis = [x+barWidth for x in xp_axis]
    plt.bar(xc_axis, chem_time_values, width = barWidth, color = 'green', label = 'CHEMISTRY')
    plt.bar(xp_axis, physics_time_values, width = barWidth, color = 'blue', label = 'PHYSICS')
    plt.bar(xm_axis, maths_time_values, width = barWidth, color = 'orange', label = 'MATHS')

    plt.ylabel('TIME')
    plt.title('TIME GRAPH')
    plt.xticks([r+barWidth for r in range(len(chem_time_values))], tdays)
    plt.legend()
    plt.show()

    menu()


def generate_speed_graph():
    global img
    global titl
    cursor = mydb.cursor()

    chem_speed_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_SPEED WHERE subject = "chemistry"'''
    cursor.execute(chem_speed_query)
    chemistry_speed = cursor.fetchall()

    physics_speed_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_SPEED WHERE subject = "physics"'''
    cursor.execute(physics_speed_query)
    physics_speed = cursor.fetchall()

    maths_speed_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_SPEED WHERE subject = "maths"'''
    cursor.execute(maths_speed_query)
    maths_speed = cursor.fetchall()

    mixed_speed_query = '''SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM JEE_SPEED WHERE subject = "mixed"'''
    cursor.execute(mixed_speed_query)
    mixed_speed = cursor.fetchall()

    sdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    chem_speed_values = []
    physics_speed_values = []
    maths_speed_values = []
    mixed_speed_values = []

    for row in chemistry_speed:
        for i in row:
            chem_speed_values.append(i)
    for row in physics_speed:
        for i in row:
            physics_speed_values.append(i)
    for row in maths_speed:
        for i in row:
            maths_speed_values.append(i)
    for row in mixed_speed:
        for i in row:
            mixed_speed_values.append(i)

    total_speed_values = chem_speed_values + physics_speed_values + maths_speed_values + mixed_speed_values
    total_valid_speed_values = []
    for value in total_speed_values:
        if value not in (0, None):
            total_valid_speed_values.append(value)
    
    try:
        avg_speed = sum(total_valid_speed_values) / len(total_valid_speed_values)
        
        if avg_speed < 1.5:
            titl = "AMAZING WORK! KEEP GOING."
            img = "\U0001F603"
            emoji()
        elif avg_speed > 3.5:
            titl = "You need to work on your PACE!"
            img = "\U0001F61E"
            emoji()
        else:
            titl = "PERFECT!"
            img = "\U0001F60A"
            emoji()
    
    except ZeroDivisionError:
        print('Please enter some RECORDS.')

    mask_mixed = np.array([True if value == 0 or value is None else False for value in mixed_speed_values])
    mixed_speed_values = np.ma.masked_array(mixed_speed_values, mask = mask_mixed)

    mask_maths = np.array([True if value == 0 or value is None else False for value in maths_speed_values])
    maths_speed_values = np.ma.masked_array(maths_speed_values, mask = mask_maths)

    mask_physics = np.array([True if value == 0 or value is None else False for value in physics_speed_values])
    physics_speed_values = np.ma.masked_array(physics_speed_values, mask = mask_physics)

    mask_chem = np.array([True if value == 0 or value is None else False for value in chem_speed_values])
    chem_speed_values = np.ma.masked_array(chem_speed_values, mask = mask_chem)
    
    x_axis = np.arange(1, 8, 1)
    plt.plot(x_axis, chem_speed_values, 'o-', color = 'blue', label = 'CHEMISTRY')
    plt.plot(x_axis, physics_speed_values, 'o-', color = 'red', label = 'PHYSICS')
    plt.plot(x_axis, maths_speed_values, 'o-', color = 'green', label = 'MATHS')
    plt.plot(x_axis, mixed_speed_values, 'o-', color = 'yellow', label = 'MIXED')

    plt.ylabel('QUESTIONS / 10-MINUTES')
    plt.title('SPEED GRAPH')
    plt.xticks(x_axis, sdays)
    plt.legend()
    plt.show()

    menu()


def update_subject_time(subject, day, study_time):
    cursor = mydb.cursor()

    update_query = '''UPDATE JEE_TIME SET {} = %s WHERE subject = %s'''.format(day)
    cursor.execute(update_query, (study_time, subject))
    mydb.commit()


def jee_time():
    print("Which subject did you study today?")
    subject = input()
    print("Please enter the day :")
    day = input()
    print("How many hours did you study?")
    study_time = input()

    if subject in ['chemistry', 'maths', 'physics']:
        update_subject_time(subject, day, study_time)
    else:
        print("INVALID subject name. Please choose from 'chemistry', 'maths' or 'physics'.")

    menu()