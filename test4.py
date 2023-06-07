import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    style={
        'background': 'linear-gradient(45deg, #ff00ff, #800080)',
        'height': '100vh',
        'padding': '20px',
        'color': 'white'
    },
    children=[
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("About", href="#")),
                dbc.NavItem(dbc.NavLink("KMS", href="#")),
                dbc.NavItem(dbc.NavLink("HSM", href="#")),
                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem("Item 1"),
                        dbc.DropdownMenuItem("Item 2")
                    ],
                    label="Dropdown",
                    nav=True
                )
            ],
            brand="Dashboard",
            brand_href="#",
            color="transparent",
            dark=True
        ),
        dbc.Row(
            style={'margin-top': '20px'},
            children=[
                dbc.Col(
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": "Servers", "id": "servers"}],
                        data=[{"servers": f"Server {i+1}"} for i in range(5)],
                        style_header={
                            'background-color': 'rgba(255, 255, 255, 0.15)',
                            'border': 'none',
                            'color': 'white',
                            'font-weight': 'bold',
                            'padding': '10px',
                            'box-shadow': '0 0 20px rgba(0, 0, 0, 0.1)',
                            'border-radius': '10px 10px 0 0'
                        },
                        style_cell={
                            'background-color': 'rgba(255, 255, 255, 0.15)',
                            'border': 'none',
                            'color': 'white',
                            'padding': '10px',
                            'box-shadow': '0 0 20px rgba(0, 0, 0, 0.1)',
                            'border-radius': '0 0 10px 10px',
                            'text-align': 'left',
                            'cursor': 'pointer'
                        },
                        style_as_list_view=True,
                        tooltip_data=[
                            {
                                column: {'value': str(value), 'type': 'markdown'}
                                for column, value in row.items()
                            } for row in [{'servers': 'Hover over the rows'}]
                        ]
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        style={
                            'background-color': 'rgba(255, 255, 255, 0.15)',
                            'border-radius': '10px',
                            'padding': '20px',
                            'box-shadow': '0 0 20px rgba(0, 0, 0, 0.1)',
                            'margin-left': '20px'
                        },
                        children=[
                            html.H5('Card 2'),
                            html.P('Card 2 content')
                        ]
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        style={
                            'background-color': 'rgba(255, 255, 255, 0.15)',
                            'border-radius': '10px',
                            'padding': '20px',
                            'box-shadow': '0 0 20px rgba(0, 0, 0, 0.1)'
                        },
                        children=[
                            html.H5('Card 3'),
                            html.P('Card 3 content')
                        ]
                    ),
                ),
            ],
            align='center',
        )
    ]
)


@app.callback(Output('table', 'style_data_conditional'),
              Input('table', 'derived_virtual_data'))
def update_table_styles(data):
    styles = []
    if data:
        styles.extend([
            {'if': {'row_index': i}, 'background-color': 'rgba(0, 0, 0, 0.2)', 'color': 'white'}
            for i in range(len(data))
        ])
    return styles


if __name__ == '__main__':
    app.run_server(debug=True)
