import pytest
import requests



@pytest.fixture
def api_url():
    url = "https://"+"regions-test.2gis.com/1.0/regions"
    return url



@pytest.fixture
def request_to_api_get_params(api_url):
    def f(params):
        resp = requests.get(api_url, params=params)
        print(resp.url)
        # print(resp.json()["items"])
        return resp
    return f
