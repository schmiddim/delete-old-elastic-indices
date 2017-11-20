# Delete old indices from Elasticsearch

### Setup ###
*activate virtual env*
````bash
virtualenv  venv 
virtualenv   -p python3 venv    #if python2 is the default interpreter
````

**goto venv**
````bash
source venv/bin/activate
````
*resolve Dependencies*
````bash
pip3 install -r requirements.txt #dependencies
````

*exit venv if you're done*
````bash
deactivate
````
 ### Config ###
 copy the file **settings.py**.dist to settings.py and modify url,index pattern, days