# Student Management System
# A beginner-friendly menu-driven console application

# Global list to store student data
# Each student is represented as a dictionary with id, name, age, grade, and email
students = []

# Function to generate a unique ID for each student
next_student_id = 1


def generate_student_id():
    """Generate a unique ID for each new student"""
    global next_student_id
    student_id = next_student_id
    next_student_id += 1
    return student_id


def add_student():
    """Add a new student to the system"""
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
    
    # Create a student dictionary
    student = {
        "id": generate_student_id(),
        "name": name,
        "age": age,
        "grade": grade,
        "email": email
    }
    
    # Add the student to the list
    students.append(student)
    print(f"✅ Student '{name}' added successfully with ID {student['id']}!")


def view_all_students():
    """Display all students in the system"""
    print("\n--- All Students ---")
    
    # Check if there are any students
    if not students:
        print("❌ No students found in the system.")
        return
    
    # Display header
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Grade':<7} {'Email':<25}")
    print("-" * 60)
    
    # Display each student's information
    for student in students:
        print(f"{student['id']:<5} {student['name']:<15} {student['age']:<5} "
              f"{student['grade']:<7} {student['email']:<25}")


def search_student():
    """Search for a student by name or ID"""
    print("\n--- Search Student ---")
    print("1. Search by ID")
    print("2. Search by Name")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Search by ID
        try:
            student_id = int(input("Enter student ID: "))
            found = False
            
            for student in students:
                if student["id"] == student_id:
                    print("\n--- Student Found ---")
                    print(f"ID: {student['id']}")
                    print(f"Name: {student['name']}")
                    print(f"Age: {student['age']}")
                    print(f"Grade: {student['grade']}")
                    print(f"Email: {student['email']}")
                    found = True
                    break
            
            if not found:
                print(f"❌ Student with ID {student_id} not found!")
        
        except ValueError:
            print("❌ Invalid ID! Please enter a number.")
    
    elif choice == "2":
        # Search by Name
        name = input("Enter student name: ").strip().lower()
        found_students = []
        
        for student in students:
            if name in student["name"].lower():
                found_students.append(student)
        
        if not found_students:
            print(f"❌ No students found with name containing '{name}'!")
        else:
            print("\n--- Search Results ---")
            for student in found_students:
                print(f"ID: {student['id']}, Name: {student['name']}, "
                      f"Age: {student['age']}, Grade: {student['grade']}, "
                      f"Email: {student['email']}")
    
    else:
        print("❌ Invalid choice!")


def update_student():
    """Update an existing student's information"""
    print("\n--- Update Student ---")
    
    try:
        student_id = int(input("Enter student ID to update: "))
        student_found = None
        
        # Find the student with the given ID
        for student in students:
            if student["id"] == student_id:
                student_found = student
                break
        
        if not student_found:
            print(f"❌ Student with ID {student_id} not found!")
            return
        
        # Display current information
        print(f"\nCurrent Information:")
        print(f"Name: {student_found['name']}")
        print(f"Age: {student_found['age']}")
        print(f"Grade: {student_found['grade']}")
        print(f"Email: {student_found['email']}")
        
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
                student_found["name"] = new_name
                print(f"✅ Name updated to '{new_name}'!")
            else:
                print("❌ Name cannot be empty!")
        
        elif update_choice == "2":
            try:
                new_age = int(input("Enter new age: "))
                if 5 <= new_age <= 100:
                    student_found["age"] = new_age
                    print(f"✅ Age updated to {new_age}!")
                else:
                    print("❌ Age must be between 5 and 100!")
            except ValueError:
                print("❌ Invalid age! Please enter a number.")
        
        elif update_choice == "3":
            new_grade = input("Enter new grade: ").strip().upper()
            if new_grade:
                student_found["grade"] = new_grade
                print(f"✅ Grade updated to '{new_grade}'!")
            else:
                print("❌ Grade cannot be empty!")
        
        elif update_choice == "4":
            new_email = input("Enter new email: ").strip()
            if new_email:
                student_found["email"] = new_email
                print(f"✅ Email updated to '{new_email}'!")
            else:
                print("❌ Email cannot be empty!")
        
        else:
            print("❌ Invalid choice!")
    
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")


def delete_student():
    """Delete a student from the system"""
    print("\n--- Delete Student ---")
    
    try:
        student_id = int(input("Enter student ID to delete: "))
        student_found = None
        
        # Find the student with the given ID
        for i, student in enumerate(students):
            if student["id"] == student_id:
                student_found = i
                break
        
        if student_found is None:
            print(f"❌ Student with ID {student_id} not found!")
            return
        
        # Confirm deletion
        student_name = students[student_found]["name"]
        confirm = input(f"Are you sure you want to delete '{student_name}'? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            deleted_student = students.pop(student_found)
            print(f"✅ Student '{deleted_student['name']}' deleted successfully!")
        else:
            print("❌ Deletion cancelled.")
    
    except ValueError:
        print("❌ Invalid ID! Please enter a number.")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("    STUDENT MANAGEMENT SYSTEM".center(50))
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 50)


def main():
    """Main function to run the application"""
    print("Welcome to the Student Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
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
            print("\n👋 Thank you for using Student Management System!")
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")


# Entry point of the program
if __name__ == "__main__":
    main()
