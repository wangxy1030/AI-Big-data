from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "PUT"])
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run()
