import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from oclock import Countdown
from datetime import date, datetime

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
    print("Which SUBJECT did you study TODAY?")
    subject = input()
    print("Please enter the DAY :")
    day = input()
    print("How many HOURS did you STUDY?")
    study_time = input()

    if subject in ['chemistry', 'maths', 'physics']:
        update_subject_time(subject, day, study_time)
    else:
        print("INVALID subject name. Please CHOOSE from 'chemistry', 'maths' or 'physics'.")

    menu()


def countdown_timer(duration):
    Countdown(duration)


def update_speed(subject, day_name, speed):
    global mydb
    cursor = mydb.cursor()
    
    update_query = '''UPDATE JEE_SPEED SET {} = %s WHERE subject = %s'''.format(day_name)
    cursor.execute(update_query, (speed, subject))
    mydb.commit()


def timer():
    timer_lengths = {20:':20:',30:':30:',1:'1::'}
    global img
    global titl
          
    print("Which SUBJECT are you studying TODAY?")
    subject = input()
    today = datetime.today()
    day_name = today.strftime("%A")

    print('*******************************************************')
    print('P.S. - Please MAXIMIZE the timer to avoid distractions!')
    print('*******************************************************')
    img = "\U0001F601"
    titl = "ALL THE BEST!"
    emoji()
    start_timer = input('Type "s" to start: ')

    if start_timer == 's':
        print('Choose TIMER LENGTH (20min, 30min, 1hr) :')
        min_ask = int(input())
        
        if min_ask in timer_lengths:
            duration = timer_lengths[min_ask]
            countdown_timer(duration)
            img = "\U0001F604"
            titl = "NICE GOING!"
            emoji()
            print('How many QUESTIONS did you get RIGHT?')
            questions_correct = int(input())
            speed = round((questions_correct / min_ask) * 10, 1)
            
            print('Your SPEED :', speed, 'QUES/10-MIN')
            if subject in ['chemistry', 'maths', 'physics', 'mixed']:
                update_speed(subject, day_name, speed)
            else:
                print("INVALID subject name. Please choose from 'chemistry', 'maths', 'physics' or 'mixed'.")

        else:
            print("INVALID timer length. Please choose from - 20min, 30min, 1hr.")

        menu()


global flag
flag = 0


