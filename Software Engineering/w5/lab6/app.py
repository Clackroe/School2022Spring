from flask import Flask, render_template, request

app = Flask(__name__)


global GLOBALS
GLOBALS = {
    'name': '',
    'age': '',
    'major': '',
    'credits': 0,
    'gpa': 0.0,
    'target_gpa': 0.0,
}


@app.get('/')
def index():
    return render_template('index.html')


# We use POST to send our previous data and GET to get the data from the form
@app.route('/task1', methods=['POST', 'GET'])
def task1():
    # Get the data from the form
    name = request.form['name']

    # TODO 1: Create a variable called `age` and assign the value of the age field from the form to it
    age = request.form['age'] 

    # TODO 2: Update the `GLOBALS` dictionary with the new values
    
    GLOBALS['name'] = name
    GLOBALS['age'] = age

    # Returns the data to the template
    return render_template('task1.html', name=name, age=age)


@app.route('/task2', methods=['POST', 'GET'])
def task2():
    # TODO 3: Get the user's major, credits, and gpa from the form
    major = request.form['major']
    creds = int(request.form['credits'])
    gpa = float(request.form['gpa'])

    # TODO 4: Update the `GLOBALS` dictionary with the new values
    
    GLOBALS['major'] = major
    GLOBALS['credits'] = creds
    GLOBALS['gpa'] = gpa

    # TODO 5: Return the data to the template
    return render_template('task2.html', major=major, credits=creds, gpa=gpa)


@app.route('/task3', methods=['POST', 'GET'])
def task3():
    # TODO 6: Retreive the target_gpa from the form, and update the `GLOBALS` dictionary
    target_gpa = float(request.form['target_gpa'])
    
    GLOBALS['target_gpa'] = target_gpa
    # TODO 7: Use the `credits_to_target` function to calculate the number of credits needed to reach the target GPA

    needed_credits = credits_to_target(current_gpa=GLOBALS['gpa'],target_gpa=GLOBALS['target_gpa'],current_credits= GLOBALS['credits'])

    # TODO 8: Return the data to the template
    return render_template('task3.html', target_gpa=target_gpa, credits_needed=needed_credits)


def credits_to_target(current_gpa: float, target_gpa: float, current_credits: int) -> int:
    """
    Calculates the number of credits needed to reach a target GPA

    args:
        - current_gpa: The student's current GPA
        - target_gpa: The student's target GPA
        - current_credits: The student's current number of credits

    returns:
        - The number of credits needed to reach the target GPA
    """
    quality_points_needed = (target_gpa * current_credits) -  (current_gpa * current_credits)
    credits_needed = quality_points_needed / 4

    return credits_needed


if __name__ == '__main__':
    app.run(debug=True)
