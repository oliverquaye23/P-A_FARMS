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
    # response = requests.get('https://newsapi.org/v2/top-headlines?q=bitcoin&apiKey=6317386d1b9541aebcb2180a0c6fe67a')
    # if response.status_code == 200:
    #     # Parse the JSON response
    #     news_data = response.json()

    #     # Extract the articles from the response
    #     articles = news_data.get('articles', [])

        return render_template('hompage.html')
    # else:
    #     return 'Error fetching news'

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')