from datetime import date
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import datetime
import plotly.graph_objs as go

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Load the data from observation.csv into a pandas DataFrame
df = pd.read_csv('navigation.csv',parse_dates=["date_time"])  

# Define app layout
app.layout = html.Div([
    # Navbar with three buttons
    html.Nav([
        html.Ul([
            html.Li(html.A('Measurement Tab', href='#', id='measurement-tab')),
            html.Li(html.A('Map Tab', href='#', id='map-tab')),
            html.Li(html.A('Setting Tab', href='#', id='setting-tab'))
        ])
    ]),
    
    # Header with title
    html.H1('GNSS Data Visualization'),
    
    # Placeholder div for content
    html.Div(id='page-content')
])

# Define callback function for all tab clicks
@app.callback(Output('page-content', 'children'),
              
              [Input('measurement-tab', 'n_clicks'),
               Input('map-tab', 'n_clicks'),
               Input('setting-tab', 'n_clicks')])

def display_content(measurement_clicks, map_clicks, setting_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'measurement-tab'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'measurement-tab':
        return html.Div([
            html.H2('Measurement Tab'),
            # Insert measurement tab content here
                            # Left content goes here
                html.Div([
                    html.H3('Measurement Start Date Time Selector'),
                    html.Div([
                        html.Label('Date', style={'margin-right': '10px'}),
                        dcc.DatePickerSingle(
                            id='measurement-start-date',
                            date=date.today(),
                            style={'margin-right': '10px'}
                        ),
                        html.Label('Time', style={'margin-right': '10px'}),
                        dcc.Dropdown(
                            id='measurement-start-hour',
                            options=[{'label': f'{h:02d}', 'value': f'{h:02d}'} for h in range(0, 24)],
                            value='00',
                            placeholder='HH',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='measurement-start-minute',
                            options=[{'label': f'{m:02d}', 'value': f'{m:02d}'} for m in range(0, 60)],
                            value='00',
                            placeholder='MM',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='measurement-start-second',
                            options=[{'label': f'{s:02d}', 'value': f'{s:02d}'} for s in range(0, 60)],
                            value='00',
                            placeholder='SS',
                            style={'display': 'inline-block', 'width': 'auto'}
                        )
                    ], style={'display': 'flex', 'align-items': 'center'})
                ]),

                html.Div([
                    html.H3('Measurement Stop Date Time Selector'),
                    html.Div([
                        html.Label('Date', style={'margin-right': '10px'}),
                        dcc.DatePickerSingle(
                            id='measurement-stop-date',
                            date=date.today(),
                            style={'margin-right': '10px'}
                        ),
                        html.Label('Time', style={'margin-right': '10px'}),
                        dcc.Dropdown(
                            id='measurement-stop-hour',
                            options=[{'label': f'{h:02d}', 'value': f'{h:02d}'} for h in range(0, 24)],
                            value='00',
                            placeholder='HH',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='measurement-stop-minute',
                            options=[{'label': f'{m:02d}', 'value': f'{m:02d}'} for m in range(0, 60)],
                            value='00',
                            placeholder='MM',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='measurement-stop-second',
                            options=[{'label': f'{s:02d}', 'value': f'{s:02d}'} for s in range(0, 60)],
                            value='00',
                            placeholder='SS',
                            style={'display': 'inline-block', 'width': 'auto'}
                        )
                    ], style={'display': 'flex', 'align-items': 'center'}),
                ]),

                html.Div([
                    html.H3('Measurement Data Selector'),
                    dcc.Dropdown(
                        id='measurement-data-selector',
                        options=[
                            {'label': 'Longitude', 'value': 'longitude'},
                            {'label': 'Latitude', 'value': 'latitude'},
                            {'label': 'Altitude', 'value': 'altitude'}
                        ],
                        value='longitude',
                        style={'width': '200px', 'margin-right': '10px'}
                    ),
                    
                    # Add a callback for the plot button
                    html.Button('Plot', id='measurement-plot-button', n_clicks=0, style={'margin-top': '10px'}),

            # Add a Div to display the plot
            html.Div([
                dcc.Graph(id='measurement-plot-output', figure={}),
            ]),
        ])
    ]) 
    
    elif button_id == 'map-tab':
        return html.Div([
                html.H2('Map Tab'),
                # Insert measurement tab content here
                
                html.Div([
                    html.H3('Map Start Date Time Selector'),
                    html.Div([
                        html.Label('Date', style={'margin-right': '10px'}),
                        dcc.DatePickerSingle(
                            id='map-start-date',
                            date=date.today(),
                            style={'margin-right': '10px'}
                        ),
                        html.Label('Time', style={'margin-right': '10px'}),
                        dcc.Dropdown(
                            id='map-start-hour',
                            options=[{'label': f'{h:02d}', 'value': f'{h:02d}'} for h in range(0, 24)],
                            value='00',
                            placeholder='HH',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='map-start-minute',
                            options=[{'label': f'{m:02d}', 'value': f'{m:02d}'} for m in range(0, 60)],
                            value='00',
                            placeholder='MM',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='map-start-second',
                            options=[{'label': f'{s:02d}', 'value': f'{s:02d}'} for s in range(0, 60)],
                            value='00',
                            placeholder='SS',
                            style={'display': 'inline-block', 'width': 'auto'}
                        )
                    ], style={'display': 'flex', 'align-items': 'center'})
                ]),


                html.Div([
                    html.H3('Map Stop Date Time Selector'),
                    html.Div([
                        html.Label('Date', style={'margin-right': '10px'}),
                        dcc.DatePickerSingle(
                            id='map-stop-date',
                            date=date.today(),
                            style={'margin-right': '10px'}
                        ),
                        html.Label('Time', style={'margin-right': '10px'}),
                        dcc.Dropdown(
                            id='map-stop-hour',
                            options=[{'label': f'{h:02d}', 'value': f'{h:02d}'} for h in range(0, 24)],
                            value='00',
                            placeholder='HH',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='map-stop-minute',
                            options=[{'label': f'{m:02d}', 'value': f'{m:02d}'} for m in range(0, 60)],
                            value='00',
                            placeholder='MM',
                            style={'display': 'inline-block', 'width': 'auto'}
                        ),
                        html.Div(':', style={'display': 'inline-block', 'margin': '0px 5px'}),
                        dcc.Dropdown(
                            id='map-stop-second',
                            options=[{'label': f'{s:02d}', 'value': f'{s:02d}'} for s in range(0, 60)],
                            value='00',
                            placeholder='SS',
                            style={'display': 'inline-block', 'width': 'auto'}
                        )
                    ], style={'display': 'flex', 'align-items': 'center'}),
                ]),


                html.Button('Plot', id='map-plot-button', n_clicks=0),

                html.Div([
                    html.H3('Scatter Plot Map'),
                    dcc.Graph(
                        id='map-plot',
                        figure={
                            'data': [go.Scattermapbox(
                                lat=df['latitude'],
                                lon=df['longitude'],
                                mode='markers',
                                marker=dict(
                                    size=10,
                                    color='blue',
                                    opacity=0.7
                                ),
                                text=df['altitude'].astype(str) + ' m'
                            )],
                            'layout': go.Layout(
                                autosize=True,
                                hovermode='closest',
                                mapbox=dict(
                                    accesstoken='pk.eyJ1IjoidmNteWhvIiwiYSI6ImNsaGkyaTlkeTAzcWgzZ216bGgzaHJ6dDQifQ.xtkRv3tLh9OuhYIRtqrXLg',
                                    center=dict(
                                        lat=df['latitude'].mean(),
                                        lon=df['longitude'].mean()
                                    ),
                                    zoom=10
                                ),
                            )
                        }
                    )
                ])
            ])

    elif button_id == 'setting-tab':
        return html.Div([
            html.H2('Setting Tab'),
            # Insert setting tab content here
        ])
    
    else:
        return html.Div([
            html.H2('Welcome to the GNSS Data Visualization App'),
            # Insert welcome message or default content here
        ])
    
# Define callback function for "Plot" button click
@app.callback(Output('measurement-plot-output', 'figure'),
              [Input('measurement-plot-button', 'n_clicks')],
              [State('measurement-start-date', 'date'),
               State('measurement-start-hour', 'value'),
               State('measurement-start-minute', 'value'),
               State('measurement-start-second', 'value'),
               State('measurement-stop-date', 'date'),
               State('measurement-stop-hour', 'value'),
               State('measurement-stop-minute', 'value'),
               State('measurement-stop-second', 'value'),
               State('measurement-data-selector', 'value')])

def update_measurement_plot(n_clicks, start_date, start_hour, start_minute, 
                            start_second, stop_date, stop_hour, stop_minute, stop_second, data_type):
    start_time = datetime.datetime.combine(datetime.datetime.strptime(start_date, '%Y-%m-%d').date(), 
                                            datetime.time(int(start_hour), int(start_minute), int(start_second)))
    stop_time = datetime.datetime.combine(datetime.datetime.strptime(stop_date, '%Y-%m-%d').date(), 
                                            datetime.time(int(stop_hour), int(stop_minute), int(stop_second)))
    
    # Filter the DataFrame based on start and stop times
    df_filtered = df[(df['date_time'] >= start_time) & (df['date_time'] <= stop_time)]
    
    # Create a new figure based on the selected data type
    if data_type == 'longitude':
        fig = px.line(df_filtered, x='date_time', y='longitude')
        fig.update_layout(title='Longitude vs Time', xaxis_title='Time', yaxis_title='Longitude')
    elif data_type == 'latitude':
        fig = px.line(df_filtered, x='date_time', y='latitude')
        fig.update_layout(title='Latitude vs Time', xaxis_title='Time', yaxis_title='Latitude')
    elif data_type == 'altitude':
        fig = px.line(df_filtered, x='date_time', y='altitude')
        fig.update_layout(title='Altitude vs Time', xaxis_title='Time', yaxis_title='Altitude')
    else:
        fig = {}
    
    return fig

@app.callback(
    Output('map-plot', 'figure'),
    [Input('map-plot-button', 'n_clicks')],
    [State('map-start-date', 'date'),
     State('map-start-hour', 'value'),
     State('map-start-minute', 'value'),
     State('map-start-second', 'value'),
     State('map-stop-date', 'date'),
     State('map-stop-hour', 'value'),
     State('map-stop-minute', 'value'),
     State('map-stop-second', 'value')
    ] 
)

def update_map(n_clicks, start_date, start_hour, start_minute, start_second, stop_date, stop_hour, stop_minute, stop_second, df=df):
    start_time = datetime.datetime.combine(datetime.datetime.strptime(start_date, '%Y-%m-%d').date(), 
                                            datetime.time(int(start_hour), int(start_minute), int(start_second)))
    stop_time = datetime.datetime.combine(datetime.datetime.strptime(stop_date, '%Y-%m-%d').date(), 
                                            datetime.time(int(stop_hour), int(stop_minute), int(stop_second)))
    
    print("Start time:", start_time)
    print("Stop time:", stop_time)

    # Filter the DataFrame based on start and stop times
    df_filtered = df[(df['date_time'] >= start_time) & (df['date_time'] <= stop_time)]
    
    # Create a scattermapbox trace for the longitude and latitude data
    trace = go.Scattermapbox(
        lat=df_filtered['latitude'],
        lon=df_filtered['longitude'],
        mode='markers',
        marker=dict(
            size=10,
            color='blue',
            opacity=0.7
        ),
        text=df_filtered['altitude'].astype(str) + ' m'
    )

    # Create the layout for the map
    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken='pk.eyJ1IjoidmNteWhvIiwiYSI6ImNsaGkyaTlkeTAzcWgzZ216bGgzaHJ6dDQifQ.xtkRv3tLh9OuhYIRtqrXLg',
            center=dict(
                lat=df_filtered['latitude'].mean(),
                lon=df_filtered['longitude'].mean()
            ),
            zoom=10,
            style='open-street-map'
        ),
    )
    # Create the figure
    fig = go.Figure(data=[trace], layout=layout)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
