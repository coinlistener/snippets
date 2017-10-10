import tweepy

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'zlm1nd1niJfJuwPU1rhAeB6Bb'
CONSUMER_SECRET = 'MR7yPaIA3YhLeZ93706pfvQC7P97I3iFfo0Ss2yTbD6UIo991F' 
ACCESS_KEY = '904022760040660992-bpxV6iW1Cjj6c1xpmJoeJCpPvvQAvfQ'
ACCESS_SECRET = 'qWQ134O0VFdp5QG8dGOBvVgPWo5eojPMisR1WRPfI7CJs'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status('So soothing, sooo soooothingg....')