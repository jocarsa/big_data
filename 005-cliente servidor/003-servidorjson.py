from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '[1,2,3,4,5,6,7,8,9,10]'

if __name__ == '__main__':
    app.run(debug=True)
