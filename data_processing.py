import json
from statistics import mean

# All data gathered and calculated are per game basis

def totalData(teamID, directory, xgoalFilesList, statsFilesList, eventsFilesList):

    if (len(xgoalFilesList) != len(statsFilesList)) or (len(statsFilesList) != len(eventsFilesList))\
        or (len(xgoalFilesList) != len(eventsFilesList)):

        message = "The number of files in 3 arrays are different: {xgoalFilesList: " + str(len(xgoalFilesList)) + \
            ", statsFilesList: " + str(len(statsFilesList)) + ", eventsFilesList: " + str(len(eventsFilesList)) + \
                "}!"

        return message
    
    else:

        # A dictionary to store the stats
        teamStats = {
            'Shots': 0,
            'Shots on target': 0,
            'Shots conceded': 0,
            'Goals scored': 0,
            'Non-penalty Goals': 0,
            'xG': 0,
            'npxG': 0,
            'Goals conceded': 0,
            'Non-penalty Goals conceded': 0,
            'xGA': 0,
            'npxGA': 0,
            'Possession %': 0,
            'Possession won': 0,
            'Possession won in opp. half': 0,
            'Possession lost': 0,
            'Possession lost in opp. half': 0,
            'Tackles attempted': 0,
            'Tackles won': 0,
            'Aerial duels attempted': 0,
            'Aerial duels won': 0,
            'Passes attempted': 0,
            'Passes completed': 0,
            'Key passes': 0,
            'Crosses attempted': 0,
            'Crosses completed': 0,
            'Dribbles attempted': 0,
            'Free kicks attempted': 0,
            'Free kicks attempted with shots': 0,
            'Corners attempted': 0,
            'Corners attempted with shots': 0
        }

        # Individual variables to store the data
        shots = 0
        shotsOnTarget = 0
        shotsConceded = 0
        goalsScored = 0
        nonpenaltyGoals = 0
        xG = 0
        npxG = 0
        goalsConceded = 0
        nonpenaltyGoalsConceded = 0
        xGA = 0
        npxGA = 0
        possessionPercentage = []
        possessionWon = 0
        possessionWonInOppHalf = 0
        possessionLost = 0
        possessionLostInOppHalf = 0
        tacklesAttempted = 0
        tacklesWon = 0
        aerialDuels = 0
        aerialDuelsWon = 0
        passesAttempted = 0
        passesCompleted = 0
        keyPasses = 0
        crossesAttempted = 0
        crossesCompleted = 0
        dribblesAttempted = 0
        freekicksAttempted = 0
        freekicksAttemptedWithShots = 0
        cornersAttempted = 0
        cornersAttemptedWithShots = 0

        # Go through all files in the lists of all xG files
        for xGoalFile in xgoalFilesList:

            # Open the file, ignore if the file does not exist
            try: 
                with open(directory + xGoalFile, encoding = 'utf-8') as jsonFile:
                    jsonXGoal = json.load(jsonFile)
                    jsonFile.close()
            except:
                continue

            # Check if the teamID matches the home team's ID or the away team's ID
            isHomeTeam = False
            matchInfo = jsonXGoal['matchInfo']
            contestant = matchInfo['contestant']
            # If clause to check if the team in question
            # is the home team or the away team
            if (contestant[0]['id'] == teamID): isHomeTeam = True
            
            # Access the stat section of the corresponding team
            liveData = jsonXGoal['liveData']

            if ('lineUp' not in liveData):

                events = liveData['event']

                for event in events:

                    if (event['typeId'] in [13, 14, 15, 16]):

                        if (event['contestantId'] == teamID):
                            shots = shots + 1
                            isOpenPlay = False

                            if (event['typeId'] == 16):
                                goalsScored = goalsScored + 1
                                shotsOnTarget = shotsOnTarget + 1
                                
                                for qualifier in event['qualifier']:
                                    if (qualifier['qualifierId'] in [22, 24]):
                                        nonpenaltyGoals = nonpenaltyGoals + 1
                                        isOpenPlay = True
                                        break

                            elif (event['typeId'] == 15):

                                isBlockedShot = False

                                for qualifier in event['qualifier']:
                                    if (qualifier['qualifierId'] == 82):
                                        isBlockedShot = True
                                        break

                                if (isBlockedShot == False):
                                    shotsOnTarget = shotsOnTarget + 1

                            for qualifier in event['qualifier']:

                                if (qualifier['qualifierId'] == 321):
                                    xG = xG + float(qualifier['value'])

                                    if (isOpenPlay == True):
                                        npxG = npxG + float(qualifier['value'])

                        else:

                            shotsConceded = shotsConceded + 1
                            isOpenPlay = False

                            if (event['typeId'] == 16):
                                goalsConceded = goalsConceded + 1
                                
                                for qualifier in event['qualifier']:
                                    if (qualifier['qualifierId'] in [22, 24]):
                                        nonpenaltyGoalsConceded = nonpenaltyGoalsConceded + 1
                                        isOpenPlay = True
                                        break

                            for qualifier in event['qualifier']:

                                if (qualifier['qualifierId'] == 321):
                                    xGA = xGA + float(qualifier['value'])

                                    if (isOpenPlay == True):
                                        npxGA = npxGA + float(qualifier['value'])

            else:

                lineUp = liveData['lineUp']
                # If the team in question is the home team
                # then access the first stat section.
                # If the team in question is the away team
                # then access the second stat section.
                if (isHomeTeam == True): 
                    stat = lineUp[0]['stat']
                    oppositionStat = lineUp[1]['stat']
                else: 
                    stat = lineUp[1]['stat']
                    oppositionStat = lineUp[0]['stat']

                for i in range(len(stat)):

                    if (stat[i]['type'] == 'totalScoringAtt'):
                        shots = shots + int(stat[i]['value'])
                    elif (stat[i]['type'] == "ontargetScoringAtt"):
                        shotsOnTarget = shotsOnTarget + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'goals'):
                        goalsScored = goalsScored + int(stat[i]['value'])
                    elif (stat[i]['type'] == "goalsOpenplay"):
                        nonpenaltyGoals = nonpenaltyGoals + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'expectedGoals'):
                        xG = xG + float(stat[i]['value'])
                    elif (stat[i]['type'] == "expectedGoalsNonpenalty"):
                        npxG = npxG + float(stat[i]['value'])
                    elif (stat[i]['type'] == 'expectedGoalsConceded'):
                        xGA = xGA + float(stat[i]['value'])
                    elif (stat[i]['type'] == "expectedGoalsNonpenaltyConceded"):
                        npxGA = npxGA + float(stat[i]['value'])

                for i in range(len(oppositionStat)):
                    
                    if (oppositionStat[i]['type'] == 'totalScoringAtt'):
                        shotsConceded = shotsConceded + int(oppositionStat[i]['value'])
                    elif (oppositionStat[i]['type'] == 'goals'):
                        goalsConceded = goalsConceded + int(oppositionStat[i]['value'])
                    elif (oppositionStat[i]['type'] == "goalsOpenplay"):
                        nonpenaltyGoalsConceded = nonpenaltyGoalsConceded + int(oppositionStat[i]['value'])

        teamStats['Shots'] = round(shots / len(xgoalFilesList), 2)
        # teamStats['Shots'] = shots
        teamStats['Shots on target'] = round(shotsOnTarget / len(xgoalFilesList), 2)
        # teamStats['Shots on target'] = shotsOnTarget
        teamStats['Shots conceded'] = round(shotsConceded / len(xgoalFilesList), 2)
        # teamStats['Shots conceded'] = shotsConceded
        teamStats['Goals scored'] = round(goalsScored / len(xgoalFilesList), 2)
        # teamStats['Goals scored'] = goalsScored
        teamStats['Non-penalty Goals'] = round(nonpenaltyGoals / len(xgoalFilesList), 2)
        # teamStats['Non-penalty Goals'] = nonpenaltyGoals
        teamStats['xG'] = round(xG / len(xgoalFilesList), 2)
        # teamStats['xG'] = xG
        teamStats['npxG'] = round(npxG / len(xgoalFilesList), 2)
        # teamStats['npxG'] = npxG
        teamStats['Goals conceded'] = round(goalsConceded / len(xgoalFilesList), 2)
        # teamStats['Goals conceded'] = goalsConceded
        teamStats['Non-penalty Goals conceded'] = round(nonpenaltyGoalsConceded / len(xgoalFilesList), 2)
        # teamStats['Non-penalty Goals conceded'] = nonpenaltyGoalsConceded
        teamStats['xGA'] = round(xGA / len(xgoalFilesList), 2)
        # teamStats['xGA'] = xGA
        teamStats['npxGA'] = round(npxGA / len(xgoalFilesList), 2)
        # teamStats['npxGA'] = npxGA

        for statsFile in statsFilesList:

            # Open the file, ignore if the file does not exist
            try:
                with open(directory + statsFile, encoding = 'utf-8') as jsonFile:
                    jsonStats = json.load(jsonFile)
                    jsonFile.close()
            except:
                continue

            # Check if the teamID matches the home team's ID or the away team's ID
            isHomeTeam = False
            matchInfo = jsonStats['matchInfo']
            matchRound = matchInfo['week']
            contestant = matchInfo['contestant']
            # If clause to check if the team in question
            # is the home team or the away team
            if (contestant[0]['id'] == teamID): isHomeTeam = True
            
            # Access the stat section of the corresponding team
            liveData = jsonStats['liveData']

            if ('lineUp' not in liveData):
                
                homeTeam = contestant[0]['code']
                awayTeam = contestant[1]['code']
                eventFile = matchRound + '_' + homeTeam + '_' + awayTeam + '_events.json'

                try:
                    with open(directory + eventFile, encoding = 'utf-8') as jsonFile:
                        jsonEvents = json.load(jsonFile)
                        jsonFile.close()
                except:
                    continue

                liveData = jsonEvents['liveData']
                events = liveData['event']

                passesAttemptedFromMatch = 0
                oppPassesAttempted = 0

                for event in events:

                    if ("contestantId" in event) and (event['contestantId'] == teamID):

                        if (event['typeId'] == 1):

                            isqualifier = False

                            for qualifier in event['qualifier']:

                                if (qualifier['qualifierId'] in [2, 5, 6, 107, 123, 124]):
                                        
                                    if (qualifier['qualifierId'] == 5):
                                        freekicksAttempted = freekicksAttempted + 1
                                    elif (qualifier['qualifierId'] == 6):
                                        cornersAttempted = cornersAttempted + 1

                                    isqualifier = True
                                    break

                            if (isqualifier == False):
                                passesAttempted = passesAttempted + 1
                                passesAttemptedFromMatch = passesAttemptedFromMatch + 1

                                if (event['outcome'] == 1):
                                    passesCompleted = passesCompleted + 1

                        elif (event['typeId'] in [7, 45]):
                            tacklesAttempted = tacklesAttempted + 1

                            if (event['typeId'] == 7):
                                tacklesWon = tacklesWon + 1

                    else:

                        if (event['typeId'] == 1):

                            isqualifier = False

                            for qualifier in event['qualifier']:

                                if (qualifier['qualifierId'] in [2, 5, 6, 107, 123, 124]):

                                    isqualifier = True
                                    break

                            if (isqualifier == False):
                                oppPassesAttempted = oppPassesAttempted + 1

                possessionPercentage.append(
                    round(passesAttemptedFromMatch / (passesAttemptedFromMatch + oppPassesAttempted) * 100, 1))

            else:

                lineUp = liveData['lineUp']
                # If the team in question is the home team
                # then access the first stat section.
                # If the team in question is the away team
                # then access the second stat section.
                if (isHomeTeam == True): stat = lineUp[0]['stat']
                else: stat = lineUp[1]['stat']

                for i in range(len(stat)):

                    if (stat[i]['type'] == 'possessionPercentage'):
                        possessionPercentage.append(float(stat[i]['value']))
                    elif (stat[i]['type'] == 'totalTackle'):
                        tacklesAttempted = tacklesAttempted + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'wonTackle'):
                        tacklesWon = tacklesWon + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'totalPass'):
                        passesAttempted = passesAttempted + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'accuratePass'):
                        passesCompleted = passesCompleted + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'fkFoulWon'):
                        freekicksAttempted = freekicksAttempted + int(stat[i]['value'])
                    elif (stat[i]['type'] == 'cornerTaken'):
                        cornersAttempted = cornersAttempted + int(stat[i]['value'])

        teamStats['Possession %'] = round(mean(possessionPercentage), 1)
        teamStats['Tackles attempted'] = round(tacklesAttempted / len(statsFilesList), 2)
        # teamStats['Tackles attempted'] = tacklesAttempted
        teamStats['Tackles won'] = round(tacklesWon / len(statsFilesList), 2)
        # teamStats['Tackles won'] = tacklesWon
        teamStats['Passes attempted'] = round(passesAttempted / len(statsFilesList), 2)
        # teamStats['Passes attempted'] = passesAttempted
        teamStats['Passes completed'] = round(passesCompleted / len(statsFilesList), 2)
        # teamStats['Passes completed'] = passesCompleted
        teamStats['Free kicks attempted'] = round(freekicksAttempted / len(statsFilesList), 2)
        # teamStats['Free kicks attempted'] = freekicksAttempted
        teamStats['Corners attempted'] = round(cornersAttempted / len(statsFilesList), 2)
        # teamStats['Corners attempted'] = cornersAttempted

        for eventsFile in eventsFilesList:

            try:
                with open(directory + eventsFile, encoding = 'utf-8') as jsonFile:
                    jsonEvents = json.load(jsonFile)
                    jsonFile.close()
            except:
                continue

            liveData = jsonEvents['liveData']
            events = liveData['event']

            for event in events:

                if ("contestantId" in event) and (event['contestantId'] == teamID):

                    if ( (event['typeId'] == 7) and (event['outcome'] == 1) ) or \
                        (event['typeId'] in [8, 49, 74]) or ( (event['typeId'] == 44) and (event['outcome'] == 1) ):

                            possessionWon = possessionWon + 1

                            if (event['x'] >= 49.9):
                                possessionWonInOppHalf = possessionWonInOppHalf + 1

                    if ( (event['typeId'] == 9) and (event['outcome'] == 0) ) \
                        or (event['typeId'] in [50, 51, 61]):

                        possessionLost = possessionLost + 1

                        if (event['x'] >= 49.9):
                            possessionLostInOppHalf = possessionLostInOppHalf + 1

                    if (event['typeId'] == 44):
                        aerialDuels = aerialDuels + 1

                        if (event['outcome'] == 1):
                            aerialDuelsWon = aerialDuelsWon + 1

                    if (event['typeId'] == 1) and ("keyPass" in event) and (event['keyPass'] == 1):
                        keyPasses = keyPasses + 1
                    
                    if (event['typeId'] == 1):

                        isCross = False
                        
                        for qualifier in event['qualifier']:
                            
                            if (qualifier['qualifierId'] == 5) or (qualifier['qualifierId'] == 6):
                                break
                            else:
                                if (qualifier['qualifierId'] == 2):
                                    isCross = True
                                    break

                        if (isCross == True):
                            crossesAttempted = crossesAttempted + 1

                            if (event['outcome'] == 1):
                                crossesCompleted = crossesCompleted + 1

                    if (event['typeId'] == 3):
                        dribblesAttempted = dribblesAttempted + 1

            for i in range(len(events)):

                isFK = False
                isCorner = False
                hasShot = False

                if (events[i]['typeId'] == 1):

                    for qualifier in events[i]['qualifier']:
                        if (qualifier['qualifierId'] == 5):
                            isFK = True
                            break
                        elif (qualifier['qualifierId'] == 6):
                            isCorner = True
                            break
                    
                    if (i != (len(events) - 2)):

                        if (events[i + 1]['typeId'] == 13) or (events[i + 1]['typeId'] == 14) \
                            or (events[i + 1]['typeId'] == 15) or (events[i + 1]['typeId'] == 16):
                            hasShot = True
                        elif (events[i + 2]['typeId'] == 13) or (events[i + 2]['typeId'] == 14) \
                            or (events[i + 2]['typeId'] == 15) or (events[i + 2]['typeId'] == 16):
                            hasShot = True

                    elif (i == (len(events) - 2)):

                        if (events[i + 1]['typeId'] == 13) or (events[i + 1]['typeId'] == 14) \
                            or (events[i + 1]['typeId'] == 15) or (events[i + 1]['typeId'] == 16):
                            hasShot = True

                if (isFK == True) and (hasShot == True):
                    freekicksAttemptedWithShots = freekicksAttemptedWithShots + 1
                elif (isCorner == True) and (hasShot == True):
                    cornersAttemptedWithShots = cornersAttemptedWithShots + 1
                    
        teamStats['Possession won'] = round(possessionWon / len(eventsFilesList), 2)
        # teamStats['Possession won'] = possessionWon
        teamStats['Possession won in opp. half'] = round(possessionWonInOppHalf / len(eventsFilesList), 2)
        # teamStats['Possession won in opp. half'] = possessionWonInOppHalf
        teamStats['Possession lost'] = round(possessionLost / len(eventsFilesList), 2)
        # teamStats['Possession lost'] = possessionLost
        teamStats['Possession lost in opp. half'] = round(possessionLostInOppHalf / len(eventsFilesList), 2)
        # teamStats['Possession lost in opp. half'] = possessionLostInOppHalf
        teamStats['Aerial duels attempted'] = round(aerialDuels / len(eventsFilesList), 2)
        # teamStats['Aerial duels attempted'] = aerialDuels
        teamStats['Aerial duels won'] = round(aerialDuelsWon / len(eventsFilesList), 2)
        # teamStats['Aerial duels won'] = aerialDuelsWon
        teamStats['Key passes'] = round(keyPasses / len(eventsFilesList), 2)
        # teamStats['Key passes'] = keyPasses
        teamStats['Crosses attempted'] = round(crossesAttempted / len(eventsFilesList), 2)
        # teamStats['Crosses attempted'] = crossesAttempted
        teamStats['Crosses completed'] = round(crossesCompleted / len(eventsFilesList), 2)
        # teamStats['Crosses completed'] = crossesCompleted
        teamStats['Dribbles attempted'] = round(dribblesAttempted / len(eventsFilesList), 2)
        # teamStats['Dribbles attempted'] = dribblesAttempted
        teamStats['Free kicks attempted with shots'] = round(freekicksAttemptedWithShots / len(eventsFilesList), 2)
        # teamStats['Free kicks attempted with shots'] = freekicksAttemptedWithShots
        teamStats['Corners attempted with shots'] = round(cornersAttemptedWithShots / len(eventsFilesList), 2)
        # teamStats['Corners attempted with shots'] = cornersAttemptedWithShots

        return teamStats