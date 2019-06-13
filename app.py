from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',method=['POST'])
def hello():
    return render_template('base.html')
    regno=request.form['regno']

@app.route('/about')
def info():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
