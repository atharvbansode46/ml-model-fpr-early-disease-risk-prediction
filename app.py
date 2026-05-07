from flask import Flask, request, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("disease_model.pkl", "rb"))

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Disease Risk Prediction</title>

    <style>
        body{
            font-family: Arial;
            background: linear-gradient(to right,#74ebd5,#ACB6E5);
            padding:40px;
        }

        .container{
            background:white;
            width:450px;
            margin:auto;
            padding:30px;
            border-radius:20px;
            box-shadow:0px 0px 20px rgba(0,0,0,0.2);
        }

        h1{
            text-align:center;
            color:#333;
        }

        input{
            width:100%;
            padding:12px;
            margin:10px 0;
            border-radius:10px;
            border:1px solid #ccc;
        }

        button{
            width:100%;
            padding:12px;
            background:#4CAF50;
            color:white;
            border:none;
            border-radius:10px;
            font-size:18px;
            cursor:pointer;
        }

        button:hover{
            background:#45a049;
        }

        .result{
            margin-top:20px;
            padding:15px;
            border-radius:10px;
            background:#f2f2f2;
        }
    </style>
</head>

<body>

<div class="container">

<h1>Early Disease Risk Prediction</h1>

<form method="POST">

<input type="number" name="age" placeholder="Age" required>

<input type="number" name="bp" placeholder="Blood Pressure" required>

<input type="number" name="sugar" placeholder="Sugar Level" required>

<input type="number" name="cholesterol" placeholder="Cholesterol" required>

<input type="number" name="heart_rate" placeholder="Heart Rate" required>

<button type="submit">Predict Risk</button>

</form>

{% if prediction %}

<div class="result">

<h2>{{prediction}}</h2>

<h3>{{disease}}</h3>

<p>{{recommendation}}</p>

</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    disease = None
    recommendation = None

    if request.method == "POST":

        age = int(request.form["age"])
        bp = int(request.form["bp"])
        sugar = int(request.form["sugar"])
        cholesterol = int(request.form["cholesterol"])
        heart_rate = int(request.form["heart_rate"])

        features = np.array([[age, bp, sugar, cholesterol, heart_rate]])

        result = model.predict(features)[0]

        if result == 0:
            prediction = "🟢 Low Risk"
            disease = "Possible Disease: Healthy"
            recommendation = "Maintain healthy diet and exercise."

        elif result == 1:
            prediction = "🟠 Medium Risk"
            disease = "Possible Disease: Diabetes / BP Risk"
            recommendation = "Consult doctor and reduce sugar & oily food."

        else:
            prediction = "🔴 High Risk"
            disease = "Possible Disease: Heart Disease"
            recommendation = "Immediate medical checkup recommended."

    return render_template_string(
        HTML,
        prediction=prediction,
        disease=disease,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)