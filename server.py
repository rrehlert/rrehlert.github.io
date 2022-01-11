from os import write
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print (__name__)

def save_data(data):
    with open('database.txt', 'a') as file:
        file.write(f"{data['name']}, {data['email']}, {data['subject']}, {data['message']}\n")

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong try again'

# @app.route('/<parameter>')
# def about(parameter = None):
#     html = f'{parameter}.html'
#     return render_template(html)

