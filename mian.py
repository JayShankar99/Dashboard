from dash import Input, Output, State, html, dcc, dash_table
import dash_bootstrap_components as dbc

from app import app

import base64
import datetime
import io

import pandas as pd

import demo

content = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Upload(id='upload-data',
                    children=html.Div(['Drag and Drop or ',
                            html.A('Select File')
                            ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            }
                ),
            ])
        ], justify="center", align="center", className="h-50"), #, justify="center", align="center", className="h-50"

        html.Div(id="status"),

        dbc.Row([
            dbc.Col([
                dbc.Button("Analyse", color="primary", className="me-1"),
            ], width={'size':6, 'offset':5} ),
        ],style={'margin-top':'10px'})

], style={"height":'100vh'})


# --------------------- Display conten ------------------#

app.layout = html.Div(
    children=[
    content
    ]
)


# ------------------------------- Call-back -------------------------

@app.callback(Output('status','children'),
              Input('upload-data','contents'),
              State('upload-data','filename'),
              State('upload-data','last_modified'))

def data(content, filename, lastmodified):
    if content:
        content_type, content_string = content.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                result = [
                        dbc.Row(id="status",
                        children=[html.B("File uploaded sucessfully!")],
                        style={"border-radius":'25px', 'height':'50px', 'background':'#00ff9c', 'padding':'10px'}), 
                    ]
                
                df = pd.read_csv(
                    io.StringIO(decoded.decode('unicode_escape')))
                demo.data(df)
            elif 'xls' in filename:
                result = [
                        dbc.Row(id="status",
                        children=[html.B("File uploaded sucessfully!")],
                        style={"border-radius":'25px', 'height':'50px', 'background':'#00ff9c', 'padding':'10px'}), 
                    ]
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                result = [
                dbc.Row(id="status",
                children=[html.B("File uploaded Failed!")],
                style={"border-radius":'25px', 'height':'50px', 'background':'#C85250', 'padding':'10px'}), 
            ]
                
        except Exception as e:
            print(e)
            result = [
                dbc.Row(id="status",
                children=[html.B("File uploaded Failed!")],
                style={"border-radius":'25px', 'height':'50px', 'background':'#C85250', 'padding':'10px'}), 
            ]
            return result 
        return result 


if __name__ == "__main__":
    app.run_server(debug=True)