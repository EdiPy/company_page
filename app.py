from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mail import Mail, Message
from forms import ContactForm
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv('SECRET_KEY')
# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Get email from .env
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Get password from .env
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(subject=f"Kontakt forma od {form.name.data}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['pythontestniracun@gmail.com'],
                      body=f"Ime: {form.name.data}\nEmail: {form.email.data}\nPoruka:\n{form.message.data}")
        mail.send(msg)
        flash("Poruka je uspješno poslana!")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)