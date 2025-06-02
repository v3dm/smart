
# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestRegressor

# app = Flask(__name__)

# # Load data
# data = pd.read_csv("agricultural_sales_data_with_moisture.csv")
# data["waste_price"] = data["Price_per_Quintal"] / 3
# data = data.drop(columns=["Latitude", "Longitude"])

# Q1 = data["Total_Sale_Value"].quantile(0.25)
# Q3 = data["Total_Sale_Value"].quantile(0.75)
# IQR = Q3 - Q1
# data = data[~((data["Total_Sale_Value"] < (Q1 - 1.5 * IQR))) | 
#             (data["Total_Sale_Value"] > (Q3 + 1.5 * IQR))]
# data.waste_price = data["waste_price"].astype(int)

# # Preprocessing
# label_encoder = LabelEncoder()
# data['Crop_Name'] = label_encoder.fit_transform(data['Crop_Name'])
# X = data[['Crop_Name', 'Quantity_Sold_Quintal', 'Moisture_Content', 'Month', 'Year']]
# y = data['Total_Sale_Value']

# scaler = StandardScaler()
# X[['Quantity_Sold_Quintal', 'Moisture_Content']] = scaler.fit_transform(
#     X[['Quantity_Sold_Quintal', 'Moisture_Content']])

# #model
# model = RandomForestRegressor(n_estimators=200, max_depth=None, random_state=42, 
#                              min_samples_leaf=1, min_samples_split=2)
# model.fit(X, y)

# @app.route('/')
# def home():
#     return render_template('index.html', 
#                            crops=list(label_encoder.classes_))

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         #inputs
#         crop_name = request.form['crop']
#         month = int(request.form['month'])
#         year = int(request.form['year'])
#         waste_quantity = float(request.form['quantity'])
        
#         # Preprocess=input
#         crop_encoded = label_encoder.transform([crop_name])[0]
#         avg_moisture = X['Moisture_Content'].mean()
        
#         user_input = np.array([[crop_encoded, waste_quantity, avg_moisture, month, year]])
#         user_input[:, [1,2]] = scaler.transform(user_input[:, [1,2]])
        
#         # Predict regular value
#         predicted_regular_total = model.predict(user_input)[0]
        
#         # Calculate regular QUINTAL
#         regular_price_per_quintal = predicted_regular_total / waste_quantity
        
#         # Calculate waste
#         waste_price_per_quintal = regular_price_per_quintal / 3
        
#         #total value 
#         total_waste_value = waste_price_per_quintal * waste_quantity
        
#         return jsonify({
#             'crop': crop_name,
#             'month': month,
#             'year': year,
#             'quantity': waste_quantity,
#             'regular_price_per_quintal': round(regular_price_per_quintal, 2),
#             'waste_price_per_quintal': round(waste_price_per_quintal, 2),
#             'total_value': round(total_waste_value, 2)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

# **********************************************************************************************************************


# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestRegressor

# app = Flask(__name__)

# # Load data
# data = pd.read_csv("agricultural_sales_data_with_moisture.csv")
# data["waste_price"] = data["Price_per_Quintal"] / 3
# data = data.drop(columns=["Latitude", "Longitude"])

