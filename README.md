# TopStop
Flask application that serves up MetroTransit NexTrip APIs.  This application is incomplete as of now due to resource contraint.  
See the list below for implemented features:

Features
_______________________________________________________________
- [x] Create GitHub repo for project
- [x] Create unit tests for model
- [x] Create UI NextTrip Templates
- [x] Add Routing for Back and Forward
- [x] Add bootstrap styling
- [x] Add exceptions
- [x] Wire up NextTrip APIs to model
- [x] Create Docker image for portability
- [x] Dynamic components
- [x] Add functional tests
- [x] Wire Route element to model
- [ ] Wire Directions and Stops to model
- [ ] Add Departures
- [ ] Add Database for NextTrip
- [ ] Add Performance tweaks for NextTrip
    - [ ] in-memory
    - [ ] Caching
    - [ ] multithreading?
    - [ ] browserfy | bootstrap
- [ ] Google Map 
- [ ] Detect location (flask-babel for timezone section)
- [ ] Add Next bus to map



Steps to run (requires Docker)
_______________________________________________________________
    Change to directory you would like to install the application
    git clone https://github.com/gdbeale/TopStop
    Validate Docker is running on local maching

Run the project
_______________________________________________________________
    docker-compose up
    navigate to localhost:5000/

Run tests
_______________________________________________________________
    docker-compose -p tests run --rm topstop pytest -v 
    Should result in 3 failed tests (functionality not implemented yet)

When finished run 'deactivate'


_______________________________________________________________
Steps build and run application without Docker
_______________________________________________________________
    Install python 3.9.x - https://www.python.org/downloads/
    Change to directory you would like to install the application
    git clone https://github.com/gdbeale/TopStop
    cd Topstop
    python3 -m venv env
    source env/bin/activate
    pip3 install Flask
    pip3 install -r requirements.txt

Run the project
_______________________________________________________________
    cd topstop_app
    export FLASK_ENV=production
    flask run
    navigate to localhost:5000/

Run tests
_______________________________________________________________
    pytest -v

    Check test coverage
    python -m pytest --cov-report term-missing --cov=topstop_app