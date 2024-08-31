import pandas as pd
import dash
from dash import html, dcc, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Register the Dash page
dash.register_page(__name__, path='/populationVsTotalCases', name='Population Vs Total Cases',order = 4)

# Load dataset
worldometer_data = pd.read_csv("worldometer_data.csv")

# Dropdown options for countries
Country = worldometer_data['Country/Region']
dd = dcc.Dropdown(id='dist_column', 
                  options=[{'label': c, 'value': c} for c in Country], 
                  value='USA', 
                  clearable=False)

# Page Layout
layout = html.Div(children=[
    html.Br(),
    html.H2("Population vs Total Cases from Worldometer_data", style={'textAlign': 'center'}),
    html.P("Select Country: "),
    dd,
    dcc.Graph(id='bar_chart')
])

# Callback to update bar chart
@callback(Output("bar_chart", "figure"), [Input("dist_column", "value")])
def update_bar_chart(selected_country):
    # Filter the data for the selected country
    country_data = worldometer_data[worldometer_data['Country/Region'] == selected_country]
    
    # Data for the bar chart
    labels = ['Population','Total Cases']
    values = [country_data['Population'].iloc[0],country_data['TotalCases'].iloc[0]]
    
    # Create bar chart
    fig = px.bar(x=labels, y=values, title=f'Population vs Total Cases in {selected_country}')
    
    fig.update_layout(
        yaxis_title="Population",
        xaxis_title="Total Cases",
        height=400
    )
    
    return fig
