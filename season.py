from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

plants_data = {
    "kharif": [
        {"Name": "Rice", "Type": "Crop", "Duration (days)": "120-150"},
        {"Name": "Maize", "Type": "Crop", "Duration (days)": "90-110"},
        {"Name": "Cotton", "Type": "Crop", "Duration (days)": "150-180"},
        {"Name": "Mango", "Type": "Fruit", "Duration (days)": "100-150"},
        {"Name": "Banana", "Type": "Fruit", "Duration (days)": "270-300"}
    ],
    "rabi": [
        {"Name": "Wheat", "Type": "Crop", "Duration (days)": "120-150"},
        {"Name": "Mustard", "Type": "Crop", "Duration (days)": "90-120"},
        {"Name": "Gram (Chickpea)", "Type": "Crop", "Duration (days)": "140-150"},
        {"Name": "Apple", "Type": "Fruit", "Duration (days)": "150-180"},
        {"Name": "Orange", "Type": "Fruit", "Duration (days)": "200-240"}
    ],
    "zaid": [
        {"Name": "Watermelon", "Type": "Crop", "Duration (days)": "80-100"},
        {"Name": "Cucumber", "Type": "Crop", "Duration (days)": "50-70"},
        {"Name": "Muskmelon", "Type": "Crop", "Duration (days)": "75-90"},
        {"Name": "Papaya", "Type": "Fruit", "Duration (days)": "180-240"},
        {"Name": "Pineapple", "Type": "Fruit", "Duration (days)": "150-180"}
    ]
}

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json() or {}
    season = data.get('season', '').strip().lower()
    if not season:
        return jsonify([]), 400
    return jsonify(plants_data.get(season, []))

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
