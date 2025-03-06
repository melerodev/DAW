from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cuadrado', methods=['GET'])
def square():
    number = request.args.get('number', default=1, type=int)
    result = number ** 2
    return render_template('square.html', number=number, result=result)

if __name__ == '__main__':
    app.run(debug=True)
