import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the gauge meter
gauge_meter = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=80,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': 'darkblue'},
            'steps': [
                {'range': [0, 20], 'color': 'lightgray'},
                {'range': [20, 50], 'color': 'gray'}
            ],
            'threshold': {
                'line': {'color': 'red', 'width': 4},
                'thickness': 0.75,
                'value': 70
            }
        }
    )
)

app.layout = html.Div(
    style={
        'background': 'linear-gradient(45deg, #ff00ff, #800080)',
        'height': '100vh',
        'padding': '20px',
        'color': 'white'
    },
    children=[
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Card 1", className="card-title"),
                                dcc.Graph(
                                    id='gauge-meter',
                                    figure=gauge_meter,
                                    config={'displayModeBar': False},
                                    style={'height': '300px', 'width': '100%'}
                                )
                            ]
                        ),
                        className="glassmorphism",
                        style={'margin': 0, 'padding': '10px'}
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Card 2", className="card-title"),
                                html.P("Card 2 content")
                            ]
                        ),
                        className="glassmorphism",
                        style={'margin': 0, 'padding': '10px'}
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Card 3", className="card-title"),
                                html.P("Card 3 content")
                            ]
                        ),
                        className="glassmorphism",
                        style={'margin': 0, 'padding': '10px'}
                    )
                ),
            ],
            className="justify-content-center"
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
