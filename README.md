# Student Management System

A beginner-friendly, menu-driven console application built with **Python** and **SQLite** for managing student records with **persistent data storage**.

## 📋 Overview

The Student Management System is a full-featured Python application that stores student information permanently in an **SQLite database**. Unlike previous in-memory versions, all data persists between application sessions, making it suitable for real-world educational use.

**Key Feature**: Data is stored persistently in `students.db` - records survive application restarts! 🗄️

## 📊 Architecture

```
┌─────────────────────────────────────────┐
│  Student Management System (Python App) │
└────────────────┬────────────────────────┘
                 │
         ┌───────▼────────┐
         │  SQLite 3      │
         │  Database      │
         └────────────────┘
                 │
         ┌───────▼────────┐
         │  students.db   │
         │  (Persistent)  │
         └────────────────┘
```

## ✨ Core Features

### CRUD Operations
- **Add Student**: Create new student records with auto-generated IDs
- **View All Students**: Display all students in a formatted table
- **Search Student**: Find students by ID or name (partial match)
- **Update Student**: Modify any student field (name, age, grade, email)
- **Delete Student**: Remove students with confirmation prompt

### Data Management
- **Persistent Storage**: All data saved to SQLite database (students.db)
- **Automatic Timestamps**: Track creation and update times for audit trail
- **Input Validation**: Age validation (5-100), required fields, error messages
- **Error Handling**: Comprehensive exception handling for database operations
- **SQL Injection Prevention**: Parameterized queries for security

### Database Features
- **Auto-Initialization**: Database and tables created automatically on first run
- **Atomic Transactions**: Data consistency guaranteed (commit/rollback)
- **Named Column Access**: Easy row manipulation with sqlite3.Row
- **Efficient Queries**: Optimized SQL for fast data retrieval

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- SQLite3 (included with Python)
- No external dependencies required

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/vvce25cse0742-rgb/student-management-system.git
cd student-management-system
```

2. **Run the application:**
```bash
python main.py
```

The application will:
- ✅ Create `students.db` automatically on first run
- ✅ Initialize the database schema
- ✅ Display the main menu

## 📖 Usage Guide

### Main Menu
```
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
```

### Example Workflows

#### 1. Adding a Student
```
Enter your choice (1-6): 1
--- Add New Student ---
Enter student name: John Doe
Enter student age: 22
Enter student grade (e.g., A, B, C): A
Enter student email: john@example.com
✅ Student 'John Doe' added successfully with ID 1!
```

**What happens:**
- Student record inserted into SQLite database
- Auto-generated ID assigned
- Timestamps recorded (created_at, updated_at)
- Data persists permanently ✅

#### 2. Viewing All Students
```
Enter your choice (1-6): 2
--- All Students ---
ID    Name            Age   Grade   Email
------------------------------------------------------------
1     John Doe        22    A       john@example.com
2     Jane Smith      20    B       jane@example.com
3     Bob Johnson     21    C       bob@example.com
```

**Database Query:**
```sql
SELECT id, name, age, grade, email FROM students ORDER BY id
```

#### 3. Searching for a Student
```
Enter your choice (1-6): 3
--- Search Student ---
1. Search by ID
2. Search by Name
Enter your choice (1 or 2): 1
Enter student ID: 1

--- Student Found ---
ID: 1
Name: John Doe
Age: 22
Grade: A
Email: john@example.com
```

#### 4. Updating Student Information
```
Enter your choice (1-6): 4
--- Update Student ---
Enter student ID to update: 1

Current Information:
Name: John Doe
Age: 22
Grade: A
Email: john@example.com

