from flask import Flask,render_template,request,redirect, url_for
from newsapi import NewsApiClient
import requests
app = Flask(__name__)

# newsapi = NewsApiClient(api_key='6317386d1b9541aebcb2180a0c6fe67a')
# top_headlines = newsapi.get_top_headlines(category='business')
# @app.route('/')
# def homepage():
#     return render_template('hompage.html')

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