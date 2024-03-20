from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def greeting():
    name = request.args.get('name')
    message = request.args.get('message')
    return f"<h1>Hello {name}! {message}</h1>"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')