from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/experience.html')
def experience():
    return render_template("experience.html")

@app.route('/projects.html')
def projects():
    return render_template("projects.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/christie.html')
def christie():
    return render_template("christie.html")

@app.route('/ewb.html')
def ewb():
    return render_template("ewb.html")

@app.route('/biotron.html')
def biotron():
    return render_template("biotron.html")

@app.route('/deep.html')
def deep():
    return render_template("deep.html")

@app.route('/uway.html')
def uway():
    return render_template("uway.html")

@app.route('/gaa.html')
def gaa():
    return render_template("gaa.html")

@app.route('/tutoring.html')
def tutoring():
    return render_template("tutoring.html")

@app.route('/tns.html')
def tns():
    return render_template("tns.html")

if __name__ == '__main__':
    app.run(debug=True)