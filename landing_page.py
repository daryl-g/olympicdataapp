# Import necessary libraries
import streamlit as st
from PIL import Image
# from MultiPage import MultiPage
# from pages import introductory, team_performance, matches_lastmatch, opposition_detailed, data_processing

st.set_page_config(
    page_title='Olympic FC Data App',
    layout="wide"
)

# app = MultiPage()

col1, col2 = st.columns([1.1, 5])
image = Image.open('Olympic.png')

col1.image(image, width = 150, output_format = 'PNG')
col2.title("Olympic FC Data App")

# app.add_page("Introduction", introductory.app)
# app.add_page("Team", team_performance.app)
# app.add_page("Player - Individual", player_individual.app)
# app.add_page("Player - Comparison", player_statscompare.app)
# app.add_page("Matches - Previous matches", matches_lastmatch.app)
# app.add_page("Matches - Last 5 matches", matches_last5.app)
# app.add_page("Opposition - Last match", opposition_overview.app)
# app.add_page("Opposition - Last 5 matches", opposition_detailed.app)

st.markdown("Navigate through the app using the widget on the left.")
st.markdown(
    "-Choose **Team** to see data and visualisations of Olympic and other teams in the league.")
st.markdown(
    "-Choose **Player** to see data and visualisations of Olympic's players and players of other teams.")
st.markdown("-Choose **Opposition** to see an overview and a detailed view of Olympic's upcoming opposition through data and visualisations.")

# app.run()