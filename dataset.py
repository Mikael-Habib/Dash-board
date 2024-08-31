import pandas as pd
import dash
from dash import dash_table
from dash import html,dcc,callback
from dash.dependencies import Input,Output
import plotly.graph_objects as go

dash.register_page(__name__,path ='/dataset',name = 'Dataset',order = 2 )

# Load datasets
country_wise_latest = pd.read_csv("country_wise_latest.csv")
covid_19_clean_complete = pd.read_csv("covid_19_clean_complete.csv")
day_wise = pd.read_csv("day_wise.csv")
worldometer_data = pd.read_csv("worldometer_data.csv")
usa_county_wise = pd.read_csv("usa_county_wise.csv")

# Define the list of datasets with consistent keys
Tables = {
    'Country Wise Latest': country_wise_latest,
    'COVID-19 Clean Complete': covid_19_clean_complete,
    'Day Wise': day_wise,
    'Worldometer Data': worldometer_data,
    'USA county wise':usa_county_wise
}
# Create the dropdown component
dd = dcc.Dropdown(
    id='Data Set DropDown',
    options=[{'label': k, 'value': k} for k in Tables.keys()],  # Use the dataset labels as options
    value='Country Wise Latest',  # Default value
    clearable=False,
    
)
# Define the page layout
layout = html.Div(children=[
    html.Br(),
    html.H2('Select Tables', style={'textAlign': 'center'}),
    dd,
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in Tables['Country Wise Latest'].columns],  # Initial column definitions
        data=Tables['Country Wise Latest'].to_dict('records'),  # Initial data
        page_size=20,
        style_cell={'background-color': 'lightgrey', 'border': 'solid 1px white', 'color': 'black'},
        style_header={'background-color': 'dodgerblue', 'font-weight': 'bold', 'color': 'black'}
    )
])

# Define the callback to update the table based on dropdown selection
@callback(
    Output('table', 'data'),
    Output('table', 'columns'),
    [Input('Data Set DropDown', 'value')]
)
def update_table(selected_dataset):
    # Retrieve the selected DataFrame
    df = Tables.get(selected_dataset)
    # Update the table columns and data
    columns = [{"name": i, "id": i} for i in df.columns]
    data = df.to_dict('records')
    
    return data, columns


