from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Load the CountVectorizer
count_vect = pickle.load(open("count_vect.pkl", "rb"))


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    prediction = model.prdict()
    return render_template(
        "index.html", prediction_text="this website is".format(prediction)
    )


if __name__ == "__main__":
    app.run(debug=True)
