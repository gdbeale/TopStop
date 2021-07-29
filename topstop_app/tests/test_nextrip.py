# test the functionality of Nextrip model class
import pytest
import time
import re
from ..src.nextrip import NexTrip, InvalidDirectionException, InvalidStopException, InvalidRouteException


# test whether routes from Nextrip match pulic API
# For reference route infomation is in src/routes.json (only for the given day)
# [{"route_id": "901","agency_id": 0,"route_label": "METRO Blue Line"},
# ...
# {"route_id": "724","agency_id": 0,"route_label": "Route 724"}]
def test_get_routes():
    test_route = {"901": "METRO Blue Line"}
    next_trip = NexTrip()
    routes = next_trip.get_routes()
    # First route is always 901, METRO Blue line, so test just the first value
    assert test_route.get("901") == routes.get("901")


# Test if we return the correct direction id from a known route
# Route 901: Blue line
# [{"direction_id":0,"direction_name":"Northbound"},{"direction_id":1,"direction_name":"Southbound"}]
def test_get_route_direction():
    directions = ["Northbound", "Southbound"]
    next_trip = NexTrip()
    assert directions == next_trip.get_route_directions(901)


# test whether stops from Nextrip match pulic API of a known route
# [{"place_code":"MAAM","description":"Mall of America Station"},
# {"place_code":"28AV","description":"28th Ave Station"},
# ....
# {"place_code":"TF2","description":"Target Field Station Platform 2"}]
def test_get_route_stops():
    # Route 901 stops Northbound (dir Id 0) - First stop is always MAAM - Mall of America Station
    stops = {"MAAM": "Mall of America Station"}
    next_trip = NexTrip()
    allstops = next_trip.get_route_stops(901, 0)
    assert stops["MAAM"] == allstops["MAAM"]


# Test Nextrip trips against public api
# Use a known stop id for a route and test if correct data comes back
# test if the JSON has the correct stop id for MAAM (Mall of America)
def test_get_departures():
    next_trip = NexTrip()
    data = next_trip.get_departures(901, 0, "MAAM")
    assert (re.search(r"\d+\d*:\d{2}", data[0]) or re.search(r"\d+ Min", data[0]) or re.search(r"Due", data[0]))


# Do we handle passing a bad route gracefully
def test_bad_route():
    with pytest.raises(InvalidRouteException) as e_info:
        next_trip = NexTrip()
        next_trip.get_route_directions(-1)


# Do we handle passing a bad directions gracefully
def test_bad_directions():
    with pytest.raises(InvalidDirectionException) as e_info:
        next_trip = NexTrip()
        next_trip.get_route_stops(901, -1)


# Do we handle passing a bad stop gracefully
def test_bad_stop():
    with pytest.raises(InvalidStopException) as e_info:
        next_trip = NexTrip()
        next_trip.get_departures(901, 0, "")
