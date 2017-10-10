import pytz
from datetime import datetime


FORMAT_STRING = "%Y%m%d%H%M%S"


def get_timestamp(datatime_in = None):
	if datatime_in is None:
		datatime_in = datetime.now(pytz.timezone("America/New_York"))

	return int(datatime_in.strftime(FORMAT_STRING))

def get_datetime(timestamp):
	return datetime.strptime(str(timestamp), FORMAT_STRING)



if __name__ == "__main__":
	# get int from now()
	print(get_timestamp()) 

	# get int from passed in datetime
	print(get_timestamp(datetime(2017, 9, 8, 19, 23, 1)))

	# get datetime from int 
	print(get_datetime(20170909192233))   