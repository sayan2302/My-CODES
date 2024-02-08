import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
    except Error as e:
        print("Error: ", e)
        return None
    finally:
        curr=database.cursor()

        # creating and using database
        curr.execute('create database if not exists parkingdata')
        curr.execute('use parkingdata')
        # creating and populating table
        curr.execute("""CREATE TABLE IF NOT EXISTS parkinginfo (
                        Owner VARCHAR(255),
                        TimeOfArrival VARCHAR(255),
                        TimeOfDeparture VARCHAR(255),
                        PlateNumber VARCHAR(20)
                    )""")

        # checking if dataset is already present
        curr.execute(""" select * from parkinginfo """)
        res= curr.fetchall()
        if(len(res)<1):
            curr.execute("""INSERT INTO  parkinginfo (Owner, TimeOfArrival, TimeOfDeparture, PlateNumber) VALUES
                                ('Smith', '09:15', '12:30', 'ABC-123'),
                                ('Johnson', '10:30', '14:45', 'XYZ-789'),
                                ('Williams', '11:45', '15:15', 'DEF-456'),
                                ('Davis', '13:00', '16:45', 'GHI-789'),
                                ('Taylor', '14:15', '18:00', 'JKL-012'),
                                ('Anderson', '15:30', '19:30', 'MNO-345'),
                                ('Martinez', '16:45', '20:15', 'PQR-678'),
                                ('Jackson', '18:00', '21:45', 'STU-901'),
                                ('White', '19:15', '23:00', 'VWX-234'),
                                ('Harris', '20:30', '00:30', 'YZA-567'),
                                ('Clark', '21:45', '01:15', 'BCD-890'),
                                ('Lewis', '23:00', '02:45', 'EFG-123'),
                                ('Lee', '00:15', '04:15', 'HIJ-456'),
                                ('Walker', '01:30', '05:45', 'KLM-789'),
                                ('Hall', '02:45', '07:15', 'NOP-012'),
                                ('Allen', '04:00', '08:45', 'QRS-345'),
                                ('Turner', '05:15', '10:15', 'TUV-678'),
                                ('Baker', '06:30', '11:45', 'WXY-901'),
                                ('Gonzalez', '07:45', '13:30', 'ZAB-234'),
                                ('Thomas', '09:00', '15:00', 'CDE-567')
                            """)
        database.commit()
        return database

def admin(conn):
        adminPassword=input("\nEnter the password: ")
        if adminPassword=="admin":
            admin1(conn)
        else:
            print("\nInvalid Password! please try again...")
            admin(conn)

def showDetails(conn):
    curr = conn.cursor()
    curr.execute('select * from parkinginfo')
    res = curr.fetchall()
    for i in res:
        print(i)
    print('\n\n\n1. Go Back\n2. Exit')
    x=int(input("select your choice: "))
    if x==1:
        admin1(conn)
    else:
        exit()
    
def validateTime(a,d):
    if(len(a)!=5 or int(a[:2])>24 or int(a[3:])<0 or a[2]!=':'):   
        a='Not Registered'                            
    if(len(d)!=5 or int(d[:2])>24 or int(d[3:])<0 or d[2]!=':'):
        d='Not Registered'
    return a,d
    
def updateDetails(conn):
    Owner = input("\nOwner: ")
    a = input("Time Of Arrival (HH:mm): ")
    d = input("Time Of Departure (HH:mm): ")
    TimeOfArrival,TimeOfDeparture= validateTime(a,d)
    PlateNumber = input("Plate Number: ")

    if(any([len(Owner)<1,   len(a)<1,  len(d)<1, len(PlateNumber)<1])):
        print('\nInvalid details!\n\n\n1. Go Back\n2. Exit')
        x=int(input("select your choice: "))
        if x==1:
            admin1(conn)
        else:
            exit()

    curr = conn.cursor()
    curr.execute(f"""insert into parkinginfo values (
                 '{Owner}',
                 '{TimeOfArrival}',
                 '{TimeOfDeparture}',
                 '{PlateNumber}')
                """)
    conn.commit()

    print('\n\n\n1. Go Back\n2. Exit')
    x=int(input("select your choice: "))
    if x==1:
        admin1(conn)
    else:
        exit()

def timeStayed(conn):
    owner = input("\nEnter Owner's name: ")

    curr = conn.cursor()
    curr.execute(f"select * from parkinginfo where owner='{owner}'")
    res = curr.fetchall()
    if(len(res)<1):
        print('\nNo matches!\n\n\n1. Go Back\n2. Exit')
        x=int(input("select your choice: "))
        if x==1:
            admin1(conn)
        else:
            exit()

    # Object destructuring   
    # res[0] =   (owner, a, d, plate) = ('Baker', '06:30', '11:45', 'WXY-901') 
    (owner,a,d,plate) = res[-1]  

    if(len(a)>5 or len(d)>5):
        print(f"\nArrival Time: {a}")
        print(f"Departure Time: {d}")
        print(f"Time Stayed: N/A")
        print(f"Cost Incurred: ₹20")
        print('\n\n\n1. Go Back\n2. Exit')
        x=int(input("select your choice: "))
        if x==1:
            admin1(conn)
        else:
            exit()

    hd = int(d[:2]) 
    ha = int(a[:2]) 
    md = int(d[3:]) 
    ma = int(a[3:]) 

    if(ha>hd):
        hd+=24
    hourDiff = hd-ha
    if(md<ma):
        hourDiff-=1
    if(ma>md):
        md+=60
    minDiff = md-ma

    ts = f"{hourDiff} Hr {minDiff} m"

    print(f"Arrival Time: {a}")
    print(f"Departure Time: {d}")
    print(f"Time Stayed:{ts}")

    # timeStayed= 2Hr20m --> 20+ 2x10 + 10
    cost = 20 + (hourDiff*10)  
    if(minDiff>0):
        cost+=10

    print(f"Cost Incurred:₹{cost}")
    

    print('\n\n\n1. Go Back\n2. Exit')
    x=int(input("select your choice: "))
    if x==1:
        admin1(conn)
    else:
        exit()
    
def admin1(conn):
    print("\n1. Show Details")
    print("2. Insert Details")
    print("3. Bill")


    x=int(input("select your choice: "))
    if x==1:
        showDetails(conn)
    elif x==2:
        updateDetails(conn)
    elif x==3:
        timeStayed(conn)
    else:
        print('\n Invalid option! please try again...')
        admin1(conn)

#Driver code
if __name__ == "__main__":

    # create Connection
    conn=create_connection()
    
    print("****************** WELCOME TO PARKING MANAGEMENT SYSTEM **********************\n\n\n\n**************** YOUR DESIGNATION? *******************\n1. Admin\n2. Exit")
    x=int(input("Choose an option: "))
    if x==1:
        admin(conn)
    else:
        exit()

