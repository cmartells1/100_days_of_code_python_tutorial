from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.date.today().year
    return render_template('index.html', num=random_number, curr_year=current_year)

@app.route('/guess/<name>')
def age_gender(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data['age']

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data['gender']

    return render_template('age_gender.html', age=age, name=name, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)