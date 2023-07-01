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
#      curl -X GET 'localhost:5000/'


#Implement default GET method for a specific route - listing all keys
@app.route('/keys', methods=['GET'])
def get_keys():
    keys_list = list(datadict.keys())
    return json.dumps(keys_list)
#      curl -X GET 'localhost:5000/keys'


#Implement GET method for a specific route - listing a specific key
@app.route('/keys/<key>', methods=['GET'])
def get_key(key):
    if key in datadict:
        return jsonify({key: datadict[key]})
    else:
        return jsonify({'message': f'{key} not found'})
# curl -X GET 'localhost:5000/keys/key1'    

#Implement GET method for a specific route - listing all values
@app.route('/values', methods=['GET'])
def get_values():
    values_list = list(datadict.values())
    return json.dumps(values_list)
#      curl -X GET 'localhost:5000/values'


#Implement DELETE method for a specific route - deleting a key
@app.route('/keys/<key>', methods=['DELETE'])
def delete_key(key):
    if key in datadict:
        del datadict[key]
        return jsonify({'message': f'{key} deleted'})
    else:
        return jsonify({'message': f'{key} not found'})
#      curl -X DELETE 'localhost:5000/keys/key1'


#Implement PUT method for a specific route - updating a key
@app.route('/keys/<key>', methods=['PUT'])
def update_key(key):
    if key in datadict:
        value = request.get_json()['value']
        datadict[key] = value
        return jsonify({'message': f'{key} updated with value {value}'})
    else:
        return jsonify({'message': f'{key} not found'})
#      curl -X PUT 'localhost:5000/keys/key2' -H "Content-Type: application/json"  --data '{"value":"valx"}'


#Implement POST method to add a new key
@app.route('/keys', methods=['POST'])
def add_data():
    message = request.get_json()
    print(message)
    key = message['key']
    value = message['value']
    datadict[key] = value
    return jsonify({'message': f'{key} added/updated with value {value}'})
#      curl -X POST 'localhost:5000/keys' -H "Content-Type: application/json"  --data '{"key": "key2","value":"val2"}'



if __name__ == '__main__':
    app.run()


# Sample calls
# - to test this app with curl use the following command
#      curl https://srinmanapitest.azurewebsites.net/
# - to test this app as a backend API with APIM, provided /apitest is the name of the API
#      curl -X GET 'https://srinmanapimpub.azure-api.net/apitest' -H 'Host: srinmanapimpub.azure-api.net' -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: 2a4482..."
#            API URL suffix is apitest           
#             Base URL is https://srinmanapimpub.azure-api.net/apitest
#            call is routed to /apitest and web service URl is set to https://srinmanapitest.azurewebsites.net/  but APIM protects the web service URL with a subscription key so that only authorized users can access it
#      curl -X POST 'localhost:5000/addkey' -H "Content-Type: application/json" --data '{"key": "key1","value":"val1"}' 
