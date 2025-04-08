from flask import render_template
from app import create_app

app = create_app()


@app.route('/')
def start():
    return render_template("index.html")


@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/case.html')
def case():
    return render_template("case.html")


@app.route('/diagnosis.html')
def diagnosis():
    return render_template("diagnosis.html")


@app.route('/login.html')
def login():
    return render_template("login.html")


@app.route('/diagnosis_result.html')
def diagnosis_result():
    return render_template("diagnosis_result.html")


@app.route('/news.html')
def news():
    return render_template("news.html")


@app.route('/newsDetail.html')
def newsDetail():
    return render_template("newsDetail.html")


@app.route('/support.html')
def support():
    return render_template("support.html")


if __name__ == '__main__':
    app.run(debug=True)
