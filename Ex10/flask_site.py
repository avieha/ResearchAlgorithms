from flask import Flask, render_template, request
from spread_sheet import read_write_to_sheet

app = Flask(__name__)


@app.route('/')
def action():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def get_data():
    url = request.form['fname']
    read_write_to_sheet(url)
    return 'Done'


if __name__ == '__main__':
    app.run()
