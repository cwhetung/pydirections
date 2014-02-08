from html_stripper import strip_tags

class DirectionStep(object):

    def __init__(self, step_data):
        self.distance = step_data['distance']
        self.duration = step_data['duration']
        self.instructions = strip_tags(step_data['html_instructions'])
        self.travel_mode = step_data['travel_mode']

