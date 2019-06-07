from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/about')
def info():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
