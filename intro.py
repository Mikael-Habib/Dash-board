import dash 
from dash import html

dash.register_page(__name__,path ='/',name = 'Introduction',order = 1)

######
layout = html.Div(children =[
    html.Div(children= [
        html.H2("Corona  dataset overview"),
        'Files included: Country wise latest, Covid 19 clean complete, day wise, full grouped, usa country wise and worldometer data',
        html.Br(),html.Br(),
    ]),
    html.Div(children = [
        html.Br(),
        html.H2("Columns in each file"),
        html.B("Country wise latest: "),'Country/Region , Confirmed , Deaths , Recovered , Active , New cases , New deaths , New recovered , Deaths / 100 cases , Recovered / 100 cases ,Deaths / 100 Recovered, Confirmed last week,1 week change, 1 week % increase,WHO Region',
        html.Br(), 
        html.B("covid_19_clean_complete"),'Province/State , Country/Region , Lat , Long , Date , Confirmed , Deaths , Recovered , Active , WHO Region',
        html.Br(),
        html.B("day_wise"),'Date,Confirmed,Deaths,Recovered,Active,New cases,New deaths,New recovered,Deaths / 100 Cases,Recovered / 100 Cases,Deaths / 100 Recovered,No. of countries',
        html.Br(),
        html.B("full_grouped"),'Date,Country/Region,Confirmed,Deaths,Recovered,Active,New cases,New deaths,New recovered,WHO Region',
        html.Br(),
        html.B("usa_county_wise"),'UID,iso2,iso3,code3,FIPS,Admin2,Province_State,Country_Region,Lat,Long_,Combined_Key,Date,Confirmed,Deaths',
        html.Br(),
        html.B('worldometer_data'),'Country/Region,Continent,Population,TotalCases,NewCases,TotalDeaths,NewDeaths,TotalRecovered,NewRecovered,ActiveCases,"Serious,Critical",Tot Cases/1M pop,Deaths/1M pop,TotalTests,Tests/1M pop,WHO Region'

    ])
],className = 'bg-Light p-4 m-2')