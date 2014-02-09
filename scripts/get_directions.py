import yaml
import sys 
from os.path import expanduser

from direction_query import DirectionQuery
from direction_response_parser import DirectionResponseParser
from direction_printer import DirectionPrinter


home = expanduser("~")
f = open(home + '/.pydirections.yml')
# use safe_load instead load
dataMap = yaml.safe_load(f)
f.close()

params = dataMap[sys.argv[1]]

resp = DirectionQuery.get_directions(params)

steps = DirectionResponseParser.parse(resp)

DirectionPrinter.print_steps(steps)

