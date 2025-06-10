from flask import Flask,render_template

# initialize the flask app
app = Flask(__name__)


# creating the homepage or index page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
