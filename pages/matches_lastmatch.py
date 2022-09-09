import streamlit as st  # Main library to create the web app
import json  # Use json files
import pandas as pd  # Create DataFrames to store data
import matplotlib as mpl  # Increase quality of the visualisation
import matplotlib.pyplot as plt  # Draw the xG timeline
import matplotlib.patches as patches  # A part of the timeline
import matplotlib.font_manager as fm  # Import fonts
# Draw pitches for the shot map
from mplsoccer import Pitch
from datetime import date, datetime
import warnings
mpl.rcParams['figure.dpi'] = 300


def app():

    warnings.filterwarnings('ignore')

    # Page setup

    # Page title
    st.title("Matches - Previous matches")

    fixtures = pd.read_csv("Fixtures.csv", delimiter = ';')
    teamIDs = pd.read_csv("Opta team IDs.csv", delimiter = ';')
    dataAvailable = []

    for i in range(len(fixtures)):
        availableMatch = ""
        if (fixtures["Data availability"][i] == "Y"):
            availableMatch = "Round " + str(fixtures["Round"][i]) + " - " + fixtures["Team"][i] + " (" + \
                            fixtures["Home/Away"][i] + ")"
            dataAvailable.append(availableMatch)

    matchOption = st.selectbox(
        label = 'Available matches with data',
        options = dataAvailable,
        index = 0
    )

    # Radio buttons to choose which visualisation to display
    vizOption = st.radio(
        label='Visualisation on display',
        options=('xG timeline', 'Shot map', "Home team's passing network",
                 "Away team's passing network"),
        index=0
    )

    home_team = ''
    away_team = ''

    if ('Brisbane City' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'BCT'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'BCT'
    elif ('Brisbane Roar Youth' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'BRR'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'BRR'
    elif ('Capalaba' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'CAP'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'CAP'
    elif ('Eastern Suburbs' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'EAS'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'EAS'
    elif ('Gold Coast Knights' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'GCK'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'GCK'
    elif ('Gold Coast United' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'GCU'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'GCU'
    elif ('Lions' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'LIO'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'LIO'
    elif ('Logan Lightning' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'LIG'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'LIG'
    elif ('Moreton Bay United' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'MBJ'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'MBJ'
    elif ('Peninsula Power' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'PEN'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'PEN'
    elif ('Sunshine Coast Wanderers' in matchOption):
        if ('Home' in matchOption):
            home_team = 'BOL'
            away_team = 'SCW'
        elif ('Away' in matchOption):
            away_team = 'BOL'
            home_team = 'SCW'

    directory = 'Opta stats/2022 data/'

    if ('SF' in matchOption):

        xgoalFile = home_team + '_' + away_team + '_SF_xgoal_stats.json'
        passNetworkFile = home_team + '_' + away_team + '_SF_pass_matrix.json'
        eventsFile = home_team + '_' + away_team + '_SF_events.json'

    elif ('GF' in matchOption):

        xgoalFile = home_team + '_' + away_team + '_GF_xgoal_stats.json'
        passNetworkFile = home_team + '_' + away_team + '_GF_pass_matrix.json'
        eventsFile = home_team + '_' + away_team + '_GF_events.json'

    else:

        xgoalFile = home_team + '_' + away_team + '_xgoal_stats.json'
        passNetworkFile = home_team + '_' + away_team + '_pass_matrix.json'
        eventsFile = home_team + '_' + away_team + '_events.json'

    # Import the fonts from the same folder as this code
    robotoRegular = fm.FontProperties(fname='./Roboto-Regular_0.ttf')
    robotoBold = fm.FontProperties(fname='./Roboto-Bold_0.ttf')

    # Data processing:
    #
    # Goals:
    # -Create a dataset to use for both the xG timeline and the shot map/use for both passing networks
    # -Dataset used for the xG timeline and the shot map needs the length of each half
    # to calculate the displaying minutes (use events file with typeId 30)
    # -Limit the attempts to process the data and open the json files
    # -Keep the visualisations as it is, but open to change if Ben wants to see something different

    # Variables to store match and team's information
    matchName = ""
    compName = ""
    homeTeam = ""
    awayTeam = ""
    homeTeamId = ""
    awayTeamId = ""

    for i in range(len(teamIDs)):
        if (home_team == teamIDs['code'][i]):
            homeTeamId = teamIDs['contestantId'][i]
        if (away_team == teamIDs['code'][i]):
            awayTeamId = teamIDs['contestantId'][i]

    if (home_team == 'BOL'):
        home_colour = '#cf122f'
        home_edge_colour = 'white'

        if (away_team == 'BCT'):
            away_colour = 'deepskyblue'
            away_edge_colour = 'white'
        elif (away_team == 'BRR'):
            away_colour = '#f26522'
            away_edge_colour = 'black'
        elif (away_team == 'CAP'):
            away_colour = '#efc939'
            away_edge_colour = '#173676'
        elif (away_team == 'EAS'):
            away_colour = '#f57a3e'
            away_edge_colour = 'black'
        elif (away_team == 'GCK'):
            away_colour = 'red'
            away_edge_colour = 'white'
        elif (away_team == 'GCU'):
            away_colour = '#fdd005'
            away_edge_colour = '#1f367d'
        elif (away_team == 'LIO'):
            away_colour = '#f26522'
            away_edge_colour = '#0055a3'
        elif (away_team == 'LIG'):
            away_colour = 'maroon'
            away_edge_colour = 'white'
        elif (away_team == 'MBJ'):
            away_colour = 'gold'
            away_edge_colour = 'black'
        elif (away_team == 'PEN'):
            away_colour = 'mediumblue'
            away_edge_colour = 'red'
        elif (away_team == 'SCW'):
            away_colour = 'goldenrod'
            away_edge_colour = 'black'

    elif (away_team == 'BOL'):
        away_colour = '#152849'
        away_edge_colour = 'white'

        if (home_team == 'BCT'):
            home_colour = 'deepskyblue'
            home_edge_colour = 'white'
        elif (home_team == 'BRR'):
            home_colour = '#f26522'
            home_edge_colour = 'black'
        elif (home_team == 'CAP'):
            home_colour = '#efc939'
            home_edge_colour = '#173676'
        elif (home_team == 'EAS'):
            home_colour = '#f57a3e'
            home_edge_colour = 'black'
        elif (home_team == 'GCK'):
            home_colour = 'red'
            home_edge_colour = 'white'
        elif (home_team == 'GCU'):
            home_colour = '#fdd005'
            home_edge_colour = '#1f367d'
        elif (home_team == 'LIO'):
            home_colour = '#f26522'
            home_edge_colour = '#0055a3'
        elif (home_team == 'LIG'):
            home_colour = 'maroon'
            home_edge_colour = 'white'
        elif (home_team == 'MBJ'):
            home_colour = 'gold'
            home_edge_colour = 'black'
        elif (home_team == 'PEN'):
            home_colour = 'mediumblue'
            home_edge_colour = 'red'
        elif (home_team == 'SCW'):
            home_colour = 'goldenrod'
            home_edge_colour = 'black'

    # A reminder to stay hydrated while the program is working!
    with st.spinner("While waiting, remember to stay hydrated!"):

        # If the chosen option is either xG timeline or shot map
        if (vizOption == 'xG timeline') or (vizOption == 'Shot map'):

            # Variables to store the length of each half
            first_half_time = 45
            second_half_time = 45
            first_extra_time = 0
            second_extra_time = 0

            # Open the json file, copy its data, and then immediately close the json file
            with open(directory + eventsFile, encoding='utf-8') as jsonFile:
                jsonData = json.load(jsonFile)
                jsonFile.close()

            # Assign each section of the json file to a variable
            matchInfo = jsonData['matchInfo']
            # Variable to store the number of periods played in the match
            periodNo = int(matchInfo['numberOfPeriods'])
            liveData = jsonData['liveData']
            events = liveData['event']

            # For loop to get the end time of each half
            for event in events:

                # Check if the number of periods played is 2 or not
                if (periodNo == 2):

                    if (event['typeId'] == 30):
                        if (event['periodId'] == 1):
                            # Get the end time of the first half
                            first_half_time = int(event['timeMin'])
                        elif (event['periodId'] == 2):
                            # Get the end time of the second half,
                            second_half_time = int(event['timeMin']) - 45
                            # then minus 45 to get the length of the half

                # If the match is played into the extra time (possible due to the Finals series)
                elif (periodNo > 2):

                    # Get the end time of the first half of the extra time
                    # then minus 90 to get the length of the first extra time
                    if (event['typeId'] == 30):
                        if (event['periodId'] == 3):
                            first_extra_time = int(event['timeMin']) - 90
                        # Get the end time of the second half of the extra time
                        # then minus 105 (first 90 + first extra time 15) to get the length of the 2nd extra time
                        elif (event['periodId'] == 4):
                            second_extra_time = int(event['timeMin']) - 105

            # Variable to check the home team
            isHomeTeam = False
            # Open the json file, copy its data, and then immediately close the json file
            with open(directory + xgoalFile, encoding='utf-8') as jsonFile:
                jsonData = json.load(jsonFile)
                jsonFile.close()

            # Assign each section of the json file to a variable
            # and get the necessary information about the match
            matchInfo = jsonData['matchInfo']
            matchName = matchInfo['description']
            compName = matchInfo['competition']['name']
            liveData = jsonData['liveData']
            matchDetails = liveData["matchDetails"]
            event = liveData['event']
            homeScore = matchDetails['scores']['total']['home']
            awayScore = matchDetails['scores']['total']['away']

            # Set the page header to the match's information
            st.header(matchName + ' - ' + compName)

            # Get the necessary information about both teams
            for contestant in matchInfo['contestant']:

                if contestant['position'] == 'home':
                    homeTeam = contestant['name']
                else:
                    if isHomeTeam == False:
                        awayTeam = contestant['name']

            # Declare variables to use for data processing
            homeXGoal = 0
            awayXGoal = 0

            # Determine the width of the gap in between each half
            gap_width = 2

            # Create a blank data frame to store the xG data
            xg_data = pd.DataFrame()

            # Create a sample dataset
            xGoalEvent = {
                'minute': 0,  # Minute displayed on the xG timeline
                'realMinute': 0,  # Minute that the shot took place in the match
                'period': 1,  # Period when the shot took place
                'shotType': 0,  # Shot type (assigned by Opta [13, 14, 15, 16])
                'x': 0,  # x coordinate of the shot
                'y': 0,  # y coordinate of the shot
                'homeScorerName': '',  # Name of the goalscorer
                'awayScorerName': '',
                'homeEachXGoal': 0,  # Each shot's expected goal
                'awayEachXGoal': 0,
                'homeXGOT': 0,  # xGOT (Expected goal on target) of each shot
                'awayXGOT': 0,
                'homeXGoal': 0,  # Cumulated expected goal
                'awayXGoal': 0,
            }

            # Add the sample dataset to the data frame
            xg_data = xg_data.append(xGoalEvent, ignore_index=True)

            # Declare variables to store the individual and cumulated expected goals
            homeXGoal = 0
            awayXGoal = 0

            # This loop will go through every shot events in the list.
            # For every shot event...
            for index, event in enumerate(event):

                # Assign the real minute when the shot took place to the dataset
                xGoalEvent['realMinute'] = event['timeMin']

                # Check if the period of the shot event is exceeding 4 or not
                if (event['periodId'] <= 4):

                    # Assign the period of the shot to the corresponding column of the dataset
                    xGoalEvent['period'] = event['periodId']

                    # Calculate the minute which the shot will be displayed in the xG timeline
                    # If the shot took place in the first half...
                    if (event['periodId'] == 1):
                        # ...assign the usual minute to the corresponding column of the dataset.
                        xGoalEvent['minute'] = event['timeMin']

                    # If the shot took place in the second half...
                    elif (event['periodId'] == 2):
                        # ...add the length of the stoppage/injury time of the first half (first_half_time - 45)
                        # and the width of the gap to the original minute when the shot took place.
                        xGoalEvent['minute'] = event['timeMin'] + \
                            first_half_time - 45 + gap_width

                    # If the shot took place in the first half of the extra time...
                    elif (event['periodId'] == 3):
                        # ...add the length of the stoppage/injury time of the first half *and* the second half
                        # and twice the width of the gap (because there are two gaps separating three halves)
                        # to the original minute when the shot took place.
                        xGoalEvent['minute'] = event['timeMin'] + first_half_time - 45 + gap_width + \
                            second_half_time - 45 + gap_width

                    # If the shot took place in the second half of the extra time...
                    elif (event['periodId'] == 4):
                        # ...add the length of the stoppage/injury time of the first half, the second half
                        # and the first half of the extra time
                        # (first_half_time - 45), (second_half_time - 45) and (first_extra_time - 15)
                        # to the original minute when the shot took place.
                        xGoalEvent['minute'] = event['timeMin'] + first_half_time - 45 + gap_width + \
                            second_half_time - 45 + gap_width + first_extra_time - 15 + gap_width

                # If the period when the shot took place exceeded 4 (into the penalty shootout)
                # then stop the for loop.
                else:
                    break

                # Error with this id
                if (event['id'] == 2207030489):
                    break
                
                isqualifier = False

                # Check if the team in possession's ID matches the home team's ID or not
                if (event['contestantId'] == homeTeamId):
                    
                    # Get the typeId of the shot
                    xGoalEvent['shotType'] = event['typeId']
                    
                    # Check if the scored goal is an own goal or not
                    for qualifier in event['qualifier']:
                        if (qualifier['qualifierId'] == 28):
                            isqualifier = True
                            break

                    if (isqualifier == False):
                        
                        # Assign the scorer's name to the respective value of the dict
                        # and leave the away scorer name field blank
                        if (xGoalEvent['shotType'] == 16):
                            xGoalEvent['homeScorerName'] = event['playerName']
                            xGoalEvent['awayScorerName'] = ""
                        else:
                            xGoalEvent['homeScorerName'] = ""
                            xGoalEvent['awayScorerName'] = ""
                        
                        # Go through the qualifiers of the shot
                        for qualifier in event['qualifier']:
                            # If the qualifierId is 321 (store the xG value of the shot)
                            if (qualifier['qualifierId'] == 321):
                                # Get the xG value of the shot
                                homeEachXGoal = float(qualifier['value'])
                                awayEachXGoal = 0
                                
                                xGoalEvent['homeEachXGoal'] = homeEachXGoal
                                xGoalEvent['awayEachXGoal'] = awayEachXGoal
                                # Add the xG value of the current shot to the total xG value of the home team
                                homeXGoal += float(qualifier['value'])
                                xGoalEvent['homeXGoal'] = homeXGoal

                            # If the qualifierId is 322 (store the xGOT value of the shot)
                            elif (qualifier['qualifierId'] == 322):
                                # Get the xGOT value of the shot
                                homeEachXGOT = float(qualifier['value'])
                                awayEachXGOT = 0
                                
                                xGoalEvent['homeXGOT'] = homeEachXGOT
                                xGoalEvent['awayXGOT'] = awayEachXGOT

                            # Check if the shot (on target) is a blocked shot or not
                            if (qualifier['qualifierId'] == 82):
                                xGoalEvent['shotType'] = 12
                                
                    else:
                        # Assign the scorer's name to the respective value of the dict
                        # and leave the away scorer name field blank
                        xGoalEvent['homeScorerName'] = ""
                        xGoalEvent['awayScorerName'] = event['playerName'] + ' (OG)'
                        xGoalEvent['shotType'] = 26
                        
                        # Go through the qualifiers of the shot
                        for qualifier in event['qualifier']:
                            # If the qualifierId is 321 (store the xG value of the shot)
                            if (qualifier['qualifierId'] == 321):
                                # Get the xG value of the shot
                                homeEachXGoal = 0
                                awayEachXGoal = 0
                                
                                xGoalEvent['homeEachXGoal'] = homeEachXGoal
                                xGoalEvent['awayEachXGoal'] = awayEachXGoal

                            # If the qualifierId is 322 (store the xGOT value of the shot)
                            elif (qualifier['qualifierId'] == 322):
                                # Get the xGOT value of the shot
                                homeEachXGOT = 0
                                awayEachXGOT = 0
                                
                                xGoalEvent['homeXGOT'] = homeEachXGOT
                                xGoalEvent['awayXGOT'] = awayEachXGOT

                else:

                    # Get the typeId of the shot
                    xGoalEvent['shotType'] = event['typeId']
                    
                    # Check if the scored goal is an own goal or not
                    for qualifier in event['qualifier']:
                        if (qualifier['qualifierId'] == 28):
                            isqualifier = True
                            break

                    if (isqualifier == False):
                        
                        # Assign the scorer's name to the respective value of the dict
                        # and leave the away scorer name field blank
                        if (xGoalEvent['shotType'] == 16):
                            xGoalEvent['homeScorerName'] = ""
                            xGoalEvent['awayScorerName'] = event['playerName']
                        else:
                            xGoalEvent['homeScorerName'] = ""
                            xGoalEvent['awayScorerName'] = ""
                        
                        # Go through the qualifiers of the shot
                        for qualifier in event['qualifier']:
                            # If the qualifierId is 321 (store the xG value of the shot)
                            if (qualifier['qualifierId'] == 321):
                                # Get the xG value of the shot
                                homeEachXGoal = 0
                                awayEachXGoal = float(qualifier['value'])
                                
                                xGoalEvent['homeEachXGoal'] = homeEachXGoal
                                xGoalEvent['awayEachXGoal'] = awayEachXGoal
                                # Add the xG value of the current shot to the total xG value of the home team
                                awayXGoal += float(qualifier['value'])
                                xGoalEvent['awayXGoal'] = awayXGoal

                            # If the qualifierId is 322 (store the xGOT value of the shot)
                            elif (qualifier['qualifierId'] == 322):
                                # Get the xGOT value of the shot
                                homeEachXGOT = 0
                                awayEachXGOT = float(qualifier['value'])
                                
                                xGoalEvent['homeXGOT'] = homeEachXGOT
                                xGoalEvent['awayXGOT'] = awayEachXGOT

                            # Check if the shot (on target) is a blocked shot or not
                            if (qualifier['qualifierId'] == 82):
                                xGoalEvent['shotType'] = 12               
                    else:
                        
                        # Assign the scorer's name to the respective value of the dict
                        # and leave the away scorer name field blank
                        xGoalEvent['homeScorerName'] = event['playerName'] + ' (OG)'
                        xGoalEvent['awayScorerName'] = ""
                        xGoalEvent['shotType'] = 26
                        
                        # Go through the qualifiers of the shot
                        for qualifier in event['qualifier']:
                            # If the qualifierId is 321 (store the xG value of the shot)
                            if (qualifier['qualifierId'] == 321):
                                # Get the xG value of the shot
                                homeEachXGoal = 0
                                awayEachXGoal = 0
                                
                                xGoalEvent['homeEachXGoal'] = homeEachXGoal
                                xGoalEvent['awayEachXGoal'] = awayEachXGoal

                            # If the qualifierId is 322 (store the xGOT value of the shot)
                            elif (qualifier['qualifierId'] == 322):
                                # Get the xGOT value of the shot
                                homeEachXGOT = 0
                                awayEachXGOT = 0
                                
                                xGoalEvent['homeXGOT'] = homeEachXGOT
                                xGoalEvent['awayXGOT'] = awayEachXGOT

                # Assign the total xG of both teams after this event
                # to the corresponding columns of the dataset.
                xGoalEvent['homeXGoal'] = homeXGoal
                xGoalEvent['awayXGoal'] = awayXGoal

                # Add each event to the big dataframe
                xg_data = xg_data.append(xGoalEvent, ignore_index=True)

                if (vizOption == 'xG timeline'):

                    # Declare a couple of variables to use
                    max_xg = 0
                    graph_end_time = 0
                    isextratime = False

                    # Check if the home team's total xG is larger than the away team's total xG or not...
                    # If it is...
                    if (xg_data['homeXGoal'].iloc[-1] >= xg_data['awayXGoal'].iloc[-1]):

                        # ...then assign the home team's total xG to the max_xg variable.
                        # We also round it up to one decimal number because
                        # this variable will be used to set the limit of the y axis of our timeline.

                        max_xg = round(xg_data['homeXGoal'].iloc[-1], 1)

                        # If the match's largest xG is smaller or equal to 2...
                        if (max_xg <= 2):
                            # ...then create two lists that...
                            # ...store the ticks values...
                            y_times = [0, 0.25, 0.5, 0.75,
                                       1, 1.25, 1.5, 1.75, 2]
                            # ...and the ticks labels...
                            y_labels = ["0", "0.25", "0.5", "0.75",
                                        "1", "1.25", "1.5", "1.75", "2"]
                            # to use when drawing the timeline.
                        # If the largest xG is larger than 2, but smaller or equal to 3.5...
                        elif (max_xg <= 3.5):
                            # ...then make these lists slightly less detailed than the previous two.
                            y_times = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
                            y_labels = ["0", "0.5", "1",
                                        "1.5", "2", "2.5", "3", "3.5"]
                        else:  # If the largest xG is larger than 3.5...
                            # ...then make both lists even less detailed than the previous two.
                            y_times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                            y_labels = ["0", "1", "2", "3", "4",
                                        "5", "6", "7", "8", "9", "10"]

                    # If the away team's xG is larger than the home team's xG...
                    # ...do the same steps for the away team's xG...
                    else:
                        # ...including assign the away team's total xG to the max_xg variable.
                        max_xg = round(xg_data['awayXGoal'].iloc[-1], 1)

                        if (max_xg <= 2):
                            y_times = [0, 0.25, 0.5, 0.75,
                                       1, 1.25, 1.5, 1.75, 2]
                            y_labels = ["0", "0.25", "0.5", "0.75",
                                        "1", "1.25", "1.5", "1.75", "2"]
                        elif (max_xg <= 3.5):
                            y_times = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
                            y_labels = ["0", "0.5", "1",
                                        "1.5", "2", "2.5", "3", "3.5"]
                        else:
                            y_times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                            y_labels = ["0", "1", "2", "3", "4",
                                        "5", "6", "7", "8", "9", "10"]

                    # Calculate the match length
                    match_length = first_half_time + second_half_time + \
                        first_extra_time + second_extra_time

                    # Get the time when the last shot was made in this match
                    last_shot = xg_data['minute'].iloc[-1]

                    # Check if the match is played through to the extra time or not
                    if (second_extra_time == 0):  # If it is not then...
                        # ...calculate the minute that the graph will end by... (it's obvious through the names of the used variables!)
                        graph_end_time = match_length + gap_width
                        isextratime = False
                    else:  # If it is played to extra time then do a similar step
                        # (gap_width * 3) here is basically because we have three gaps separating the four halves played.
                        graph_end_time = match_length + (gap_width * 3)
                        isextratime = True
                    # We also assign the True/False value to the isextratime variable for the code below.

                    # Create three variables to store the length and the number of gaps used for each half
                    tmp1st = first_half_time
                    tmp2nd = first_half_time + gap_width + second_half_time
                    tmp1et = first_half_time + gap_width + \
                        second_half_time + gap_width + first_extra_time

                    # If the match did not play to extra time...
                    if (isextratime == False):
                        # ...then create these lists to store the ticks values and labels for the x axis.
                        # Very similar to what we have done at the start for the y axis.
                        x_times = [0, 15, 30, 45, first_half_time, first_half_time + gap_width, first_half_time +
                                   15 + gap_width, first_half_time + 30 + gap_width, first_half_time + 45 + gap_width, graph_end_time]
                        x_labels = ["", "15", "30", "45", "", "45",
                                    "60", "75", "90", str(second_half_time + 45)]
                    else:
                        x_times = [0, 15, 30, 45, tmp1st, tmp1st + gap_width, tmp1st +
                                   15 + gap_width, tmp1st + 30 + gap_width, tmp1st + 45 + gap_width, tmp2nd,
                                   tmp2nd + gap_width, tmp1et, tmp1et + gap_width, tmp1et + 15 + gap_width, graph_end_time]
                        x_labels = ["", "15", "30", "45", "", "45", "60",
                                    "75", "90", "", "90", "", "105", "", "120"]

                    # Choose the background colour for the timeline and the stripes colour for the shots map
                    bg = "white"
                    # stripe_colour = '#bf4789'

                # Draw the xG timeline:

                    # Create the figure to draw the xG timeline
                    fig, ax = plt.subplots(figsize=(12, 8))
                    # This one is used to remove the outline that connects the plot and the ticks
                    plt.box(False)

                    # Import the lists of x and y ticks values and labels
                    plt.xticks(x_times, x_labels,
                               fontproperties=robotoRegular, color="black")
                    plt.yticks(y_times, y_labels,
                               fontproperties=robotoRegular, color="black")

                    # Set the label of the x and y axes
                    plt.ylabel("Cumulative Expected Goals (xG)", fontsize=10,
                               fontproperties=robotoBold, color="black")
                    plt.xlabel("Minutes Played", fontsize=10,
                               fontproperties=robotoBold, color="black")

                    # Set the limit of the x and y axes
                    plt.xlim(0, graph_end_time + 2)
                    # Adding two is for creating a small gap to see where the xG lines end
                    plt.ylim(0, max_xg + 0.1)

                    # Change the properties of the plot's grid and the parameters for the ticks
                    plt.grid(zorder=1, color="black", axis='y', alpha=0.2)
                    plt.tick_params(axis=u'both', which=u'both', length=0)

                    # Add the gaps in between both halves
                    rect1 = ax.patch
                    rect2 = ax.patch
                    rect3 = ax.patch
                    rect1 = patches.Rectangle((first_half_time, 0), gap_width, 10,
                                              linewidth=0, edgecolor='white', facecolor=bg, zorder=2)
                    rect2 = patches.Rectangle((first_half_time + gap_width + second_half_time, 0), gap_width, 10,
                                              linewidth=0, edgecolor='white', facecolor=bg, zorder=2)
                    rect3 = patches.Rectangle((first_half_time + gap_width + second_half_time + gap_width + first_extra_time, 0), gap_width, 10,
                                              linewidth=0, edgecolor='white', facecolor=bg, zorder=2)
                    ax.add_patch(rect1)
                    if (periodNo > 2):  # Only add the other two patches if there is extra time
                        ax.add_patch(rect2)
                        ax.add_patch(rect3)
                        # Draw the border for the added gaps (extra time gaps)
                        ax.axvline(first_half_time + gap_width + second_half_time,
                                   color='black', linestyle='-', alpha=0.2)
                        ax.axvline(first_half_time + gap_width + second_half_time +
                                   gap_width, color='black', linestyle='-', alpha=0.2)
                        ax.axvline(first_half_time + gap_width + second_half_time + gap_width +
                                   first_extra_time, color='black', linestyle='-', alpha=0.2)
                        ax.axvline(first_half_time + gap_width + second_half_time + gap_width +
                                   first_extra_time + gap_width, color='black', linestyle='-', alpha=0.2)

                    # Draw the borders for the added gaps (gap between two halves)
                    ax.axvline(first_half_time, color='black',
                               linestyle='-', alpha=0.2)
                    ax.axvline(first_half_time + gap_width,
                               color='black', linestyle='-', alpha=0.2)

                    # Draw the line to indicate the time when the last shot of the match was made
                    ax.axvline(last_shot, color='black',
                               linestyle='--', alpha=0.2)

                    # Draw the steps for each shot event from the xg_data dataframe
                    ax.step(x='minute', y='homeXGoal', data=xg_data,
                            color=home_colour, linewidth=3, where='post', zorder=1)
                    ax.step(x='minute', y='awayXGoal', data=xg_data,
                            color=away_colour, linewidth=3, where='post', zorder=1)

                    # Continue drawing the xG line until the last minute of the match,
                    # rather than stopping at the last shot of the match
                    ax.step(x=[graph_end_time, last_shot], y=[xg_data['homeXGoal'][len(xg_data) - 1], xg_data['homeXGoal'][len(xg_data) - 1]],
                            color=home_colour, linewidth=3, where='post', zorder=1)
                    ax.step(x=[graph_end_time, last_shot], y=[xg_data['awayXGoal'][len(xg_data) - 1], xg_data['awayXGoal'][len(xg_data) - 1]],
                            color=away_colour, linewidth=3, where='post', zorder=1)

                    # Look for the goalscorer's information in the xg_data dataframe
                    for i in range(len(xg_data)):

                        # If the shot event has a homeScorerName assigned to it
                        # (Essentially if the shot event is a goal and has the goalscorer's name)
                        if (xg_data['shotType'][i] == 16) and (xg_data['homeScorerName'][i] != ""):

                            # Create a text string which will store the name of the goal scorer and the xG of the goal
                            home_text = xg_data['homeScorerName'][i] + "\n" + \
                                "{:.2f}".format(float(xg_data['homeEachXGoal'][i])) + " xG\n" + \
                                "{:.2f}".format(
                                    float(xg_data['homeXGOT'][i])) + " xGOT"

                            # Create a text box to store the text string
                            props = dict(boxstyle='round', facecolor='white',
                                         edgecolor=home_colour, alpha=0.7)

                            # Plot a dot at the displayed minute when the goal was scored
                            ax.scatter(xg_data['minute'][i], xg_data['homeXGoal'][i],
                                       s=60, facecolors=home_colour, edgecolors=home_edge_colour, zorder=6, linewidth=3)

                            # Display the information of the goal (the text string) within the text box
                            ax.text(xg_data['realMinute'][i] + 0.5, xg_data['homeXGoal'][i] + (max_xg / 10 * 0.3), home_text,
                                    ha='center', color=home_colour, zorder=6, fontproperties=robotoBold, bbox=props)

                        # If the goal is scored by an away player then do the steps similarly,
                        # but use the information of the away team.
                        elif (xg_data['shotType'][i] == 16) and (xg_data['awayScorerName'][i] != ""):

                            away_text = xg_data['awayScorerName'][i] + "\n" + \
                                "{:.2f}".format(float(xg_data['awayEachXGoal'][i])) + " xG\n" + \
                                "{:.2f}".format(
                                    float(xg_data['awayXGOT'][i])) + " xGOT"

                            props = dict(boxstyle='round', facecolor='white',
                                         edgecolor=away_colour, alpha=0.7)

                            ax.scatter(xg_data['minute'][i], xg_data['awayXGoal'][i],
                                       s=60, facecolors=away_colour, edgecolors=away_edge_colour, zorder=6, linewidth=3)
                            ax.text(xg_data['realMinute'][i] + 0.5, xg_data['awayXGoal'][i] + (max_xg / 10 * 0.3), away_text,
                                    ha='center', color=away_colour, zorder=6, fontproperties=robotoBold, bbox=props)

                    # Determine if each team has scored less/equal to or more than 1 goal
                    # to create a text string that stores each team's xG information
                    if (homeScore <= 1):
                        home_xG = homeTeam + '\n' + \
                            str(homeScore) + ' goal\n' + \
                            "{:.2f}".format(
                                float(xg_data['homeXGoal'][i])) + ' xG'
                    else:
                        home_xG = homeTeam + '\n' + \
                            str(homeScore) + ' goals\n' + \
                            "{:.2f}".format(
                                float(xg_data['homeXGoal'][i])) + ' xG'

                    if (awayScore <= 1):
                        away_xG = awayTeam + '\n' + \
                            str(awayScore) + ' goal\n' + \
                            "{:.2f}".format(
                                float(xg_data['awayXGoal'][i])) + ' xG'
                    else:
                        away_xG = awayTeam + '\n' + \
                            str(awayScore) + ' goals\n' + \
                            "{:.2f}".format(
                                float(xg_data['awayXGoal'][i])) + ' xG'

                    # Add each team's text string to the end of their respective xG line
                    home_x_position = graph_end_time + 3
                    away_x_position = graph_end_time + 3
                    ax.text(home_x_position, xg_data['homeXGoal'][len(xg_data) - 1] - 0.05, home_xG,
                            color=home_colour, font_properties=robotoBold, fontsize=15, ha='left')
                    ax.text(away_x_position, xg_data['awayXGoal'][len(xg_data) - 1] - 0.05, away_xG,
                            color=away_colour, font_properties=robotoBold, fontsize=15, ha='left')

                    # Add the text to indicate which half is which
                    # (Divide by 2 allows the text to be at the central of its respective space that has been separated by the gap)
                    ax.text((first_half_time / 2), max_xg + 0.13, 'First half', color='black',
                            font_properties=robotoBold, fontsize=15, ha='center')
                    ax.text(first_half_time + gap_width + (second_half_time / 2), max_xg + 0.13, 'Second half',
                            color='black', font_properties=robotoBold, fontsize=15, ha='center')

                    if (periodNo > 2):
                        ax.text(first_half_time + gap_width + second_half_time + gap_width + (first_extra_time / 2), max_xg + (max_xg / 10 * 0.2),
                                'First ET', color='black', font_properties=robotoBold, fontsize=15, ha='center')
                        ax.text(first_half_time + gap_width + second_half_time + gap_width + first_extra_time + gap_width + (second_extra_time / 2), max_xg + (max_xg / 10 * 0.2),
                                'Second ET', color='black', font_properties=robotoBold, fontsize=15, ha='center')

                    home_team = homeTeam + ' - ' + \
                        str(homeScore) + ' (' + \
                        "{:.2f}".format(
                            float(xg_data['homeXGoal'][len(xg_data) - 1])) + ' xG)'
                    away_team = ' v ' + awayTeam + ' - ' + \
                        str(awayScore) + ' (' + \
                        "{:.2f}".format(
                            float(xg_data['awayXGoal'][len(xg_data) - 1])) + ' xG)'

                    # Calculate the y values for the title
                    if (max_xg <= 1):
                        y = max_xg + 0.17
                    elif (max_xg <= 2):
                        y = max_xg + 0.25
                    else:
                        y = max_xg + 0.35

                    # Write the title and the credit
                    ax.text(49.5, y, home_team, color=home_colour,
                            font_properties=robotoBold, fontsize=22, ha='right')
                    ax.text(49.6, y, away_team, color=away_colour,
                            font_properties=robotoBold, fontsize=22, ha='left')

                elif (vizOption == 'Shot map'):

                    # Create counting variables and categorise the shots
                    home_goals = 0
                    home_on_target = 0
                    home_post = 0
                    home_off_target = 0
                    home_blocked = 0

                    away_goals = 0
                    away_on_target = 0
                    away_post = 0
                    away_off_target = 0
                    away_blocked = 0

                    # Setup and draw the pitch
                    pitch = Pitch(pitch_type='opta', pitch_color='grass', line_color='white',
                                  stripe=True)
                    fig, ax = pitch.draw(figsize=(10, 8))

                    # Go through the xg_data list to get the shots data
                    for i in range(0, len(xg_data)):

                        # If the shot belongs to a home player...
                        if (xg_data['homeScorerName'][i] != ''):

                            # Check to see which type of shot it is
                            # (16 = goal, 15 = shot on target, 12 = shot blocked,
                            # 14 = shot hit post, 13 = shot off target)
                            #
                            # Then plot the shot location (x, y coordinates) and
                            # the size of the shot based on the xG, and increase
                            # the counter for the respective type of shot.
                            if (xg_data['shotType'][i] == 16):
                                nodes = pitch.scatter(xg_data['x'][i] - ((xg_data['x'][i] - 50.1) * 2), xg_data['y'][i] - ((xg_data['y'][i] - 49.9) * 2), s=700 * xg_data['homeEachXGoal'][i], marker='o',
                                                      color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                                home_goals = home_goals + 1
                                home_on_target = home_on_target + 1
                            elif (xg_data['shotType'][i] == 15):
                                nodes = pitch.scatter(xg_data['x'][i] - ((xg_data['x'][i] - 50.1) * 2), xg_data['y'][i] - ((xg_data['y'][i] - 49.9) * 2), s=700 * xg_data['homeEachXGoal'][i], marker='^',
                                                      color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                                home_on_target = home_on_target + 1
                            elif (xg_data['shotType'][i] == 14):
                                nodes = pitch.scatter(xg_data['x'][i] - ((xg_data['x'][i] - 50.1) * 2), xg_data['y'][i] - ((xg_data['y'][i] - 49.9) * 2), s=700 * xg_data['homeEachXGoal'][i], marker='s',
                                                      color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                                home_post = home_post + 1
                            elif (xg_data['shotType'][i] == 12):
                                nodes = pitch.scatter(xg_data['x'][i] - ((xg_data['x'][i] - 50.1) * 2), xg_data['y'][i] - ((xg_data['y'][i] - 49.9) * 2), s=700 * xg_data['homeEachXGoal'][i], marker='D',
                                                      color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                                home_blocked = home_blocked + 1
                            else:
                                nodes = pitch.scatter(xg_data['x'][i] - ((xg_data['x'][i] - 50.1) * 2), xg_data['y'][i] - ((xg_data['y'][i] - 49.9) * 2), s=700 * xg_data['homeEachXGoal'][i], marker='X',
                                                      color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                                home_off_target = home_off_target + 1
                        else:
                            if (xg_data['shotType'][i] == 16):
                                nodes = pitch.scatter(xg_data['x'][i], xg_data['y'][i], s=700 * xg_data['awayEachXGoal'][i], marker='o',
                                                      color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                                away_goals = away_goals + 1
                                away_on_target = away_on_target + 1
                            elif (xg_data['shotType'][i] == 15):
                                nodes = pitch.scatter(xg_data['x'][i], xg_data['y'][i], s=700 * xg_data['awayEachXGoal'][i], marker='^',
                                                      color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                                away_on_target = away_on_target + 1
                            elif (xg_data['shotType'][i] == 14):
                                nodes = pitch.scatter(xg_data['x'][i], xg_data['y'][i], s=700 * xg_data['awayEachXGoal'][i], marker='s',
                                                      color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                                away_post = away_post + 1
                            elif (xg_data['shotType'][i] == 12):
                                nodes = pitch.scatter(xg_data['x'][i], xg_data['y'][i], s=700 * xg_data['awayEachXGoal'][i], marker='D',
                                                      color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                                away_blocked = away_blocked + 1
                            else:
                                nodes = pitch.scatter(xg_data['x'][i], xg_data['y'][i], s=700 * xg_data['awayEachXGoal'][i], marker='X',
                                                      color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                                away_off_target = away_off_target + 1

                    # Prepare two strings to store the teams' name, goals scored, and xG
                    home_team = homeTeam + ' - ' + \
                        str(homeScore) + ' (' + \
                        "{:.2f}".format(
                            float(xg_data['homeXGoal'][len(xg_data) - 1])) + ' xG)'
                    away_team = 'v ' + awayTeam + ' - ' + \
                        str(awayScore) + ' (' + \
                        "{:.2f}".format(
                            float(xg_data['awayXGoal'][len(xg_data) - 1])) + ' xG)'

                    # Write the two above strings
                    ax.text(49.5, 95, home_team, color=home_colour,
                            font_properties=robotoBold, fontsize=20, ha='right')
                    ax.text(50.5, 95, away_team, color=away_colour,
                            font_properties=robotoBold, fontsize=20, ha='left')

                    # Prepare three text boxes, one for the goal type, two for each team's quantity
                    text_box = dict(boxstyle='round', facecolor='white')
                    home_values = dict(boxstyle='round', facecolor=home_colour,
                                       edgecolor=home_edge_colour)
                    away_values = dict(boxstyle='round', facecolor=away_colour,
                                       edgecolor=away_edge_colour)

                    # Indicate how many goals each team have scored
                    ax.text(50, 65, 'Goals', color='black', font_properties=robotoBold,
                            fontsize=12, ha='center', bbox=text_box)
                    ax.text(39, 65, str(home_goals), color=home_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=home_values)
                    ax.text(59, 65, str(away_goals), color=away_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=away_values)

                    # Indicate how many shots on target (including goals) each team have made
                    ax.text(50, 57, 'Shots on target', color='black',
                            font_properties=robotoBold, fontsize=12, ha='center', bbox=text_box)
                    ax.text(39, 57, str(home_on_target), color=home_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=home_values)
                    ax.text(59, 57, str(away_on_target), color=away_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=away_values)

                    # Indicate how many shots that hit the post each team have made
                    ax.text(50, 49, 'Hit post', color='black', font_properties=robotoBold,
                            fontsize=12, ha='center', bbox=text_box)
                    ax.text(39, 49, str(home_post), color=home_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=home_values)
                    ax.text(59, 49, str(away_post), color=away_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=away_values)

                    # Indicate how many shots off target each team have made
                    ax.text(49.85, 41, 'Shots off target', color='black',
                            font_properties=robotoBold, fontsize=12, ha='center', bbox=text_box)
                    ax.text(39, 41, str(home_off_target), color=home_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=home_values)
                    ax.text(59, 41, str(away_off_target), color=away_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=away_values)

                    # Indicate how many blocked shots each team have made
                    ax.text(50, 33, 'Shots blocked', color='black',
                            font_properties=robotoBold, fontsize=12, ha='center', bbox=text_box)
                    ax.text(39, 33, str(home_blocked), color=home_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=home_values)
                    ax.text(59, 33, str(away_blocked), color=away_edge_colour,
                            font_properties=robotoBold, fontsize=12, ha='left', bbox=away_values)

                    # Draw the legends (shape, shot type and xG value) at the bottom of the plot
                    ax.text(27, 8, 'Outcomes:', color='white',
                            font_properties=robotoBold, fontsize=15, ha='center')
                    nodes = pitch.scatter(4, 4, s=300, marker='o',
                                          color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                    ax.text(8, 3.25, 'Goal', color='white',
                            font_properties=robotoBold, fontsize=12, ha='center')
                    nodes = pitch.scatter(12, 4, s=300, marker='^',
                                          color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                    ax.text(17.5, 3.25, 'On target', color='white',
                            font_properties=robotoBold, fontsize=12, ha='center')
                    nodes = pitch.scatter(23.5, 4, s=300, marker='s',
                                          color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                    ax.text(28.7, 3.25, 'Hit post', color='white',
                            font_properties=robotoBold, fontsize=12, ha='center')
                    nodes = pitch.scatter(35, 4, s=300, marker='D',
                                          color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                    ax.text(41, 3.25, 'Blocked', color='white',
                            font_properties=robotoBold, fontsize=12, ha='center')
                    nodes = pitch.scatter(46.5, 4, s=300, marker='X',
                                          color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                    ax.text(52.5, 3.25, 'Off target', color='white',
                            font_properties=robotoBold, fontsize=12, ha='center')

                    # (The size of the dot increases by the xG value of the shot)
                    ax.text(80, 8, 'Dot size increases by the xG value of the shot', color='white',
                            font_properties=robotoBold, fontsize=12, ha='center')
                    nodes = pitch.scatter(70.5, 4, s=100, marker='o',
                                          color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                    nodes = pitch.scatter(73, 4, s=200, marker='o',
                                          color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                    nodes = pitch.scatter(75.8, 4, s=300, marker='o',
                                          color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)
                    nodes = pitch.scatter(79.2, 4, s=400, marker='o',
                                          color=away_colour, edgecolors=away_edge_colour, zorder=1, ax=ax)
                    nodes = pitch.scatter(83, 4, s=500, marker='o',
                                          color=home_colour, edgecolors=home_edge_colour, zorder=1, ax=ax)

        elif (vizOption == "Home team's passing network") or (vizOption == "Away team's passing network"):

            # Variable to check the home team
            isHomeTeam = False
            # Open the json file, copy its data, and then immediately close the json file
            with open(directory + passNetworkFile, encoding='utf-8') as jsonFile:
                jsonData = json.load(jsonFile)
                jsonFile.close()

            # Assign each section of the json file to a variable
            # and get the necessary information about the match
            matchInfo = jsonData['matchInfo']
            matchName = matchInfo['description']
            compName = matchInfo['competition']['name']
            liveData = jsonData['liveData']
            matchDetails = liveData["matchDetails"]
            homeScore = matchDetails['scores']['total']['home']
            awayScore = matchDetails['scores']['total']['away']

            # Get the necessary information about both teams
            for contestant in matchInfo['contestant']:

                if contestant['position'] == 'home':
                    homeTeamId = contestant['id']
                    homeTeam = contestant['name']
                else:
                    if isHomeTeam == False:
                        awayTeamId = contestant['id']
                        awayTeam = contestant['name']

            # Access the lineUp section of the json file
            # and get the lineups of both teams
            liveData = jsonData['liveData']
            squadList = liveData['lineUp']
            home = squadList[0]
            away = squadList[1]

            # Create a few variables and some arrays to store passing data
            ballPasser = ''
            ballReceiver = ''
            passValue = 0  # Number of passes made to the second player
            player_x_value = 0
            player_y_value = 0
            homeXI = []  # Array to store the home team's starting lineup
            homeShirtNo = []
            awayXI = []  # Array to store the away team's starting lineup
            awayShirtNo = []
            home_x_y_values = []  # Array to store the home player's x and y values
            away_x_y_values = []  # Array to store the away player's x and y values
            home_pass_success = []  # Array to store the home player's accurate passes value
            away_pass_success = []  # Array to store the away player's accurate passes value
            # Array to store the home player's x and y values of the pass destination
            homePassLocation = []
            # Array to store the away player's x and y values of the pass destination
            awayPassLocation = []

            for player in home['player']:

                if (player['position'] != 'Substitute'):
                    homeXI.append(player['matchName'])
                    homeShirtNo.append(player['shirtNumber'])
                else:
                    break

            for player in away['player']:

                if player['position'] != 'Substitute':
                    awayXI.append(player['matchName'])
                    awayShirtNo.append(player['shirtNumber'])
                else:
                    break

            for player in home['player']:

                if (player['position'] != 'Substitute'):

                    if ('x' in player):
                        player_x_value = player['x']
                        player_y_value = player['y']
                        home_x_y_values.append([player['playerId'], player['matchName'], player_x_value, player_y_value])
                        home_pass_success.append(player['passSuccess'])
                else:
                    break

            for player in away['player']:

                if (player['position'] != 'Substitute'):

                    if ('x' in player):
                        player_x_value = player['x']
                        player_y_value = player['y']
                        away_x_y_values.append([player['playerId'], player['matchName'], player_x_value, player_y_value])
                        away_pass_success.append(player['passSuccess'])
                else:
                    break

            # Go through the home team's squad list
            # and gather necessary information
            for player in home['player']:

                # Check if a player is a substitute or not
                if (player['position'] != 'Substitute') and ('playerPass' in player):

                    for playerPass in player['playerPass']:

                        if ('playerId' in player) and ('playerId' in playerPass):
                            ballPasser = player['playerId']
                            ballReceiver = playerPass['playerId']
                            passValue = playerPass['value']
                            homePassLocation.append([ballPasser, ballReceiver, passValue])
                else:
                    break

            for player in away['player']:

                if (player['position'] != 'Substitute') and ('playerPass' in player):

                    for playerPass in player['playerPass']:

                        if ('playerId' in player) and ('playerId' in playerPass):
                            ballPasser = player['playerId']
                            ballReceiver = playerPass['playerId']
                            passValue = playerPass['value']
                            awayPassLocation.append([ballPasser, ballReceiver, passValue])
                else:
                    break

            # Setup and draw the pitch
            pitch = Pitch(pitch_type='opta', pitch_color='#050b31', line_color='white',
                          stripe=False)
            fig, ax = pitch.draw(figsize=(10, 8))

            if (vizOption == "Home team's passing network"):

                for i in range(0, len(homePassLocation)):
                    isStarting = False
                    for y in range(0, len(home_x_y_values)):
                        if homePassLocation[i][0] == home_x_y_values[y][0]:
                            x_start = home_x_y_values[y][2]
                            y_start = home_x_y_values[y][3]
                        if homePassLocation[i][1] == home_x_y_values[y][0]:
                            x_end = home_x_y_values[y][2]
                            y_end = home_x_y_values[y][3]
                            isStarting = True
                    if isStarting == False:
                        continue

                for passes in homePassLocation:
                    ballPasser = passes[0]
                    ballReceiver = passes[1]
                    passValue = passes[2]
                    for player in home_x_y_values:
                        if ballPasser == player[0]:
                            x_start = player[2]
                            y_start = player[3]
                        elif ballReceiver == player[0]:
                            x_end = player[2]
                            y_end = player[3]

                    if passValue < 4:
                        # arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 1.5, headwidth = 1, headlength = 1, color = '#32527b', alpha = 0.1, ax = ax)
                        continue
                    elif passValue < 6:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 2.5, headwidth=4, headlength=2, headaxislength=2, color = '#c7d5ed', alpha = 0.3, ax = ax)
                    elif passValue < 12:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 3.5, headwidth=4, headlength=2, headaxislength=2, color = '#abc0e4', alpha = 0.5, ax = ax)
                    elif passValue < 16:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 4.5, headwidth=4, headlength=2, headaxislength=2, color = '#dde5f4', alpha = 0.65, ax = ax)
                    else:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 5.5, headwidth=4, headlength=2, headaxislength=2, color = '#f6f8fc', alpha = 0.85, ax = ax)

                for i in range(0, len(home_x_y_values)):
                    nodes = pitch.scatter(home_x_y_values[i][2], home_x_y_values[i][3], s = 4.5 * home_pass_success[i], color = home_colour, edgecolors = home_edge_colour, zorder = 1, ax = ax)
                    playerInfo = homeXI[i]
                    playerPosition = (home_x_y_values[i][2], home_x_y_values[i][3])
                    text = pitch.annotate(playerInfo, playerPosition, (home_x_y_values[i][2], home_x_y_values[i][3] + 4.2), ha = 'center', va = 'center', fontproperties = robotoRegular, fontsize = 12, color = 'white', ax = ax)

            elif (vizOption == "Away team's passing network"):

                # The process for the away team's passing network is similar to the home team's passing network.
                # The comments from the code section to draw home team's passing network
                # also applies to the code section to draw the away team's passing network,
                # but the lists used here belong to the away team, not the home team.

                # Create variables to store the starting and ending x,y coordinates of the passes
                x_start = 0
                y_start = 0
                x_end = 0
                y_end = 0

                # Set the page header to the match's information
                st.header(awayTeam + " | Passing network")
                st.subheader(matchName + ' - ' + compName)

                for passes in awayPassLocation:
                    ballPasser = passes[0]
                    ballReceiver = passes[1]
                    passValue = passes[2]
                    for player in away_x_y_values:
                        if ballPasser == player[0]:
                            x_start = player[2]
                            y_start = player[3]
                        elif ballReceiver == player[0]:
                            x_end = player[2]
                            y_end = player[3]

                    if passValue < 4:
                        # arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 1.5, headwidth = 1, headlength = 1, color = '#c7d5ed', alpha = 0.15, ax = ax)
                        continue
                    elif passValue < 6:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 2.5, headwidth=4, headlength=2, headaxislength=2, color = '#abc0e4', alpha = 0.35, ax = ax)
                    elif passValue < 12:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 3.5, headwidth=4, headlength=2, headaxislength=2, color = '#c8d5ed', alpha = 0.5, ax = ax)
                    elif passValue < 16:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 4.5, headwidth=4, headlength=2, headaxislength=2, color = '#dde5f4', alpha = 0.75, ax = ax)
                    else:
                        arrow = pitch.arrows(x_start, y_start, x_end, y_end, width = 5.5, headwidth=4, headlength=2, headaxislength=2, color = '#f6f8fc', alpha = 1, ax = ax)

                for i in range(0, len(away_x_y_values)):
                    nodes = pitch.scatter(away_x_y_values[i][2], away_x_y_values[i][3], s = 4.5 * away_pass_success[i], color = away_colour, edgecolors = away_edge_colour, zorder = 1, ax = ax)
                    
                    playerInfo = awayXI[i]
                    playerPosition = (away_x_y_values[i][2], away_x_y_values[i][3])
                    text = pitch.annotate(playerInfo, (playerPosition), (away_x_y_values[i][2], away_x_y_values[i][3] + 4.2), ha = 'center', va = 'center', fontproperties = robotoRegular, fontsize = 12, color = 'white', ax = ax)

            # Create a colour map from the colours used for the arrows
            cmap0 = mpl.colors.LinearSegmentedColormap.from_list(
                'green2red', ['#abc0e4', '#c8d5ed', '#dde5f4', '#f6f8fc'])
            # Set the range of the colour map
            norm = mpl.colors.Normalize(vmin=6, vmax=16)

            # Draw the colour map and set the tick params and the label
            cbar = ax.figure.colorbar(
                mpl.cm.ScalarMappable(norm=norm, cmap=cmap0),
                ax=ax, location='bottom', orientation='horizontal', fraction=.05, pad=0.02)
            cbar.ax.tick_params(color="white", labelcolor="white")
            cbar.set_label('Pass combinations', color='white')

            # Write the note
            ax.text(20, 2, "Size of dot increases by the player's accurate passes",
                    color='white', fontsize=10, ha='center')

            # Credit
            ax.text(1, 97, "By Daryl - @dgouilard", color='white',
                    fontproperties=robotoRegular, fontsize=10)

            # Set the figure's face colour, width and height
            fig.set_facecolor('#050b31')
            fig.set_figwidth(10.5)
            fig.set_figheight(10)

        # Ask Streamlit to plot the figure
        st.pyplot(fig)
