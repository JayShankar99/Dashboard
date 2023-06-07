import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Data for the area chart
x = [1, 2, 3, 4, 5]
y = [1, 3, 2, 4, 3]

# Create the area chart
area_chart = go.Figure(data=[go.Scatter(x=x, y=y, fill='tozeroy')])

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
                                    id='area-chart',
                                    figure=area_chart,
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
    app.run_server(debug=True)
