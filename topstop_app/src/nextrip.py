from flask import jsonify, request
from werkzeug.exceptions import BadRequest
import requests


class NexTrip:

    # Return a dictionary object of all routes.  Route number is the key, Route label is the value
    def get_routes(self):
        routes = {}
        res = requests.get(url="https://svc.metrotransit.org/nextripv2/routes/")
        data = res.json()
        for route in data:
            routes[route["route_id"]] = route["route_label"]
        return routes

    # Return a list of directions.  The list index also functions as the Metro Transit ID for subsequent calls
    # requiring the RouteID
    def get_route_directions(self, route_id):
        directions = []
        res = requests.get(url="https://svc.metrotransit.org/nextripv2/directions/"+str(route_id))
        data = res.json()
        if "Bad Request" == res.reason:
            raise InvalidRouteException(data['detail'])
        for item in data:
            directions.append(item['direction_name'])
        return directions

    # Return a dictionary object of all stops (place codes) for a given route in a given direction.
    # key:value is place_code:description, i.e. {"Mall of America Station": "MAAM"}
    def get_route_stops(self, route_id, dir):
        routes = {}
        res = requests.get(url="https://svc.metrotransit.org/nextripv2/stops/"+str(route_id)+"/"+str(dir))
        data = res.json()
        if "Bad Request" == res.reason:
            raise InvalidDirectionException(data['detail'])
        for route in data:
            routes[route["place_code"]] = route["description"]
        return routes

    # Returns a list of departures from a given statiuon
    def get_departures(self, route_id, dir, place_code):
        routes = []
        res = requests.get(url="https://svc.metrotransit.org/nextripv2/" +
                           str(route_id)+"/"+str(dir)+"/"+place_code)
        if 404 == res.status_code:
            raise InvalidStopException(res.reason)
        data = res.json()
        for route in data["departures"]:
            routes.append(route["departure_text"])
        return routes


class InvalidRouteException(BadRequest):
    code = 490
    description = 'Submited route is not a valid Metro Transit Route'


class InvalidDirectionException(BadRequest):
    code = 491
    description = 'Submited direction is not correct'


class InvalidStopException(BadRequest):
    code = 492
    description = 'Submited stop is not a valid Metro Transit stop'


class InvalidNextTripException(BadRequest):
    code = 493
    description = 'NexTrip service requested with incorrect data'


# app.register_error_handler(InvalidStopException, handle_490)
# raise InvalidStopException()
