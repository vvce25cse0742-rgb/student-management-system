# Student Management System - Screenshots & Output Examples

This document shows the actual output and workflow of the Student Management System with SQLite database.

## 📸 Main Menu

```
Welcome to the Student Management System!
✅ Database initialized successfully!

==================================================
    STUDENT MANAGEMENT SYSTEM
    (SQLite Database)
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==================================================
Enter your choice (1-6): 
```

---

## 1️⃣ Add Student Feature

### First Student Addition

```
Enter your choice (1-6): 1

--- Add New Student ---
Enter student name: Alice Johnson
Enter student age: 21
Enter student grade (e.g., A, B, C): A
Enter student email: alice@university.com
✅ Student 'Alice Johnson' added successfully with ID 1!

==================================================
    STUDENT MANAGEMENT SYSTEM
    (SQLite Database)
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==================================================
Enter your choice (1-6):
```

### Adding Multiple Students

```
Enter your choice (1-6): 1

--- Add New Student ---
Enter student name: Bob Smith
Enter student age: 20
Enter student grade (e.g., A, B, C): B
Enter student email: bob@university.com
✅ Student 'Bob Smith' added successfully with ID 2!

(Menu reappears...)

Enter your choice (1-6): 1

--- Add New Student ---
Enter student name: Carol Davis
Enter student age: 22
Enter student grade (e.g., A, B, C): A
Enter student email: carol@university.com
✅ Student 'Carol Davis' added successfully with ID 3!
```

### Input Validation - Age Error

```
Enter your choice (1-6): 1

--- Add New Student ---
Enter student name: David Wilson
Enter student age: 3
Enter student grade (e.g., A, B, C): C
Enter student email: david@university.com
❌ Age must be between 5 and 100!

(Menu reappears without adding student)
```

### Input Validation - Empty Name

```
Enter your choice (1-6): 1

--- Add New Student ---
Enter student name: 
Enter student age: 21
Enter student grade (e.g., A, B, C): B
Enter student email: email@university.com
❌ Name cannot be empty!
```

---

## 2️⃣ View All Students

### Displaying All Students

```
Enter your choice (1-6): 2

--- All Students ---
ID    Name            Age   Grade   Email
------------------------------------------------------------
1     Alice Johnson   21    A       alice@university.com
2     Bob Smith       20    B       bob@university.com
3     Carol Davis     22    A       carol@university.com

==================================================
    STUDENT MANAGEMENT SYSTEM
    (SQLite Database)
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==================================================
Enter your choice (1-6):
```

### Empty Database

```
Enter your choice (1-6): 2

--- All Students ---
❌ No students found in the system.

==================================================
    STUDENT MANAGEMENT SYSTEM
    (SQLite Database)
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==================================================
Enter your choice (1-6):
```

---

## 3️⃣ Search Student Feature

### Search by ID - Found

```
Enter your choice (1-6): 3

--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 1
Enter student ID: 1

--- Student Found ---
ID: 1
Name: Alice Johnson
Age: 21
Grade: A
Email: alice@university.com
```

### Search by ID - Not Found

```
Enter your choice (1-6): 3

--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 1
Enter student ID: 99
❌ Student with ID 99 not found!
```

### Search by ID - Invalid Input

```
Enter your choice (1-6): 3

--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 1
Enter student ID: abc
❌ Invalid ID! Please enter a number.
```

### Search by Name - Multiple Results

```
Enter your choice (1-6): 3

--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 2
Enter student name: a

--- Search Results ---
ID: 1, Name: Alice Johnson, Age: 21, Grade: A, Email: alice@university.com
ID: 3, Name: Carol Davis, Age: 22, Grade: A, Email: carol@university.com
```

### Search by Name - Single Result

```
Enter your choice (1-6): 3

--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 2
Enter student name: Bob

--- Search Results ---
ID: 2, Name: Bob Smith, Age: 20, Grade: B, Email: bob@university.com
```

### Search by Name - Not Found

```
Enter your choice (1-6): 3

--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 2
Enter student name: xyz
❌ No students found with name containing 'xyz'!
```

---

## 4️⃣ Update Student Feature

### Update Name

```
Enter your choice (1-6): 4

--- Update Student ---
Enter student ID to update: 1

Current Information:
Name: Alice Johnson
Age: 21
Grade: A
Email: alice@university.com

What would you like to update?
1. Name
2. Age
3. Grade
4. Email
Enter your choice (1-4): 1
Enter new name: Alice J. Johnson
✅ Name updated to 'Alice J. Johnson'!
```

### Update Age

