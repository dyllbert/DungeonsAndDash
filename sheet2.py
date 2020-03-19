from My_Dash_Pack.My_Goog_Sub import get_my_data as goog
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime
import dash_table
import plotly.graph_objects as go


#Read data from csv on github
df = pd.read_csv('https://raw.githubusercontent.com/dyllbert/DungeonsAndDash/master/charSheetData.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/dyllbert/DungeonsAndDash/master/peopleDetails.csv')
colors = {
    'background': '#111111',
    'text': '#111111'
}
df['id'] = df['Name']

df2['id'] = df2['Name']
#df.set_index('id', inplace=True, drop=False)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4
    (
        children='People Info', 
        style=
        {
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dash_table.DataTable
    (
        id = 'datatable-row-ids',
        columns=[
            {'name': i, 'id': i} for i in df.columns
            if i != 'id'
        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        page_action='native',
    ),
    html.Div(id='datatable-row-ids-container')
])

@app.callback(
    Output('datatable-row-ids-container', 'children'),
    [Input('datatable-row-ids', 'derived_virtual_row_ids'),
     Input('datatable-row-ids', 'selected_row_ids'),
     Input('datatable-row-ids', 'active_cell')])
def update_graphs(row_ids, selected_row_ids, active_cell):
    if row_ids is None:
        dff = df
        # pandas Series works enough like a list for this to be OK
        row_ids = df['id']
    else:
        dff = df.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None
    #active_name = active_cell['']
    print(active_row_id)
    return [
       
    ]

if __name__ == '__main__':
    app.run_server(debug=True)