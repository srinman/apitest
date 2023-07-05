# apitest


## APIM configuration


APIM hostname +  API URL suffix + Operation URL

mapped to   

Webservice URL  + Operation URL




Clients call APIM hostname +  API URL suffix + Operation URL 

which is routed to 

backend API URL  + Operation URL



for Webservice URL, don't use suffix / at the end.  For example, use https://www.google.com instead of https://www.google.com/  
APIM uses Operation URL to construct inbound URI.  
For example 

APIM hostname + 'api5' + '/test' 
https://10.244.0.9:8081/api5/test 

is mapped to 

Webservice URL + '/test'
https://srinmanapitest.azurewebsites.net/test




## Sample Calls


 Sample calls
 - to test this app with curl use the following command
      curl https://srinmanapitest.azurewebsites.net/
 - to test this app as a backend API with APIM, provided /apitest is the name of the API
      curl -X GET 'https://srinmanapimpub.azure-api.net/apitest' -H 'Host: srinmanapimpub.azure-api.net' -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: 2a4482..."
            API URL suffix is apitest           
             Base URL is https://srinmanapimpub.azure-api.net/apitest
            call is routed to /apitest and web service URl is set to https://srinmanapitest.azurewebsites.net/  but APIM protects the web service URL with a subscription key so that only authorized users can access it
      curl -X POST 'localhost:5000/addkey' -H "Content-Type: application/json" --data '{"key": "key1","value":"val1"}' 
