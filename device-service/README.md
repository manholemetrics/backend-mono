# Microservice Template

## Setup of environment

After cloning the project create a virtual environment using 
```
python3 -m venv env
```
Then activate the environment using 
```
source ./env/bin/activate
```
If using fish shell use the following instead
```
source ./env/bin/activate/fish
```
Next install the requirements using 
```
pip install -r requirments.txt
```

## Generation of models
Models are automatically generated from json schemas in the app/api/schema folder. The generation can be run by running
```
./scripts/setup
```
Whenever the schemas are changed this needs to be rerun

## Modifying libraries
Whenever new libraries are installed run
```
pip freeze > requirements.txt
```

## Running locally
To run locally run in the route directory:
```
./scripts/local_run
```
The docker containers needed and environment variables should also be set in this file

## Running tests
