from flask import Flask, render_template, request, redirect, url_for, flash
import MySQLdb
from werkzeug.security import generate_password_hash
import random

app = Flask(__name__)
app.secret_key = 'flask-app'
 
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validate form data
        error = None
        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif '@' not in email:
            error = 'Invalid email address.'
        elif len(password) < 8:
            error = 'Password must be at least 8 characters long.'
        
        if error is None:
         try:
            print(f"Attempting to connect to database...")
            # Create database connection
            connection = MySQLdb.connect(
               host='localhost',
               port=3306,
               user='root',
               passwd='', # Leave blank or replace with your actual password
               db='app_database'
               )
            
            cursor = connection.cursor()
            print("Database connection successful!")
          
            # Add to user table
            user = email
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            
            cursor.execute("INSERT INTO tbl_user (username, password) VALUES (%s, %s)", (user, hashed_password))
            connection.commit()
            print("User added to database.")
            
            # Execute SELECT and fetch results
            cursor.execute(f"SELECT * FROM tbl_user WHERE username = '{user}'")
            data = cursor.fetchall()
            print(f"Query results: {data}")
                     
            # Terminate connection
            cursor.close()
            connection.close()
            print("Database connection closed.")
            
            flash('Account created successfully!', 'success')

         except Exception as e:
            print(f"Database error: {e}") 
            flash("An error occurred, please try again.", 'error')
         
         return redirect(url_for('signup'))            
        else:
            flash(error, 'error')
    
    return render_template('signup.html')
 
if __name__ == '__main__':
   app.run(debug=True)