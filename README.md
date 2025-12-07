# Web - Personal Website with Flask

A personal blog and website built with Python Flask. This project includes user authentication, admin panel, profile management, and a dynamic homepage showcasing the site owner.

---

## Features

- **User Authentication** - Login and logout with session management
- **Two User Roles** - Admin and regular user accounts
- **Email OTP Verification** - Registration requires email verification
- **Admin Dashboard** - Full user management (Create, Read, Update, Delete)
- **User Dashboard** - Personal dashboard with profile information
- **Profile Management** - Users can update their personal info
- **Games Page** - Reserved games section for verified users
- **Homepage Content Editor** - Admin can edit homepage text content
- **Dynamic Owner Info** - Homepage displays admin's profile (name, email, birthday) from database
- **Profile Image Upload** - Admin can upload profile image for homepage
- **Responsive Design** - Mobile-friendly layout with hamburger menu
- **Magenta & Black Theme** - Modern color scheme throughout

---

## Requirements

- **Python 3.x** (Python 3.8 or higher recommended)
- **XAMPP** (for MySQL database)
- **Web Browser** (Chrome, Firefox, Edge, etc.)
- **Code Editor** (VS Code recommended)

---

## Installation Guide

### Step 1: Install XAMPP

1. Download XAMPP from https://www.apachefriends.org/
2. Install and open XAMPP Control Panel
3. Start **Apache** and **MySQL** services

### Step 2: Clone or Download the Project

```
git clone https://github.com/matrix505/flask_WEB_SYSTEM_client1.git
```

Or download and extract the ZIP file.

### Step 3: Install Python Dependencies

Open terminal/command prompt in the project folder and run (Make sure to download python lib):

```
pip install -r requirements.txt
or python -m pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- mysql-connector-python (database connector)
- Other required packages

### Step 4: Setup the Database

Run the setup script to create the database and tables:

```
python setup_database.py
```

This will:
- Create the `flask_blog_db` database
- Create all required tables (users, otp_codes, email_log, pending_registrations, site_content)
- Create default admin and test user accounts
- Add default site content

### Step 5: Run the Application

```
python app.py
```

### Step 6: Open in Browser

Go to: **http://127.0.0.1:5000**

---

## Default Login Accounts

| Role  | Username  | Password  |
|-------|-----------|-----------|
| Admin | admin     | admin123  |
| User  | testuser  | user123   |

---

## Project Structure

```
flask_app1/
├── app.py                  # Main Flask application (routes)
├── config.py               # Configuration (database, email, secrets)
├── database.py             # Database connection helper
├── models.py               # Database operations (CRUD)
├── email_helper.py         # Email and OTP functions
├── setup_database.py       # Database setup script
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── images/
│       └── profile.png     # Profile image
│
└── templates/
    ├── base.html           # Base template (navbar, footer)
    ├── index.html          # Homepage
    ├── login.html          # Login page
    ├── register.html       # Registration form
    ├── verify_otp.html     # OTP verification page
    ├── user_dashboard.html # User dashboard
    ├── profile.html        # Profile edit page
    ├── games.html          # Games page
    ├── admin_dashboard.html# Admin dashboard
    ├── admin_users.html    # User management list
    ├── admin_add_user.html # Add new user form
    ├── admin_edit_user.html# Edit user form
    ├── admin_content.html  # Homepage content editor
    └── 404.html            # Error page
```

---

## Configuration

### Database Configuration

Edit `config.py` to change database settings:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',           # XAMPP default is empty
    'database': 'flask_blog_db'
}
```

### Email Configuration (for OTP)

To enable email OTP sending, update `config.py`:

```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': 'your_email@gmail.com',
    'password': 'your_app_password'   # Use Gmail App Password
}
```

**Note:** For Gmail, you need to generate an App Password:
1. Go to Google Account > Security
2. Enable 2-Factor Authentication
3. Go to App Passwords and generate one

