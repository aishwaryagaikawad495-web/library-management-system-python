# 📚 Library Management System (Python OOP)

A **console-based Library Management System** built using **Python** and **Object-Oriented Programming (OOP)** principles. This project is designed to strengthen core Python programming skills, OOP concepts, modular programming, and Git/GitHub workflow.

The project is being developed incrementally, with each new feature added through separate Git commits to demonstrate a structured software development process.

---

## ✨ Features

### ✅ Current Features 

-  Add a new book
-  View all books in a formatted table
-  Search books by title
-  Search books by Book ID
-  Search books by author
-  Edit book details
-  Remove books
-  Display total number of books
-  Prevent duplicate Book IDs
-  Basic input validation
-  Interactive menu-driven console application
-  Store book data using JSON
-  Member Management
-  Issue Books
-  Return Books
- View all available books
- View currently issued books
- Automatically load saved books
- Fine Calculation
- Login System (Admin & User)
- Registration System
- Admin and user permission management

---

## 📂 Project Structure

library-management-system-python/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── library.py
│   └── member.py
│   └── member_manager.py
│   └── user.py
│   └── auth_manager.py
│  
├── data/
│   ├── books.json
│   ├── members.json
│   ├── users.json
│
├── utils/
│   ├── fine.py
│
├── docs/
│
├── README.md
└── .gitignore

---

## 🛠️ Technologies Used

- Python 
- Object-Oriented Programming (OOP)
- Git
- GitHub
- Visual Studio Code

---

## 💡 OOP Concepts Implemented

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes
- Methods
- Encapsulation
- Object Interaction
- Modular Project Structure

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/aishwaryagaikawad495-web/library-management-system-python.git
```

### 2. Navigate to the project directory

```bash
cd library-management-system-python
```

### 3. Run the project

```bash
python main.py
```

---

## 📌 Menu

```text
===================================
      Library Management System
===================================

1. Add Book
2. View Books
3. Search Book by Title
4. Search Book by ID
5. Search by Author
6. Remove Book
7. Edit Book
8. Total Books
9. Add Member
10. View Members
11. Search Member
12.Remove Member
13. Issue Book
14. Return Book 
15. View Available Books
16. View Issued Books
17. Exit

```

---

## 🚀 Future Enhancements

The following features are planned for future versions:

### 🗄️ Database Integration
- Replace JSON file storage with SQLite/PostgreSQL database
- Implement database queries for books, members, and transactions
- Improve data management for large-scale records

### 📚 Advanced Book Management
- Track multiple copies of the same book
- Maintain available and issued copy counts

### ⏳ Borrowing & Return Improvements
- Add book due date tracking
- Automated fine calculation based on late returns
- Maintain complete borrowing history

### 📊 Analytics & Reports
- Library statistics dashboard
- Most borrowed books analysis

### 🔐 Security Improvements
- Password hashing for user accounts
- Role-based access control

### 🌐 Web Application Upgrade
- Convert console application into a Flask web application
- Create frontend interface using HTML, CSS, and JavaScript
- Build REST APIs for library operations
- Deploy application online

### 🤖 Smart Features
- Book recommendation system
- Search suggestions
- AI-based library assistant

---

## 🎯 Learning Objectives

This project helps in learning:

- Python Programming
- Object-Oriented Programming
- Modular Code Organization
- Git & GitHub Version Control
- Problem Solving
- Console Application Development

---

## 👩‍💻 Author

**Aishwarya Gaikwad**

- 🎓 Second-Year Engineering Student
- 💻 Python | C++ | Data Structures & Algorithms
- 🌱 Currently learning Software Development and Open Source

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.