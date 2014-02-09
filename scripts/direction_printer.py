from pcolors import pcolors

class DirectionPrinter(object):

    @classmethod
    def print_steps(klass, directions):
        printer = DirectionPrinter(directions)
        printer._print_steps()

    def __init__(self, directions):
        self.steps = directions.steps
        self.arrival = directions.arrival_time
        self.departure = directions.departure_time

    def _print_steps(self):
        if self.arrival is not None and self.departure is not None:
            self.print_timeline()
        for step in self.steps:
            self.print_instruction(step.instructions)
            self.print_detail("\tdistance: ", step.distance)
            self.print_detail("\tduration: ", step.duration)
            self.print_detail("\ttravel_mode: ", step.travel_mode)

    def print_timeline(self):
        self.print_detail("depart at: ", self.departure)
        self.print_detail("arrive at: ", self.arrival)

    def print_instruction(self, instruction):
        print self.add_color("GREEN", instruction)

    def print_detail(self, detail_prompt, detail):
        color_prompt = self.add_color("PURPLE", detail_prompt)
        color_detail = self.add_color("ORANGE", detail)
        print "{0}{1}".format(color_prompt, color_detail)
        
    def add_color(self, color, string):
        return pcolors.COLOR_DICT[color] + string + pcolors.ENDC

