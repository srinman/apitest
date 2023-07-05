import json
from flask import Flask, request, jsonify, render_template, url_for
#from flask_cors import CORS 

datadict = {}
app = Flask(__name__)

#Implement default GET method 
@app.route('/test', methods=['GET'])
def home():
    #return render_template('index.html')
    response = {'message': 'Hello World Test!'}
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


#Implement GET method for all keys and values
@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(datadict)

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

#Implement POST method to initialize the dictionary with example keys and values with 10 sets
# curl -X POST 'localhost:5000/init' -H "Content-Type: application/json"  --data '{"count": 10}'
# curl -X POST 'https://srinmanapitest.azurewebsites.net/init' -H "Content-Type: application/json"  --data '{"count": 10}'
@app.route('/init', methods=['POST'])
def init_data():
    message = request.get_json()
    print(message)
    count = message['count']
    for i in range(count):
        key = 'key' + str(i)
        value = 'val' + str(i)
        datadict[key] = value
    return jsonify({'message': f'{count} keys added/updated'}) 


#Implement POST method to read values from Redis database and populate the dictionary 
# curl -X POST 'localhost:5000/readredis' -H "Content-Type: application/json"  --data '{"count": 10}'
# curl -X POST 'https://srinmanapitest.azurewebsites.net/readredis' -H "Content-Type: application/json"  --data '{"count": 10}'
#@app.route('/readredis', methods=['POST'])
#def read_redis():
    # Connect to Redis database
#    r = redis.Redis(host='localhost', port=6379, db=0)
    # Read all keys from Redis database
#    keys = r.keys()
    # Read all values from Redis database
#    values = r.mget(keys)
    # Populate the dictionary with keys and values
#    for i in range(len(keys)):
#        datadict[keys[i]] = values[i]
#    return jsonify({'message': f'{len(keys)} keys added/updated'})




if __name__ == '__main__':
    app.run()


