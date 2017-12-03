from collections import namedtuple
import json

# ScrapedData = namedtuple('ScrapedData', 'title code employment_2016 employment_2026 change_number change_percent anual_wage')
# s = ScrapedData(title='Management Occupations', code='11-0000', employment_2016='9,533.1', employment_2026='10,411.5', 
# 	change_number='878.3', change_percent='9.4', anual_wage='100,790')

class Occupation(object):
	# init
    def __init__(self, data):
    	# set our data constants
        self.title = data[0]# data.title
        self.code = data[1] # data.code
        self.employment_2016 = data[2] # data.employment_2016
        self.employment_2026 = data[3] # data.employment_2026
        self.change_number = data[4] # data.change_number
        self.change_percent = data[5] # data.change_percent
        self.anual_wage = data[6] # data.anual_wage
    # json data
    def jsonData(self):
    	# takes class properties into json format
    	json_data = {
    		self.title : [
    			{'code' : self.code },
    			{'employment' : [
    				{'employment_2016': self.employment_2016},
    				{'employment_2016': self.employment_2026}
    			]},
    			{'change_employment' : [
    				{'change_number' : self.change_number},
    				{'change_percentage': self.change_percent}
    			]},
    			{'anual_wage' : self.anual_wage}
    		]
    	}
    	# return json data
    	return json_data

# in order for out class to be a json object
def jsonDefault(object):
	return object.__dict__

# # class instance
# employee = Occupation(s)

# # write it in json file
# filename = "careers.json"
# f = open(filename, "w")
# jsonstuff = json.dumps(employee.jsonData(), indent=4, default=jsonDefault)
# f.write(jsonstuff)