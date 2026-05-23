import psycopg2
# from dash import Dash, html


def get_connection():
           return psycopg2.connect(dbname="student",
                                    user="postgres",
                                    password="Priyanshi@569",
                                    host="localhost",
                                    port="5433")


def create_table():
        connect = get_connection()
        cursor = connect.cursor()
        cursor.execute('''
            create table IF NOT EXISTS students(name Text NOT NULL,
            rollno INT PRIMARY KEY,
            course Text, 
            age int CHECK (age>0));
                    ''')

        connect.commit()
        connect.close()  


def add_data():
        connect = get_connection()
        cursor = connect.cursor()

        name = input('enter name:')
        rollno = input('enter roll num.:')
        course = input('enter course:')
        age = input('enter age:')
        if age<=0:
             print("Invalid age")
             return
        query ='''insert into students(name,rollno,course,age) values(%s,%s,%s,%s);'''
        try:
           cursor.execute(query,(name,rollno,course,age))
        except Exception as err:
             print("Error :",err) 
        print("data added successfully")

        connect.commit()
        connect.close()


def update_data():
        connect = get_connection()
        cursor = connect.cursor()
        roll = int(input("Enter roll no:"))
        new_age = int(input("Enter age:"))
        new_course = input("Enter new course:")

        query = '''UPDATE students 
                        SET age = %s,
                            course = %s
                        WHERE rollno = %s'''
        
        cursor.execute(query,(new_age,new_course,roll))

        print("data updated successfully")

        connect.commit()
        connect.close()


def view_data():
        connect = get_connection()
        cursor = connect.cursor()
        cursor.execute('''
        select * from students;
                ''')
        rows = cursor.fetchall()
        print("\n--- Student Details ---")
        for row in rows:
          print(f"Name: {row[0]}")
          print(f"Roll no: {row[1]}")
          print(f"course: {row[2]}")
          print(f"Age: {row[3]}")
          print()

        connect.close()


def search_data():
        connect = get_connection()
        cursor = connect.cursor()

        roll = int(input("Enter roll no to search: "))
        query = "SELECT * FROM students WHERE rollno = %s"
        cursor.execute(query,(roll,))    

        row = cursor.fetchone()

        if row:
          print(f"Name: {row[0]}")
          print(f"Roll no: {row[1]}")
          print(f"Course: {row[2]}")
          print(f"Age: {row[3]}")
          print()
        else:
            print("student not found")

        connect.close()

def delete_data():
        connect = get_connection()
        cursor = connect.cursor()

        roll = int(input("Enter roll no to delete: "))

        query = "DELETE FROM students WHERE rollno = %s"
        cursor.execute(query,(roll,))

        print("Data deleted successfully")    
        connect.commit()
        connect.close()

create_table()

while True:
    print("Press 1 add data \n Press 2 for Update data \n Press 3 View data \n Press 4 Search data \n Press 5 Delete data \n Press 6 Exit data" )
    try:
        res = int(input("What do you want to do:"))
    except Exception as err:
        print("Please enter valid number!")
        continue

    if res == 1:
        add_data()

    elif res == 2:
        update_data()

    elif res == 3:
        view_data()
        
    elif res == 4:
        search_data()

    elif res == 5:
        delete_data()
    
    elif res == 6:
        print("program ended")
        break
