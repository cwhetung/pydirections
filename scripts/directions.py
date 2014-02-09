class Directions(object):

    def __init__(self):
        self.arrival_time = None
        self.departure_time = None
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def set_timeline(self, arrival, departure):
        self.arrival_time = arrival
        self.departure_time = departure
