from My_Dash_Pack.My_Goog_Sub import get_my_data as goog
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime
import dash_table


#Read data from csv on github
df = pd.read_csv('https://raw.githubusercontent.com/dyllbert/DungeonsAndDash/master/charSheetData.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/dyllbert/DungeonsAndDash/master/form.csv')

#Google stuff, not currently using
#rangebits= 'Form Responses 1!1:4'
#df2=pd.DataFrame(goog.sheetinfo(rangebits))
#names=df2[1]

#print(df)
#data = pd.DataFrame(df)
#names = data[1]


#To activate (dylan):source dashenv/bin/activate after navigating out of the dungeons and dash folder
#to deactivate: deactivate




def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


#Start Dash

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#111111'
}

app.layout = html.Div(
children=
[
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
        id='overview',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        page_action='native',
    ),

    html.Hr(),

    html.Div(id = 'selected-name'),

    dash_table.DataTable
    (
        id='detail',
        columns=[{'name': i, 'id': i} for i in df2.columns],
        data=df2.to_dict('records2'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        page_action='native',
        
    ),

])

@app.callback(Output('selected-name', 'children'),
              [Input('overview', 'active_cell'),
               Input('overview', 'data'),
               Input('overview', 'derived_virtual_row_ids'),
               Input('overview', 'selected_row_ids')])
def get_active_letter(active_cell, data, row_id, selected):
    if not active_cell:
        return df.iloc[0,0]
    if active_cell:
        r = active_cell['row']
        c = active_cell['column']
        return str(df.iloc[r,c])


if __name__ == '__main__':
    app.run_server(debug=True)