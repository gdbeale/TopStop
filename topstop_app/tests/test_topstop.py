# test the functionality of TopStop model class
import pytest
import time
import re
from ..src.topstop import TopStopRequest


@pytest.fixture
def topstop_request():
    topstop_req = TopStopRequest(901)
    topstop_req.set_direction("Northbound")
    topstop_req.stop_name = "MAAM"
    return topstop_req


# Test if we a set of departures is returned.  Since this information is real-time
# just testing the size and content of the data will be done
def test_departures(topstop_request):
    data = topstop_request.get_departures()
    assert data.len() > 0
    assert re.match(r"\d{2}:\d{2}", data[0])


# We should track if departures are out of date.  As we don't want to have this test run for the full
# two minutes, we will temproarily change the timeout
def test_out_of_date(topstop_request):
    topstop_request.timeout = 5
    time.sleep(6)
    assert topstop_request.is_timeout()


# Test getting location long/lat, test if the result is in Minneaplois / St. Paul
def get_stop_coordinates():
    assert 1 == 1


# Test the retrieving bus locations within a distance of a stop
def get_bus_locations():
    assert 1 == 1
