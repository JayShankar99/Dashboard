import dash
from dash import Input, Output, State, html, dcc, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

# Set up the background color
app.layout = html.Div(className="test",
    style={
        "background-image": "linear-gradient(to right, #AA076B, #61045F)",
    },
    children=[
        # Create a card
        dbc.Card(
            style={
                "width": "50%",
                "height": "50%",
                "border-radius": "10px",
                "box-shadow": "0 0 10px 0px rgba(196, 196, 196, 32%)",
                "border": "1px solid black",
                "filter": "blur(1px)",
            },
            children=[
                # Add some text to the card
                html.H3("This is a card"),
                html.P("This is some text inside the card."),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)