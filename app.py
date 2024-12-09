from flask import Flask

# initialize the flask app
app = Flask(__name__)


# creating the homepage or index page
@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello Portfolio"


# main function
if __name__ == "__main__":
    app.run(debug=True)
