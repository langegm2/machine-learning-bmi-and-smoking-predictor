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
model = pickle.load(open('./model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        #data = request.get_json(force=True)
        print(request.form['age'])
        data = float(request.form['age'])
        print("Data", model.predict([[data]]))
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([[data]])

        # Take the first value of prediction
        output = prediction[0]

        return render_template("results.html", output=output, age=data)

if __name__ == '__main__':
    app.run(debug=True)
