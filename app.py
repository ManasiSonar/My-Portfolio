from email import message
from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
   return render_template("index.html")

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
   if request.method == "POST":
      try:
         data=request.form.to_dict()
         write_data_csv(data)
         message = "Form submitted, I will get in touch to you shortly!!!"
         return render_template("thankyou.html", message = message)
      except:
         message = "Did not save Data to Database."
         return render_template("thankyou.html", message = message)
   else:
      message = "Form not submitted. Please try again!"
      return render_template("thankyou.html", message = message)

def write_data_csv(data):
   email = data['email']
   subject = data['subject']
   message = data['message']
   with open('db.csv', 'a', newline='') as csvfile:
      db_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
      db_writer.writerow([email, subject, message])

@app.route('/components')
def components():
   return render_template("components.html")


if __name__ == '__main__':
   app.run(debug = True)  
   