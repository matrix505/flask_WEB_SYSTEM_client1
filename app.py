# app.py - Main Flask Application
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import models
import os
import time
from email_helper import generate_otp, send_otp_email
from config import SECRET_KEY,ALLOWED_EXTENSIONS
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.secret_key = SECRET_KEY



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def login_required(f):
    """Decorator to check if user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('loggedIn'):
            flash('Please login first!', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to check if user is admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('loggedIn'):
            flash('Please login first!', 'error')
            return redirect(url_for('login'))
        if session.get('role') != 'admin':
            flash('Admin access required!', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Homepage"""
    user = None
    if session.get('loggedIn'):
        user = models.get_user_by_id(session.get('user_id'))
    content = models.get_site_content()
    admin = models.get_admin_user()
    return render_template('index.html', user=user, content=content, admin=admin)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if session.get('loggedIn'):
        if session.get('role') == 'admin':
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate input
        if not username or not password:
            flash('Please fill all fields!', 'error')
            return render_template('login.html')
        
        # Verify credentials
        user = models.verify_login(username, password)
        
        if user:
            # Set session variables
            session['loggedIn'] = True
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['firstname'] = user['firstname']
            session['role'] = user['role']
            
            flash(f'Welcome back, {user["firstname"]}!', 'success')
            
            # Redirect based on role
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('index'))
        else:
            flash('Invalid username or password, or account is deactivated!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash('You have been logged out!', 'success')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    if session.get('loggedIn'):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        middlename = request.form.get('middlename', '')
        lastname = request.form.get('lastname')
        birthday = request.form.get('birthday')
        contact = request.form.get('contact')
        
        # Validation
        errors = []
        
        if not all([username, password, email, firstname, lastname, birthday, contact]):
            errors.append('Please fill all required fields!')
        
        if password != confirm_password:
            errors.append('Passwords do not match!')
        
        if len(password) < 6:
            errors.append('Password must be at least 6 characters!')
        
        if models.get_user_by_username(username):
            errors.append('Username already exists!')
        
        if models.get_user_by_email(email):
            errors.append('Email already registered!')
        
        # Check for spam
        if models.check_email_spam(email):
            errors.append('Too many OTP requests. Please try again later.')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html')
        
        # Save pending registration
        models.save_pending_registration(username, password, email, firstname, 
                                         middlename, lastname, birthday, contact)
        
        # Generate and save OTP
        otp = generate_otp()
        models.save_otp(email, otp)
        models.log_email_sent(email)
        
        # Send OTP email
        send_otp_email(email, otp)
        
        # Store email in session for verification
        session['pending_email'] = email
        
        flash('OTP has been sent to your email!', 'success')
        return redirect(url_for('verify_otp'))
    
    return render_template('register.html')

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    """OTP verification page"""
    if not session.get('pending_email'):
        flash('Please register first!', 'error')
        return redirect(url_for('register'))
    
    if request.method == 'POST':
        otp_code = request.form.get('otp')
        email = session.get('pending_email')
        
        if models.verify_otp(email, otp_code):
            # Complete registration
            models.complete_registration(email)
            session.pop('pending_email', None)
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid or expired OTP!', 'error')
    
    return render_template('verify_otp.html', email=session.get('pending_email'))

@app.route('/resend-otp')
def resend_otp():
    """Resend OTP"""
    email = session.get('pending_email')
    if not email:
        flash('Please register first!', 'error')
        return redirect(url_for('register'))
    
    # Check spam
    if models.check_email_spam(email):
        flash('Too many OTP requests. Please try again later.', 'error')
        return redirect(url_for('verify_otp'))
    
    # Generate new OTP
    otp = generate_otp()
    models.save_otp(email, otp)
    models.log_email_sent(email)
    send_otp_email(email, otp)
    
    flash('New OTP has been sent!', 'success')
    return redirect(url_for('verify_otp'))


@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    """Admin dashboard"""
    return render_template('admin_dashboard.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
