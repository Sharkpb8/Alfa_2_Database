# Cinema Database Project

## Project Information

- **Project Name**: Cinema city database
- **Author**: Adam Hlaváčik
- **Contact Information**: hlavacik@spsejecna.cz
- **Date of Completion**: 17.01.2025
- **Institution:** Střední průmyslová škola elektrotechnická, Praha 2, Ječná 30 
- **Type of project:** School project

---

## Project Description
This project is a Cinema Database Manager, built using MySQL for the database and Python for application logic. It allows for the management of genres, movies, halls, screenings, customers, reservations, and loyalty points.

---

## Features and Components

![Image](./doc/Architecture-diagram.png "ER-diagram")
### Architecture
- User
  - This is the client that acceses this app.
- Interface
  - This is the part of the application that mannges inputs and messages.
- Application
  - This is the part of the application that connects the interface with DAO
- DAO
  - This is the part that connects to Database and executes CRUD operations.
- Database
  - This is the databse where the data is stored

---

## Database Design

### E-R Model
![Image](./doc/ER-diagram.png "ER-diagram")

### Import/Export Schema
- The application enables importing data from json.

---

## Configuration

### Application Configuration
- Configuration file: `appconfig.json`.
- Includes database connection settings (e.g., host, port, user, password, database).
- Example of `appconfig.json`:
```
{
    "database":{
        "host":"ip",
        "port":port,
        "user":"username",
        "password":"password",
        "database":"DatabaseName"
    }
}
```

### Transaction Isolation Levels
- Users can set isolation levels:
  - `READ UNCOMMITTED`
  - `READ COMMITTED`
  - `REPEATABLE READ`
  - `SERIALIZABLE`
- Example scenarios for `Dirty Reads` and `Dirty Writes` are implemented.

---

## Installation and Setup
1. Clone the repository.
2. Configure the database connection in `appconfig.json`.
3. Run the database setup scripts to create the schema.
4. Execute the application using:
   ```bash
   python main.py
   ```

---

## Usage

### Core Features
- **Manage Movies and Genres**: Add, update, delete movie and genre records.
- **Screenings**: Schedule and manage screenings.
- **Reservations**: Create and manage reservations for screenings.
- **Loyalty Points**: Transfer points and view transaction history.
- **Reports**:
  - Total movie ticket sales.
  - Customer reservations for upcoming screenings.
  - All reservations summary.
  - Movie performance summary.
  - Revenue by hall type and genre.

### Example Commands
- **Modify Isolation Levels**:
  ```python
  SetIsolationLevel()
  ```
- **Dirty Reads and Writes**:
  Available in `CustomerDAO` and demonstrated via the interface.

---

## Error Handling
- **Global Errors**: Managed using custom exceptions (e.g., `IDValueError`, `NameValueError`).
- **Database Connection Errors**: Handled gracefully with rollback mechanisms.
- **Validation**:
  - String validation (length, special characters).
  - Numeric validation (limits, decimals).
  - Date and Boolean validation.

---

## Dependencies
- Python libraries:
  - `mysql-connector`
  - `ast`
  - `datetime`
  - `math`
  - `re`
- MySQL database.

---

## Summary
This Cinema Database Management System provides a robust and modular solution for managing cinema operations. It ensures data integrity, supports advanced features like loyalty programs, and adheres to high standards of configurability and error handling. The project demonstrates effective use of UML diagrams, transaction isolation levels, and database design principles.

---

## Acknowledgments
- Project guidance by [Your Teacher or Mentor's Name].
- Tools: MySQL, Python, and UML modeling tools.
