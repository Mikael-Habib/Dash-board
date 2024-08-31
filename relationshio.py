import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input,Output

dash.register_page(__name__, path = '/relationship', name= 'Relationship',order = 5)

#### DataSet ###
country_wise_latest = pd.read_csv("country_wise_latest.csv")

####Scatter Chart####
def create_scatter_chart(x_axis = 'Confirmed',y_axis= 'Deaths'):
    return px.scatter(data_frame = country_wise_latest , x = x_axis , y = y_axis , height = 600)

###Widgets ####
columns =['Confirmed','Deaths','Recovered','Active']
x_axis = dcc.Dropdown(id = 'x_axis', options = columns, value = 'Confirmed',clearable= False)
y_axis = dcc.Dropdown(id ='y_axis', options = columns, value = 'Deaths',clearable= False)
### PAge Layout ####
layout = html.Div(children = [
    html.Br(),
    'X-Axis', x_axis ,
    'Y-Axis', y_axis ,
    dcc.Graph(id = 'scatter')
])
####CallBacks######
@callback(Output("scatter", "figure"),[Input("x_axis", "value"),Input("y_axis",'value')])
def update_scatter_chart(x_axis,y_axis):
    return create_scatter_chart(x_axis,y_axis)