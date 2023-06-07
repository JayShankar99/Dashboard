from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from app import app
from apps import test3

Value = [
    dbc.Row(
        style={"margin-top":"20px"},
        children=[
            dbc.Col(
                children=[
                    dcc.Graph(
                        id='gauge-meter',
                        figure=test3.gauge_meter,
                        config={'displayModeBar': False},
                        style={'height': '300px', 'width': '100%'}
                        )
                    ]
            ),
            dbc.Col(
                children=[
                    dcc.Graph(
                        id="gauge-meter",
                        figure=test3.gauge_meter,
                        config={'displayModeBar':False},
                        style={'height':'300px', 'width':'100%'}
                    )
                ]
            ),
            dbc.Col(
                children=[
                    dcc.Graph(
                        id="gauge-meter",
                        figure=test3.gauge_meter,
                        config={'displayModeBar':False},
                        style={'height':'300px', 'width':'100%'}
                    )
                ]
            ),
            dbc.Col(
                children=[
                    dcc.Graph(
                        id="gauge-meter",
                        figure=test3.gauge_meter,
                        config={'displayModeBar':False},
                        style={'height':'300px', 'width':'100%'}
                    )
                ]
            )
        ]
    )
]