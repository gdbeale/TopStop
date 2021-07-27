from flask import jsonify, request
from werkzeug.exceptions import BadRequest
import requests


class NexTrip:

    def get_route_directions(self, route_id):
        res = requests.get(url="https://svc.metrotransit.org/nextripv2/directions/"+str(route_id))
        data = res.json()
        directions = []
        for item in data:
            directions.append(item['direction_name'])

        return directions


class InvalidStopException(BadRequest):
    code = 490
    description = 'Submited stop is not a valid Metro Transit stop'


class InvalidRouteException(BadRequest):
    code = 490
    description = 'Submited stop is not a valid Metro Transit stop'

# app.register_error_handler(InvalidStopException, handle_490)
# raise InvalidStopException()
