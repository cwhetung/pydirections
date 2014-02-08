import json
from direction_step import DirectionStep

class DirectionResponseParser(object):
    
    @classmethod
    def parse(klass, response):
        parser = DirectionResponseParser(response)
        return parser._parse()

    def __init__(self, response):
        self.response = response
        self.direction_steps = []

    def _parse(self):
        if self.response_valid():
            self.build_steps()
            return self.direction_steps     
        else:
            return None

    def response_valid(self):
        return self.response.status == 200

    def build_steps(self): 
        json_dict = self.response_dict()
        steps = json_dict['routes'][0]['legs'][0]['steps']
        
        for step in steps:
            self.direction_steps.append(DirectionStep(step))

    def response_dict(self):
        return json.loads(self.response.read())
