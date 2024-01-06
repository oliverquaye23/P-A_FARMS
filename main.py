from flask import Flask,render_template,request,redirect, url_for
import requests
app = Flask(__name__)

@app.route('/')
def news():
    return render_template('hompage.html')
    
@app.route('/contact', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Handle the form submission here
        
     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')