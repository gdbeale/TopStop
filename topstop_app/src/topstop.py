import time

from ..src.nextrip import NexTrip


# Class TopStop represents a user's "TopStop" request.  This stateful object will store the route, directions, stop
# and real-time departure information of a user request for NexTrip information
class TopStopRequest:

    route_id = None
    direction = None
    direction_id = None
    stop_name = None
    departures = []
    latitude = None
    longitude = None
    req_time = None
    dir_dict = {"Northbound": 0, "Southbound": 1, "Eastbound": 0, "Westbound": 1}
    timeout = 120

    def __init__(self, route_id) -> None:
        self.route_id = route_id
        self.reset_time()

    # Call Nexttrip to get the departures list and restart the clock on timing out
    def get_departures(self):
        self.departures = NexTrip().get_departures(self.route_id, self.direction_id, self.stop_name)
        self.reset_time()
        return self.departures

    # Simple setter plus saving the direction id from the directions dictionary
    def set_direction(self, dir):
        self.direction = dir
        self.direction_id = self.dir_dict[dir]

    # Convience funtion to reset out of date timer
    def reset_time(self):
        self.req_time = time.time()

    def is_timeout(self):
        return time.time() - self.timeout >= self.req_time
