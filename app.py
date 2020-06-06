# Import Flask and other modules
from flask import Flask
from flask import request
import employees
    
# Create a Flask app
app = Flask(__name__)

# Establish a Flask route to serve HTTP traffic  
@app.route('/', methods=['POST'])

def employee_filter():
	
	if not request.json or not "filters" in request.json:
		abort(400)

	resp = employees.filter(request.json["filters"])
	return resp

# Setup 
if __name__ == '__main__':
    app.run(debug=True)

