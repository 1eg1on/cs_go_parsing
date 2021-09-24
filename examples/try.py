print(-1)
from csgo.parser import DemoParser
print(0)
demo_parser = DemoParser(demofile = '5346930_5102434.dem', demo_id = 'first_parsed' parse_rate = 128)
print(1)
data = demo_parser.parse()
print(type(data))