# Microservice Template

## About

- Create authentication tokens with different access levels for a company.
    - Request authentication token for a sub account using username and password
- Can create sub accounts for a company with different access levels.
    - Need to be able to access a list of accounts.
    - Need to see information for a single account
    - Need to be edit an account
    - Need to be able to create an account
    - Need to be able to destroy an account

## Instructions

### Setup of environment

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

### Generation of models
Models are automatically generated from json schemas in the app/api/schema folder. The generation can be run by running
```
./scripts/setup
```
Whenever the schemas are changed this needs to be rerun

### Modifying libraries
Whenever new libraries are installed run
```
pip freeze > requirements.txt
```

### Running locally
To run locally run in the route directory:
```
sudo docker-compose up --build
```
The service will be run locally on port 8000

### Running tests
