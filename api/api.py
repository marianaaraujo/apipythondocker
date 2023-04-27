from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def teste():
    return render_template("oi.html")

app.run(host='localhost', port=5000, debug=True)