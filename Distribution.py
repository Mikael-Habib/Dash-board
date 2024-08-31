import pandas as pd 
import dash
from dash import html,dash_table,dcc,callback
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input,Output

dash.register_page(__name__,path = '/distribution',name= 'Distribution',order = 3)
#### Load DataSet ###
country_wise_latest = pd.read_csv("country_wise_latest.csv")
###### Histogram ####
def create_distribution(col_name = 'Confirmed'):
    return px.histogram (data_frame =country_wise_latest,x = col_name,height = 600 )
##### Widgets ####
columns =['Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered']
dd = dcc.Dropdown(id = 'dist_column',options = columns, value = 'Confirmed',clearable=False)
#####Page Layout ###
layout = html.Div(children = [
    html.Br(),
    html.P("Select Columns : "),
    dd,
    dcc.Graph(id = 'histogram')

])

####CallBacks######
@callback(Output("histogram", "figure"),[Input("dist_column", "value")])
def update_histogram(dist_column):
    return create_distribution(dist_column)