from flask import g
import pytest
import re
from ..src import create_app
from ..src.topstop import TopStopRequest


# Application context fixture
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('topstop_app.config.DevConfig')
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client


# TopStopRequest object fixture for comparisons
@pytest.fixture(scope='module')
def test_topstop_req():
    test_topstop_req = TopStopRequest(901)
    test_topstop_req.set_direction("Northbound")
    test_topstop_req.stop_name = "MAAM"
    return test_topstop_req


# Test home page route
def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"real-time MetroTransit bus and train departures" in response.data
    assert b"2021 - Target Case Study" in response.data


# Negative test posting to home page
def test_home_page_post(test_client, test_topstop_req):
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"real-time MetroTransit bus and train departures" not in response.data


# Test topstop page route and validate that the routes have been loaded
def test_topstop_page(test_client):
    response = test_client.get('/topstop/')
    assert response.status_code == 200
    assert b'<option value="902" >METRO Green Line</option>' in response.data


# Test if we correctly initiate a TopStopRequest object when calling for the
# directions of the route and put that request into the application context
# Also test that the results match our test request object
def test_get_direction(test_client, test_topstop_req):
    response = test_client.get('/route_directions/?route_id=' + str(test_topstop_req.route_id))
    assert response.status_code == 200
    assert g.topstop_req.direction == test_topstop_req.direction
    assert g.topstop_req.direction_id == test_topstop_req.direction_id


# Test if we correctly initiate a TopStopRequest object when calling for the
# stops of the route and put that request into the application context
# Also test that the results match our test request object
def test_get_stop(test_client, test_topstop_req):
    response = test_client.get('/get_stops/' + test_topstop_req.route + '/' + test_topstop_req.direction_id)
    assert response.status_code == 200
    assert g.topstop_req.stop_name == test_topstop_req.stop_name
    assert g.topstop_req.latitude == test_topstop_req.latitude
    assert g.topstop_req.longitude == test_topstop_req.longitude


# Test if we correctly initiate a TopStopRequest object when calling for the
# departures of the route and put that request into the application context
# Since the departures change due to the time of the request call, just test
# if we have good data in the departures array
def test_get_departures(test_client, test_topstop_req):
    response = test_client.get('/get_departures/' + test_topstop_req.route + '/' +
                               test_topstop_req.direction_id + '/' + test_topstop_req.stop_name)
    assert response.status_code == 200
    assert (re.search(r"\d+\d*:\d{2}", g.topstop_req[0]) or re.search(r"\d+ Min",
            g.topstop_req[0]) or re.search(r"Due", g.topstop_req[0]))
