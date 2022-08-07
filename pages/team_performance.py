import streamlit as st
import json
import pandas as pd
import matplotlib as mpl
from numpy import mean, arange
from mplsoccer import Radar, Pitch, VerticalPitch
import matplotlib.patheffects as path_effects
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from pages import data_processing
mpl.rcParams['figure.dpi'] = 700

def radar_mosaic(radar_height=0.915, title_height=0.06, figheight=14):
   
    endnote_height = 1 - title_height - radar_height
    figwidth = figheight * radar_height
    figure, axes = plt.subplot_mosaic([['title'], ['radar'], ['endnote']],
                                      gridspec_kw={'height_ratios': [title_height, radar_height,
                                                                     endnote_height],
                                                   'bottom': 0, 'left': 0, 'top': 1,
                                                   'right': 1, 'hspace': 0},
                                      figsize=(figwidth, figheight))
    axes['title'].axis('off')
    axes['endnote'].axis('off')
    return figure, axes

def app():
    
    st.title("Team performance")

    nplqFixtures = pd.read_csv('NPLQ fixtures.csv', delimiter = ',')
    teamIds = pd.read_csv('Opta team IDs.csv', delimiter = ';')

    nplqTeams = ['Brisbane City', 'Brisbane Roar Youth', 'Capalaba', 'Eastern Suburbs', 'Gold Coast Knights',
                'Gold Coast United', 'Lions', 'Logan Lightning', 'Moreton Bay United', 'Olympic',
                'Peninsula Power', 'Sunshine Coast Wanderers']

    col1, col2 = st.columns(2)

    with col1:

        teamOption = st.selectbox(
            label = 'Choose a team',
            options = nplqTeams,
            index = 0
        )

        vizOption = st.selectbox(
            label = 'Choose visualisation to be displayed',
            options = (
                'Radar plot',
                'Shot map',
                'Scatter plot',
                'Zonal map'
            ),
            index = 0
        )

    homeTeamCode = ''
    awayTeamCode = ''
    xGoalFile = ''
    statsFile = ''
    eventsFile = ''

    xgoalBrisbaneCity = []
    statsBrisbaneCity = []
    eventsBrisbaneCity = []
    teamIdBrisbaneCity = teamIds['contestantId'][0]
    directoryBrisbaneCity = "Opta stats/Opposition's data/Brisbane City/"

    xgoalRoarYouth = []
    statsRoarYouth = []
    eventsRoarYouth = []
    teamIdRoarYouth = teamIds['contestantId'][1]
    directoryRoarYouth = "Opta stats/Opposition's data/Brisbane Roar Youth/"

    xgoalCapalaba = []
    statsCapalaba = []
    eventsCapalaba = []
    teamIdCapalaba = teamIds['contestantId'][2]
    directoryCapalaba = "Opta stats/Opposition's data/Capalaba/"

    xgoalEastsSuburbs = []
    statsEastsSuburbs = []
    eventsEastsSuburbs = []
    teamIdEastsSuburbs = teamIds['contestantId'][3]
    directoryEasternSuburbs = "Opta stats/Opposition's data/Eastern Suburbs/"

    xgoalGCKnights = []
    statsGCKnights = []
    eventsGCKnights = []
    teamIdGCKnights = teamIds['contestantId'][4]
    directoryGCKnights = "Opta stats/Opposition's data/Gold Coast Knights/"

    xgoalGCUnited = []
    statsGCUnited = []
    eventsGCUnited = []
    teamIdGCUnited = teamIds['contestantId'][5]
    directoryGCUnited = "Opta stats/Opposition's data/Gold Coast United/"

    xgoalLions = []
    statsLions = []
    eventsLions = []
    teamIdLions = teamIds['contestantId'][6]
    directoryLions = "Opta stats/Opposition's data/Lions/"

    xgoalLoganLightning = []
    statsLoganLightning = []
    eventsLoganLightning = []
    teamIdLoganLightning = teamIds['contestantId'][7]
    directoryLoganLightning = "Opta stats/Opposition's data/Logan Lightning/"

    xgoalMoretonBayUtd = []
    statsMoretonBayUtd = []
    eventsMoretonBayUtd = []
    teamIdMoretonBayUtd = teamIds['contestantId'][8]
    directoryMoretonBayUtd = "Opta stats/Opposition's data/Moreton Bay United/"

    xgoalOlympic = []
    statsOlympic = []
    eventsOlympic = []
    teamIdOlympic = teamIds['contestantId'][9]
    directoryOlympic = "Opta stats/2022 data/"

    xgoalPenPower = []
    statsPenPower = []
    eventsPenPower = []
    teamIdPenPower = teamIds['contestantId'][10]
    directoryPenPower = "Opta stats/Opposition's data/Peninsula Power/"

    xgoalSCWanderers = []
    statsSCWanderers = []
    eventsSCWanderers = []
    teamIdSCWanderers = teamIds['contestantId'][11]
    directorySCWanderers = "Opta stats/Opposition's data/Sunshine Coast Wanderers/"

    homeTeamCode = ''
    awayTeamCode = ''
    xGoalFile = ''
    statsFile = ''
    eventsFile = ''

    for i in range(len(nplqFixtures)):

        if (nplqFixtures["Data availability"][i] == "Y"):

            homeTeamCode = nplqFixtures["Home team code"][i]
            awayTeamCode = nplqFixtures["Away team code"][i]

            xGoalFile = homeTeamCode + "_" + awayTeamCode + "_xgoal_stats.json"
            statsFile = homeTeamCode + "_" + awayTeamCode + "_stats.json"
            eventsFile = homeTeamCode + "_" + awayTeamCode + "_events.json"
            
            if (homeTeamCode == "BCT") or (awayTeamCode == "BCT"):

                xgoalBrisbaneCity.append(xGoalFile)
                statsBrisbaneCity.append(statsFile)
                eventsBrisbaneCity.append(eventsFile)

            if (homeTeamCode == "BRR") or (awayTeamCode == "BRR"):

                xgoalRoarYouth.append(xGoalFile)
                statsRoarYouth.append(statsFile)
                eventsRoarYouth.append(eventsFile)

            if (homeTeamCode == "CAP") or (awayTeamCode == "CAP"):

                xgoalCapalaba.append(xGoalFile)
                statsCapalaba.append(statsFile)
                eventsCapalaba.append(eventsFile)

            if (homeTeamCode == "EAS") or (awayTeamCode == "EAS"):

                xgoalEastsSuburbs.append(xGoalFile)
                statsEastsSuburbs.append(statsFile)
                eventsEastsSuburbs.append(eventsFile)

            if (homeTeamCode == "GCK") or (awayTeamCode == "GCK"):

                xgoalGCKnights.append(xGoalFile)
                statsGCKnights.append(statsFile)
                eventsGCKnights.append(eventsFile)

            if (homeTeamCode == "GCU") or (awayTeamCode == "GCU"):

                xgoalGCUnited.append(xGoalFile)
                statsGCUnited.append(statsFile)
                eventsGCUnited.append(eventsFile)

            if (homeTeamCode == "LIO") or (awayTeamCode == "LIO"):

                xgoalLions.append(xGoalFile)
                statsLions.append(statsFile)
                eventsLions.append(eventsFile)

            if (homeTeamCode == "LIG") or (awayTeamCode == "LIG"):

                xgoalLoganLightning.append(xGoalFile)
                statsLoganLightning.append(statsFile)
                eventsLoganLightning.append(eventsFile)

            if (homeTeamCode == "MBJ") or (awayTeamCode == "MBJ"):

                xgoalMoretonBayUtd.append(xGoalFile)
                statsMoretonBayUtd.append(statsFile)
                eventsMoretonBayUtd.append(eventsFile)

            if (homeTeamCode == "BOL") or (awayTeamCode == "BOL"):

                xgoalOlympic.append(xGoalFile)
                statsOlympic.append(statsFile)
                eventsOlympic.append(eventsFile)

            if (homeTeamCode == "PEN") or (awayTeamCode == "PEN"):

                xgoalPenPower.append(xGoalFile)
                statsPenPower.append(statsFile)
                eventsPenPower.append(eventsFile)

            if (homeTeamCode == "SCW") or (awayTeamCode == "SCW"):

                xgoalSCWanderers.append(xGoalFile)
                statsSCWanderers.append(statsFile)
                eventsSCWanderers.append(eventsFile)

    with col2:

        if (vizOption == 'Radar plot'):

            yesComparison = st.checkbox(
                label = 'Comparison radar',
                value = False
            )

            radarOption = st.radio(
                label = 'Choose a radar plot',
                options = (
                    'General performance',
                    'Attacking',
                    'Defending'
                ),
                index = 0
            )

        elif (vizOption == 'Shot map'):

            shotmapOption = st.radio(
                label = 'Choose a shot map',
                options = (
                    'Shots made',
                    'Shots conceded'
                ),
                index = 0
            )

            st.markdown("Choose the shooting ranges")
            yes6Yards = st.checkbox(
                label = 'Inside the 6-yard box',
                value = False
            )
            yes18Yards = st.checkbox(
                label = 'Inside the 18-yard box',
                value = True
            )
            yesOutside18Yards = st.checkbox(
                label = 'Outside the 18-yard box',
                value = True
            )

        elif (vizOption == 'Scatter plot'):

            scatterOption = st.radio(
                label = 'Choose an in-game action',
                options = (
                    'Attacking',
                    'Defending',
                    'Possession',
                    'Set pieces'
                ),
                index = 0
            )

            if (scatterOption == 'Attacking'):

                attackingOption = st.radio(
                    label = 'Choose a scatter plot',
                    options = (
                        'Attacking efficiency', # Shots per game - (Goal per shot) %
                        # 'Shooting', # Shots on target per game - xG per shot
                        'Goal-scoring' # Goals - xG (per game)
                    ),
                    index = 0
                )

            elif (scatterOption == 'Defending'):

                defendingOption = st.radio(
                    label = 'Choose a scatter plot',
                    options = (
                        'Defending efficiency', # Shots faced per game - Opp. conversion %
                        'Tackling', # Tackles attempted per game - Won %
                        'Aerial duels' # Aerial duels attempted per game - Won %
                    ),
                    index = 0
                )

            elif (scatterOption == 'Possession'):

                possessionOption = st.radio(
                    label = 'Choose a scatter plot',
                    options = (
                        # 'Passing efficiency', # Passes attempted per game - Completion %
                        'Possession won/lost', # Pos won - Pos lost (per game)
                        'Dribbling', # Dribbles attempted - Pos lost in opp. half (per game)
                        'Crossing' # Crosses attempted per game - Completion %
                    ),
                    index = 0
                )

            elif (scatterOption == 'Set pieces'):

                setPiecesOption = st.radio(
                    label = 'Choose a scatter plot',
                    options = (
                        'Free kicks', # Attempted - With shots (per game)
                        'Corners' # Attempted - With shots (per game)
                    ),
                    index = 0
                )

        elif (vizOption == 'Zonal map'):

            zonalOption = st.radio(
                label = 'Choose a zonal map',
                options = (
                    'Pass starting locations',
                    'Pass ending locations',
                    'Defensive actions',
                    'Possession won',
                    'Possession lost'
                ),
                index = 0
            )

    robotto_thin = fm.FontProperties(fname='Roboto-Light_0.ttf')
    robotto_regular = fm.FontProperties(fname='Roboto-Regular_0.ttf')
    robotto_bold = fm.FontProperties(fname='Roboto-Bold_0.ttf')

    with st.spinner("This app is trying its hardest to bring you the best visualisation!"):

        BrisbaneCity = data_processing.totalData(teamIdBrisbaneCity, directoryBrisbaneCity, xgoalBrisbaneCity, statsBrisbaneCity, eventsBrisbaneCity)
        RoarYouth = data_processing.totalData(teamIdRoarYouth, directoryRoarYouth, xgoalRoarYouth, statsRoarYouth, eventsRoarYouth)
        Capalaba = data_processing.totalData(teamIdCapalaba, directoryCapalaba, xgoalCapalaba, statsCapalaba, eventsCapalaba)
        EastsSuburbs = data_processing.totalData(teamIdEastsSuburbs, directoryEasternSuburbs, xgoalEastsSuburbs, statsEastsSuburbs, eventsEastsSuburbs)
        GCKnights = data_processing.totalData(teamIdGCKnights, directoryGCKnights, xgoalGCKnights, statsGCKnights, eventsGCKnights)
        GCUnited = data_processing.totalData(teamIdGCUnited, directoryGCUnited, xgoalGCUnited, statsGCUnited, eventsGCUnited)
        Lions = data_processing.totalData(teamIdLions, directoryLions, xgoalLions, statsLions, eventsLions)
        LoganLightning = data_processing.totalData(teamIdLoganLightning, directoryLoganLightning, xgoalLoganLightning, statsLoganLightning, eventsLoganLightning)
        MoretonBayUtd = data_processing.totalData(teamIdMoretonBayUtd, directoryMoretonBayUtd, xgoalMoretonBayUtd, statsMoretonBayUtd, eventsMoretonBayUtd)
        Olympic = data_processing.totalData(teamIdOlympic, directoryOlympic, xgoalOlympic, statsOlympic, eventsOlympic)
        PenPower = data_processing.totalData(teamIdPenPower, directoryPenPower, xgoalPenPower, statsPenPower, eventsPenPower)
        SCWanderers = data_processing.totalData(teamIdSCWanderers, directorySCWanderers, xgoalSCWanderers, statsSCWanderers, eventsSCWanderers)

        params = list(Olympic.keys())

        teamStats = [BrisbaneCity, RoarYouth, Capalaba, EastsSuburbs, GCKnights, GCUnited, Lions, LoganLightning, 
                    MoretonBayUtd, Olympic, PenPower, SCWanderers]

        teamA = {}
        teamB = {}

        teamA_facecolor = ''
        teamA_edgecolor = ''
        teamB_facecolor = ''
        teamB_edgecolor = ''

        if (teamOption == 'Brisbane City'): 
            teamA = BrisbaneCity
            teamA_facecolor = 'deepskyblue'
            teamA_edgecolor = 'white'
        elif (teamOption == 'Brisbane Roar Youth'): 
            teamA = RoarYouth
            teamA_facecolor = '#f26522'
            teamA_edgecolor = 'black'
        elif (teamOption == 'Capalaba'): 
            teamA = Capalaba
            teamA_facecolor = '#efc939'
            teamA_edgecolor = '#173676'
        elif (teamOption == 'Eastern Suburbs'): 
            teamA = EastsSuburbs
            teamA_facecolor = '#f57a3e'
            teamA_edgecolor = 'black'
        elif (teamOption == 'Gold Coast Knights'): 
            teamA = GCKnights
            teamA_facecolor = 'red'
            teamA_edgecolor = 'white'
        elif (teamOption == 'Gold Coast United'): 
            teamA = GCUnited
            teamA_facecolor = '#fdd005'
            teamA_edgecolor = '#1f367d'
        elif (teamOption == 'Lions'): 
            teamA = Lions
            teamA_facecolor = '#f26522'
            teamA_edgecolor = '#0055a3'
        elif (teamOption == 'Logan Lightning'): 
            teamA = LoganLightning
            teamA_facecolor = 'maroon'
            teamA_edgecolor = 'white'
        elif (teamOption == 'Moreton Bay United'): 
            teamA = MoretonBayUtd
            teamA_facecolor = 'gold'
            teamA_edgecolor = 'black'
        elif (teamOption == 'Olympic'): 
            teamA = Olympic
            teamA_facecolor = '#cf122f'
            teamA_edgecolor = 'white'
        elif (teamOption == 'Peninsula Power'): 
            teamA = PenPower
            teamA_facecolor = 'mediumblue'
            teamA_edgecolor = 'red'
        elif (teamOption == 'Sunshine Coast Wanderers'): 
            teamA = SCWanderers
            teamA_facecolor = 'goldenrod'
            teamA_edgecolor = 'black'

        if (vizOption == 'Radar plot'):

            gprParams = [params[4], params[6], params[8], params[10], params[0], params[1], params[11], params[21], params[24], params[12], params[16], params[17]]
            attackingParams = [params[4], params[6], params[0], params[1], params[25], params[23], params[24], params[11], params[20], params[21]]
            defendingParams = [params[8], params[10], params[2], params[12], params[13], params[14], params[15], params[16], params[17], params[19]]

            team_a_values = []
            team_b_values = []

            if (yesComparison == True):

                nplqTeams_backup = nplqTeams
                nplqTeams_backup.remove(teamOption)

                secondTeamOption = st.selectbox(
                    label = 'Choose the second team',
                    options = nplqTeams_backup,
                    index = 0
                )

                if (secondTeamOption == 'Brisbane City'): 
                    teamB = BrisbaneCity
                    teamB_facecolor = 'deepskyblue'
                    teamB_edgecolor = 'white'
                elif (secondTeamOption == 'Brisbane Roar Youth'): 
                    teamB = RoarYouth
                    teamB_facecolor = '#f26522'
                    teamB_edgecolor = 'black'
                elif (secondTeamOption == 'Capalaba'): 
                    teamB = Capalaba
                    teamB_facecolor = '#efc939'
                    teamB_edgecolor = '#173676'
                elif (secondTeamOption == 'Eastern Suburbs'): 
                    teamB = EastsSuburbs
                    teamB_facecolor = '#f57a3e'
                    teamB_edgecolor = 'black'
                elif (secondTeamOption == 'Gold Coast Knights'): 
                    teamB = GCKnights
                    teamB_facecolor = 'red'
                    teamB_edgecolor = 'white'
                elif (secondTeamOption == 'Gold Coast United'): 
                    teamB = GCUnited
                    teamB_facecolor = '#fdd005'
                    teamB_edgecolor = '#1f367d'
                elif (secondTeamOption == 'Lions'): 
                    teamB = Lions
                    teamB_facecolor = '#f26522'
                    teamB_edgecolor = '#0055a3'
                elif (secondTeamOption == 'Logan Lightning'): 
                    teamB = LoganLightning
                    teamB_facecolor = 'maroon'
                    teamB_edgecolor = 'white'
                elif (secondTeamOption == 'Moreton Bay United'): 
                    teamB = MoretonBayUtd
                    teamB_facecolor = 'gold'
                    teamB_edgecolor = 'black'
                elif (secondTeamOption == 'Olympic'): 
                    teamB = Olympic
                    teamB_facecolor = '#cf122f'
                    teamB_edgecolor = 'white'
                elif (secondTeamOption == 'Peninsula Power'): 
                    teamB = PenPower
                    teamB_facecolor = 'mediumblue'
                    teamB_edgecolor = 'red'
                elif (secondTeamOption == 'Sunshine Coast Wanderers'): 
                    teamB = SCWanderers
                    teamB_facecolor = 'goldenrod'
                    teamB_edgecolor = 'black'

            lowValue = 0
            highValue = 0
            averageValue = 0

            if (radarOption == 'General performance'):

                gprLow = []
                gprHigh = []
                gprLeagueAverage = []

                for param in gprParams:

                    gprValues = []

                    for team in teamStats:
                        gprValues.append(team[param])

                    lowValue = min(gprValues)
                    gprLow.append(lowValue)

                    highValue = max(gprValues)
                    gprHigh.append(highValue)

                    averageValue = round(mean(gprValues), 2)
                    gprLeagueAverage.append(averageValue)

                    team_a_values.append(teamA[param])
                    if (yesComparison == True): team_b_values.append(teamB[param])

            elif (radarOption == 'Attacking'):

                attackingLow = []
                attackingHigh = []
                attackingLeagueAverage = []
                    
                for param in attackingParams:

                    attackingValues = []

                    for team in teamStats:
                        attackingValues.append(team[param])

                    lowValue = min(attackingValues)
                    attackingLow.append(lowValue)

                    highValue = max(attackingValues)
                    attackingHigh.append(highValue)

                    averageValue = round(mean(attackingValues), 2)
                    attackingLeagueAverage.append(averageValue)

                    team_a_values.append(teamA[param])
                    if (yesComparison == True): team_b_values.append(teamB[param])

            elif (radarOption == 'Defending'):

                defendingLow = []
                defendingHigh = []
                defendingLeagueAverage = []

                for param in defendingParams:

                    defendingValues = []

                    for team in teamStats:
                        defendingValues.append(team[param])

                    lowValue = min(defendingValues)
                    defendingLow.append(lowValue)

                    highValue = max(defendingValues)
                    defendingHigh.append(highValue)

                    averageValue = round(mean(defendingValues), 2)
                    defendingLeagueAverage.append(averageValue)

                    team_a_values.append(teamA[param])
                    if (yesComparison == True): team_b_values.append(teamB[param])

            if (yesComparison == False):

                if (radarOption == 'General performance'):
                    team_b_values = gprLeagueAverage
                elif (radarOption == 'Attacking'):
                    team_b_values = attackingLeagueAverage
                elif (radarOption == 'Defending'):
                    team_b_values = defendingLeagueAverage

                secondTeamOption = "NPL Queensland average"
                teamB_facecolor = 'maroon'
                teamB_edgecolor = 'black'

            if (radarOption == 'General performance'):

                radar = Radar(gprParams, gprLow, gprHigh, lower_is_better = ['Non-penalty Goals conceded', 'npxGA'],
                                    # Round values to integer or keep them as float values
                                    round_int = [False] * len(gprParams),
                                    num_rings = 6,  # The number of concentric circles (excluding center circle)
                                    ring_width = 0.65, center_circle_radius = 0.5)

                fig, axs = radar_mosaic(radar_height = 0.8, title_height = 0.07, figheight = 13)

                radar.setup_axis(ax = axs['radar'], facecolor='None') # Setup an axis to draw the radar
                rings_inner = radar.draw_circles(ax = axs['radar'], facecolor = '#1f2445') # Draw inner circles
                radar_output = radar.draw_radar_compare(team_a_values, team_b_values, ax = axs['radar'],
                                                        kwargs_radar={'facecolor': teamA_facecolor, 'alpha': 0.6},
                                                        kwargs_compare={'facecolor': teamB_facecolor, 'alpha': 0.6})
                radar_poly, rings_outer, vertices1, vertices2 = radar_output
                range_labels = radar.draw_range_labels(ax = axs['radar'], fontsize = 17.5, 
                                                        fontproperties = robotto_thin, color = "#ffffff")
                param_labels = radar.draw_param_labels(ax = axs['radar'], fontsize = 18, 
                                                        fontproperties = robotto_regular, color = '#ffffff')
                axs['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                                    c = teamA_facecolor, edgecolors = teamA_edgecolor, marker = 'o', s = 200, zorder = 2)
                axs['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                                    c = teamB_facecolor, edgecolors = teamB_edgecolor, marker = 'o', s = 200, zorder = 2)

                title1_text = axs['title'].text(0.01, 0.65, teamOption, fontsize = 25, fontproperties = robotto_bold, 
                                                ha = 'left', va = 'center', color = teamA_facecolor)
                title2_text = axs['title'].text(0.99, 0.65, secondTeamOption, fontsize = 25, fontproperties = robotto_bold,
                                                ha='right', va='center', color = teamB_facecolor)
                endnote1_text = axs['endnote'].text(0.5, 0.35, 'General performance (All stats are per game basis)\nNPL Queensland, 2022 season', fontsize = 20,
                                                        fontproperties = robotto_regular, ha = 'center', va = 'center', color = 'white')

            elif (radarOption == 'Attacking'):

                radar = Radar(attackingParams, attackingLow, attackingHigh,
                                    # Round values to integer or keep them as float values
                                    round_int = [False] * len(attackingParams),
                                    num_rings = 6,  # The number of concentric circles (excluding center circle)
                                    ring_width = 0.65, center_circle_radius = 0.5)

                fig, axs = radar_mosaic(radar_height = 0.8, title_height = 0.07, figheight = 13)

                radar.setup_axis(ax = axs['radar'], facecolor='None') # Setup an axis to draw the radar
                rings_inner = radar.draw_circles(ax = axs['radar'], facecolor = '#1f2445') # Draw inner circles
                radar_output = radar.draw_radar_compare(team_a_values, team_b_values, ax = axs['radar'],
                                                        kwargs_radar={'facecolor': teamA_facecolor, 'alpha': 0.6},
                                                        kwargs_compare={'facecolor': teamB_facecolor, 'alpha': 0.6})
                radar_poly, rings_outer, vertices1, vertices2 = radar_output
                range_labels = radar.draw_range_labels(ax = axs['radar'], fontsize = 17.5, 
                                                        fontproperties = robotto_thin, color = "#ffffff")
                param_labels = radar.draw_param_labels(ax = axs['radar'], fontsize = 18, 
                                                        fontproperties = robotto_regular, color = '#ffffff')
                axs['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                                    c = teamA_facecolor, edgecolors = teamA_edgecolor, marker = 'o', s = 200, zorder = 2)
                axs['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                                    c = teamB_facecolor, edgecolors = teamB_edgecolor, marker = 'o', s = 200, zorder = 2)

                title1_text = axs['title'].text(0.01, 0.65, teamOption, fontsize = 25, fontproperties = robotto_bold, 
                                                ha = 'left', va = 'center', color = teamA_facecolor)
                title2_text = axs['title'].text(0.99, 0.65, secondTeamOption, fontsize = 25, fontproperties = robotto_bold,
                                                ha='right', va='center', color = teamB_facecolor)
                endnote1_text = axs['endnote'].text(0.5, 0.35, 'Team attacking (All stats are per game basis)\nNPL Queensland, 2022 season', fontsize = 20,
                                                        fontproperties = robotto_regular, ha = 'center', va = 'center', color = 'white')

            elif (radarOption == 'Defending'):

                radar = Radar(defendingParams, defendingLow, defendingHigh, lower_is_better = ['Non-penalty Goals conceded', 'npxGA', 'Shots conceded', 'Possession lost', 'Possession lost in opp. half'],
                                    # Round values to integer or keep them as float values
                                    round_int = [False] * len(defendingParams),
                                    num_rings = 6,  # The number of concentric circles (excluding center circle)
                                    ring_width = 0.65, center_circle_radius = 0.5)

                fig, axs = radar_mosaic(radar_height = 0.8, title_height = 0.07, figheight = 13)

                radar.setup_axis(ax = axs['radar'], facecolor='None') # Setup an axis to draw the radar
                rings_inner = radar.draw_circles(ax = axs['radar'], facecolor = '#1f2445') # Draw inner circles
                radar_output = radar.draw_radar_compare(team_a_values, team_b_values, ax = axs['radar'],
                                                        kwargs_radar={'facecolor': teamA_facecolor, 'alpha': 0.6},
                                                        kwargs_compare={'facecolor': teamB_facecolor, 'alpha': 0.6})
                radar_poly, rings_outer, vertices1, vertices2 = radar_output
                range_labels = radar.draw_range_labels(ax = axs['radar'], fontsize = 17.5, 
                                                        fontproperties = robotto_thin, color = "#ffffff")
                param_labels = radar.draw_param_labels(ax = axs['radar'], fontsize = 18, 
                                                        fontproperties = robotto_regular, color = '#ffffff')
                axs['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                                    c = teamA_facecolor, edgecolors = teamA_edgecolor, marker = 'o', s = 200, zorder = 2)
                axs['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                                    c = teamB_facecolor, edgecolors = teamB_edgecolor, marker = 'o', s = 200, zorder = 2)

                title1_text = axs['title'].text(0.01, 0.65, teamOption, fontsize = 25, fontproperties = robotto_bold, 
                                                ha = 'left', va = 'center', color = teamA_facecolor)
                title2_text = axs['title'].text(0.99, 0.65, secondTeamOption, fontsize = 25, fontproperties = robotto_bold,
                                                ha='right', va='center', color = teamB_facecolor)
                endnote1_text = axs['endnote'].text(0.5, 0.35, 'Team defending (All stats are per game basis)\nNPL Queensland, 2022 season', fontsize = 20,
                                                        fontproperties = robotto_regular, ha = 'center', va = 'center', color = 'white')

            fig.set_facecolor('#050b31')
            fig.set_figwidth(13)
            fig.set_figheight(13)

        elif (vizOption == 'Scatter plot'):

            brisbane_city = plt.imread('Logos/Brisbane City.png')
            capalaba = plt.imread('Logos/Capalaba.png')
            easts_suburbs = plt.imread("Logos/Eastern Suburbs.png")
            gc_knights = plt.imread("Logos/GC Knights.png")
            gc_united = plt.imread("Logos/GC United.png")
            lions_fc = plt.imread("Logos/Lions.png")
            logan_lightning = plt.imread("Logos/Logan Lightning.png")
            moreton_bay = plt.imread("Logos/Moreton Bay.png")
            olympic = plt.imread("Logos/Olympic.png")
            pen_power = plt.imread("Logos/Peninsula Power.png")
            roar_youth = plt.imread("Logos/Brisbane Roar.png")
            sunny_coast_w = plt.imread("Logos/SC Wanderers.png")

            npl_teams = [
                brisbane_city,
                roar_youth,
                capalaba,
                easts_suburbs,
                gc_knights,
                gc_united,
                lions_fc,
                logan_lightning,
                moreton_bay,
                olympic,
                pen_power,
                sunny_coast_w
            ]

            scatter_xvalues = []
            scatter_yvalues = []

            if (scatterOption == 'Attacking'):

                if (attackingOption == 'Attacking efficiency'):
                    scatter_params = ['Shots', 'Chances conversion %']

                    for team in teamStats:

                        shotsMade = 0
                        goalsScored = 0
                        
                        shotsMade = team[scatter_params[0]]
                        goalsScored = team['Goals scored']
                        chancesConversion = round(goalsScored / shotsMade * 100, 1)
                        
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(chancesConversion)

                # elif (attackingOption == 'Shooting'):
                #     scatter_params = ['Shots on target', 'npxG per shot']

                #     for team in teamStats:

                #         shotsMade = 0
                #         npxG = 0
                        
                #         shotsMade = team[scatter_params[0]]
                #         npxG = team['npxG']
                #         xGPerGoal = round(npxG / shotsMade, 2)
                        
                #         scatter_xvalues.append(team[scatter_params[0]])
                #         scatter_yvalues.append(xGPerGoal)

                elif (attackingOption == 'Goal-scoring'):
                    scatter_params = ['Goals scored', 'xG']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

            elif (scatterOption == 'Defending'):
                
                if (defendingOption == 'Defending efficiency'):
                    scatter_params = ['Shots conceded', 'Opp. conversion %']

                    for team in teamStats:

                        shotsConceded = 0
                        goalsConceded = 0
                        
                        shotsConceded = team[scatter_params[0]]
                        goalsConceded = team['Goals conceded']
                        oppConversion = round(goalsConceded / shotsConceded * 100, 1)
                        
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(oppConversion)

                elif (defendingOption == 'Tackling'):
                    scatter_params = ['Tackles attempted', 'Tackles won']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

                elif (defendingOption == 'Aerial duels'):
                    scatter_params = ['Aerial duels attempted', 'Aerial duels won']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

            elif (scatterOption == 'Possession'):
                
                # if (possessionOption == 'Passing efficiency'):
                #     scatter_params = ['Passes attempted', 'Passes completed %']

                #     for team in teamStats:

                #         passesAttempted = 0
                #         passesCompleted = 0
                #         passesCompletion = 0

                #         passesAttempted = team[scatter_params[0]]
                #         passesCompleted = team['Passes completed']
                #         passesCompletion = round(passesCompleted / passesAttempted * 100, 1)

                #         scatter_xvalues.append(team[scatter_params[0]])
                #         scatter_yvalues.append(passesCompletion)

                if (possessionOption == 'Possession won/lost'):
                    scatter_params = ['Possession won', 'Possession lost']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

                elif (possessionOption == 'Dribbling'):
                    scatter_params = ['Dribbles attempted', 'Possession lost in opp. half']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

                elif (possessionOption == 'Crossing'):
                    scatter_params = ['Crosses attempted', 'Crosses completed']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

            elif (scatterOption == 'Set pieces'):
                
                if (setPiecesOption == 'Free kicks'):
                    scatter_params = ['Free kicks attempted', 'Free kicks attempted with shots']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

                elif (setPiecesOption == 'Corners'):
                    scatter_params = ['Corners attempted', 'Corners attempted with shots']

                    for team in teamStats:
                        scatter_xvalues.append(team[scatter_params[0]])
                        scatter_yvalues.append(team[scatter_params[1]])

            min_x_value = scatter_xvalues[0]
            max_x_value = 0
            min_y_value = scatter_yvalues[0]
            max_y_value = 0

            for i in range(1, len(scatter_xvalues)):
                if (scatter_xvalues[i] < min_x_value):
                    min_x_value = scatter_xvalues[i]

                if (scatter_yvalues[i] < min_y_value):
                    min_y_value = scatter_yvalues[i]

            for i in range(0, len(scatter_xvalues)):
                if (scatter_xvalues[i] > max_x_value):
                    max_x_value = scatter_xvalues[i]
                
                if (scatter_yvalues[i] > max_y_value):
                    max_y_value = scatter_yvalues[i]

            x_average = round(mean(scatter_xvalues), 2)
            y_average = round(mean(scatter_yvalues), 2)

            col3, col4 = st.columns(2)

            with col3:

                fig, axs = plt.subplots(figsize = (8, 6))

                if (max_x_value > 5) or (max_y_value > 5):
                    for i in range(len(scatter_yvalues)):
                        axs.scatter(scatter_xvalues, scatter_yvalues, s = 30, linewidth = 1, alpha = 0)
                        axs.imshow(npl_teams[i], extent=[scatter_xvalues[i], scatter_xvalues[i] + 0.3, scatter_yvalues[i], scatter_yvalues[i] + 0.3])

                    axs.annotate("League average", xy = (x_average, max_y_value), xytext = (x_average + 0.1, max_y_value - 2), 
                                color = 'grey', size = 8, rotation = 270, fontproperties = robotto_thin)
                    axs.annotate("League average", xy = (min_x_value, y_average), xytext = (min_x_value + 2, y_average + 0.1), 
                                    color = 'grey', size = 8, fontproperties = robotto_thin)

                elif (max_x_value < 5) or (max_y_value < 5):
                    for i in range(len(scatter_yvalues)):
                        axs.scatter(scatter_xvalues, scatter_yvalues, s = 30, linewidth = 1, alpha = 0)
                        axs.imshow(npl_teams[i], extent=[scatter_xvalues[i], scatter_xvalues[i] + 0.15, scatter_yvalues[i], scatter_yvalues[i] + 0.15])

                    axs.annotate("League average", xy = (x_average, max_y_value), xytext = (x_average + 0.03, max_y_value - 0.5), 
                                color = 'grey', size = 8, rotation = 270, fontproperties = robotto_thin)
                    axs.annotate("League average", xy = (min_x_value, y_average), xytext = (min_x_value + 2, y_average + 0.03), 
                                    color = 'grey', size = 8, fontproperties = robotto_thin)

                axs.axvline(x_average, color = 'grey', linestyle = '--', alpha = 0.7)
                axs.axhline(y_average, color = 'grey', linestyle = '--', alpha = 0.7)

                left = min_x_value
                right = max_x_value
                top = max_y_value
                bottom = min_y_value

                if (scatterOption == 'Attacking'):
                    if (attackingOption == 'Attacking efficiency'):
                        annotations = ['Passive, Clinical', 'Orange', 'Aggressive, Clinical', 'Green',
                                        'Passive, Wasteful', 'Red', 'Aggressive, Wasteful', 'Orange']
                    elif (attackingOption == 'Goal-scoring'):
                        annotations = ['Few goals, High-quality chances', 'Orange', 'Many goals, High-quality chances', 'Green',
                                        'Few goals, Low-quality chances', 'Red', 'Many goals, Low-quality chances', 'Orange']
                elif (scatterOption == 'Defending'):
                    if (defendingOption == 'Defending efficiency'):
                        annotations = ['Few shots, Conceded frequently', 'Orange', 'Many shots, Conceded frequently', 'Red',
                                        'Few shots, Conceded less often', 'Green', 'Many shots, Conceded less often', 'Orange']
                    elif (defendingOption == 'Tackling'):
                        annotations = ['Tackle less, Won more tackles', 'Orange', 'Tackle often, Won more tackles', 'Green',
                                        'Tackle less, Won less tackles', 'Red', 'Tackle often, Won less tackles', 'Orange']
                    elif (defendingOption == 'Aerial duels'):
                        annotations = ['Less aerial duels, Won more aerial duels', 'Orange', 'More aerial duels, Won more aerial duels', 'Green',
                                        'Less aerial duels, Won less aerial duels', 'Red', 'More aerial duels, Won less aerial duels', 'Orange']
                elif (scatterOption == 'Possession'):
                    if (possessionOption == 'Possession won/lost'):
                        annotations = ['Won less possession, Lost more possession', 'Red', 'Won more possession, Lost more possession', 'Orange',
                                        'Won less possession, Lost less possession', 'Orange', 'Won more possession, Lost less possession', 'Green']
                    elif (possessionOption == 'Dribbling'):
                        annotations = ['Dribble less, Lost more possession', 'Orange', 'Dribble more, Lost more possession', 'Red',
                                        'Dribble less, Lost less possession', 'Orange', 'Dribble more, Lost less possession', 'Green']
                    elif (possessionOption == 'Crossing'):
                        annotations = ['Cross less often, High efficiency', 'Orange', 'Cross more often, High efficiency', 'Green',
                                        'Cross less often, Low efficiency', 'Orange', 'Cross more often, Low efficiency', 'Red']
                elif (scatterOption == 'Set pieces'):
                    if (setPiecesOption == 'Free kicks'):
                        annotations = ['Less free kicks, Made more shots', 'Orange', 'More free kicks, Made more shots', 'Green',
                                        'Less free kicks, Made less shots', 'Orange', 'More free kicks, Made less shots', 'Red']
                    elif (setPiecesOption == 'Corners'):
                        annotations = ['Less corners, Made more shots', 'Orange', 'More corners, Made more shots', 'Green',
                                        'Less corners, Made less shots', 'Orange', 'More corners, Made less shots', 'Red']

                axs.text(0.1 + left, 0.1 + top, annotations[0], ha = 'left', va = 'top',
                                color = annotations[1], size = 8, fontproperties = robotto_bold)
                axs.text(0.1 + right, 0.1 + top, annotations[2], ha = 'right', va = 'top',
                                color = annotations[3], size = 8, fontproperties = robotto_bold)
                axs.text(0.1 + left, 0.05 + bottom, annotations[4], ha = 'left', va = 'bottom',
                                color = annotations[5], size = 8, fontproperties = robotto_bold)
                axs.text(0.1 + right, 0.05 + bottom, annotations[6], ha = 'right', va = 'bottom',
                                color = annotations[7], size = 8, fontproperties = robotto_bold)

                axs.autoscale()

                userChoice = ''
                if (scatterOption == 'Attacking'):
                    userChoice = attackingOption
                elif (scatterOption == 'Defending'):
                    userChoice = defendingOption
                elif (scatterOption == 'Possession'):
                    userChoice = possessionOption
                elif (scatterOption == 'Set pieces'):
                    userChoice = setPiecesOption

                title = userChoice + ' (Stats are per game basis)\nNPL Queensland, 2022 season'

                fig.set_facecolor("#050b31")
                axs.set_facecolor("#050b31")
                plt.title(title, 
                            color = 'white', fontproperties = robotto_bold, fontsize = 15)
                plt.xlabel(scatter_params[0], 
                            color = 'white', fontproperties = robotto_bold, fontsize = 12)
                plt.ylabel(scatter_params[1], 
                            color = 'white', fontproperties = robotto_bold, fontsize = 12)
                plt.tick_params(grid_color = 'white')
                plt.xticks(color = 'white', fontproperties = robotto_regular)
                plt.yticks(color = 'white', fontproperties = robotto_regular)

                bbox = axs.get_window_extent()
                ax = fig.gca()
                bbox_data = bbox.transformed(ax.transData.inverted())
                ax.update_datalim(bbox_data.corners())
                ax.autoscale_view()

            with col4:

                statsInfo = teamOption + ' | ' + scatterOption + ' stats'
                st.subheader(statsInfo)

                team_xvalue = 0
                team_yvalue = 0

                if (teamOption == 'Brisbane City'): 
                    team_xvalue = BrisbaneCity[scatter_params[0]]
                    team_yvalue = scatter_yvalues[0]
                elif (teamOption == 'Brisbane Roar Youth'): 
                    team_xvalue = RoarYouth[scatter_params[0]]
                    team_yvalue = scatter_yvalues[1]
                elif (teamOption == 'Capalaba'): 
                    team_xvalue = Capalaba[scatter_params[0]]
                    team_yvalue = scatter_yvalues[2]
                elif (teamOption == 'Eastern Suburbs'): 
                    team_xvalue = EastsSuburbs[scatter_params[0]]
                    team_yvalue = scatter_yvalues[3]
                elif (teamOption == 'Gold Coast Knights'): 
                    team_xvalue = GCKnights[scatter_params[0]]
                    team_yvalue = scatter_yvalues[4]
                elif (teamOption == 'Gold Coast United'): 
                    team_xvalue = GCUnited[scatter_params[0]]
                    team_yvalue = scatter_yvalues[5]
                elif (teamOption == 'Lions'): 
                    team_xvalue = Lions[scatter_params[0]]
                    team_yvalue = scatter_yvalues[6]
                elif (teamOption == 'Logan Lightning'): 
                    team_xvalue = LoganLightning[scatter_params[0]]
                    team_yvalue = scatter_yvalues[7]
                elif (teamOption == 'Moreton Bay United'): 
                    team_xvalue = MoretonBayUtd[scatter_params[0]]
                    team_yvalue = scatter_yvalues[8]
                elif (teamOption == 'Olympic'): 
                    team_xvalue = Olympic[scatter_params[0]]
                    team_yvalue = scatter_yvalues[9]
                elif (teamOption == 'Peninsula Power'): 
                    team_xvalue = PenPower[scatter_params[0]]
                    team_yvalue = scatter_yvalues[10]
                elif (teamOption == 'Sunshine Coast Wanderers'): 
                    team_xvalue = SCWanderers[scatter_params[0]]
                    team_yvalue = scatter_yvalues[11]

                stats = "(" + str(team_xvalue) + " " + scatter_params[0] + ", " + str(team_yvalue) + " " + scatter_params[1] + ")"
                st.subheader(stats)

        elif (vizOption == 'Shot map') or (vizOption == 'Zonal map'):

            directory = ''
            teamId = ''
            xgoal_list = []
            events_list = []

            if (teamOption == 'Brisbane City'): 
                directory = directoryBrisbaneCity
                teamId = teamIdBrisbaneCity
                xgoal_list = xgoalBrisbaneCity
                events_list = eventsBrisbaneCity
            elif (teamOption == 'Brisbane Roar Youth'): 
                directory = directoryRoarYouth
                teamId = teamIdRoarYouth
                xgoal_list = xgoalRoarYouth
                events_list = eventsRoarYouth
            elif (teamOption == 'Capalaba'): 
                directory = directoryCapalaba
                teamId = teamIdCapalaba
                xgoal_list = xgoalCapalaba
                events_list = eventsCapalaba
            elif (teamOption == 'Eastern Suburbs'): 
                directory = directoryEasternSuburbs
                teamId = teamIdEastsSuburbs
                xgoal_list = xgoalEastsSuburbs
                events_list = eventsEastsSuburbs
            elif (teamOption == 'Gold Coast Knights'): 
                directory = directoryGCKnights
                teamId = teamIdGCKnights
                xgoal_list = xgoalGCKnights
                events_list = eventsGCKnights
            elif (teamOption == 'Gold Coast United'): 
                directory = directoryGCUnited
                teamId = teamIdGCUnited
                xgoal_list = xgoalGCUnited
                events_list = eventsGCUnited
            elif (teamOption == 'Lions'): 
                directory = directoryLions
                teamId = teamIdLions
                xgoal_list = xgoalLions
                events_list = eventsLions
            elif (teamOption == 'Logan Lightning'): 
                directory = directoryLoganLightning
                teamId = teamIdLoganLightning
                xgoal_list = xgoalLoganLightning
                events_list = eventsLoganLightning
            elif (teamOption == 'Moreton Bay United'): 
                directory = directoryMoretonBayUtd
                teamId = teamIdMoretonBayUtd
                xgoal_list = xgoalMoretonBayUtd
                events_list = eventsMoretonBayUtd
            elif (teamOption == 'Olympic'): 
                directory = directoryOlympic
                teamId = teamIdOlympic
                xgoal_list = xgoalOlympic
                events_list = eventsOlympic
            elif (teamOption == 'Peninsula Power'): 
                directory = directoryPenPower
                teamId = teamIdPenPower
                xgoal_list = xgoalPenPower
                events_list = eventsPenPower
            elif (teamOption == 'Sunshine Coast Wanderers'): 
                directory = directorySCWanderers
                teamId = teamIdSCWanderers
                xgoal_list = xgoalSCWanderers
                events_list = eventsSCWanderers

            if (vizOption == 'Shot map'):

                shots_data = []

                if (shotmapOption == 'Shots made'):
                    
                    for file in xgoal_list:

                        with open(directory + file, encoding = 'utf-8') as jsonFile:
                            jsonData = json.load(jsonFile)
                            jsonFile.close()
                            
                        liveData = jsonData['liveData']
                        event = liveData['event']
                        
                        for shot in event:
                            
                            isqualifier = False
                            ispenalty = False
                            
                            if ('contestantId' in shot) and (shot['contestantId'] == teamId):
                                
                                for qualifier in shot['qualifier']:
                                    
                                    if (qualifier['qualifierId'] == 28):
                                        isqualifier = True
                                        break
                                        
                                if (isqualifier == False):
                                    
                                    x_value = shot['x']
                                    y_value = shot['y']
                                    shot_type = shot['typeId']

                                    for qualifier in shot['qualifier']:
                                        
                                        if (qualifier['qualifierId'] == 321):
                                            xg_value = float(qualifier['value'])
                                            
                                        if (qualifier['qualifierId'] == 82):
                                            shot_type = 82
                                            
                                        if (qualifier['qualifierId'] == 9):
                                            ispenalty = True
                                    
                                    if (yes6Yards):
                                        if (94.2 <= x_value < 100) and (36.8 <= y_value <= 63.2):
                                            shots_data.append([shot_type, x_value, y_value, xg_value, ispenalty])
                                    if (yes18Yards):
                                        yes6Yards = False
                                        if (83 <= x_value < 100) and (21.1 <= y_value <= 78.9):
                                            shots_data.append([shot_type, x_value, y_value, xg_value, ispenalty])
                                    if (yesOutside18Yards):
                                        if (x_value < 83):
                                            shots_data.append([shot_type, x_value, y_value, xg_value, ispenalty])

                elif (shotmapOption == 'Shots conceded'):

                    for file in xgoal_list:

                        with open(directory + file, encoding = 'utf-8') as jsonFile:
                            jsonData = json.load(jsonFile)
                            jsonFile.close()
                            
                        liveData = jsonData['liveData']
                        event = liveData['event']
                        
                        for shot in event:
                            
                            isqualifier = False
                            ispenalty = False
                            
                            if ('contestantId' in shot) and (shot['contestantId'] != teamId):
                                
                                for qualifier in shot['qualifier']:
                                    
                                    if (qualifier['qualifierId'] == 28):
                                        isqualifier = True
                                        break
                                        
                                if (isqualifier == False):
                                    
                                    x_value = shot['x']
                                    y_value = shot['y']
                                    shot_type = shot['typeId']

                                    for qualifier in shot['qualifier']:
                                        
                                        if (qualifier['qualifierId'] == 321):
                                            xg_value = float(qualifier['value'])
                                            
                                        if (qualifier['qualifierId'] == 82):
                                            shot_type = 82
                                            
                                        if (qualifier['qualifierId'] == 9):
                                            ispenalty = True
                                    
                                    if (yes6Yards):
                                        if (94.2 <= x_value < 100) and (36.8 <= y_value <= 63.2):
                                            shots_data.append([shot_type, x_value, y_value, xg_value, ispenalty])
                                    if (yes18Yards):
                                        yes6Yards = False
                                        if (83 <= x_value < 100) and (21.1 <= y_value <= 78.9):
                                            shots_data.append([shot_type, x_value, y_value, xg_value, ispenalty])
                                    if (yesOutside18Yards):
                                        if (x_value < 83):
                                            shots_data.append([shot_type, x_value, y_value, xg_value, ispenalty])

                penalties = 0
                home_goals = 0
                home_on_target = 0
                blocked_shots = 0
                home_post = 0
                home_off_target = 0
                total_xg = 0

                pitch = VerticalPitch(pitch_type = 'opta', pitch_color = '#050b31', line_color = 'white', half = True)
                fig, ax = pitch.draw(figsize = (10, 8))

                teamColor = teamA_facecolor
                teamEdge = teamA_edgecolor

                statColor = 'white'

                for i in range(0, len(shots_data)):

                    if (shots_data[i][0] == 16):
                        nodes = pitch.scatter(shots_data[i][1], shots_data[i][2], s = 1500 * shots_data[i][3], marker = 'o',
                                            color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                        home_goals += 1
                        home_on_target += 1
                    elif (shots_data[i][0] == 15):
                        nodes = pitch.scatter(shots_data[i][1], shots_data[i][2], s = 1500 * shots_data[i][3], marker = '^',
                                            color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                        home_on_target += 1
                    elif (shots_data[i][0] == 82):
                        nodes = pitch.scatter(shots_data[i][1], shots_data[i][2], s = 1500 * shots_data[i][3], marker = 'D',
                                            color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                        blocked_shots += 1
                    elif (shots_data[i][0] == 14):
                        nodes = pitch.scatter(shots_data[i][1], shots_data[i][2], s = 1500 * shots_data[i][3], marker = 's',
                                            color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                        home_post += 1
                    else:
                        nodes = pitch.scatter(shots_data[i][1], shots_data[i][2], s = 1500 * shots_data[i][3], marker = 'X',
                                            color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                        home_off_target += 1
                    
                    if (shots_data[i][4] == False):    
                        total_xg = total_xg + shots_data[i][3]
                    else:
                        penalties += 1
                
                ax.text(98, 47.5, "Size of dot increases by the shot's xG value", 
                        color = 'white', fontproperties = robotto_regular, fontsize = 10)

                text_box = dict(boxstyle='round', facecolor='white')
                home_values = dict(boxstyle='round', facecolor = teamColor,
                                    edgecolor = teamEdge)

                xg_text = str(round(total_xg, 2)) + " xG + " + str(penalties) + " penalties" 

                ax.text(94, 65, 'Goals', color = 'black', font_properties = robotto_bold, fontsize = 12, ha = 'center', bbox  = text_box)
                ax.text(79, 65, str(home_goals), color = statColor, font_properties = robotto_bold, fontsize = 12, ha = 'left', bbox  = home_values)

                ax.text(90, 62, 'Shots on target', color = 'black', font_properties = robotto_bold, fontsize = 12, ha = 'center', bbox  = text_box)
                ax.text(79, 62, str(home_on_target), color = statColor, font_properties = robotto_bold, fontsize = 12, ha = 'left', bbox  = home_values)

                ax.text(90.5, 59, 'Shots blocked', color = 'black', font_properties = robotto_bold, fontsize = 12, ha = 'center', bbox  = text_box)
                ax.text(79, 59, str(blocked_shots), color = statColor, font_properties = robotto_bold, fontsize = 12, ha = 'left', bbox  = home_values)

                ax.text(93, 56, 'Hit post', color = 'black', font_properties = robotto_bold, fontsize = 12, ha = 'center', bbox  = text_box)
                ax.text(79, 56, str(home_post), color = statColor, font_properties = robotto_bold, fontsize = 12, ha = 'left', bbox  = home_values)

                ax.text(90, 53, 'Shots off target', color = 'black', font_properties = robotto_bold, fontsize = 12, ha = 'center', bbox  = text_box)
                ax.text(79, 53, str(home_off_target), color = statColor, font_properties = robotto_bold, fontsize = 12, ha = 'left', bbox  = home_values)

                ax.text(92, 50, 'Total npxG', color = 'black', font_properties = robotto_bold, fontsize = 12, ha = 'center', bbox  = text_box)
                ax.text(79, 50, xg_text, color = statColor, font_properties = robotto_bold, fontsize = 12, ha = 'left', bbox  = home_values)

                ax.text(2, 63, 'Outcomes:', color = 'white', font_properties = robotto_bold, fontsize = 10, ha = 'right')
                nodes = pitch.scatter(61, 2, s = 100, marker = 'o',
                                        color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                ax.text(5, 60.5, 'Goal', color = 'white', font_properties = robotto_bold, fontsize = 10, ha = 'center')
                nodes = pitch.scatter(58, 2, s = 100, marker = '^',
                                                color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                ax.text(6.5, 57.5, 'On target', color = 'white', font_properties = robotto_bold, fontsize = 10, ha = 'center')
                nodes = pitch.scatter(55, 2, s = 100, marker = 's',
                                        color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                ax.text(6.5, 54.5, 'Hit post', color = 'white', font_properties = robotto_bold, fontsize = 10, ha = 'center')
                nodes = pitch.scatter(52, 2, s = 100, marker = 'D',
                                                color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                ax.text(6.5, 51.5, 'Blocked', color = 'white', font_properties = robotto_bold, fontsize = 10, ha = 'center')
                nodes = pitch.scatter(49, 2, s = 100, marker = 'X',
                                        color = teamColor, edgecolors = teamEdge, zorder = 1, ax = ax)
                ax.text(6.8, 48.5, 'Off target', color = 'white', font_properties = robotto_bold, fontsize = 10, ha = 'center')

                fig.set_facecolor('#050b31')

                competition_info = "Queensland NPL - 2022 season"
                viz_info = teamOption + ' | ' + shotmapOption

                ax.text(72, 104.5, viz_info, color = 'white', fontproperties = robotto_bold, fontsize = 25)
                ax.text(69.5, 102, competition_info, color = 'white', fontproperties = robotto_bold, fontsize = 15)

            elif (vizOption == 'Zonal map'):

                path_eff = [path_effects.Stroke(linewidth=3, foreground='black'),
                                path_effects.Normal()]

                if (zonalOption == 'Defensive actions') or (zonalOption == 'Possession won') or (zonalOption == 'Possession lost'):

                    team_data = []
                    userChosenZonal = []
                    defActions_typeId = [4, 7, 8, 12, 44, 45]
                    possWon_typeId = [7, 8, 44, 49, 74]
                    possLost_typeId = [9, 50, 51, 61]

                    if (zonalOption == 'Defensive actions'):
                        userChosenZonal = defActions_typeId
                    elif (zonalOption == 'Possession won'):
                        userChosenZonal = possWon_typeId
                    elif (zonalOption == 'Possession lost'):
                        userChosenZonal = possLost_typeId

                    for file in events_list:

                        with open(directory + file, encoding = 'utf-8') as jsonFile:
                            jsonData = json.load(jsonFile)
                            jsonFile.close()

                        liveData = jsonData['liveData']
                        event = liveData['event']
                        
                        for touch in event:
                            
                            isqualifier = False
                        
                            if ("contestantId" in touch) and (touch["contestantId"] == teamId):

                                if (touch["typeId"] in userChosenZonal):

                                    touch_period = touch["periodId"]
                                    touch_min = touch["timeMin"]
                                    touch_sec = touch["timeSec"]
                                    touch_type = touch["typeId"]
                                    
                                    x_start = touch["x"]
                                    y_start = touch["y"]
                                    
                                    team_data.append([touch_period, touch_min, touch_sec, touch_type, x_start, y_start])

                    x_coordinates = []
                    y_coordinates = []

                    for i in range(len(team_data)):
                        x_coordinates.append(team_data[i][4])
                        y_coordinates.append(team_data[i][5])

                    pitch = Pitch(pitch_type = 'opta', pitch_color = '#050b31', 
                                line_color = "white")
                    fig, axs = pitch.grid(endnote_height = 0.03, endnote_space = 0,
                                        title_height = 0.08, title_space = 0,
                                        axis = False,
                                        grid_height = 0.84)

                    # heatmap and labels
                    bin_statistic = pitch.bin_statistic_positional(x_coordinates, y_coordinates, statistic = 'count',
                                                                positional = 'full', normalize = True)
                    pitch.heatmap_positional(bin_statistic, ax = axs['pitch'],
                                            cmap = 'YlOrRd', edgecolors = 'black')
                    labels = pitch.label_heatmap(bin_statistic, color = '#f4edf0', fontsize = 18,
                                                ax = axs['pitch'], ha = 'center', va = 'center',
                                                str_format = '{:.0%}', path_effects = path_eff)
                        
                    viz_info = teamOption + ' | ' + zonalOption
                    competition_info = 'NPL Queensland - 2022 season'
                    axs['title'].text(0.5, 0.6, viz_info, color = 'white',
                                    va = 'center', ha = 'center',
                                    fontproperties = robotto_bold, fontsize = 26)
                    axs['title'].text(0.5, 0, competition_info, color = 'white',
                                    va = 'center', ha = 'center',
                                    fontproperties = robotto_bold, fontsize = 18)

                    axs['pitch'].scatter(1, 102, s = 200, marker = "$→$",
                                color = "white", edgecolors = "white")
                    axs['pitch'].text(7.5, 101.5, 'Attacking direction', color = 'white', font_properties = robotto_bold, fontsize = 8, ha = 'center')

                    fig.set_facecolor('#050b31')
                    fig.set_figwidth(10.5)
                    fig.set_figheight(8)

                elif (zonalOption == 'Pass starting locations') or (zonalOption == 'Pass ending locations'):

                    passes_data = []

                    for file in events_list:
                        
                        with open(directory + file, encoding = 'utf-8') as jsonFile:
                            jsonData = json.load(jsonFile)
                            jsonFile.close()
                            
                        liveData = jsonData['liveData']
                        event = liveData['event']

                        for passes in event:
                            
                            isqualifier = False
                            isassist = 0
                            issecondassist = 0
                            
                            if ("contestantId" in passes) and (passes["contestantId"] == teamId):
                                
                                if (passes["typeId"] == 1):
                                    
                                    if ("assist" in passes) and (passes["assist"] == 1):
                                        isassist = 1
                                    
                                    if ("keyPass" in passes) and (passes["keyPass"] == 1):
                                        iskeypass = 1
                                    
                                    for qualifier in passes["qualifier"]:
                                        
                                        if (qualifier["qualifierId"] == 5) or (qualifier["qualifierId"] == 6):
                                            isqualifier = True
                                            break
                                            
                                        if (qualifier["qualifierId"] == 140):
                                            ending_x = float(qualifier["value"])
                                            
                                        if (qualifier["qualifierId"] == 141):
                                            ending_y = float(qualifier["value"])
                                    
                                    if (isqualifier == False):
                                        
                                        passes_period = passes["periodId"]
                                        passes_min = passes["timeMin"]
                                        passes_outcome = passes["outcome"]
                                        
                                        starting_x = passes["x"]
                                        starting_y = passes["y"]
                                        
                                        passes_data.append([passes_period, passes_min, passes_outcome, isassist, issecondassist, starting_x, starting_y, ending_x, ending_y])

                    xStart_coordinates = []
                    yStart_coordinates = []
                    xEnd_coordinates = []
                    yEnd_coordinates = []

                    for i in range(len(passes_data)):
                        xStart_coordinates.append(passes_data[i][5])
                        yStart_coordinates.append(passes_data[i][6])

                        xEnd_coordinates.append(passes_data[i][7])
                        yEnd_coordinates.append(passes_data[i][8])

                    pitch = Pitch(pitch_type = 'opta', pitch_color = '#050b31', line_zorder = 2, line_color = 'black')

                    fig, axs = pitch.grid(endnote_height = 0.03, endnote_space = 0,
                                        title_height = 0.08, title_space = 0,
                                        axis = False,
                                        grid_height = 0.84)

                    if (zonalOption == 'Pass starting locations'):
                        bin_statistic = pitch.bin_statistic(xStart_coordinates, yStart_coordinates, 
                                                statistic = 'count', bins = (3, 6), normalize = True)
                    elif (zonalOption == 'Pass ending locations'):
                        bin_statistic = pitch.bin_statistic(xEnd_coordinates, yEnd_coordinates, 
                                                statistic = 'count', bins = (3, 6), normalize = True)
                    heatmap = pitch.heatmap(bin_statistic, ax = axs['pitch'], cmap = 'coolwarm', edgecolors = 'black')
                    annotate = pitch.label_heatmap(bin_statistic, color = 'white', fontproperties = robotto_regular,
                                                    path_effects = path_eff, fontsize = 35, ax = axs['pitch'],
                                                    str_format = '{:.0%}', ha = 'center', va = 'center')

                    viz_info = teamOption + ' | ' + zonalOption
                    competition_info = 'NPL Queensland - 2022 season'
                    axs['title'].text(0.5, 0.6, viz_info, color = 'white',
                                    va = 'center', ha = 'center',
                                    fontproperties = robotto_bold, fontsize = 26)
                    axs['title'].text(0.5, 0, competition_info, color = 'white',
                                    va = 'center', ha = 'center',
                                    fontproperties = robotto_bold, fontsize = 18)

                    axs['pitch'].scatter(1, 102, s = 200, marker = "$→$",
                                color = "white", edgecolors = "white")
                    axs['pitch'].text(7.5, 101.5, 'Attacking direction', color = 'white', font_properties = robotto_bold, fontsize = 8, ha = 'center')

                    fig.set_facecolor('#050b31')
                    fig.set_figwidth(10.5)
                    fig.set_figheight(8)

        # Ask Streamlit to plot the figure
        st.pyplot(fig)