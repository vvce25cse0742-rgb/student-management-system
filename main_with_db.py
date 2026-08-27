# Student Management System with SQLite Database
# A beginner-friendly menu-driven console application with persistent data storage

import sqlite3
import os
from datetime import datetime

# Database file name
DB_FILE = "students.db"


def create_database():
    """Create the SQLite database and students table if they don't exist"""
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        
        # Create students table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL,
                email TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        connection.commit()
        connection.close()
        print("✅ Database initialized successfully!")
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")


def get_database_connection():
    """Establish a connection to the database"""
    try:
        connection = sqlite3.connect(DB_FILE)
        connection.row_factory = sqlite3.Row  # Access columns by name
        return connection
    except sqlite3.Error as e:
        print(f"❌ Connection error: {e}")
        return None


def add_student():
    """Add a new student to the database"""
    print("\n--- Add New Student ---")
    
    # Get student details from user input
    name = input("Enter student name: ").strip()
    
    # Validate name
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    try:
        age = int(input("Enter student age: "))
        if age < 5 or age > 100:
            print("❌ Age must be between 5 and 100!")
            return
    except ValueError:
        print("❌ Age must be a valid number!")
        return
    
    grade = input("Enter student grade (e.g., A, B, C): ").strip().upper()
    email = input("Enter student email: ").strip()
    
    # Insert into database
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            
            cursor.execute("""
                INSERT INTO students (name, age, grade, email)
                VALUES (?, ?, ?, ?)
            """, (name, age, grade, email))
            
            connection.commit()
            student_id = cursor.lastrowid
            connection.close()
            
            print(f"✅ Student '{name}' added successfully with ID {student_id}!")
    except sqlite3.Error as e:
        print(f"❌ Error adding student: {e}")


def view_all_students():
    """Display all students from the database"""
    print("\n--- All Students ---")
    
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, age, grade, email FROM students ORDER BY id")
            
            students = cursor.fetchall()
            connection.close()
            
            if not students:
                print("❌ No students found in the system.")
                return
            
            # Display header
            print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Grade':<7} {'Email':<25}")
            print("-" * 60)
            
            # Display each student
            for student in students:
                print(f"{student['id']:<5} {student['name']:<15} {student['age']:<5} "
                      f"{student['grade']:<7} {student['email']:<25}")
    
    except sqlite3.Error as e:
        print(f"❌ Error retrieving students: {e}")


def search_student():
    """Search for a student by name or ID"""
    print("\n--- Search Student ---")
    print("1. Search by ID")
    print("2. Search by Name")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    try:
        if choice == "1":
            # Search by ID
            try:
                student_id = int(input("Enter student ID: "))
                
                connection = get_database_connection()
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
                    
                    student = cursor.fetchone()
                    connection.close()
                    
                    if student:
                        print("\n--- Student Found ---")
                        print(f"ID: {student['id']}")
                        print(f"Name: {student['name']}")
                        print(f"Age: {student['age']}")
                        print(f"Grade: {student['grade']}")
                        print(f"Email: {student['email']}")
                        print(f"Created: {student['created_at']}")
                        print(f"Updated: {student['updated_at']}")
                    else:
                        print(f"❌ Student with ID {student_id} not found!")
            
            except ValueError:
                print("❌ Invalid ID! Please enter a number.")
        
        elif choice == "2":
            # Search by Name
            name = input("Enter student name: ").strip().lower()
            
            connection = get_database_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT id, name, age, grade, email FROM students WHERE LOWER(name) LIKE ?",
                    (f"%{name}%",)
                )
                
                students = cursor.fetchall()
                connection.close()
                
                if not students:
                    print(f"❌ No students found with name containing '{name}'!")
                else:
                    print("\n--- Search Results ---")
                    for student in students:
                        print(f"ID: {student['id']}, Name: {student['name']}, "
                              f"Age: {student['age']}, Grade: {student['grade']}, "
                              f"Email: {student['email']}")
        
        else:
            print("❌ Invalid choice!")
    
    except sqlite3.Error as e:
        print(f"❌ Search error: {e}")


