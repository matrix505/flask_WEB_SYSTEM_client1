# MyBlog - Personal Website with Flask

A personal blog and website project built with Python Flask for a 2nd year CS student project.

## Features

- **User Authentication**: Login/logout with session management
- **Two User Roles**: Admin and regular users
- **Registration with OTP**: Email verification during registration
- **Admin Dashboard**: Manage all users (CRUD operations)
- **User Dashboard**: Personal dashboard with profile info
- **Profile Management**: Update personal information
- **Responsive Design**: Works on desktop and mobile

## Requirements

- Python 3.x
- XAMPP (for MySQL database)
- Flask and mysql-connector-python
- Vscode

## Installation

1. **Start XAMPP** and make sure MySQL is running

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Setup the database**:
   ```
   python setup_database.py
   ```
   Or manually run `database_setup.sql` in phpMyAdmin

4. **Run the application**:
   ```
   python app.py
   ```

5. **Open in browser**: http://127.0.0.1:5000

## Default Login Credentials

**Admin Account**:
- Username: admin
- Password: admin123

**Test User Account**:
- Username: testuser  
- Password: user123

## Project Structure

```
flask_app1/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── database.py         # Database connection helper
├── models.py           # User model and database operations
├── email_helper.py     # Email/OTP helper functions
├── setup_database.py   # Database setup script
├── database_setup.sql  # SQL script for manual setup
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── images/
│       └── profile.png # Profile placeholder image
└── templates/
    ├── base.html           # Base template
    ├── index.html          # Homepage
    ├── login.html          # Login page
    ├── register.html       # Registration page
    ├── verify_otp.html     # OTP verification
    ├── user_dashboard.html # User dashboard
    ├── profile.html        # Profile page
    ├── admin_dashboard.html # Admin dashboard
    ├── admin_users.html    # User management
    ├── admin_add_user.html # Add user form
    ├── admin_edit_user.html # Edit user form
    └── 404.html            # Error page
```

## Email Configuration (Optional)

To enable OTP email sending, update `config.py`:

```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': 'your_email@gmail.com',
    'password': 'your_app_password' 
}
```

Note: For testing, OTP verification still works without email configuration.

## Created By

2nd Year Computer Science Student
December 2024

Game
