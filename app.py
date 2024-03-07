from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load the trained model and CountVectorizer
model = pickle.load(open("model.pkl", "rb"))
count_vect = pickle.load(open("count_vect.pkl", "rb"))


# Define a function to preprocess the URL
def preprocess_url(url):
    # Preprocess the URL (similar to training data preprocessing)
    url = re.sub(r"[^\w\s]", "", url)
    return url


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        url = request.form["url"]
        # Preprocess the URL
        url = preprocess_url(url)
        # Vectorize the URL using the same CountVectorizer
        url_vectorized = count_vect.transform([url])
        # Predict phishing or legitimate
        prediction = model.predict(url_vectorized)
        if prediction[0] == 1:
            result = "Phishing Website Detected"
        else:
            result = "Legitimate Website"
        return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)
