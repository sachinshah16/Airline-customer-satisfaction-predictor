
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open(r"C:\Users\Sachi\Downloads\ML-MODEL-DEPLOYMENT-USING-FLASK-main\ML-MODEL-DEPLOYMENT-USING-FLASK-main\airline.pkl", "rb"))


@flask_app.route("/")
def Home():
    return render_template("index2.html")


@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = pd.DataFrame(float_features).T
    features.columns = 'Gender', 'Customer Type', 'Type of Travel', 'Class', 'Seat comfort','Food and drink', 'Inflight wifi service', 'Inflight entertainment','Online support', 'Ease of Online booking', 'On-board service','Leg room service', 'Baggage handling', 'Checkin service','Cleanliness', 'Online boarding', 'Departure Delay in Minutes','Arrival Delay in Minutes'

    prediction = model.predict(features)
    if prediction == 1:
        pred = "satisfied"
    else:
        pred = "disatified"
    return render_template("index2.html", prediction_text = "Costumer is {}".format(pred))


if __name__ == "__main__":
    flask_app.run(debug=False)