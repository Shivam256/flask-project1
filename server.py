from crypt import methods
from urllib import request
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:pagename>")
def html_page(pagename  = None):
    return render_template(pagename)


def write_to_file(data):
    with open('database.txt','a') as database:
        email = data['email']
        subject= data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv','a',  newline='') as database2:
        email = data['email']
        subject= data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter = ",", quotechar = "|", quoting = csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form",methods=['POST','GET'])
def submitForm():
    if request.method == 'POST':
       try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'something went wrong! Didn\'t save to database'
    else:
        return 'something went wrong!'



