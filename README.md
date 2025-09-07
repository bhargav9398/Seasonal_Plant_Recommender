# Seasonal Plant Recommender

A web app to recommend crops and fruits based on the selected season (Kharif, Rabi, Zaid).

## Features

- Enter a season and get a list of recommended crops and fruits with their growing duration.
- Clean, responsive UI.
- Powered by Flask backend.

## Usage

1. **Install dependencies**  
   Make sure you have Python and Flask installed:
   ```sh
   pip install flask
   ```

2. **Run the server**  
   ```sh
   python season.py
   ```

3. **Open in browser**  
   Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Project Structure

- [`index.html`](index.html): Frontend UI
- [`season.py`](season.py): Flask backend

## API

- `POST /recommend`  
  Request JSON: `{ "season": "rabi" }`  
  Response: List of crops/fruits for the season.

## License
