import os


SECRET_KEY = 'my_secret_key_12345'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # 
    'database': 'flask_blog_db'
}

# Email Configuration (use your own email settings)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': '',
    'password': ''
}

# OTP Settings
OTP_EXPIRY_MINUTES = 5
