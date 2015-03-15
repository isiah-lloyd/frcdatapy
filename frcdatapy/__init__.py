import requests
###HELPER FUNCTIONS###
def verify_year(season):
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
def verify_tournament_level(tournamentLevel):
    if(type(tournamentLevel) is str):
        if (tournamentLevel == 'qual' or tournamentLevel == 'playoff'):
            return 1
        else:
            raise ValueError('tournamentLevel must either be "qual" or "playoff"')
    else:
        raise ValueError('tournamentLevel must be a string')
###API CLASSES###
def get_ancillary():
    """
    Returns basic info about the API. 
    """
    r = requests.get(BASE_URL, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        Ancillary = r.json()
        return Ancillary
def get_event_alliances(season, eventCode):
    verify_year(season)
    if(len(eventCode) >= 3):
        r = requests.get(BASE_URL+'alliances/'+str(season)+'/'+eventCode, headers=HEADERS, auth=AUTH)
        if(r.status_code != 200):
            r.raise_for_status()
        else:
            event_alliances = r.json()
            return event_alliances
def get_team_listings(season, teamNumber=None, eventCode=None, districtCode=None, page=None):
    if(teamNumber != None and eventCode != None):
        raise ValueError('You can\'t supply both a teamnumber and an eventCode')
    if(teamNumber != None and districtCode != None):
        raise ValueError('You can\'t supply both a teamnumber and an districtCode')
    verify_year(season)
    payload = {}
    if (teamNumber != None):
        payload['teamNumber'] = teamNumber
    if (eventCode != None):
        payload['eventCode'] = eventCode
    if (districtCode != None):
        payload['districtCode'] = districtCode
    if (page != None):
        payload['page'] = page
    r = requests.get(BASE_URL+"teams/"+str(season), params=payload, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        teamListings = r.json()
        return teamListings
def get_event_schedule(season, eventCode, tournamentLevel, teamNumber=None, start= None, end=None):
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
    verify_year(season)
    verify_tournament_level(tournamentLevel)
    payload = {}
    payload['tournamentLevel'] = tournamentLevel
    if (teamNumber != None):
        payload['teamNumber'] = teamNumber
    if (start != None):
        payload['start'] = start
    if (end != None):
        payload['end'] = end
    r = requests.get(BASE_URL+"schedule/"+str(season)+"/"+eventCode+"/", params=payload, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        eventSchedule = r.json()
        return eventSchedule
def get_hybrid_event_schedule(season, eventCode, tournamentLevel, start=None, end=None):
    verify_year(season)
    verify_tournament_level(tournamentLevel)
    payload = {}
    if (start != None):
        payload['start'] = start
    if (end != None):
        payload['end'] =end
    r = requests.get(BASE_URL+"schedule/"+str(season)+"/"+eventCode+"/" + tournamentLevel + "/hybrid", params=payload, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        eventHybridSchedule = r.json()
        return eventHybridSchedule

def get_event_match_results(season,eventCode,teamNumber = None, tournamentLevel=None, matchNumber=None, start=None, end=None):
    payload = {}
    verify_year(season)
    if(tournamentLevel is not None):
        verify_tournament_level(tournamentLevel)
    if(matchNumber != None or start != None or end != None):
        if(tournamentLevel == None):
            raise ValueError('If you supply a matchNumber, start, or end parameter then you must supply a tournamentLevel')
    if(teamNumber != None and matchNumber != None):
        raise ValueError('You can not supply both a teamNumber and a matchNumber')
    if(matchNumber != None and start != None):
        raise ValueError("You can't specify both a matchNumber and start")
    if(matchNumber != None and end != None):
        raise ValueError("You can't specify both a matchNumber and end")
    if(teamNumber != None):
        payload['teamNumber'] = teamNumber
    if(tournamentLevel != None):
        payload['tournamentLevel'] = tournamentLevel
    if(matchNumber != None):
        payload['matchNumber'] = matchNumber
    if(start != None):
        payload['start'] = start
    if(end != None):
        payload['end'] = end
    r = requests.get(BASE_URL+"matches/"+str(season)+ "/"+eventCode, params=payload, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        matchResults = r.json()
        return matchResults
def get_season_summary(season):
    verify_year(season)
    r = requests.get(BASE_URL+str(season), headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        seasonSummary = r.json()
    return seasonSummary
def get_event_listings(season, eventCode=None, teamNumber=None, districtCode=None, excludeDistrict=False):
    verify_year(season)
    if(eventCode != None):
        if(districtCode != None or excludeDistrict != False):
            raise ValueError('You cannot name an eventCode and another optional parameter')
        else:
            payload = {'eventCode': eventCode}
            r = requests.get(BASE_URL+str(season)+"/events", params=payload, headers=HEADERS, auth=AUTH)
            event_listings = r.json()
            return event_listings
    if(excludeDistrict == True):
        if(districtCode != None):
            raise ValueError('You cannot exclude districts but also define a districtCode')
        r = requests.get(BASE_URL+str(season)+"/events?excludeDistrict=true", headers=HEADERS)
        event_listings = r.json()
        return event_listings
    if(districtCode != None):
        r = requests.get(BASE_URL+str(season)+"/events?districtCode="+str(districtCode), headers=HEADERS, auth=AUTH)
        event_listings = r.json()
        return event_listings
    else:
        r = requests.get(BASE_URL+str(season)+"/events", headers=HEADERS, auth=AUTH)
        event_listings = r.json()
        return event_listings
def get_event_rankings(season, eventCode, teamNumber=None, top=None):
    verify_year(season)
    payload = {}
    if(teamNumber != None):
        payload['teamNumber'] = teamNumber
    if(top != None):
        payload['top'] = top
    if(teamNumber != None and top != None):
        raise ValueError("You cant supply both a teamNumber and a top parameter")
    r = requests.get(BASE_URL+'rankings/'+str(season)+'/'+eventCode, params=payload, headers=HEADERS, auth=AUTH)    
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        event_rankings = r.json()
        return event_rankings
def get_event_awards(season, eventCode=None, teamNumber=None):
    verify_year(season)
    payload = {}
    if (teamNumber == None and eventCode == None):
        raise ValueError('You need to specify either a teamNumber or eventCode')
    if(teamNumber != None):
        payload['teamNumber'] = teamNumber
    if (eventCode != None):
        payload['eventCode'] = eventCode
    r = requests.get(BASE_URL+"awards/"+str(season)+"/", params=payload, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        print r.url
        r.raise_for_status()
    else:
        eventAwards = r.json()
        return eventAwards
def get_award_listings(season):
    r = requests.get(BASE_URL+"awards/" + str(season) +"/list", headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        print r.url
        r.raise_for_status()
    else:
        awardsList = r.json()
        return awardsList
def get_district_listings(season):
    verify_year(season)
    r = requests.get(BASE_URL+str(season)+"/districts", headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        districtListings = r.json()
    return districtListings 

def set_up(baseUrl, username=None, authToken=None):
    global BASE_URL
    global HEADERS
    global AUTH
    if(username != None and authToken != None):
        BASE_URL = baseUrl
        HEADERS = {'Accept': 'application/json', 'Authorization': authToken}
        AUTH = (username, authToken)
    elif(username == None and authToken ==  None):
        BASE_URL = baseUrl
        HEADERS = {'Accept': 'application/json'}
        AUTH = ()
    else:
        raise ValueError("Your set_up request was malformed. It either need both a username and authToken or none of those (if working on the mock server)")
