from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/love')
def SWORD():
    return render_template('love.html')

if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host="0.0.0.0", port=8000)