**Tip:** OTP verification works even without email setup (check terminal for OTP code).

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| MySQL connection error | Make sure XAMPP MySQL is running |
| Module not found | Run `pip install -r requirements.txt` |
| Port already in use | Change port in `app.py` or close other apps |
| Email not sending | Check EMAIL_CONFIG settings in `config.py` |

---

## Technologies Used

- **Backend:** Python Flask
- **Database:** MySQL (via XAMPP)
- **Frontend:** HTML, CSS, Jinja2 Templates
- **Icons:** Font Awesome 6
- **Security:** SHA256 password hashing, session management

---

## Created By

2nd Year Computer Science Student  
December 2025

---

## HTML Pages & Descriptions

Below are the main HTML pages/templates used in this project. Each page has a specific purpose and is styled for a modern, responsive experience.

- **index.html (Homepage):**
  - The main landing page. Shows the site owner's info, a hero section, about, and a games promo. Dynamic content is fetched from the database.

- **login.html (Login Page):**
  - Allows users to log in with their username and password. Modern minimalist design.

- **register.html (Registration Page):**
  - New users can sign up by providing personal details. Includes email OTP verification for security.

- **verify_otp.html (OTP Verification):**
  - After registration, users must enter a code sent to their email to verify their account.

- **user_dashboard.html (User Dashboard):**
  - Shows user info, quick links, and access to games. Only visible to logged-in users.

- **profile.html (Profile Edit Page):**
  - Users can update their personal information and upload a profile image.

- **games.html (Games Page):**
  - Reserved for verified users. Contains fun games and activities.

- **admin_dashboard.html (Admin Dashboard):**
  - Main dashboard for admins. Shows user stats, recent users, and quick management links.

- **admin_users.html (Manage Users):**
  - Admins can view, edit, activate/deactivate, or delete user accounts.

- **admin_add_user.html (Add User):**
  - Admins can manually add new users to the system.

- **admin_edit_user.html (Edit User):**
  - Admins can update user details and status.

- **admin_content.html (Homepage Content Editor):**
  - Admins can update homepage text, tagline, about, and upload the profile image shown on the homepage.

- **404.html (Error Page):**
  - Shown when a page is not found. Friendly error message and link to homepage.

---

## Beginner-Friendly Setup Instructions

Follow these steps to set up and run the project. No advanced experience required!

### 1. Install XAMPP (MySQL Database)
- Download XAMPP from [apachefriends.org](https://www.apachefriends.org/)
- Install and open the XAMPP Control Panel
- Start **Apache** and **MySQL** (these are needed for the website and database)

### 2. Download the Project
- Click the green "Code" button on GitHub and choose "Download ZIP" or use this command:
  ```
  git clone https://github.com/matrix505/flask_WEB_SYSTEM_client1.git
  ```
- Extract the ZIP file if you downloaded it.
- Open the project folder in VS Code or your favorite editor.

### 3. Install Python and Required Libraries
- Make sure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/)
- Open a terminal in the project folder and run:
  ```
  pip install -r requirements.txt
  ```
- This installs Flask and other needed libraries.

### 4. Set Up the Database
- In the terminal, run:
  ```
  python setup_database.py
  ```
- This will create the database, tables, and add sample users/content.
- If you see errors, make sure MySQL is running in XAMPP.

### 5. Run the Website
- In the terminal, run:
  ```
  python app.py
  ```
- Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 6. Login and Explore
- Use the default accounts:
  - Admin: **admin** / **admin123**
  - User: **testuser** / **user123**
- Try registering a new user and check your email for the OTP code (or see the code in the terminal if email isn't set up).

---

## Tips 
- If you get stuck, check the Troubleshooting section below.
- You can change database or email settings in `config.py`.
- All HTML templates are in the `templates/` folder. You can customize them for your own style.
- The CSS is in `static/css/style.css`.
- This project is a great starting point for learning Flask, databases, and web design!

---
