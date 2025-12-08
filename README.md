# Flask Authentication System

A modern, minimalist web application built with Python Flask featuring user authentication, email OTP verification, and a clean admin dashboard. Perfect for learning web development basics!

---

## 🎯 What This Project Does

This is a **simplified Flask web application** that demonstrates core web development concepts:

- **User Registration & Login** with secure password hashing
- **Email OTP Verification** for account security
- **Admin Dashboard** for administrators
- **Responsive Design** that works on phones and computers
- **Session Management** to keep users logged in
- **MySQL Database** for storing user data

**Perfect for:** College students learning web development, Flask beginners, or anyone wanting to understand authentication systems.

---

## ✨ Features

- 🔐 **Secure Authentication** - Login/logout with session management
- 📧 **Email OTP Verification** - Registration requires email verification
- 👨‍💼 **Admin Dashboard** - Simple admin interface
- 📱 **Mobile-Friendly** - Responsive design with hamburger menu
- 🎨 **Modern UI** - Clean magenta & black theme
- 🛡️ **Security Features** - SHA256 password hashing, session protection

---

## 🛠️ What You'll Need

### Software Requirements
- **Python 3.8 or higher** (Download from [python.org](https://www.python.org/downloads/))
- **XAMPP** (for MySQL database - Download from [apachefriends.org](https://www.apachefriends.org/))
- **Web Browser** (Chrome, Firefox, Edge, etc.)
- **Code Editor** (VS Code recommended - Download from [code.visualstudio.com](https://code.visualstudio.com/))

### Hardware Requirements
- **RAM:** At least 4GB (8GB recommended)
- **Storage:** 500MB free space
- **Internet:** Required for downloading dependencies

---

## 📚 Step-by-Step Setup Guide

### Step 1: Install XAMPP (Database Server)

XAMPP gives us MySQL database and Apache server. Follow these steps carefully:

1. **Download XAMPP:**
   - Go to https://www.apachefriends.org/
   - Download the latest version for Windows
   - Choose the installer (.exe file)

2. **Install XAMPP:**
   - Run the installer as Administrator
   - Choose default installation location (usually `C:\xampp\`)
   - Select components: Apache, MySQL, PHP (default selections are fine)
   - Complete the installation

3. **Start XAMPP:**
   - Open XAMPP Control Panel (search for "XAMPP" in Start menu)
   - Click "Start" next to **Apache**
   - Click "Start" next to **MySQL**
   - You should see green checkmarks ✅

   ![XAMPP Control Panel](https://i.imgur.com/xampp-control.png)

**Troubleshooting XAMPP:**
- If ports are blocked, click "Config" → "Apache (httpd.conf)" and change port from 80 to 8080
- If MySQL won't start, end task "mysqld.exe" in Task Manager and try again

---

### Step 2: Install Python

1. **Download Python:**
   - Go to https://www.python.org/downloads/
   - Download Python 3.8 or higher (3.11 recommended)
   - Choose the Windows installer (64-bit)

2. **Install Python:**
   - Run the installer
   - ✅ **Important:** Check "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation:**
   - Open Command Prompt (search "cmd" in Start menu)
   - Type: `python --version`
   - You should see: `Python 3.x.x`
   - Type: `pip --version`
   - You should see pip version

---

### Step 3: Download the Project

1. **Option A - Download ZIP:**
   - Go to https://github.com/matrix505/flask_WEB_SYSTEM_client1
   - Click the green "Code" button
   - Choose "Download ZIP"
   - Extract the ZIP file to your desired location

2. **Option B - Git Clone (Recommended for developers):**
   - Open Command Prompt
   - Navigate to where you want the project: `cd Desktop`
   - Run: `git clone https://github.com/matrix505/flask_WEB_SYSTEM_client1.git`
   - The project will be in `flask_WEB_SYSTEM_client1` folder

3. **Open in VS Code:**
   - Open VS Code
   - File → Open Folder
   - Select the project folder (`flask_WEB_SYSTEM_client1`)

---

### Step 4: Install Python Libraries

1. **Open Terminal in VS Code:**
   - In VS Code: View → Terminal
   - Or: Ctrl + ` (backtick)

2. **Navigate to Project Folder:**
   ```bash
   cd flask_WEB_SYSTEM_client1
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - **Flask** - Web framework
   - **mysql-connector-python** - Database connection
   - **python-dotenv** - Environment variables
   - Other helper libraries

4. **Verify Installation:**
   ```bash
   python -c "import flask; print('Flask installed successfully!')"
   ```

---

### Step 5: Set Up the Database

1. **Make Sure XAMPP is Running:**
   - Apache ✅ and MySQL ✅ should be green in XAMPP Control Panel

2. **Run Database Setup:**
   ```bash
   python setup_database.py
   ```

   This script will:
   - Create a database called `flask_blog_db`
   - Create tables for users, OTP codes, and site content
   - Add default admin and test user accounts
   - Add sample content

3. **Check for Success:**
   - You should see messages like:
     - "Database created successfully!"
     - "Tables created successfully!"
     - "Default users added!"

**If you get database errors:**
- Make sure XAMPP MySQL is running
- Check if port 3306 is available (XAMPP default)
- Try restarting XAMPP services

---

### Step 6: Configure Email (Optional but Recommended)

For email OTP verification, you need to set up Gmail:

1. **Enable 2-Factor Authentication on Gmail:**
   - Go to https://myaccount.google.com/security
   - Turn on 2-Step Verification

2. **Generate App Password:**
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password

3. **Update Configuration:**
   - Open `config.py` in VS Code
   - Find the `EMAIL_CONFIG` section
   - Replace with your Gmail and app password:
   ```python
   EMAIL_CONFIG = {
       'smtp_server': 'smtp.gmail.com',
       'smtp_port': 587,
       'email': 'your_email@gmail.com',
       'password': 'your_app_password'  # The 16-character code
   }
   ```

**Note:** If you skip this, OTP codes will show in the terminal instead of being emailed.

---

### Step 7: Run the Application

1. **Start the Flask App:**
   ```bash
   python app.py
   ```

2. **Check the Output:**
   - You should see: `* Running on http://127.0.0.1:5000/`
   - Don't close this terminal window!

3. **Open in Browser:**
   - Go to: http://127.0.0.1:5000
   - You should see the homepage!

---

### Step 8: Test the Application

**Default Login Accounts:**

| Role  | Username  | Password  | What You Can Do |
|-------|-----------|-----------|-----------------|
| Admin | `admin`   | `admin123`| Access admin dashboard |
| User  | `testuser`| `user123` | Basic user access |

**Testing Steps:**
1. **Visit Homepage** - See the welcome page
2. **Try Registration** - Click "Register", fill form, check email/terminal for OTP
3. **Login** - Use admin or testuser credentials
4. **Admin Dashboard** - Login as admin to see the dashboard
5. **Logout** - Test the logout functionality

---

## 📁 Project Structure

```
flask_WEB_SYSTEM_client1/
├── app.py                 # 🚀 Main Flask application with routes
├── config.py              # ⚙️ Database and email configuration
├── database.py            # 💾 Database connection helper
├── models.py              # 📊 Database operations (CRUD functions)
├── email_helper.py        # 📧 Email and OTP functions
├── setup_database.py      # 🛠️ Database setup script
├── requirements.txt       # 📦 Python dependencies list
├── README.md              # 📖 This documentation
│
├── static/                # 🎨 Static files (CSS, images)
│   ├── css/
│   │   └── style.css      # 🎨 Main stylesheet
│   └── images/            # 🖼️ Image files
│
└── templates/             # 📄 HTML templates
    ├── base.html          # 🏠 Base template (navigation, footer)
    ├── index.html         # 🏡 Homepage
    ├── login.html         # 🔑 Login page
    ├── register.html      # 📝 Registration page
    ├── verify_otp.html    # ✅ OTP verification page
    └── admin_dashboard.html # 👨‍💼 Admin dashboard
```

---

## ⚙️ Configuration Files

### Database Settings (`config.py`)
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',           # Empty for XAMPP default
    'database': 'flask_blog_db'
}
```

### Email Settings (`config.py`)
```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': 'your_email@gmail.com',
    'password': 'your_app_password'
}
```

---

## 🐛 Troubleshooting Guide

| Problem | Solution |
|---------|----------|
| **"Python is not recognized"** | Reinstall Python and check "Add to PATH" |
| **"pip command not found"** | Use `python -m pip` instead of `pip` |
| **MySQL connection error** | Make sure XAMPP MySQL is running (green) |
| **Port 5000 already in use** | Close other Flask apps or change port in `app.py` |
| **Module not found errors** | Run `pip install -r requirements.txt` again |
| **Database setup fails** | Check XAMPP MySQL is running, try restarting services |
| **Emails not sending** | Check Gmail settings, use app password, verify 2FA |
| **Page not loading** | Make sure Flask app is running (don't close terminal) |

**Common XAMPP Issues:**
- **Port conflicts:** Change Apache port to 8080 in httpd.conf
- **MySQL won't start:** End mysqld.exe in Task Manager, try again
- **Access denied:** Run XAMPP as Administrator

---

## 🎓 Learning Outcomes

After setting up this project, you'll understand:

- **Web Frameworks** - How Flask works
- **Databases** - MySQL setup and queries
- **Authentication** - Login systems and security
- **Email Integration** - SMTP and OTP systems
- **Session Management** - Keeping users logged in
- **HTML Templates** - Dynamic web pages with Jinja2
- **CSS Styling** - Responsive design
- **Deployment** - Running web apps locally

---

## 🛠️ Technologies Used

- **Backend:** Python Flask
- **Database:** MySQL (via XAMPP)
- **Frontend:** HTML5, CSS3, Jinja2 Templates
- **Icons:** Font Awesome 6
- **Security:** SHA256 password hashing, session management
- **Email:** SMTP protocol for OTP

---

## 📞 Support & Learning Resources

**Getting Help:**
- Check the Troubleshooting section above
- Google error messages (most issues are common)
- Ask questions on Stack Overflow

**Learning Resources:**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql_getstarted.asp)
- [HTML/CSS Basics](https://www.w3schools.com/html/)
- [FreeCodeCamp Web Development](https://www.freecodecamp.org/)

---

## 👨‍💻 About the Creator

Created by a 2nd Year Computer Science Student  
December 2025

**Happy Coding! 🎉**
