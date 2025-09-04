from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def log():
    return render_template('index.html')


@app.route('/log', methods=['POST', 'GET'])
def success_page():
    email = request.form['email']
    return f"<h1>Success<br>Email:{email}</h1>" \
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWM4YXVmaWRkMGczNm1ueXN0aTA4Y2dheHd3djF0eGxjdDhoZml6dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xThtar0e9kO3WkwQ1O/giphy.gif'>"


app.run(debug=True)
