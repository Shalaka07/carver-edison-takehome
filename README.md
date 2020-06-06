# carver-edison-takehome
Instructions for setup -
1. Download repository.
2. Navigate to the repo on your local machine and create a new virtual environment. <br /> `python3 -m venv venv`
3. Activate the virtual environment. <br /> `source venv/bin/activate`

Install dependencies - <br />
We need to install Flask, pandas and datetime inside the virtual environment. Use the command `pip3 install Flask` and similar to install them.

Running the API - <br />
The Flask API can be run locally with the `python3 app.py` command from inside venv. 
Once the API is running, open a new terminal and use CURL to make a POST request to the API. You may be required to install CURL on your system if not already installed. <br />

`curl -i -H "Content-Type:application/json" -X POST -d '{"filters":{"Languages":["spanish","italian"], "Salary":{"max":300000,"min":100000}, "Date":{}}}' http://localhost:5000/`

Replace "filters" in the command with the required filtering criteria.  <br />
The output returned by the API can be seen on the terminal. You may use an external JSON formatting tool to view the terminal response.
