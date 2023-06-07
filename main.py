from dash import Dash, Input, Output, html, dcc 
import dash_bootstrap_components as dbc

from app import app
from app import server

from apps import homepage

# NAVBAR

navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("Home", href="/", active='exact')),
    dbc.NavItem(dbc.NavLink("About", href="#")),
    dbc.NavItem(dbc.NavLink("KMS",href="#")),
    dbc.DropdownMenu([
        dbc.DropdownMenuItem("Item 1"),
        dbc.DropdownMenuItem("Item 2")
    ],
    label="Dropdown",
    nav=True,    
    )
],
brand="Dashboard",
brand_href="#",
color='#526D82',
dark=True
)



# Content

display_content = dbc.Container(id="display-page", children=[], fluid=True)


# Layout

app.layout = html.Div(style={'height':'100vh',
                             'color':'Black',
                             'padding':'20px'
                             },
    children=[
        dcc.Location(id="url"),
        navbar, display_content
    ]
)

# Call-backs

@app.callback(Output("display-page","children"),
              Input("url","pathname"))

def page_render(pathname):
    if pathname == "/":
        return homepage.Value



if __name__ == "__main__":
    app.run_server(debug=True, port=8080)