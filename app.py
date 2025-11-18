import pandas as pd
import joblib
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model/model.pkl')

# Define the expected columns (exact order from training!)
# This helps us reconstruct the dataframe with 0s and 1s
model_columns = [
    'pages_visited', 'time_on_site', 'email_opens', 'interaction_score', 
    'profile_complete', 'previous_purchases', 
    'lead_source_Facebook', 'lead_source_Google Ads', 
    'lead_source_Instagram', 'lead_source_LinkedIn', 
    'lead_source_Referral', 
    'country_Germany', 'country_India', 'country_UK', 'country_USA'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 1. Get data from the HTML form
        pages_visited = int(request.form['pages_visited'])
        time_on_site = float(request.form['time_on_site'])
        email_opens = int(request.form['email_opens'])
        interaction_score = int(request.form['interaction_score'])
        profile_complete = int(request.form['profile_complete'])
        previous_purchases = int(request.form['previous_purchases'])
        
        # Handle Categorical: Lead Source
        lead_source = request.form['lead_source']
        
        # Handle Categorical: Country
        country = request.form['country']
        
        # 2. Create a DataFrame with all columns set to 0 initially
        input_data = pd.DataFrame(0, index=[0], columns=model_columns)
        
        # 3. Fill in the numerical values
        input_data['pages_visited'] = pages_visited
        input_data['time_on_site'] = time_on_site
        input_data['email_opens'] = email_opens
        input_data['interaction_score'] = interaction_score
        input_data['profile_complete'] = profile_complete
        input_data['previous_purchases'] = previous_purchases
        
        # 4. Set the correct One-Hot columns to 1
        # Example: If lead_source is 'Facebook', set 'lead_source_Facebook' to 1
        if f'lead_source_{lead_source}' in model_columns:
            input_data[f'lead_source_{lead_source}'] = 1
            
        if f'country_{country}' in model_columns:
            input_data[f'country_{country}'] = 1

        # 5. Make the prediction
        prediction = model.predict(input_data)[0]
        
        result = "High Potential Lead! 🚀" if prediction == 1 else "Low Potential Lead 📉"
        
        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)