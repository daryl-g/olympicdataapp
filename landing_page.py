# Import necessary libraries
import streamlit as st
from PIL import Image
from MultiPage import MultiPage
from pages import introductory, team_performance, matches_lastmatch, opposition_detailed, data_processing

st.set_page_config(
    page_title='Olympic FC Data App',
    layout="wide"
)

app = MultiPage()

col1, col2 = st.columns([1.1, 5])
image = Image.open('Olympic.png')

col1.image(image, width = 150, output_format = 'PNG')
col2.title("Olympic FC Data App")

app.add_page("Introduction", introductory.app)
app.add_page("Team", team_performance.app)
# app.add_page("Player - Individual", player_individual.app)
# app.add_page("Player - Comparison", player_statscompare.app)
app.add_page("Matches - Previous matches", matches_lastmatch.app)
# app.add_page("Matches - Last 5 matches", matches_last5.app)
# app.add_page("Opposition - Last match", opposition_overview.app)
app.add_page("Opposition - Last 5 matches", opposition_detailed.app)

app.run()