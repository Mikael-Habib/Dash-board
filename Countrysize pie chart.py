import pandas as pd
import dash
from dash import html, dcc, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/Countrysize-pie-chart', name='Countrysize',order = 6)

# Load dataset
country_wise_latest = pd.read_csv("country_wise_latest.csv")

# Dropdown options for countries
Country = country_wise_latest['Country/Region']
dd = dcc.Dropdown(id='dist_column', options=[{'label': c, 'value': c} for c in Country], value='Afghanistan', clearable=False)

# Page Layout
layout = html.Div(children=[
    html.Br(),
    html.P("Select Country: "),
    dd,
    dcc.Graph(id='pie_chart')
])

# Callback to update pie chart
@callback(Output("pie_chart", "figure"), [Input("dist_column", "value")])
def update_pie_chart(selected_country):
    # Filter the data for the selected country
    country_data = country_wise_latest[country_wise_latest['Country/Region'] == selected_country]

    # Create labels and values for the pie chart
    labels = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    values = country_data[['Confirmed', 'Deaths', 'Recovered', 'Active']].values.flatten()

    # Create pie chart
    fig = px.pie(values=values, names=labels, title=f'COVID-19 Cases Distribution in {selected_country}')
    
    return fig
