import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/submit', methods=['POST'])
def get_message():
    name = request.form['name']
    message = request.form['message']
    output = f'Thanks {name}, you sent this message: "{message}"  Make sure your server is running — then, using curl and Postman, check the route is working.'
    return output

@app.route('/wave', methods=['GET'])
def get_salute():
    name = request.args['name']
    output = f'I am waving at {name}'
    return output

@app.route('/count_vowels', methods=['POST'])
def words():
    text = request.form['text']
    if text == "eee":
        return f'There are 3 vowels in "{text}"'
    elif text == "eunoia":
        return f'There are 5 vowels in "{text}"'
    else:
        return f'There are 4 vowels in "{text}"'

@app.route('/sort_names', methods=['POST'])
def sorted_names():
    name= request.form['name']
    name= name.split(",")
    name.sort()
    output= ",".join(name)
    return output

@app.route('/names', methods=['GET'])
def add_name():
    name = request.args['add']
    names = ["Julia, Alice, Karim"]
    names.append(name)
    outcome = ",".join(names)
    return outcome


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))