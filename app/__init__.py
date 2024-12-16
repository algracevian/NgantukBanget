from flask import Flask
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Configure Amazon RDS MySQL connection
    app.config['MYSQL_HOST'] = 'aws.c9sg46gomcv9.ap-southeast-1.rds.amazonaws.com'  # Replace with your RDS endpoint
    app.config['MYSQL_USER'] = 'root'               # Replace with your RDS username
    app.config['MYSQL_PASSWORD'] = 'Babayaga123'           # Replace with your RDS password
    app.config['MYSQL_DB'] = 'ngantukbanget'                     # Your RDS database name
    app.config['MYSQL_PORT'] = 3306                              # Default MySQL port

    # Initialize MySQL
    mysql = MySQL(app)
    app.mysql = mysql  # Attach MySQL to the app instance

    from .routes import main
    app.register_blueprint(main)

    return app