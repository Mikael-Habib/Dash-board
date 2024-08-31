from dash import Dash, html, dcc
import dash
import plotly.express as px

px.defaults.template = 'ggplot2' # String that is based on a famous library rgb plot 2

external_css = ['https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css',] # style various widgets of the dashboard Famous front end bootstrap

app = Dash(__name__ , pages_folder="pages", use_pages= True, external_stylesheets=external_css) # creating the Dash app

app.layout = html.Div ([
    html.Br(),
    html.P('Multi-Page-Dash-Plotly Web app',className = 'text-dark text-center fw-bold fs-1',style={'textAlign':'center'}),
    html.Div(children=[
        dcc.Link(page['name'],href = page['relative_path'],className='btn btn-dark m-2 fs-5')\
            for page in dash.page_registry.values()]
    ),
    dash.page_container
    ],className = 'col-8 mx-auto')

if __name__ =='__main__':
    app.run(debug=True)
