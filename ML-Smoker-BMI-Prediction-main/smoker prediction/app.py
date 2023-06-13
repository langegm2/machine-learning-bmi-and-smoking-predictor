# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('./smoker_model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        charges = float(request.form['charges'])
        sex_updated = float(request.form['sex_updated'])

        # Make prediction using model loaded from disk with the input data
        prediction = model.predict([[age, bmi, charges, sex_updated]])

        # Take the first value of the prediction
        if prediction[0] == 1:
            output = "We predict that you are a smoker."
        else:
            output = "We predict that you are not a smoker."

        return render_template("results.html", output=output, age=age, bmi=bmi, charges=charges, sex_updated=sex_updated)

@app.route("/data_overview")
def happiness():
    return render_template("data_overview.html")

if __name__ == '__main__':
    app.run(debug=True)