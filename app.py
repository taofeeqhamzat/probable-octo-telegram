from flask import Flask, render_template
import MySQLdb
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/')
def home():
   # TODO: Remove example test db connection and queries below
   try:
      print(f"Attempting to connect to database...")
      
      # Create database connection
      connection = MySQLdb.connect(
          host='localhost',
          user='root',
          passwd='', # Leave blank or replace with your actual password
          db='app_database'
      )
      
      cursor = connection.cursor()
      
      # # Add test row to 'user' table
      user = 'test_user_' + str(random.randint(1, 5000*2))
      password = 'strong_password'
      hashed_password = generate_password_hash(password)
      cursor.execute("INSERT INTO tbl_user (username, password) VALUES (%s, %s)", (user, hashed_password))
      connection.commit()
      
      # Execute SELECT and fetch results
      cursor.execute(f"SELECT * FROM tbl_user WHERE username = '{user}'")
      data = cursor.fetchall()
      print(f"Query results: {data}")
      print("Database connection successful!")
      
      # Terminate connection
      cursor.close()
      connection.close()
   except Exception as e:
      print(f"Database error: {e}") 
      
   return render_template('index.html')
 
if __name__ == '__main__':
   app.run(debug=True)