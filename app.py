from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/")
def greeting():
    name: str = request.args.get("name", "")
    message: str = request.args.get("message", "")
    return render_template("index.html", name=name, message=message )

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")