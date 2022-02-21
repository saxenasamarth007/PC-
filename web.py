from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/<string:html_page>')
def other_pages(html_page):
    return render_template(html_page)