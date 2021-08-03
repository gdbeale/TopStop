# TopStop
Flask application that serves up MetroTransit NexTrip APIs

Steps to run (requires Docker)
_______________________________________________________________
    Change to directory you would like to install the application
    git clone https://github.com/gdbeale/TopStop
    Validate Docker is running on local maching

Run the project
_______________________________________________________________
    docker-compose up
    docker-compose -p tests run --rm topstop pytest -v 
    Run tests
_______________________________________________________________
    pytest -v

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

Run tests
_______________________________________________________________
    pytest -v

    Check test coverage
    python -m pytest --cov-report term-missing --cov=topstop_app