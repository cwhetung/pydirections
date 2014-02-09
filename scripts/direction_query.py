import httplib
import urllib
import time

class DirectionQuery(object):

    BASE_API_URL = "maps.googleapis.com"
    API_PATH = "/maps/api/directions/json"

    @classmethod
    def get_directions(klass, params):
        query = DirectionQuery(params)
        return query._get_directions()

    def __init__(self, params):
        self.params = self.params_with_defaults(params)
        self.conn = httplib.HTTPConnection(self.BASE_API_URL)

    def _get_directions(self):
        self.conn.request("GET", self.request_url())
        return self.conn.getresponse()

    def request_url(self):
        return "{0}?{1}".format(self.API_PATH, self.encoded_params())

    def encoded_params(self):
        return urllib.urlencode(self.params)
    
    def params_with_defaults(self, params):
        request_params = self.default_params()
        request_params.update(params)
        return request_params

    def default_params(self):
        return { "sensor": "false", "departure_time": int(time.time())}
