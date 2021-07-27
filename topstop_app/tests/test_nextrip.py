# test the functionality of Nextrip model class
import pytest
from ..src.nextrip import NexTrip, InvalidStopException, InvalidRouteException


# test whether routes from Nextrip match pulic API
# For reference route infomation is in src/routes.json (only for the given day)
# [{"route_id": "901","agency_id": 0,"route_label": "METRO Blue Line"},
# ...
# {"route_id": "724","agency_id": 0,"route_label": "Route 724"}]
def test_get_routes():
    test_route = ["901", "METRO Blue Line"]
    next_trip = NexTrip()
    routes = next_trip.get_routes()
    # First route is always 901, METRO Blue line, so test just the first value
    assert test_route == routes[0]


# Test if we return the correct direction id from a known route
# Route 901: Blue line
# [{"direction_id":0,"direction_name":"Northbound"},{"direction_id":1,"direction_name":"Southbound"}]
def test_get_route_direction():
    directions = {"Northbound": 0, "Southbound": 1}
    next_trip = NexTrip()
    assert directions == next_trip.get_route_directions(901)


# test whether stops from Nextrip match pulic API of a known route
# [{"place_code":"MAAM","description":"Mall of America Station"},
# {"place_code":"28AV","description":"28th Ave Station"},
# ....
# {"place_code":"TF2","description":"Target Field Station Platform 2"}]
def test_get_stops():
    # Route 901 stops Northbound (dir Id 0) - First stop is always MAAM - Mall of America Station
    stops = {"Mall of America Station": "MAAM"}
    next_trip = NexTrip()
    assert stops == next_trip.get_route_stops(901, 1)


# Test Nextrip trips against public api
def get_next_trips():
    assert 1 == 1


# Do we handle passing a bad stop gracefully
def test_stop_not_found():
    next_trip = NexTrip()
    with pytest.raises(InvalidStopException) as e_info:
        next_trip.get_route_stops(901, -1)


# Do we handle passing a bad route gracefully
def test_route_not_found():
    next_trip = NexTrip()
    with pytest.raises(InvalidRouteException) as e_info:
        next_trip.get_route_stops(901, -1)
