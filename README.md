# Flask Web Application

A comprehensive web application built with Flask, featuring user authentication, admin dashboard, interactive games, and responsive design.

## Description

This Flask-based web application provides a complete user management system with authentication, profile management, and an admin panel. It includes several interactive games built with Tkinter and features a responsive design that works on both desktop and mobile devices.

## Features

### User Management
- User registration with email verification
- OTP (One-Time Password) verification system
- Secure login/logout functionality
- User profile management
- Password hashing with Werkzeug

### Admin Panel
- Admin dashboard with user management
- User CRUD operations (Create, Read, Update, Delete)
- Role-based access control (Admin/User)
- Homepage content management
- User statistics and overview

### Games
- **Snake Game**: Classic snake game with score tracking
- **Guess Game**: Number guessing game with attempts counter
- **Memory Cards**: Card matching memory game
- **Tetris Blocks**: Falling blocks puzzle game
- **Space Shooter**: Alien defense game
- **Color Memory**: Color sequence memory game

### Additional Features
- Responsive navbar with hamburger menu for mobile
- Flash message system for user feedback
- Email notifications (SMTP)
- Discord webhook integration
- SQLite database for data persistence
- Session management
- File upload for profile images

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd flask_app1
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   python setup_database.py
   ```

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
SECRET_KEY=your-secret-key-here
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
DISCORD_WEBHOOK_URL=your-discord-webhook-url
```

### Application Configuration

The application uses `config.py` for configuration settings. Key configurations include:

- Database URI
- Upload folder paths
- Session settings
- Email settings

## Database Setup

The application uses SQLite as the database. The database schema includes:

- **users** table: Stores user information (id, username, email, password, etc.)
- **content** table: Stores homepage content

Run `setup_database.py` to initialize the database and create tables.

## Running the Application

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your browser and go to `http://localhost:5000`

## Usage

### User Registration and Login
1. Visit the homepage
2. Click "Register" to create a new account
3. Verify your email with the OTP sent
4. Login with your credentials

### Admin Access
- Admin accounts can access the admin dashboard at `/admin_dashboard`
- Manage users, edit homepage content, and view statistics

### Playing Games
- Navigate to the Games page
- Click on any game to launch it
- Games run as separate Tkinter windows

## API Endpoints

The application includes several routes:

### Public Routes
- `/` - Homepage
- `/login` - User login
- `/register` - User registration
- `/verify_otp` - OTP verification
- `/resend_otp` - Resend OTP

### Protected Routes (User)
- `/user_dashboard` - User dashboard
- `/profile` - User profile management
- `/games` - Games page
- `/logout` - User logout

### Protected Routes (Admin)
- `/admin_dashboard` - Admin dashboard
- `/admin_users` - User management
- `/admin_add_user` - Add new user
- `/admin_edit_user/<user_id>` - Edit user
- `/admin_content` - Edit homepage content
- `/admin_upload_profile` - Upload profile image

### Game Launch Routes
- `/launch_game/<game_name>` - Launch specific game (POST)

## Technologies Used

### Backend
- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **Flask-Mail** - Email functionality
- **Werkzeug** - Password hashing
- **Requests** - HTTP requests for Discord webhooks

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with CSS Variables for theming
- **JavaScript** - Client-side interactions
- **Font Awesome** - Icons

### Games
- **Tkinter** - GUI framework for games
- **Pygame** - Game development library (for some games)

### Database
- **SQLite** - Database engine

### Other
- **python-dotenv** - Environment variable management
- **Pillow** - Image processing

## Project Structure

```
flask_app1/
├── app.py                 # Main Flask application
├── config.py             # Application configuration
├── database.py           # Database models and functions
├── discord_webhook.py    # Discord integration
├── email_smtp.py         # Email functionality
├── models.py             # SQLAlchemy models
├── setup_database.py     # Database initialization
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── pygame/               # Game files
│   ├── guess_game.py
│   ├── memory_cards_game.py
│   ├── snake_game.py
│   ├── space_shooter_game.py
│   └── tetris_blocks_game.py
├── static/               # Static files
│   ├── css/
│   │   └── style.css
│   └── images/
├── templates/            # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── verify_otp.html
│   ├── user_dashboard.html
│   ├── profile.html
│   ├── games.html
│   ├── admin_dashboard.html
│   ├── admin_users.html
│   ├── admin_add_user.html
│   ├── admin_edit_user.html
│   ├── admin_content.html
│   └── 404.html
└── __pycache__/          # Python cache files
```

## Security Features

- Password hashing using Werkzeug
- Session management with secure cookies
- CSRF protection
- Input validation
- Role-based access control
- Secure file upload handling

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

To run tests (if implemented):

```bash
python -m pytest
```

## Deployment

### Local Deployment
Follow the installation and running instructions above.

### Production Deployment
For production deployment, consider using:
- Gunicorn as WSGI server
- Nginx as reverse proxy
- Environment-specific configuration
- Database migration tools

## Troubleshooting

### Common Issues
1. **Database connection errors**: Ensure `setup_database.py` has been run
2. **Email not sending**: Check SMTP credentials in `.env`
3. **Games not launching**: Ensure Tkinter is installed and display is available
4. **Static files not loading**: Check Flask static folder configuration

### Debug Mode
Run with debug mode for development:
```bash
FLASK_ENV=development python app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact the development team.

## Changelog

### Version 1.0.0
- Initial release with core features
- User authentication system
- Admin panel
- Interactive games
- Responsive design

## Future Enhancements

- [ ] User avatar upload
- [ ] Password reset functionality
- [ ] Game leaderboards
- [ ] Multi-language support
- [ ] API documentation with Swagger
- [ ] Unit and integration tests
- [ ] Docker containerization