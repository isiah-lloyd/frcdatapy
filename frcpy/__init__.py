import requests
import json
AUTH_TOKEN = 'Token communitysampletoken'
BASE_URL = 'http://private-1246e-frceventsprelimapitraffic.apiary-proxy.com/api/'
HEADERS = {'Accept': 'application/json', 'Authorization': AUTH_TOKEN}
###HELPER FUNCTIONS###
class APIerror(Exception):
	pass
def verifyYear(season):
	'''
	This class is to make sure the year is valid according the the API specs
	'''
	if(type(season) is int):
		if(len(str(season)) != 4):
			raise ValueError('Year must be four digits')
		if(season-2014 < 0):
			raise ValueError('Year must be greater than 2014')
	else:
		raise ValueError('Year must be an integer')
	return 1
def verifyTournamentLevel(tournamentLevel):
	if(type(tournamentLevel))
###API CLASSES###
def getTeamInfo(teamNumber,season):
	"""
	Request info of an indivdual team
	Input:
	teamNumber = the team number that you wish to return info on
	season = year of info you would like to return; must be valid (greater then 2014 and less then the current year)
	Returns:
	json encoded team info. See API docs for what it return
	"""
	verifyYear(season)
	payload = {'teamNumber': teamNumber}
	r = requests.get(BASE_URL+str(season)+"/teams", params=payload, headers=HEADERS)
	if(r.status_code != 200):
		r.raise_for_status()
	else:
		teamInfo = json.loads(r.text)
		if(teamInfo["teamCountTotal"] == 0):
			raise APIerror('No team found using that number')
		else:
			return teamInfo['teams'][0]
def getEventSchedule(eventCode, tournamentLevel, teamNumber=None):
	"""
	'The schedule API returns the match schedule for the desired tournament level of a particular event in a particular season.'
	Parameters: 
	eventCode: The event code for the event you wish to get the schedule for. EX: ILIL
	tournamentLevel: The type of schedule you want to return. Can be either 'qual' or 'elim'
	
	Returns:
	A python dictionary converted from the JSON.
	
	Example calls:
	getEventSchedule('ilil, 'qual')  #Without teamnumber
	getEventSchedule('ilil', 'qual', )
	"""
	if(type(eventCode) is str and type(tournamentLevel) is str):
		if teamNumber == None:
			payload = {}
		else:
			payload = {'teamNumber': teamNumber }
		r = requests.get(BASE_URL+"schedule/2014/" + eventCode + "/" + tournamentLevel, params=payload, headers=HEADERS)
		if(r.status_code != 200):
			r.raise_for_status()
		else:
			eventSchedule = json.loads(r.text)
			return eventSchedule
	else:
		raise ValueError('eventCode and/or tournamentLevel must be a string')
def getTeamMatchResults(season,eventCode,teamNumber, tournamentLevel='qual', start=None, end=None):
	payload = {}
	verifyYear(season)
	
	


