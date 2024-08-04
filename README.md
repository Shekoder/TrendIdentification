# Trend Identification System
A full-stack application for identifying and analyzing fashion trends using Flask (backend) and React (frontend). 

## Features

- **Trend Management**: Add and view trends.
- **Data Operations**: Execute data cleaning and analysis scripts.
- **Analysis Results**: Fetch and display results.

## Tech Stack

- **Backend**: Flask, MongoDB, 
- **Frontend**: React

## Getting Started

### Backend

1. Clone the repository:
   ```sh
   git clone https://github.com/shekoder/trendIdentification.git
   cd trendIdentification
   ```

2. Set up and activate the virtual environment:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows


3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```sh
   python app.py
   ```

### Frontend

1. Navigate to the React app directory:
   ```sh
   cd client
   ```

2. Install dependencies and start the app:
   ```sh
   npm install
   npm start
   ```

## API Endpoints

- **GET `/api/trends`**: Retrieve trends.
- **POST `/api/trends`**: Add a trend.
- **GET `/api/analysis-results`**: Fetch analysis results.
- **GET `/api/data-operations`**: Run data scripts.
