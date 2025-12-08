import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG

def generate_otp():
    """Generate a 6-digit OTP"""
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp_code):
    
    try:
      
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['email']
        msg['To'] = to_email
        msg['Subject'] = 'Your OTP Code for Registration'
        
        body = f"""
        Dear User,
        Your OTP code for registration is: <h3>{otp_code}</h3>
        
        This code will expire in 5 minutes.
        
        <p style="color:red;">If you didn't request this code, please ignore this email.</p>
        
        Best regards,
        {EMAIL_CONFIG['authorized_senders']}
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        # Connect and send
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        # For demo purposes, return True even if email fails
        # In production, you should handle this properly
        return False  # Change to False in production
