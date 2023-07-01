import json
from flask import Flask, request, jsonify, render_template, url_for
#from flask_cors import CORS 

datadict = {}
app = Flask(__name__)

#Implement default GET method 
@app.route('/', methods=['GET'])
def home():
    #return render_template('index.html')
    response = {'message': 'Hello World'}
    return jsonify(response)
#Implement default GET method for a specific route - listing all keys
@app.route('/keys', methods=['GET'])
def get_keys():
    keys_list = list(datadict.keys())
    return json.dumps(keys_list)
#Implement GET method for a specific route - listing all values
@app.route('/values', methods=['GET'])
def get_values():
    values_list = list(datadict.values())
    return json.dumps(values_list)
#Implement POST method
@app.route('/keys', methods=['POST'])
def add_data():
    message = request.get_json()
    print(message)
    key = message['key']
    value = message['value']
    datadict[key] = value
    return jsonify({'message': f'{key} added/updated with value {value}'})

if __name__ == '__main__':
    app.run()



# - to test this app with curl use the following command
#      curl https://srinmanapitest.azurewebsites.net/
# - to test this app as a backend API with APIM, provided /apitest is the name of the API
#      curl -X GET 'https://srinmanapimpub.azure-api.net/apitest' -H 'Host: srinmanapimpub.azure-api.net' -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: 2a4482..."
#            API URL suffix is apitest           
#             Base URL is https://srinmanapimpub.azure-api.net/apitest
#            call is routed to /apitest and web service URl is set to https://srinmanapitest.azurewebsites.net/  but APIM protects the web service URL with a subscription key so that only authorized users can access it
#      curl -X POST 'localhost:5000/addkey' -H "Content-Type: application/json" --data '{"key": "key1","value":"val1"}' 