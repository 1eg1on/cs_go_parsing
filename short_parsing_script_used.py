# all the instructions of setting up are here:
# https://github.com/pnxenopoulos/csgo/blob/master/examples/00_Parsing_a_CSGO_Demofile.ipynb
# this is a python wrapper for the Golang parser used by HLTV.org <1eg10n>



from csgo.parser import DemoParser
import json
# the names of the demos in the directory:

# 5346456_5101929.dem
# 5346930_5102434.dem
# 5348528_5104153.dem



demo_parser = DemoParser(demofile = 'demo_files/5346930_5102434.dem', demo_id = 'first_parsed', parse_rate = 128)
data = demo_parser.parse()
#with open("demo_1", "w") as fp:
#    json.dump(data , fp) 


demo_parser = DemoParser(demofile = 'demo_files/5346456_5101929.dem', demo_id = 'second_parsed', parse_rate = 128)
data = demo_parser.parse()
#with open("demo_2", "w") as fp:
#    json.dump(data , fp)


demo_parser = DemoParser(demofile = 'demo_files/5348528_5104153.dem', demo_id = 'third_parsed', parse_rate = 128)
data = demo_parser.parse()
#with open("demo_3", "w") as fp:
#    json.dump(data , fp)