# # Create detailed valorization dictionary
# valorization_dict = {
#     "Wheat": (
#         "Processed into eco-friendly paper",
#         "Composted to create organic fertilizers",
#         "Used as an alternative to coal for clean energy",
#         "Straw fibers used in biodegradable plastics and textiles"
#     ),
#     "Sugarcane": (
#         "Bagasse burned in co-generation plants to produce electricity and steam",
#         "Bagasse separated from extracted juice after harvesting",
#         "Molasses collected after sugar extraction",
#         "Leaves & tops repurposed or burned"
#     ),
#     "Rice": (
#         "Rice husk ash used in cement and concrete",
#         "Straw used for insulation panels",
#         "Composted to create organic fertilizers",
#         "Converted into biogas, bioethanol, and biomass briquettes"
#     ),
#     "Mustard": (
#         "Husk compressed into biomass briquettes for fuel",
#         "Used in power plants, brick kilns, and boilers",
#         "Residues beneficial for livestock feed",
#         "Stalks used as mulch to retain soil moisture"
#     ),
#     "Paddy (Common)": (
#         "Consumed worldwide as a staple food",
#         "Rice bran oil extracted for cooking and skincare",
#         "Rice husk used for biomass energy",
#         "Rice straw processed into eco-friendly paper"
#     ),
#     "Paddy (Grade A)": (
#         "Consumed worldwide as a staple food",
#         "Rice bran oil extracted for cooking and skincare",
#         "Rice husk used for biomass energy",
#         "Rice straw processed into eco-friendly paper"
#     ),
#     "Maize": (
#         "Key ingredient in livestock feed",
#         "Used in food processing as corn starch & syrup",
#         "Converted into renewable bioethanol fuel",
#         "Corn-based bioplastics reduce petroleum dependency"
#     ),
#     "Jowar (Hybrid)": (
#         "Gluten-free flour used in baking",
#         "Stalks processed into bioethanol",
#         "High-energy grain for cattle and poultry",
#         "Used in brewing sorghum-based beer"
#     ),
#     "Jowar (Maldandi)": (
#         "Gluten-free flour used in baking",
#         "Stalks processed into bioethanol",
#         "High-energy grain for cattle and poultry",
#         "Used in brewing sorghum-based beer"
#     ),
#     "Bajra": (
#         "Used in making rotis and porridge",
#         "Provides essential nutrients to livestock",
#         "Used in biomass energy generation",
#         "Drought-resistant crop helps soil conservation"
#     ),
#     "Arhar (Tur)": (
#         "Staple protein-rich dal",
#         "Used as green manure for soil fertility",
#         "Used in poultry and cattle feed",
#         "Leaves and seeds have anti-inflammatory properties"
#     ),
#     "Moong": (
#         "High-protein sprouted food used in salads",
#         "Essential dal & flour in Indian cooking",
#         "Fixes nitrogen in soil, improving fertility",
#         "Used in skincare for exfoliation"
#     ),
#     "Urad": (
#         "Used in making idli, dosa, and vada",
#         "Ayurvedic medicine for digestion and muscle health",
#         "Protein-rich livestock feed",
#         "Improves nitrogen levels in soil"
#     ),
#     "Groundnut": (
#         "Edible oil extracted for cooking",
#         "Used in peanut butter production",
#         "Used as poultry and cattle feed",
#         "Peanut shells utilized for biofuel production"
#     ),
#     "Cotton (Long Staple)": (
#         "Used in textile industry for clothing and fabrics",
#         "Cottonseed oil extracted for cooking and industrial use",
#         "Cotton fibers used in high-quality paper",
#         "Medical bandages and wound dressings"
#     ),
#     "Cotton (Medium Staple)": (
#         "Used in textile industry for clothing and fabrics",
#         "Cottonseed oil extracted for cooking and industrial use",
#         "Cotton fibers used in high-quality paper",
#         "Medical bandages and wound dressings"
#     ),
#     "Gram (Chana)": (
#         "Staple protein-rich dal",
#         "Gram flour (besan) used in cooking and skincare",
#         "Provides nutrients for livestock feed",
#         "Fixes nitrogen in soil improving fertility"
#     ),
#     "Lentil (Masur)": (
#         "Dal & flour used in soups and curries",
#         "Essential plant-based protein for vegetarian diets",
#         "Used in poultry and cattle feed",
#         "Improves nitrogen levels in soil"
#     ),
#     "Barley": (
#         "Key ingredient in beer brewing",
#         "Used as livestock feed for nutrition",
#         "Used in cereals and dietary supplements",
#         "Medicinal uses for digestion and cholesterol control"
#     ),
#     "Safflower": (
#         "Edible oil extracted for cooking and health benefits",
#         "Natural dye production for textiles",
#         "Medicinal uses for heart health and inflammation",
#         "Used as poultry and livestock feed"
#     )
# }

# # Get unique crop names BEFORE encoding
# unique_crops = sorted(data['Crop_Name'].unique())

# # Data preprocessing
# Q1 = data["Total_Sale_Value"].quantile(0.25)
# Q3 = data["Total_Sale_Value"].quantile(0.75)
# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR
# data = data[(data["Total_Sale_Value"] >= lower_bound) & 
#             (data["Total_Sale_Value"] <= upper_bound)]
# data.waste_price = data["waste_price"].astype(int)

# # Preprocessing
# label_encoder = LabelEncoder()
# data['Crop_Encoded'] = label_encoder.fit_transform(data['Crop_Name'])
# X = data[['Crop_Encoded', 'Quantity_Sold_Quintal', 'Moisture_Content', 'Month', 'Year']]
# y = data['Total_Sale_Value']

# # Scale numerical features
# scaler = StandardScaler()
# X[['Quantity_Sold_Quintal', 'Moisture_Content']] = scaler.fit_transform(
#     X[['Quantity_Sold_Quintal', 'Moisture_Content']])

# # Train model
# model = RandomForestRegressor(n_estimators=200, max_depth=None, random_state=42, 
#                              min_samples_leaf=1, min_samples_split=2)
# model.fit(X, y)

# @app.route('/')
# def home():
#     return render_template('index.html', crops=unique_crops)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get form data
#         crop_name = request.form['crop']
#         month = int(request.form['month'])
#         year = int(request.form['year'])
#         waste_quantity = float(request.form['quantity'])
        
#         # Get valorization
#         valorization = valorization_dict.get(crop_name, "Crop waste can be used for composting or biomass energy.")
        
