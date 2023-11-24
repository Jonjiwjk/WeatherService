from flask import Flask, render_template, request
import requests

app = Flask(__name__)
lista = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        lista.append(location)
        print(lista)
        api_key = 'e6lRhTP6eIToGV8H7gLYlrzR5apgxQo6'  # Replace with your actual API key
        url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}'
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        # Process the data and display it on the webpage
        return render_template('index.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