What would you like to update?
1. Name
2. Age
3. Grade
4. Email
Enter your choice (1-4): 2
Enter new age: 23
✅ Age updated to 23!
```

**Database Update:**
```sql
UPDATE students 
SET age = 23, updated_at = CURRENT_TIMESTAMP 
WHERE id = 1
```

#### 5. Deleting a Student
```
Enter your choice (1-6): 5
--- Delete Student ---
Enter student ID to delete: 2
Are you sure you want to delete 'Jane Smith'? (yes/no): yes
✅ Student 'Jane Smith' deleted successfully!
```

## 💾 Database Details

### File Location
```
student-management-system/
└── students.db  (Created automatically on first run)
```

### Database Schema

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Column Description

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Unique auto-incrementing student ID |
| `name` | TEXT | Student's full name |
| `age` | INTEGER | Age (5-100) |
| `grade` | TEXT | Academic grade (A, B, C, etc.) |
| `email` | TEXT | Email address |
| `created_at` | TIMESTAMP | Record creation timestamp |
| `updated_at` | TIMESTAMP | Last modification timestamp |

### Persistence Benefits

| Feature | Before (In-Memory) | After (SQLite) |
|---------|-------------------|----------------|
| **Data Persistence** | ❌ Lost on exit | ✅ Permanent |
| **Crash Recovery** | ❌ Complete loss | ✅ Full recovery |
| **Multi-Session** | ❌ Isolated | ✅ Shared data |
| **Large Datasets** | ⚠️ Memory limited | ✅ Disk limited |
| **Audit Trail** | ❌ None | ✅ Timestamps |

## 📁 Project Files

```
student-management-system/
│
├── main.py                 # Main application (SQLite implementation)
├── main_with_db.py         # Alternative with statistics feature
├── README.md               # This documentation
├── DATABASE.md             # Detailed database documentation
├── TEST_REPORT.md          # Test results and validation
├── .gitignore              # Git ignore rules
│
└── [students.db]           # SQLite database (auto-created)
```

### File Descriptions

- **main.py** (280+ lines)
  - Complete Student Management System
  - SQLite database operations
  - CRUD implementation with error handling
  - Input validation and user interface

- **main_with_db.py** (350+ lines)
  - Enhanced version with statistics feature
  - Shows grade distribution
  - Calculates average age
  - Displays total student count

- **DATABASE.md**
  - Complete database architecture guide
  - SQL implementation details
  - Security and optimization considerations
  - Troubleshooting guide

- **TEST_REPORT.md**
  - Comprehensive test results
  - All features verified and working
  - Input validation tests
  - Error handling confirmation

## 🏗️ Code Structure

```
main.py Structure:
│
├── create_database()          # Initialize SQLite database
├── get_database_connection()  # Manage connections
├── add_student()              # INSERT operation
├── view_all_students()        # SELECT operation
├── search_student()           # SEARCH operation
├── update_student()           # UPDATE operation
├── delete_student()           # DELETE operation
├── display_menu()             # UI rendering
└── main()                     # Main application loop
```

## ⚠️ Input Validation

The system validates all user inputs:

| Field | Validation | Error Message |
|-------|-----------|---------------|
| Name | Non-empty | "Name cannot be empty!" |
| Age | 5-100 range | "Age must be between 5 and 100!" |
| Age | Numeric | "Age must be a valid number!" |
| Menu | 1-6 | "Invalid choice! Please enter a number between 1 and 6." |
| Confirmation | yes/no | "Deletion cancelled." |

## 🧪 Testing

All features have been tested and verified:

✅ **All menu options** working correctly  
✅ **Input validation** preventing errors  
✅ **Database operations** functioning properly  
✅ **Error handling** graceful and informative  
✅ **Data persistence** verified across sessions  

See `TEST_REPORT.md` for comprehensive test results.

## 🔒 Security Features

- **SQL Injection Prevention**: Parameterized queries used throughout
- **Input Validation**: All user inputs validated before processing
- **Error Handling**: Exceptions caught and handled gracefully
- **Atomic Operations**: Database transactions ensure consistency
- **No Hardcoded Credentials**: Application is self-contained

## 📚 Learning Concepts

This project demonstrates:

**Python Fundamentals**
- Functions and code organization
- Lists, dictionaries, and data structures
- User input/output (input/print)
- Loops and conditional statements
- Exception handling (try/except)
- String manipulation and formatting

**Database Programming**
- SQLite database connection management
- SQL query construction
- CRUD operations (Create, Read, Update, Delete)
- Parameterized queries for security
- Transaction management
- Data persistence

**Software Development**
- Error handling and validation
- User interface design
- Code comments and documentation
- Git version control
- Testing and quality assurance

## 🚀 Future Enhancements

### Potential Improvements

1. **Advanced Search**
   - Filter by grade range
   - Sort by any column
   - Date-based searches

2. **Data Export**
   - CSV export functionality
   - JSON backup format
   - Print reports

3. **Statistics**
   - Grade distribution analysis
   - Average age calculation
   - Performance metrics

4. **Performance**
   - Database indexing
   - Query optimization
   - Connection pooling

5. **Additional Features**
   - Roll number field
   - Class/Section tracking
   - GPA management
   - Attendance tracking

6. **User Interface**
   - GUI with Tkinter/PyQt
   - Web interface with Flask
   - Mobile app support

## 🔧 Configuration

### Environment Variables (Optional)
```bash
# Set custom database location (if implemented)
export SMS_DB_PATH="/custom/path/students.db"
```

### Modifying Database Location

To use a custom database path, modify `main.py`:
```python
DB_FILE = "students.db"  # Change this line
```

## 🐛 Troubleshooting

### Database Issues

**Q: "Database disk image is malformed"**
- A: Delete `students.db` and restart (new database will be created)

**Q: Database is locked**
- A: Ensure only one instance of the application is running

**Q: Can't find students.db**
- A: Check that you're running the application from the correct directory

### Application Issues

**Q: No menu appears after running python main.py**
- A: Ensure Python 3.6+ is installed
- A: Check that you're in the correct directory
- A: Try: `python --version`

**Q: Error: "No module named sqlite3"**
- A: Reinstall Python (sqlite3 is included by default)

## 📞 Support

For help or questions:

1. **Check Documentation**
   - README.md (this file)
   - DATABASE.md (database details)
   - TEST_REPORT.md (test results)

2. **Review Code Comments**
   - main.py has detailed comments
   - Each function is well-documented

3. **View Test Results**
   - TEST_REPORT.md shows all tested scenarios
   - Examples of expected output

## 📜 License

This project is open source and available for educational purposes.

## 🎓 Educational Value

Perfect for:
- Learning Python fundamentals
- Understanding database concepts
- Studying CRUD operations
- Learning SQLite implementation
- Understanding menu-driven applications
- Input validation and error handling
- Git and GitHub workflow

## 👥 Project Information

**Version**: 2.0 (SQLite Edition)  
**Date**: August 2026  
**Status**: ✅ Fully Functional & Tested  
**Lines of Code**: 280+  
**Database**: SQLite 3  
**Python Version**: 3.6+  

---

**Your data is safe and persistent!** 🔐

Made with ❤️ for beginners learning Python
