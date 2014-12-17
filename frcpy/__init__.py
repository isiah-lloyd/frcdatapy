import requests
import ConfigParser
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
	if(type(tournamentLevel) is str):
		if (tournamentLevel == 'qual' or tournamentLevel == 'elim'):
			return 1
		else:
			raise ValueError('tournamentLevel must either be "qual" or "elim"')
	else:
		raise ValueError('tournamentLevel must be a string')
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
		teamInfo = r.json()
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
	
	if(type(eventCode) is str):
		if teamNumber == None:
			payload = {}
		else:
			payload = {'teamNumber': teamNumber }
		r = requests.get(BASE_URL+"schedule"+str(season) + eventCode + "/" + tournamentLevel, params=payload, headers=HEADERS)
		if(r.status_code != 200):
			r.raise_for_status()
		else:
			eventSchedule = r.json()
			return eventSchedule
	else:
		raise ValueError('eventCode and/or tournamentLevel must be a string')
def getMatchResults(season,eventCode,teamNumber = None, tournamentLevel=None, matchNumber=None, start=None, end=None):
	payload = {}
	verifyYear(season)
	if(tournamentLevel is not None):
		verifyTournamentLevel(tournamentLevel)
	if(matchNumber != None or start != None or end != None):
		if(tournamentLevel == None):
			raise ValueError('If you supply a matchNumber, start, or end parameter then you must supply a tournamentLevel')
	if(teamNumber is not None and matchNumber is not None):
		raise ValueError('You can not supply both a teamNumber and a matchNumber')
	if(teamNumber is not None):
		payload['teamNumber'] = teamNumber
	if(tournamentLevel is not None):
		payload['tournamentLevel'] = tournamentLevel
	if(matchNumber is not None):
		payload['matchNumber'] = matchNumber
	if(start is not None):
		payload['start'] = start
	if(end is not None):
		payload['end'] = end
	r = requests.get(BASE_URL+"/matches/"+str(season)+ "/"+eventCode, params=payload, headers=HEADERS)
	if(r.status_code != 200):
		r.raise_for_status()
	else:
		matchResults = r.json()
		return matchResults
	
def setUp(authToken, baseUrl):
	global AUTH_TOKEN
	global BASE_URL
	global HEADERS
	AUTH_TOKEN = authToken
	BASE_URL = baseUrl
	HEADERS = {'Accept': 'application/json', 'Authorization': AUTH_TOKEN}


		
	
	


