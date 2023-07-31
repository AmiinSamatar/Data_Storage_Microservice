import sqlite3
from flask import Flask, request, jsonify, render_template, g
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)  # Enable CORS for the entire app

DATABASE = 'vehicle_database.db'

# Helper function to get the database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close the database connection when the application context is popped
@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Create a table for storing vehicle information if it doesn't exist
def create_table():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                mileage REAL NOT NULL
            )
        ''')
        conn.commit()

# Route to serve the index.html page
@app.route('/')
def index():
    create_table()
    return render_template('add_vehicle.html')

# Route to add a new vehicle to the database
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    make = data['make']
    model = data['model']
    year = data['year']
    mileage = data['mileage']

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO vehicles (make, model, year, mileage)
            VALUES (?, ?, ?, ?)
        ''', (make, model, year, mileage))
        conn.commit()

    return jsonify({'message': 'Vehicle added successfully'}), 201

# Route to get all vehicles from the database
@app.route('/get_vehicles', methods=['GET'])
def get_vehicles():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vehicles')
        vehicles = cursor.fetchall()

        vehicle_list = []
        for vehicle in vehicles:
            vehicle_data = {
                'id': vehicle[0],
                'make': vehicle[1],
                'model': vehicle[2],
                'year': vehicle[3],
                'mileage': vehicle[4],
            }
            vehicle_list.append(vehicle_data)

    return jsonify(vehicle_list), 200

if __name__ == '__main__':
    app.run(debug=True)
