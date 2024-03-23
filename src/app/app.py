from flask import Flask, request, jsonify
from joblib import load

modelo = load('src/model/mejor_modelo.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = modelo.predict([data['features']])
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0:5000')