#         # Preprocess input
#         crop_encoded = label_encoder.transform([crop_name])[0]
#         avg_moisture = data['Moisture_Content'].mean()
        
#         # Prepare input array
#         user_input = np.array([[crop_encoded, waste_quantity, avg_moisture, month, year]])
        
#         # Scale quantity and moisture
#         user_input[:, [1, 2]] = scaler.transform(user_input[:, [1, 2]])
        
#         # Predict regular value
#         predicted_regular_total = model.predict(user_input)[0]
#         regular_price_per_quintal = predicted_regular_total / waste_quantity
#         waste_price_per_quintal = regular_price_per_quintal / 3
#         total_waste_value = waste_price_per_quintal * waste_quantity
        
#         return jsonify({
#             'crop': crop_name,
#             'month': month,
#             'year': year,
#             'quantity': waste_quantity,
#             'regular_price_per_quintal': round(regular_price_per_quintal, 2),
#             'waste_price_per_quintal': round(waste_price_per_quintal, 2),
#             'total_value': round(total_waste_value, 2),
#             'valorization': valorization
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import os

app = Flask(__name__, template_folder='templates')

# Load data - UPDATE PATH TO YOUR CSV FILE
data = pd.read_csv("./prediction_app/agricultural_sales_data_with_moisture.csv")
data["waste_price"] = data["Price_per_Quintal"] / 3
data = data.drop(columns=["Latitude", "Longitude"])

# Emission factors dictionary (kg CO2 per quintal)
emission_factors = {
    "Wheat": 181.82,
    "Mustard": 208.00,
    "Groundnut": 234.23,
    "Safflower": 218.49,
    "Bajra": 176.87,
    "Paddy (Common)": 181.82,
    "Jowar (Hybrid)": 187.05,
    "Barley": 181.82,
    "Gram (Chana)": 196.97,
    "Urad": 196.97,
    "Lentil (Masur)": 187.05,
    "Jowar (Maldandi)": 187.05,
    "Cotton (Medium Staple)": 218.49,
    "Maize": 196.97,
    "Moong": 200.00,
    "Cotton (Long Staple)": 218.49,
    "Sugarcane": 196.97,
    "Arhar (Tur)": 203.12,
    "Paddy (Grade A)": 181.82
}

# Valorization dictionary remains the same as before
valorization_dict = {
    "Wheat": (
        "Processed into eco-friendly paper",
        "Composted to create organic fertilizers",
        "Used as an alternative to coal for clean energy",
        "Straw fibers used in biodegradable plastics and textiles"
    ),
    "Sugarcane": (
        "Bagasse burned in co-generation plants to produce electricity and steam",
        "Bagasse separated from extracted juice after harvesting",
        "Molasses collected after sugar extraction",
        "Leaves & tops repurposed or burned"
    ),
    "Rice": (
        "Rice husk ash used in cement and concrete",
        "Straw used for insulation panels",
        "Composted to create organic fertilizers",
        "Converted into biogas, bioethanol, and biomass briquettes"
    ),
    "Mustard": (
        "Husk compressed into biomass briquettes for fuel",
        "Used in power plants, brick kilns, and boilers",
        "Residues beneficial for livestock feed",
        "Stalks used as mulch to retain soil moisture"
    ),
    "Paddy (Common)": (
        "Consumed worldwide as a staple food",
        "Rice bran oil extracted for cooking and skincare",
        "Rice husk used for biomass energy",
        "Rice straw processed into eco-friendly paper"
    ),
    "Paddy (Grade A)": (
        "Consumed worldwide as a staple food",
        "Rice bran oil extracted for cooking and skincare",
        "Rice husk used for biomass energy",
        "Rice straw processed into eco-friendly paper"
    ),
    "Maize": (
        "Key ingredient in livestock feed",
        "Used in food processing as corn starch & syrup",
        "Converted into renewable bioethanol fuel",
        "Corn-based bioplastics reduce petroleum dependency"
    ),
    "Jowar (Hybrid)": (
        "Gluten-free flour used in baking",
        "Stalks processed into bioethanol",
        "High-energy grain for cattle and poultry",
        "Used in brewing sorghum-based beer"
    ),
    "Jowar (Maldandi)": (
        "Gluten-free flour used in baking",
        "Stalks processed into bioethanol",
        "High-energy grain for cattle and poultry",
        "Used in brewing sorghum-based beer"
    ),
    "Bajra": (
        "Used in making rotis and porridge",
        "Provides essential nutrients to livestock",
        "Used in biomass energy generation",
        "Drought-resistant crop helps soil conservation"
    ),
    "Arhar (Tur)": (
        "Staple protein-rich dal",
        "Used as green manure for soil fertility",
        "Used in poultry and cattle feed",
        "Leaves and seeds have anti-inflammatory properties"
    ),
    "Moong": (
        "High-protein sprouted food used in salads",
        "Essential dal & flour in Indian cooking",
        "Fixes nitrogen in soil, improving fertility",
        "Used in skincare for exfoliation"
    ),
    "Urad": (
        "Used in making idli, dosa, and vada",
        "Ayurvedic medicine for digestion and muscle health",
        "Protein-rich livestock feed",
        "Improves nitrogen levels in soil"
    ),
    "Groundnut": (
        "Edible oil extracted for cooking",
        "Used in peanut butter production",
        "Used as poultry and cattle feed",
        "Peanut shells utilized for biofuel production"
    ),
    "Cotton (Long Staple)": (
        "Used in textile industry for clothing and fabrics",
        "Cottonseed oil extracted for cooking and industrial use",
        "Cotton fibers used in high-quality paper",
        "Medical bandages and wound dressings"
    ),
    "Cotton (Medium Staple)": (
        "Used in textile industry for clothing and fabrics",
        "Cottonseed oil extracted for cooking and industrial use",
        "Cotton fibers used in high-quality paper",
        "Medical bandages and wound dressings"
    ),
    "Gram (Chana)": (
        "Staple protein-rich dal",
        "Gram flour (besan) used in cooking and skincare",
        "Provides nutrients for livestock feed",
        "Fixes nitrogen in soil improving fertility"
    ),
    "Lentil (Masur)": (
        "Dal & flour used in soups and curries",
        "Essential plant-based protein for vegetarian diets",
        "Used in poultry and cattle feed",
        "Improves nitrogen levels in soil"
    ),
    "Barley": (
        "Key ingredient in beer brewing",
        "Used as livestock feed for nutrition",
        "Used in cereals and dietary supplements",
        "Medicinal uses for digestion and cholesterol control"
    ),
    "Safflower": (
        "Edible oil extracted for cooking and health benefits",
        "Natural dye production for textiles",
        "Medicinal uses for heart health and inflammation",
        "Used as poultry and livestock feed"
    )
}

