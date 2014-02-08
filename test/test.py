from direction_query import DirectionQuery
from direction_response_parser import DirectionResponseParser
import httplib

params = {'origin': 'Toronto', 'destination': 'New York'}

resp = DirectionQuery.get_directions(params)

print resp.status
steps = DirectionResponseParser.parse(resp)

for step in steps:
    print step.instructions
