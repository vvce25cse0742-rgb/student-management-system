# SQLite Database Implementation

## Overview

The Student Management System has been enhanced with **SQLite database persistence**, replacing the previous in-memory data storage. This ensures that all student records are permanently saved and available across application sessions.

## Database Architecture

```
┌─────────────────────────────────────┐
│  Student Management System (Python) │
└────────────────┬────────────────────┘
                 │
         ┌───────┴────────┐
         │   SQLite 3     │
         │   Database     │
         └────────────────┘
                 │
         ┌───────┴────────┐
         │  students.db   │
         │  (Persistent)  │
         └────────────────┘
```

## Database Schema

### Students Table

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

### Column Descriptions

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `id` | INTEGER | Unique student identifier | PRIMARY KEY, AUTO_INCREMENT |
| `name` | TEXT | Student's full name | NOT NULL |
| `age` | INTEGER | Student's age in years | NOT NULL (5-100 validated in code) |
| `grade` | TEXT | Academic grade (A, B, C, etc.) | NOT NULL |
| `email` | TEXT | Student's email address | NOT NULL |
| `created_at` | TIMESTAMP | Record creation datetime | AUTO-GENERATED |
| `updated_at` | TIMESTAMP | Last update datetime | AUTO-UPDATED |

## Key Features

### 1. **Automatic Database Initialization**
```python
def create_database():
    """Create the SQLite database and students table if they don't exist"""
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (...)
    """)
    connection.commit()
    connection.close()
```
- Database is created automatically on first run
- Table is created if it doesn't exist
- Idempotent operation - safe to call multiple times

### 2. **Connection Management**
```python
def get_database_connection():
    """Establish a connection to the database"""
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row  # Access columns by name
    return connection
```
- Centralized connection creation
- Uses `row_factory` for named column access
- Connection objects properly closed after use

### 3. **SQL Injection Prevention**
All database operations use parameterized queries:

```python
# ✅ SAFE - Using parameter placeholders
cursor.execute("""
    INSERT INTO students (name, age, grade, email)
    VALUES (?, ?, ?, ?)
""", (name, age, grade, email))

# ❌ UNSAFE - String concatenation
cursor.execute(f"INSERT INTO students VALUES ('{name}', ...)")
```

### 4. **Timestamp Tracking**
- `created_at`: Automatically set when record is inserted
- `updated_at`: Automatically updated on each modification
- Useful for audit trails and data history

### 5. **Atomic Operations**
All database operations use transactions:
- `connection.commit()` - Persists changes
- Ensures data consistency and integrity
- Rollback on errors (handled by exception catching)

## CRUD Operations

### CREATE - Add Student

```python
cursor.execute("""
    INSERT INTO students (name, age, grade, email)
    VALUES (?, ?, ?, ?)
""", (name, age, grade, email))
connection.commit()
student_id = cursor.lastrowid
```

**Features:**
- Returns auto-generated student ID
- Validates input before insertion
- Auto-timestamps record

### READ - Retrieve Students

**All Students:**
```python
cursor.execute("SELECT id, name, age, grade, email FROM students ORDER BY id")
students = cursor.fetchall()
```

**By ID:**
```python
cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
student = cursor.fetchone()
```

**By Name (Partial Match):**
```python
cursor.execute("""
    SELECT id, name, age, grade, email FROM students 
    WHERE LOWER(name) LIKE ?
""", (f"%{name}%",))
students = cursor.fetchall()
```

### UPDATE - Modify Student

```python
cursor.execute("""
    UPDATE students 
    SET name = ?, updated_at = CURRENT_TIMESTAMP 
    WHERE id = ?
""", (new_name, student_id))
connection.commit()
```

**Features:**
- Updates `updated_at` timestamp automatically
- Supports selective field updates
- Validates age field (5-100)

### DELETE - Remove Student

```python
cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
connection.commit()
```

**Features:**
- Confirmation required before deletion
- Retrieves student name before deletion
- Atomic operation

## Error Handling

```python
try:
    connection = get_database_connection()
    if connection:
        cursor = connection.cursor()
        # ... SQL operations ...
        connection.commit()
        connection.close()
except sqlite3.Error as e:
    print(f"❌ Error: {e}")
```

**Error Types Handled:**
- Connection errors
- SQL syntax errors
- Data type errors
- Constraint violations
- File I/O errors

## Data Types

### SQLite to Python Mapping

| SQLite Type | Python Type | Example |
|------------|------------|---------|
| INTEGER | int | `22` |
| TEXT | str | `"John Doe"` |
| TIMESTAMP | str (ISO format) | `"2026-08-27 15:30:00"` |

