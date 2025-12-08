import os

SECRET_KEY = 'my_secret_12345'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'), 
    'database': os.getenv('DB_NAME', 'my_flask_db_web')
}


EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': os.getenv('EMAIL_USER'),
    'password': os.getenv('EMAIL_PASSWORD')
}
OTP_EXPIRY_MINUTES = 5