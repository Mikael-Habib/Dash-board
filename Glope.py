from dash import dcc, html, callback
import dash
import plotly.graph_objs as go
import pandas as pd


from dash.dependencies import Input,Output

dash.register_page(__name__, path = '/Glope', name= 'Glope',order = 7)
# Load the dataset
data = pd.read_csv("covid_19_clean_complete.csv")


# Create the choropleth map
fig = go.Figure(go.Scattergeo(
    locationmode='ISO-3',
    lon=data['Long'],  # Longitude column
    lat=data['Lat'],   # Latitude column
    text=data['Country/Region'],  # Hover info
    mode='markers',
    marker=dict(
        size=5,            # Marker size
        color='blue',       # Marker color
        line=dict(width=1, color='white'),  # Marker outline
    )))
fig.update_layout(
    title_text='Country lat and long',
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='orthographic',  # Globe projection
        showocean=True,
        oceancolor='rgb(204, 230, 255)',
        landcolor='rgb(217, 217, 217)',
        showland=True,
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'
))
layout = html.Div(children = [
    html.Br(),
    dcc.Graph(figure = fig)
    
 ])

