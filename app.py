from flask import Flask
from flask import render_template, redirect, request, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process form data here (e.g., save to database or send email)
        return redirect(url_for('index'))
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)