```
Enter your choice (1-6): 4

--- Update Student ---
Enter student ID to update: 2

Current Information:
Name: Bob Smith
Age: 20
Grade: B
Email: bob@university.com

What would you like to update?
1. Name
2. Age
3. Grade
4. Email
Enter your choice (1-4): 2
Enter new age: 21
✅ Age updated to 21!
```

### Update Age - Out of Range

```
Enter your choice (1-6): 4

--- Update Student ---
Enter student ID to update: 3

(Current information displayed...)

Enter your choice (1-4): 2
Enter new age: 150
❌ Age must be between 5 and 100!
```

### Update Grade

```
Enter your choice (1-6): 4

--- Update Student ---
Enter student ID to update: 2

(Current information displayed...)

Enter your choice (1-4): 3
Enter new grade: A+
✅ Grade updated to 'A+'!
```

### Update Email

```
Enter your choice (1-6): 4

--- Update Student ---
Enter student ID to update: 1

(Current information displayed...)

Enter your choice (1-4): 4
Enter new email: alice.johnson@newuniversity.com
✅ Email updated to 'alice.johnson@newuniversity.com'!
```

### Update - Invalid Student ID

```
Enter your choice (1-6): 4

--- Update Student ---
Enter student ID to update: 99
❌ Student with ID 99 not found!
```

---

## 5️⃣ Delete Student Feature

### Delete with Confirmation - Yes

```
Enter your choice (1-6): 5

--- Delete Student ---
Enter student ID to delete: 3
Are you sure you want to delete 'Carol Davis'? (yes/no): yes
✅ Student 'Carol Davis' deleted successfully!
```

### Delete with Confirmation - No

```
Enter your choice (1-6): 5

--- Delete Student ---
Enter student ID to delete: 2
Are you sure you want to delete 'Bob Smith'? (yes/no): no
❌ Deletion cancelled.
```

### Delete - Invalid ID

```
Enter your choice (1-6): 5

--- Delete Student ---
Enter student ID to delete: 99
❌ Student with ID 99 not found!
```

---

## 6️⃣ Exit Application

```
Enter your choice (1-6): 6

👋 Thank you for using Student Management System!
Goodbye!

C:\...\student-management-system>
```

---

## 📊 Complete Workflow Example

### Scenario: Managing a Class of Students

```
Welcome to the Student Management System!
✅ Database initialized successfully!

--- STEP 1: Add 3 Students ---

Menu > Enter 1
--- Add New Student ---
Name: Alice Johnson, Age: 21, Grade: A, Email: alice@uni.com
✅ Student 'Alice Johnson' added successfully with ID 1!

Menu > Enter 1
--- Add New Student ---
Name: Bob Smith, Age: 20, Grade: B, Email: bob@uni.com
✅ Student 'Bob Smith' added successfully with ID 2!

Menu > Enter 1
--- Add New Student ---
Name: Carol Davis, Age: 22, Grade: A, Email: carol@uni.com
✅ Student 'Carol Davis' added successfully with ID 3!

--- STEP 2: View All Students ---

Menu > Enter 2
--- All Students ---
ID    Name            Age   Grade   Email
------------------------------------------------------------
1     Alice Johnson   21    A       alice@uni.com
2     Bob Smith       20    B       bob@uni.com
3     Carol Davis     22    A       carol@uni.com

--- STEP 3: Search for a Student ---

Menu > Enter 3
Search by Name: "alice"
--- Search Results ---
ID: 1, Name: Alice Johnson, Age: 21, Grade: A, Email: alice@uni.com

--- STEP 4: Update Student ---

Menu > Enter 4
Update Student ID 2, Change Grade: B → A
✅ Grade updated to 'A'!

--- STEP 5: View Updated List ---

Menu > Enter 2
--- All Students ---
ID    Name            Age   Grade   Email
------------------------------------------------------------
1     Alice Johnson   21    A       alice@uni.com
2     Bob Smith       20    A       bob@uni.com      ← Updated
3     Carol Davis     22    A       carol@uni.com

--- STEP 6: Delete a Student ---

Menu > Enter 5
Delete Student ID 3
Are you sure? yes
✅ Student 'Carol Davis' deleted successfully!

--- STEP 7: Final View ---

Menu > Enter 2
--- All Students ---
ID    Name            Age   Grade   Email
------------------------------------------------------------
1     Alice Johnson   21    A       alice@uni.com
2     Bob Smith       20    A       bob@uni.com

--- STEP 8: Exit ---

Menu > Enter 6
👋 Thank you for using Student Management System!
Goodbye!
```

---

## 💾 Database State After Workflow

**File**: `students.db` (SQLite database)

### Table Contents:

