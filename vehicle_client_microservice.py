import requests
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

# URL of the data storage microservice
DATA_STORAGE_URL = 'http://127.0.0.1:5000'

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all vehicles from the data storage microservice
@app.route('/get_vehicles', methods=['GET'])
def get_vehicles():
    response = requests.get(f'{DATA_STORAGE_URL}/get_vehicles')
    if response.status_code == 200:
        vehicles = response.json()
        return render_template('vehicle_list.html', vehicles=vehicles)
    else:
        return 'Failed to get vehicles.'

if __name__ == '__main__':
    app.run(debug=True,port=5001)
