# setup_database.py - Run this to create the database tables
import mysql.connector
from config import DB_CONFIG
import hashlib


def setup_database():
    
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_flask_db_web")
        print("Database created successfully!")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
        return

    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return
    
    # Create tables
    tables = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            firstname VARCHAR(50) NOT NULL,
            middlename VARCHAR(50),
            lastname VARCHAR(50) NOT NULL,
            birthday DATE NOT NULL,
            contact VARCHAR(20) NOT NULL,
            role ENUM('user', 'admin') DEFAULT 'user',
            is_active TINYINT(1) DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS otp_codes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            otp_code VARCHAR(10) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS email_log (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            sent_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS pending_registrations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) NOT NULL,
            firstname VARCHAR(50) NOT NULL,
            middlename VARCHAR(50),
            lastname VARCHAR(50) NOT NULL,
            birthday DATE NOT NULL,
            contact VARCHAR(20) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS site_content (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content_key VARCHAR(50) UNIQUE NOT NULL,
            content_value TEXT,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
    ]
    
    for table in tables:
        cursor.execute(table)
    print("Tables created successfully!")
    
    # Create admin user
    admin_password = hash_password(ACCOUNTS["admin_password"])
    try:
        cursor.execute("""
            INSERT INTO users (username, password, email, firstname, middlename, lastname, birthday, contact, role, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (ACCOUNTS["admin"], admin_password, 'admin@example.com', 'Admin', '', 'User', '2000-01-01', '09123456789', 'admin', 1))
        print("Admin user created! Username: admin, Password: admin123")
    except mysql.connector.IntegrityError:
        print("Admin user already exists!")
    
    user_password = hash_password(ACCOUNTS["testuser_password"])
    try:
        cursor.execute("""
            INSERT INTO users (username, password, email, firstname, middlename, lastname, birthday, contact, role, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (ACCOUNTS["testuser"], user_password, 'user@example.com', 'Juan', 'Santos', 'Dela Cruz', '2003-05-15', '09987654321', 'user', 1))
        print("Test user created! Username: testuser, Password: user123")
    except mysql.connector.IntegrityError:
        print("Test user already exists!")
    
    # Insert default site content
    site_content = [
        ('site_title', 'Welcome to my website!'),
        ('tagline', 'None'),
        ('about_me', 'None'),
        ('dream_job_title', 'None'),
        ('dream_job_text', 'None')
    ]
    
    for key, value in site_content:
        try:
            cursor.execute("""
                INSERT INTO site_content (content_key, content_value)
                VALUES (%s, %s)
            """, (key, value))
        except mysql.connector.IntegrityError:
            pass
    print("Default site content added!")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print("\n=== Database setup complete! ===")
    print("You can now run the app with: python app.py")
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

ACCOUNTS = {
    "admin": "admin",
    "testuser": "testuser",
    "admin_password": "admin123",
    "testuser_password": "user123"
}

if __name__ == '__main__':
    print("Setting up database...")
    setup_database()
