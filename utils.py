import mysql

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = sqlite3.connect('gym_database.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
        VALUES (?, ?, ?, ?)
        ''', (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e} - Check if the member ID is valid or other constraints.")
    finally:
        conn.close()

def update_member_age(member_id, new_age):
    conn = sqlite3.connect('gym_database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
    if cursor.fetchone():
        cursor.execute('UPDATE Members SET age = ? WHERE id = ?', (new_age, member_id))
        conn.commit()
        print("Member age updated successfully.")
    else:
        print("Member not found.")
    
    conn.close()

def delete_workout_session(session_id):
    conn = sqlite3.connect('gym_database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM WorkoutSessions WHERE id = ?', (session_id,))
    if cursor.fetchone():
        cursor.execute('DELETE FROM WorkoutSessions WHERE id = ?', (session_id,))
        conn.commit()
        print("Workout session deleted successfully.")
    else:
        print("Session ID not found.")
    
    conn.close()

import mysql.connector

# Add a member


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