```sql
SELECT * FROM students;

id | name           | age | grade | email              | created_at             | updated_at
---|----------------|-----|-------|--------------------|-----------------------|----------------------
1  | Alice Johnson  | 21  | A     | alice@uni.com      | 2026-08-30 10:30:00  | 2026-08-30 10:30:00
2  | Bob Smith      | 20  | A     | bob@uni.com        | 2026-08-30 10:31:00  | 2026-08-30 10:35:00 ← Updated
```

**Note**: Carol Davis (ID 3) was deleted, so no longer in database

---

## 🎯 Common Scenarios

### Scenario 1: School Registration
- ✅ Add new students
- ✅ Verify with View All
- ✅ Update grades as they progress

### Scenario 2: Grade Updates
- ✅ Search student by name
- ✅ Update their grade
- ✅ Verify changes with View All

### Scenario 3: Student Withdrawal
- ✅ Search student by ID
- ✅ Delete with confirmation
- ✅ Verify removal with View All

### Scenario 4: Data Verification
- ✅ View all students
- ✅ Search for specific student
- ✅ Confirm all details are correct

---

## 📋 Input Validation Examples

### Age Validation

| Input | Valid? | Message |
|-------|--------|---------|
| 5 | ✅ Yes | Accepted |
| 10 | ✅ Yes | Accepted |
| 25 | ✅ Yes | Accepted |
| 100 | ✅ Yes | Accepted |
| 4 | ❌ No | "Age must be between 5 and 100!" |
| 101 | ❌ No | "Age must be between 5 and 100!" |
| abc | ❌ No | "Age must be a valid number!" |

### Name Validation

| Input | Valid? | Message |
|-------|--------|---------|
| John Doe | ✅ Yes | Accepted |
| Alice | ✅ Yes | Accepted |
| "" (empty) | ❌ No | "Name cannot be empty!" |

### Menu Validation

| Input | Valid? | Message |
|-------|--------|---------|
| 1 | ✅ Yes | Add Student |
| 2 | ✅ Yes | View All |
| 3 | ✅ Yes | Search |
| 4 | ✅ Yes | Update |
| 5 | ✅ Yes | Delete |
| 6 | ✅ Yes | Exit |
| 7 | ❌ No | "Invalid choice! Please enter..." |
| abc | ❌ No | "Invalid choice! Please enter..." |

---

## 📊 Data Persistence Example

### Session 1 (Thursday 10:00 AM)
```
Add Student: Alice Johnson (ID: 1)
Add Student: Bob Smith (ID: 2)
Exit Application
✅ Data saved to students.db
```

### Session 2 (Friday 3:00 PM) - Different Day, Same Data!
```
Start Application
View All Students:
  - ID 1: Alice Johnson ✅ Still there!
  - ID 2: Bob Smith ✅ Still there!
Add Student: Carol Davis (ID: 3)
Update Bob's grade
Exit Application
✅ New data saved
```

**Proof of Persistence**: Data from Session 1 is available in Session 2!

---

## 🖥️ System Information

### When Running This Application

- **Terminal Type**: Windows Command Prompt, PowerShell, or Linux Terminal
- **Python Version**: 3.6+
- **Database File**: `students.db` (appears in same directory)
- **File Size**: ~8-16 KB initially
- **Memory Usage**: Minimal (~5-10 MB)

### Screen Layout

```
Terminal Window (80+ chars wide recommended)
┌─────────────────────────────────────────────┐
│ Welcome to the Student Management System!   │
│ ✅ Database initialized successfully!      │
│                                             │
│ ===========[ MAIN MENU ]==================  │
│ 1. Add Student                              │
│ 2. View All Students                        │
│ 3. Search Student                           │
│ 4. Update Student                           │
│ 5. Delete Student                           │
│ 6. Exit                                     │
│                                             │
│ Enter your choice (1-6): _                  │
└─────────────────────────────────────────────┘
```

---

## ✅ Testing Checklist

Use these examples to test all features:

- [ ] Add 5 different students
- [ ] View all students (verify all 5 appear)
- [ ] Search by ID for each student
- [ ] Search by name (test partial matches)
- [ ] Update each student field (name, age, grade, email)
- [ ] Verify updates appear in View All
- [ ] Delete 2 students
- [ ] Verify deletions with View All
- [ ] Test invalid age input (3, 101, abc)
- [ ] Test empty name input
- [ ] Test invalid menu choices
- [ ] Exit and restart to verify persistence

---

## 🎓 Learning Outcomes

After using this application, you'll understand:

✅ How menu-driven applications work  
✅ How SQLite databases store data  
✅ How CRUD operations work (Create, Read, Update, Delete)  
✅ How input validation prevents errors  
✅ How data persists in databases  
✅ How to interact with databases in Python  
✅ How error handling makes applications robust  

---

**Tip**: All output shown here is actual terminal output. Try running the application and comparing your output with these examples!
