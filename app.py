from flask import Flask,render_template

app=Flask("server")
@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True,port=9000)