### Type Affinity

SQLite uses "type affinity" rather than strict types:
- INTEGER columns store integers
- TEXT columns store text strings
- TIMESTAMP columns store datetime strings

## Performance Considerations

### Indexing

The current implementation uses a simple schema without additional indexes. For future optimization:

```sql
-- Add indexes for frequently searched columns
CREATE INDEX idx_students_name ON students(name);
CREATE INDEX idx_students_grade ON students(grade);
```

### Query Optimization

**Current queries are optimized for:**
- Small to medium datasets (< 10,000 records)
- Single-user access
- Console application performance

## Advantages Over In-Memory Storage

| Feature | In-Memory | SQLite |
|---------|-----------|--------|
| **Data Persistence** | ❌ Lost on exit | ✅ Permanent |
| **Crash Recovery** | ❌ Data lost | ✅ Fully recoverable |
| **Large Datasets** | ⚠️ Memory limited | ✅ Disk limited |
| **Multi-Session Access** | ❌ Each session isolated | ✅ Shared data |
| **Query Capability** | ❌ Manual searching | ✅ SQL queries |
| **File Size** | N/A | ✅ Lightweight (KB) |
| **Setup Complexity** | ✅ Simple | ⚠️ Requires SQLite |

## Database File Management

### Location
```
student-management-system/
└── students.db  (Created automatically on first run)
```

### File Size
- Initial: ~8-16 KB
- Per 100 students: ~2-5 KB additional

### Backup & Recovery

**Manual Backup:**
```bash
# Copy the database file
cp students.db students.db.backup
```

**Restore from Backup:**
```bash
# Replace corrupted database with backup
cp students.db.backup students.db
```

### Deleting Data

**Remove all student records:**
```sql
DELETE FROM students;
VACUUM;  -- Reclaim space
```

**Delete database file entirely:**
```bash
# Application will recreate database on next run
rm students.db
```

## Git Configuration

The `.gitignore` file excludes the database:

```
# SQLite Database files
*.db
*.sqlite
*.sqlite3
```

**Rationale:**
- Database contains instance-specific data
- Should not be committed to version control
- Each deployment gets its own fresh database

## Advanced Features

### Statistics (Alternative Version)

The `main_with_db.py` file includes a statistics feature:

```python
def get_statistics():
    # Total students count
    # Average age calculation
    # Grade distribution
```

### Future Enhancements

1. **Database Migrations**
   - Schema versioning
   - Automated upgrades

2. **Data Export**
   - CSV export functionality
   - JSON backup format

3. **Advanced Queries**
   - Sorting by any column
   - Filtering by grade range
   - Age-based search

4. **Optimization**
   - Connection pooling
   - Query result caching
   - Bulk operations

## Migration from In-Memory to SQLite

### For Existing Users

If you previously used the in-memory version:

1. **Old data is not automatically migrated** (separate systems)
2. **To preserve old data:**
   - Export from in-memory version (if available)
   - Re-enter manually into new SQLite version
   - Or implement custom migration script

### Backward Compatibility

The new SQLite version is **not backward compatible** with the old in-memory version because:
- Different data storage mechanism
- No shared data between versions
- Each version maintains its own data

## SQL Reference

### Common Queries

**Count total students:**
```sql
SELECT COUNT(*) as total FROM students;
```

**Find students by grade:**
```sql
SELECT * FROM students WHERE grade = 'A';
```

**Sort by name:**
```sql
SELECT * FROM students ORDER BY name ASC;
```

**Find average age:**
```sql
SELECT AVG(age) as average_age FROM students;
```

**Recent updates:**
```sql
SELECT * FROM students ORDER BY updated_at DESC LIMIT 5;
```

## Troubleshooting

### Database is Locked
**Cause:** Application crashed while database was open
**Solution:** Delete `students.db` and restart (application recreates it)

### "Database disk image is malformed"
**Cause:** File corruption
**Solution:** Restore from backup or delete and recreate

### Slow Performance
**Cause:** Large number of records or frequent queries
**Solution:** 
- Add indexes to frequently searched columns
- Implement result pagination
- Consider query optimization

## Conclusion

The SQLite implementation provides:
✅ **Persistent data storage** across sessions  
✅ **ACID compliance** for data integrity  
✅ **Easy backup and recovery** mechanisms  
✅ **Future-proof scalability** for growth  
✅ **Industry-standard database** solution  

The Student Management System is now production-ready for real-world use!
