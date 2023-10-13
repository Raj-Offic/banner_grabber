import sys
import requests
import socket

if len(sys.argv) < 2 :
    print('please pass an argument :)') 
    sys.exit()

else :
    req = requests.get('http://'+sys.argv[1])
    
    print('\n'+str(req.headers)) #it gets all the header values

    print('\n'+'the status code - '+str(req.status_code))
    print('\n'+'Date            - '+str(req.headers['date']))
    print('\n'+'The Server      -  '+str(req.headers['server']))


    ip = socket.gethostbyname(sys.argv[1])
    
    print('\n'+'the ip_address of - '+sys.argv[1] +' is '+ ip+'\n')

