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
            raise ValueError('tournamentLevel must either be "qual" or "elim"')
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
def get_team_info(teamNumber,season):
    """
    Request info of an individual team
    Input:
    teamNumber = the team number that you wish to return info on
    season = year of info you would like to return; must be valid (greater then 2014 and less then the current year)
    Returns:
    json encoded team info. See API docs for what it return
    """
    verify_year(season)
    payload = {'teamNumber': teamNumber}
    r = requests.get(BASE_URL+str(season)+"/teams", params=payload, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        teamInfo = r.json()
        if(teamInfo["teamCountTotal"] == 0):
            raise APIerror('No team found using that number')
        else:
            return teamInfo['teams'][0]
def get_event_schedule(eventCode, tournamentLevel, teamNumber=None):
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
        r = requests.get(BASE_URL+"schedule"+str(season)+eventCode+"/"+tournamentLevel, params=payload, headers=HEADERS, auth=AUTH)
        if(r.status_code != 200):
            r.raise_for_status()
        else:
            eventSchedule = r.json()
            return eventSchedule
    else:
        raise ValueError('eventCode and/or tournamentLevel must be a string')
def get_event_match_results(season,eventCode,teamNumber = None, tournamentLevel=None, matchNumber=None, start=None, end=None):
    payload = {}
    verify_year(season)
    if(tournamentLevel is not None):
        verify_tournament_level(tournamentLevel)
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
    r = requests.get(BASE_URL+"/matches/"+str(season)+ "/"+eventCode, params=payload, headers=HEADERS, auth=AUTH)
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
def get_event_listings(season, eventCode=None, districtCode=None, excludeDistrict=False):
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
def get_event_rankings(season, eventCode, top=None):
    verify_year(season)
    if (len(eventCode) >= 3):
        if(top != None):
            payload = {'top': top}
            r = requests.get(BASE_URL+'rankings/'+str(season)+'/'+eventCode, params=payload, headers=HEADERS, auth=AUTH)
        else:
            r = requests.get(BASE_URL+'rankings/'+str(season)+'/'+eventCode, headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        event_rankings = r.json()
        return event_rankings
def get_event_awards(season, eventCode, teamNumber=None):
    verify_year(season)
    if(teamNumber != None):
        payload = {'teamNumber': teamNumber}
        r = requests.get(BASE_URL+"/awards/"+str(season)+"/"+str(eventCode), params=payload, headers=HEADERS, auth=AUTH)
    else:
        r =requests.get(BASE_URL+"/awards/"+str(season)+"/"+str(eventCode), headers=HEADERS, auth=AUTH)
    if(r.status_code != 200):
        r.raise_for_status()
    else:
        eventAwards = r.json()
    return eventAwards 


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
