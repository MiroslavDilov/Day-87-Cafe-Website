from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

# Reading DB
con = sqlite3.connect("cafes.db")
cur = con.cursor()
cur.execute('SELECT * FROM cafe')
rows = cur.fetchall()

@app.route("/")
def index():
    return render_template('index.html', coffees=rows)


if __name__ == '__main__':
    app.run(debug=True)