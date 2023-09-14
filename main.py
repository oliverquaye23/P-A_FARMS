from flask import Flask,render_template,request,redirect, url_for
import requests
app = Flask(__name__)

@app.route('/get_news',methods = ['GET'])
def get_news():

    api_url = 'https://newsapi.org/v2/top-headlines'
    api_key = "6317386d1b9541aebcb2180a0c6fe67a"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(api_url,headers=headers)

    if response.status_code == 200:
        # The request was successful. You can access the API response data using response.json()
        data = response.json()
        print(data)
    else:
        # The request failed. Handle the error appropriately.
        print(f"Request failed with status code {response.status_code}")


@app.route('/')
def homepage():
    return render_template('hompage.html')


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')