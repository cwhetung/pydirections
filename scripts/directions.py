class Directions(object):

    def __init__(self):
        self.arrival_time = ""
        self.departure_time = ""
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def set_timeline(self, arrvial, departure):
        self.arrival_time = arrival
        self.departure = departure
