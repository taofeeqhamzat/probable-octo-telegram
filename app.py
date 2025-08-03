from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
app.secret_key = 'flask-app'
 
@app.route('/')
def home():
   return render_template('signup.html')

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
            # Here you would typically save the user to a database
            # For now, we'll just redirect to home with a success message
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            flash('Account created successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash(error, 'error')
    
    return render_template('signup.html')
 
if __name__ == '__main__':
   app.run(debug=True)