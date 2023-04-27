from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def teste():
    return render_template("oi.html")

app.run(host='0.0.0.0', port=8080, debug=True)