def test_insert():
    global flag
    today = date.today()
    today_date = today.strftime('%Y-%m-%d')

    nques = int(input("Enter number of QUESTIONS per SUBJECT = "))
    p_ques = int(input("Enter POSITIVE marking = "))
    n_ques = int(input("Enter NEGATIVE marking(-1, etc.) = "))

    if n_ques > 0:
        print("WRONG INPUT. Please TRY AGAIN!")
        n_ques = int(input("Enter NEGATIVE marking(-1,etc.)= "))

    c_phy = int(input("Number of CORRECT questions in PHYSICS = "))
    na_phy = int(input("Number of NON-ATTEMPTED questions in PHYSICS = "))
    in_phy = nques - c_phy - na_phy

    c_chem = int(input("Number of CORRECT questions in CHEMISTRY = "))
    na_chem = int(input("Number of NON-ATTEMPTED questions in CHEMISTRY = "))
    in_chem = nques - c_chem - na_chem

    c_maths = int(input("Number of CORRECT questions in MATHS = "))
    na_maths = int(input("Number of NON-ATTEMPTED questions in MATHS = "))
    in_maths = nques - c_maths - na_maths

    ttl_pstv = (c_phy + c_chem + c_maths)*p_ques
    ttl_ngtv = (in_phy + in_chem + in_maths)*n_ques
    ttl_mrks = ttl_pstv + ttl_ngtv
 
    ttl_max = nques*3*p_ques
    prcnt = (ttl_mrks / ttl_max)*100
    
    global img
    global titl

    if prcnt > 80 or prcnt == 80:
        titl = "AMAZING WORK!"
        img = "\U0001F603"
        emoji()
    elif prcnt < 80 and prcnt > 60:
        titl = "WOHOO! KEEP GOING!"
        img = "\U0001F60A"
        emoji()
    else:
        titl = "It’s okay! You will do BETTER next time!"
        img = "\U0001F61E"
        emoji()

    cursor = mydb.cursor()
    insertion = '''INSERT INTO JEE_MARKS
            (date,nques,c_phy,na_phy,in_phy,c_chem,na_chem,in_chem,
            c_maths,na_maths,in_maths,prcnt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
    data = (today_date, nques, c_phy, na_phy, in_phy, c_chem, na_chem, in_chem,
            c_maths, na_maths, in_maths, prcnt)

    cursor.execute(insertion, data)
    cursor.close()
    mydb.commit()

    choice = input("WANT TO SEE PIE GRAPHS? (Y/y): ")
    
    if choice in 'yY':
        flag = 1
        pie_charts()
    else:
        menu()


def pie_charts():
    global flag

    if flag == 1:
        today = date.today()
        req_date = today.strftime('%Y-%m-%d')
    else:
        req_date = input("Enter the DATE for which you want to see the TEST DETAILS ('YYYY-MM-DD'): ")


    def retrieve_data(req_date):
        cursor = mydb.cursor()

        select_query = '''SELECT c_phy,na_phy,in_phy,
            c_chem,na_chem,in_chem,c_maths,na_maths,in_maths, nques
            FROM JEE_marks WHERE date = %s
            ORDER BY date DESC
            LIMIT 1'''
    
        cursor.execute(select_query, (req_date,))
        result = cursor.fetchone()

        if result is not None:
            phy = [result[0], result[1], result[2]]
            chem = [result[3], result[4], result[5]]
            maths = [result[6], result[7], result[8]]
            ttl_ques = result[9]
            return phy, chem, maths, ttl_ques
        else:
            print('NO DATA found for the given date.')
            return None, None, None, None
        
    phy_data, chem_data, maths_data ,ttl_ques = retrieve_data(req_date)


    def pie_charts_combined(phy_data, chem_data, maths_data):
        labels = ['CORRECT', 'UNATTEMPTED', 'INCORRECT']
        colors = ['#00FF00', '#FFFF00', '#FF0000']
        subjects = ['PHYSICS', 'CHEMISTRY', 'MATHS']
        all_data = [phy_data, chem_data, maths_data]

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        fig.suptitle(f"QUESTION DISTRIBUTION on {req_date}", fontsize=14)

        for ax, data, sub in zip(axes, all_data, subjects):
            non_zero_labels = []
            non_zero_values = []
            non_zero_colors = []

            for label, value, color in zip(labels, data, colors):
                if value != 0:
                    non_zero_labels.append(label)
                    non_zero_values.append(value)
                    non_zero_colors.append(color)

            ax.pie(non_zero_values, labels=non_zero_labels, colors=non_zero_colors,
                   startangle=90, autopct=lambda pct: f"{pct * ttl_ques / 100:.0f}")
            ax.set_title(sub)
            ax.axis('equal')
            ax.set_xlabel(f"TOTAL: {ttl_ques}")

        plt.tight_layout()
        plt.show()

    if phy_data is not None:
        pie_charts_combined(phy_data, chem_data, maths_data)

    mydb.commit()
    flag = 0

    menu()


def line_graph():
    cursor = mydb.cursor()
    select_query = "SELECT date, prcnt FROM JEE_marks ORDER BY date ASC LIMIT 5"
    cursor.execute(select_query)
    result = cursor.fetchall()

    if len(result) < 5:
        print("LESS DATA available in the table. Enter MORE to see the graph.")

    else:
        data_points = [data[0] for data in result]
        percentages = [data[1] for data in result]
        fig, ax = plt.subplots(figsize = (8, 6))
        ax.plot(data_points, percentages)
        ax.set_xlabel('DATA POINTS')
        ax.set_ylabel('PERCENTAGE')
        ax.set_title('LINE GRAPH OF LATEST 5 DATA POINTS')

        plt.show()
        cursor.close()
        mydb.commit()

    menu()


def terminate():
    print('Bye-Bye!')
    

def menu():

    print('******************************')
    print("WOULD YOU LIKE TO :")
    print('1. Enter TIME spent studying.')
    print('2. View the TIME CHART.')
    print('3. Start TIMER.')
    print('4. View the SPEED GRAPH.')
    print('5. View WEAK POINTS.')
    print('6. Enter your TEST DETAILS.')
    print('7. View TEST DETAIL GRAPH.')
    print('8. View PIE CHART (ANALYSIS).')
    print('9. EXIT!')
    print('******************************')
        
    user_action = input('Enter your CHOICE (1-9): ')

    if user_action == '1':
        jee_time()
    elif user_action == '2':
        generate_time_graph()
    elif user_action == '3':
        timer()
    elif user_action == '4':
        generate_speed_graph()
    elif user_action == '5':
        analyze_weaknesses()
    elif user_action == '6':
        test_insert()
    elif user_action == '7':
        line_graph()
    elif user_action == '8':
        pie_charts()
    elif user_action == '9':
        terminate()


if ls == 'signup' or ls == 'SIGNUP':
    user_name = input("Enter your NAME : ")
    global mydb
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "unpocoloco",
    )
    
    def setup_database():
        global mydb
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE {}".format(user_name))
        
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "unpocoloco",
            database = user_name
        )
        
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("-----You are IN. WELCOME!-----")
        
        create_jee_time_table_query = """CREATE TABLE JEE_TIME (
            subject varchar(250),
            monday int(4) NOT NULL,
            tuesday int(4) NOT NULL,
            wednesday int(4) NOT NULL,
            thursday int(4) NOT NULL,
            friday int(4) NOT NULL,
            saturday int(4) NOT NULL,
            sunday int(4) NOT NULL
        )"""
        cursor = mydb.cursor()
        cursor.execute(create_jee_time_table_query)
       
        insert_default_jee_time_query = "INSERT INTO JEE_TIME (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('chemistry', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        insert_default_jee_time_query = "INSERT INTO JEE_TIME (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('maths', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        insert_default_jee_time_query = "INSERT INTO JEE_TIME (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('physics', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        create_jee_speed_table_query = """CREATE TABLE JEE_SPEED (
            subject varchar(250),
            monday int(4) NOT NULL,
            tuesday int(4) NOT NULL,
            wednesday int(4) NOT NULL,
            thursday int(4) NOT NULL,
            friday int(4) NOT NULL,
            saturday int(4) NOT NULL,
            sunday int(4) NOT NULL
        )"""
        cursor = mydb.cursor()
        cursor.execute(create_jee_speed_table_query)
    
        insert_default_jee_time_query = "INSERT INTO JEE_SPEED (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('chemistry', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        insert_default_jee_time_query = "INSERT INTO JEE_SPEED (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('maths', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        insert_default_jee_time_query = "INSERT INTO JEE_SPEED (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('physics', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        insert_default_jee_time_query = "INSERT INTO JEE_SPEED (subject,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        default_time_values = ('mixed', 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(insert_default_jee_time_query, default_time_values)
        mydb.commit()

        create_jee_marks_table_query = """CREATE TABLE JEE_MARKS (
            date DATE,
            nques INT,
            c_phy INT,
            na_phy INT,
            in_phy INT,
            c_chem INT,
            na_chem INT,
            in_chem INT,
            c_maths INT,
            na_maths INT,
            in_maths INT,
            prcnt FLOAT
        )"""
        cursor = mydb.cursor()
        cursor.execute(create_jee_marks_table_query)
        mydb.commit()

    setup_database()
    menu()

elif ls == 'login' or ls == 'LOGIN':
    x = input("Enter NAME : ")
    
    # Check if DATABASE EXISTS before CONNECTING
    temp = mysql.connector.connect(host = "localhost", user = "root", password = "unpocoloco")
    temp_cursor = temp.cursor()
    temp_cursor.execute("SHOW DATABASES LIKE %s",(x,))
    result=temp_cursor.fetchone()
    temp.close()
    
    def login():
        global mydb
    
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "unpocoloco",
            database = x)
        
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("-----You are IN. WELCOME!-----")
    
    if result:
        login()
        menu()
    else:
        print(f"NO ACCOUNT found for '{x}'. Please SIGNUP.")

else:
    print("WRONG INPUT. PLEASE TRY AGAIN!")


