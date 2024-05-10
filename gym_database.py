import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Gretschwhitefalcon1",
        database="gym_database"
    )


def add_member(id, name, age, trainer_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO Members (id, name, age, trainer_id)
        VALUES (%s, %s, %s, %s)
        ''', (id, name, age, trainer_id))
        conn.commit()
        print("Member added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def add_member(id, name, age, trainer_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO Members (id, name, age, trainer_id)
        VALUES (%s, %s, %s, %s)
        ''', (id, name, age, trainer_id))
        conn.commit()
        print("Member added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
        VALUES (%s, %s, %s, %s)
        ''', (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


def update_member_age(member_id, new_age):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM Members WHERE id = %s', (member_id,))
    if cursor.fetchone():
        cursor.execute('UPDATE Members SET age = %s WHERE id = %s', (new_age, member_id))
        conn.commit()
        print("Member age updated successfully.")
    else:
        print("Member not found.")
    
    cursor.close()
    conn.close()

def delete_workout_session(session_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM WorkoutSessions WHERE id = %s', (session_id,))
    if cursor.fetchone():
        cursor.execute('DELETE FROM WorkoutSessions WHERE id = %s', (session_id,))
        conn.commit()
        print("Workout session deleted successfully.")
    else:
        print("Session ID not found.")
    
    cursor.close()
    conn.close()

def list_distinct_trainers():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "SELECT DISTINCT trainer_id FROM Members;"
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("Distinct Trainers:")
    for trainer in results:
        print(trainer[0])
    
    cursor.close()
    conn.close()

def count_members_per_trainer():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = """
    SELECT trainer_id, COUNT(*) AS member_count
    FROM Members
    GROUP BY trainer_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("Members Per Trainer:")
    for result in results:
        print(f"Trainer ID: {result[0]}, Members: {result[1]}")
    
    cursor.close()
    conn.close()
    
def get_members_in_age_range(start_age, end_age):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = """
    SELECT name, age, trainer_id
    FROM Members
    WHERE age BETWEEN %s AND %s;
    """
    cursor.execute(query, (start_age, end_age))
    results = cursor.fetchall()
    
    print(f"Members aged between {start_age} and {end_age}:")
    for result in results:
        print(f"Name: {result[0]}, Age: {result[1]}, Trainer ID: {result[2]}")
    
    cursor.close()
    conn.close()

def main():
    while True:
        print("\nGym Database Management System")
        print("1. Add a new member")
        print("2. Add a new workout session")
        print("3. Update a member's age")
        print("4. Delete a workout session")
        print("5. List distinct trainers")
        print("6. Count members per trainer")
        print("7. Get members in age range")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            id = int(input("Enter member ID: "))
            name = input("Enter member name: ")
            age = int(input("Enter member age: "))
            trainer_id = int(input("Enter trainer ID: "))
            add_member(id, name, age, trainer_id)
        elif choice == '2':
            member_id = int(input("Enter member ID: "))
            date = input("Enter session date (YYYY-MM-DD): ")
            duration_minutes = int(input("Enter duration of session in minutes: "))
            calories_burned = int(input("Enter calories burned: "))
            add_workout_session(member_id, date, duration_minutes, calories_burned)
        elif choice == '3':
            member_id = int(input("Enter member ID: "))
            new_age = int(input("Enter new age: "))
            update_member_age(member_id, new_age)
        elif choice == '4':
            session_id = int(input("Enter session ID: "))
            delete_workout_session(session_id)
        elif choice == '5':
            list_distinct_trainers()
        elif choice == '6':
            count_members_per_trainer()
        elif choice == '7':
            start_age = int(input("Enter start age: "))
            end_age = int(input("Enter end age: "))
            get_members_in_age_range(start_age, end_age)
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
