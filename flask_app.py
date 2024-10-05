from flask import Flask, make_response, jsonify, request, render_template
import os
from flask_cors import CORS
import pickle
import joblib
import numpy as np

app = Flask(__name__)

# Use CORS if necessary
CORS(app)

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
        return render_template('Homepage.html')

@app.route('/search', methods=['GET'])
def search():
     return render_template('Search.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the comma-separated data from the request
    data = request.form.get('formData')

    if data:
        # Split the string into a list
        data_list = data.split(',')

        # Assuming you have a fixed order for the data:
        age_category = int(data_list[0])
        gender = int(data_list[1])
        duration_days = int(data_list[2])
        symptoms_values = [int(i) for i in data_list[3:]]

        # Create a response dictionary (you can modify this as needed)
        response = [age_category, gender, duration_days] + symptoms_values
        response = np.array(response).reshape(1, -1)  # Reshape to 2D array

        # Load the model
        with open("C:\\Users\\m\\Desktop\\mohhhhhhyyyy\\model_test_two.pkl", 'rb') as file:
                model = pickle.load(file)
                print("Model loaded successfully. Type:", type(model))
                prediction = model.predict(response)
                prediction = prediction.tolist()[0]
        
        disease_dict = {
    "hypertension": ("Lisinopril", "Zestril"),
    "bronchitis": ("Albuterol", "Ventolin"),
    "migraine": ("Sumatriptan", "Imitrex"),
    "gastritis": ("Omeprazole", "Prilosec"),
    "allergy": ("Loratadine", "Claritin"),
    "pneumonia": ("Amoxicillin", "Augmentin"),
    "asthma": ("Fluticasone", "Flovent"),
    "eczema": ("Cetirizine", "Zyrtec"),
    "food poisoning": ("Loperamide", "Imodium"),
    "diabetes": ("Metformin", "Glucophage"),
    "depression": ("Sertraline", "Zoloft"),
    "anxiety": ("Diazepam", "Valium"),
    "sinusitis": ("Fluticasone", "Fluticasone"),
    "covid-19": ("Remdesivir", "Remdesivir"),
    "common cold": ("Fexofenadine", "Allegra"),
    "flu": ("Oseltamivir", "Tamiflu")
}


        # return jsonify(prediction.tolist()), 200  # Return the prediction as JSON
        return f"Disease:  {prediction} \nActive Ingredient:  {disease_dict[str(prediction).lower()][0]} \nMedicine: {disease_dict[str(prediction).lower()][1]}", 200



if __name__ == "__main__":      
    app.run(debug=True)



#     with open("C:\\Users\\m\\Desktop\\Price Comparison\\Price Comparison\\project\\KNN.pkl", 'rb') as file:
#         model = pickle.load(file)
#     with open('C:\\Users\\m\\Desktop\\Price Comparison\\Price Comparison\\project\\vectorizer.pkl', 'rb') as file2:
#         loaded_vectorizer  = pickle.load(file2)

#     with open('C:\\Users\\m\\Desktop\\Price Comparison\\Price Comparison\\project\\mlb.pkl', 'rb') as file3:
#         mlb  = pickle.load(file3)

#     result = model.predict(loaded_vectorizer.transform([query]))      
#     result = mlb.inverse_transform(result)
#     print(result)