def update_student():
    """Update an existing student's information"""
    print("\n--- Update Student ---")
    
    try:
        student_id = int(input("Enter student ID to update: "))
        
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            
            student = cursor.fetchone()
            
            if not student:
                print(f"❌ Student with ID {student_id} not found!")
                connection.close()
                return
            
            # Display current information
            print(f"\nCurrent Information:")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print(f"Email: {student['email']}")
            
            # Ask which field to update
            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Grade")
            print("4. Email")
            
            update_choice = input("Enter your choice (1-4): ").strip()
            
            if update_choice == "1":
                new_name = input("Enter new name: ").strip()
                if new_name:
                    cursor.execute(
                        "UPDATE students SET name = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                        (new_name, student_id)
                    )
                    connection.commit()
                    print(f"✅ Name updated to '{new_name}'!")
                else:
                    print("❌ Name cannot be empty!")
            
            elif update_choice == "2":
                try:
                    new_age = int(input("Enter new age: "))
                    if 5 <= new_age <= 100:
                        cursor.execute(
                            "UPDATE students SET age = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                            (new_age, student_id)
                        )
                        connection.commit()
                        print(f"✅ Age updated to {new_age}!")
                    else:
                        print("❌ Age must be between 5 and 100!")
                except ValueError:
                    print("❌ Invalid age! Please enter a number.")
            
            elif update_choice == "3":
                new_grade = input("Enter new grade: ").strip().upper()
                if new_grade:
                    cursor.execute(
                        "UPDATE students SET grade = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                        (new_grade, student_id)
                    )
                    connection.commit()
                    print(f"✅ Grade updated to '{new_grade}'!")
                else:
                    print("❌ Grade cannot be empty!")
            
            elif update_choice == "4":
                new_email = input("Enter new email: ").strip()
                if new_email:
                    cursor.execute(
                        "UPDATE students SET email = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                        (new_email, student_id)
                    )
                    connection.commit()
                    print(f"✅ Email updated to '{new_email}'!")
                else:
                    print("❌ Email cannot be empty!")
            
            else:
                print("❌ Invalid choice!")
            
            connection.close()
    
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")
    except sqlite3.Error as e:
        print(f"❌ Update error: {e}")


def delete_student():
    """Delete a student from the database"""
    print("\n--- Delete Student ---")
    
    try:
        student_id = int(input("Enter student ID to delete: "))
        
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
            
            student = cursor.fetchone()
            
            if not student:
                print(f"❌ Student with ID {student_id} not found!")
                connection.close()
                return
            
            # Confirm deletion
            student_name = student['name']
            confirm = input(f"Are you sure you want to delete '{student_name}'? (yes/no): ").strip().lower()
            
            if confirm == "yes":
                cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
                connection.commit()
                print(f"✅ Student '{student_name}' deleted successfully!")
            else:
                print("❌ Deletion cancelled.")
            
            connection.close()
    
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")
    except sqlite3.Error as e:
        print(f"❌ Delete error: {e}")


def get_statistics():
    """Display database statistics"""
    print("\n--- Database Statistics ---")
    
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            
            # Total students
            cursor.execute("SELECT COUNT(*) as total FROM students")
            total = cursor.fetchone()['total']
            
            if total == 0:
                print("❌ No students in the database.")
                connection.close()
                return
            
            # Average age
            cursor.execute("SELECT AVG(age) as avg_age FROM students")
            avg_age = cursor.fetchone()['avg_age']
            
            # Grade distribution
            cursor.execute("SELECT grade, COUNT(*) as count FROM students GROUP BY grade ORDER BY grade")
            grades = cursor.fetchall()
            
            connection.close()
            
            print(f"Total Students: {total}")
            print(f"Average Age: {avg_age:.1f} years")
            print("\nGrade Distribution:")
            for grade_info in grades:
                print(f"  Grade {grade_info['grade']}: {grade_info['count']} student(s)")
    
    except sqlite3.Error as e:
        print(f"❌ Statistics error: {e}")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("    STUDENT MANAGEMENT SYSTEM".center(50))
    print("    (With SQLite Database)".center(50))
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. View Statistics")
    print("7. Exit")
    print("=" * 50)


def main():
    """Main function to run the application"""
    print("Welcome to the Student Management System!")
    
    # Initialize database
    create_database()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            get_statistics()
        elif choice == "7":
            print("\n👋 Thank you for using Student Management System!")
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 7.")


# Entry point of the program
if __name__ == "__main__":
    main()