# Get unique crop names BEFORE encoding
unique_crops = sorted(data['Crop_Name'].unique())

# Data preprocessing
Q1 = data["Total_Sale_Value"].quantile(0.25)
Q3 = data["Total_Sale_Value"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data["Total_Sale_Value"] >= lower_bound) & 
            (data["Total_Sale_Value"] <= upper_bound)]
data.waste_price = data["waste_price"].astype(int)

# Preprocessing
label_encoder = LabelEncoder()
data['Crop_Encoded'] = label_encoder.fit_transform(data['Crop_Name'])
X = data[['Crop_Encoded', 'Quantity_Sold_Quintal', 'Moisture_Content', 'Month', 'Year']]
y = data['Total_Sale_Value']

# Scale numerical features
scaler = StandardScaler()
X[['Quantity_Sold_Quintal', 'Moisture_Content']] = scaler.fit_transform(
    X[['Quantity_Sold_Quintal', 'Moisture_Content']])

# Train model
model = RandomForestRegressor(n_estimators=200, max_depth=None, random_state=42, 
                             min_samples_leaf=1, min_samples_split=2)
model.fit(X, y)

@app.route('/')
def home():
    return render_template('predictor.html', crops=unique_crops)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        crop_name = request.form['crop']
        month = int(request.form['month'])
        year = int(request.form['year'])
        waste_quantity = float(request.form['quantity'])
        
        # Get valorization
        valorization = valorization_dict.get(crop_name, "Crop waste can be used for composting or biomass energy.")
        
        # Preprocess input
        crop_encoded = label_encoder.transform([crop_name])[0]
        avg_moisture = data['Moisture_Content'].mean()
        
        # Prepare input array
        user_input = np.array([[crop_encoded, waste_quantity, avg_moisture, month, year]])
        
        # Scale quantity and moisture
        user_input[:, [1, 2]] = scaler.transform(user_input[:, [1, 2]])
        
        # Predict regular value
        predicted_regular_total = model.predict(user_input)[0]
        regular_price_per_quintal = predicted_regular_total / waste_quantity
        waste_price_per_quintal = regular_price_per_quintal / 3
        total_waste_value = waste_price_per_quintal * waste_quantity
        
        # Calculate CO2 emissions
        emission_factor = emission_factors.get(crop_name, 0)
        co2_emissions = waste_quantity * emission_factor
        
        return jsonify({
            'crop': crop_name,
            'month': month,
            'year': year,
            'quantity': waste_quantity,
            'regular_price_per_quintal': round(regular_price_per_quintal, 2),
            'waste_price_per_quintal': round(waste_price_per_quintal, 2),
            'total_value': round(total_waste_value, 2),
            'valorization': valorization,
            'co2_emissions': round(co2_emissions, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)