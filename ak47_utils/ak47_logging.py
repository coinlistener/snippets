import tweepy
import os.path
import inspect

from datetime import datetime
from pytz import timezone
import pytz

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'zlm1nd1niJfJuwPU1rhAeB6Bb'
CONSUMER_SECRET = 'MR7yPaIA3YhLeZ93706pfvQC7P97I3iFfo0Ss2yTbD6UIo991F' 
ACCESS_KEY = '904022760040660992-bpxV6iW1Cjj6c1xpmJoeJCpPvvQAvfQ'
ACCESS_SECRET = 'qWQ134O0VFdp5QG8dGOBvVgPWo5eojPMisR1WRPfI7CJs'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# api.update_status('So soothing, sooo soooothingg....')


class Logging(object):

	def __init__(self):
		self.is_debug = False

	def set_debug(self,debug = True):
		self.is_debug = debug

	def _print_line(self, level, msg):
		tz = pytz.timezone('America/New_York')
		timestr = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

		callerframerecord = inspect.stack()[2]
  		frame = callerframerecord[0]
  		info = inspect.getframeinfo(frame)  		
		fname = info.filename
  		lineno = info.lineno

  		all_msg = timestr+': '+level+': '+fname+': '+str(lineno)+': '+str(msg)

		print(all_msg)
		if level == "ERROR":
			try:
				api.update_status(all_msg[:140])
			except:
				pass

	def error(self,msg):
		self._print_line("ERROR",msg)

	def info(self,msg):
		self._print_line("INFO",msg)

	def debug(self,msg):
		if self.is_debug:
			self._print_line("DEBUG",msg)		

ak47_logger = Logging()

if __name__ == "__main__":

    a=5
    try:
    	a['a'] = 5
    except Exception as e:
    	ak47_logger.error(str(e))

    ak47_logger.debug('should not log')
    ak47_logger.set_debug(True)
    ak47_logger.debug('should log')    