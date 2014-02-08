import json
from direction_step import DirectionStep
from directions import Directions

class DirectionResponseParser(object):
    
    @classmethod
    def parse(klass, response):
        parser = DirectionResponseParser(response)
        return parser._parse()

    def __init__(self, response):
        self.response = response
        self.directions = Directions()

    def _parse(self):
        if self.response_valid():
            #self.set_timeline()
            self.build_steps()
            return self.directions     
        else:
            return None

    def response_valid(self):
        return self.response.status == 200

    def set_timeline(self):
        json_dict = self.response_dict()
        arrival = json_dict['routes'][0]['legs'][0]['arrival_time']['text']
        departure = json_dict['routes'][0]['legs'][0]['departure_time']['text']
        self.directions.set_timeline(arrival, departure)   

    def build_steps(self): 
        json_dict = self.response_dict()
        steps = json_dict['routes'][0]['legs'][0]['steps']
        
        for step in steps:
            self.directions.add_step(DirectionStep(step))

    def response_dict(self):
        return json.loads(self.response.read())
