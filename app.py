from flask import Flask, render_template, request
import json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load predefined locations from JSON
with open('data/unique_locations.json', 'r') as f:
    locations = json.load(f)

locations.remove('Other')

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_price(location, area, bathroom, bhk):
    location_index = locations.index(location) if location in locations else -1

    x = np.zeros(len(locations) + 3)
    x[0] = area
    x[1] = bathroom
    x[2] = bhk
    if location_index >= 0:
        x[location_index] = 1

    x = pd.DataFrame([x], columns=model.feature_names_in_)  # Convert to DataFrame
    predicted_price = "{:,.2f}".format(model.predict(x)[0] * 100000)
    return predicted_price


@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price = None
    selected_specs = None
    
    if request.method == 'POST':
        # Get user inputs from the form
        location = request.form['location']
        area = float(request.form['area'])
        bathrooms = int(request.form['bathrooms'])
        bhk = int(request.form['bhk'])
        
        predicted_price = predict_price(location, area, bathrooms, bhk)
        selected_specs = {
            'location': location,
            'area': area,
            'bathrooms': bathrooms,
            'bhk': bhk
        }
    
    return render_template('index.html', locations=locations, predicted_price=predicted_price, selected_specs=selected_specs)

if __name__ == '__main__':
    app.run(debug=False)
