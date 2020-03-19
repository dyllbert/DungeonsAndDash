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
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": name, "id": name} for name in df.columns],
        data=df.to_dict("rows"),
        editable=True,
    ),
    html.H3(
    id='text-output',
    children='',
    style={'textAlign': 'left'}
    )
])

@app.callback(  Output('text-output', 'children'),
                [Input('table', 'data_timestamp'),
                 Input('table', 'active_cell'),
                 Input('table', 'data')])
def get_active_cell_value (timestamp, active_cell, data):
    active_cell_row_index = 'NA '
    active_cell_column_index = 'NA '
    active_cell_value = 'NA '
    if active_cell:
        active_cell_row_index = 'RowIndex: ' + str(active_cell[0])
        active_cell_column_index = '    ColumnIndex: ' + str(active_cell[1])
        # not working for column index
        # active_cell_value = '  CellValue: ' + str(data[active_cell[0]][active_cell[1]]) 
        # working for column name
        active_cell_value = '    UpdatedCellValue: ' + str(data[active_cell[0]]['State']) 
        # how to dynamically get active cell value?
    return active_cell_row_index, active_cell_column_index, active_cell_value

if __name__ == '__main__':
    app.run_server(debug=True)