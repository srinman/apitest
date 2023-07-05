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