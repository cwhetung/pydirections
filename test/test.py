from direction_query import DirectionQuery
from direction_response_parser import DirectionResponseParser
from direction_printer import DirectionPrinter
import httplib

params = {'origin': '11 e 4th manhttan ny', 'destination': '694 metropolitan ave brooklyn ny'}

resp = DirectionQuery.get_directions(params)

steps = DirectionResponseParser.parse(resp)

DirectionPrinter.print_steps(steps)
