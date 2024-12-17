from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('.\database.txt', mode = "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"{email}, {subject}, {message} \n")

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='\n') as csvfile:
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)


@app.route("/<string:page_name>")
def show_dynamic_html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if(request.method == 'POST'):
        data =  request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        print ('something went wrong')
    
