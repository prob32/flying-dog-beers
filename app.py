
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.read_excel('domestic_shipment_predictions.xlsx')
df2 = df.set_index("Lookup")
#print(df2)
#print(df2.loc['Santa Clara, CAChicago IL, U.S.A.',5])
location_name = df['Home city'].unique()

familysizes = [1,2,3,4,5,6,7]

app.layout = html.Div(children=[
    html.H1(children='Shipping Estimates',
            style = {'color': colors['text']}
),
    html.Div(children='''
    Created by: Patrick Robinson.
'''),

#break
    html.Label('Home'),
    dcc.Dropdown(
        id='home',
        options=[{'label': i, 'value': i} for i in location_name],
        value='Atlanta GA, U.S.A.'
    ),


    #break
    html.Label('Host'),
    dcc.Dropdown(
        id='host',
        options=[{'label': i, 'value': i} for i in location_name],
        value='Austin TX, U.S.A.'
    ),

    #break
    html.Label('Family Size'),
    dcc.Dropdown(
        id='familysize',
        options=[{'label': i, 'value': i} for i in familysizes],
        value=1
    ),

    #output style/color
    html.H4(id='my-div3', style={'color': colors['text']}),
], style={'columnCount': 1},

)


@app.callback(
    Output(component_id='my-div3', component_property='children'),
    [Input(component_id='home', component_property='value'),
     Input(component_id='host', component_property='value'),
     Input(component_id='familysize', component_property='value')])

def update_output_div(home,host,familysize):
      x = home+host
      estimate = df2.loc[x,familysize]
      estimate= round(estimate,0)
      return 'Your estimate is {}'.format(estimate)

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)