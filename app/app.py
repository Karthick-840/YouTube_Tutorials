from flask import Flask, render_template, request, redirect, url_for
#from ics import Calendar, Event
from datetime import datetime

app = Flask(__name__)

def function1(url):
    # Implement your logic for function 1 here
    # Example: Fetch data from the URL and process it
    # Return data for rendering the table
    return [
        {'column1': 'Data1', 'column2': 'Data2'},
        {'column1': 'Data3', 'column2': 'Data4'}
    ]

def function2(data):
    # Implement your logic for function 2 here
    # Example: Use data to create events for the calendar
    cal = Calendar()
    for entry in data:
        event = Event()
        event.name = entry['column1']
        event.begin = datetime.now()
        cal.events.add(event)
    
    # Save the calendar to a file
    cal_file_path = 'output.ics'
    with open(cal_file_path, 'w') as cal_file:
        cal_file.writelines(cal)

    return cal_file_path

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/process_url', methods=['POST'])
def process_url():
    url = request.form['url']
    data = function1(url)
    return render_template('table.html', data=data)

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get user-filled columns from the form
    user_columns = {
        'column1': request.form['column1'],
        'column2': request.form['column2']
    }
    
    # Use the user-filled columns to run function 2
    cal_file_path = function2(user_columns)

    return render_template('verification.html', cal_file_path=cal_file_path)
## use ideas to change home screen
# Put do something great.

if __name__ == "__main__":
    app.run(debug=True)
    