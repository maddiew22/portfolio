from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/experience.html')
def experience():
    return render_template("experience.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)