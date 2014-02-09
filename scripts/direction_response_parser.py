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
        self.json_dict = json.loads(response.read())
        self.directions = Directions()

    def _parse(self):
        if self.response_valid():
            self.set_timeline()
            self.build_steps()
            return self.directions     
        else:
            return None

    def response_valid(self):
        return self.response.status == 200

    def set_timeline(self):
        route = self.json_dict['routes'][0]['legs'][0]
        if 'arrival_time' in route.keys() and 'departure_time' in route.keys():
            arrival = route['arrival_time']['text']
            departure = route['departure_time']['text']
            self.directions.set_timeline(arrival, departure)   

    def build_steps(self): 
        steps = self.json_dict['routes'][0]['legs'][0]['steps']
        
        for step in steps:
            self.directions.add_step(DirectionStep(step))
