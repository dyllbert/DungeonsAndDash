import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/desmalley/cuddly-garbanzo/master/dnd_data.csv')


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

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#111111'
}



#'background-image': 'url("/assets/back2.jpg")',
#'background-repeat': 'no-repeat',
#'background-position': 'right top',
#'height': '500px',
#'background-size': 'cover'

#'background-image': 'linear-gradient(red, black)'



app.layout = html.Div(style={
'background-image': 'url("/assets/b1.png")',
'background-repeat': 'no-repeat',
'background-position': 'right top',
'height': '500px',
'background-size': 'cover'

}, children=[
        html.H4(children='Stats'),
    generate_table(df),
    html.H1(
        children='EHL Quest Dashboard', 
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='''
        A web dashboard for EHL quest support.
    '''),
    
    html.Img(src=app.get_asset_url('dylan2.png')),   
    html.Div(html.P("___Dylan")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=5,
        ),
    html.Img(src=app.get_asset_url('caitlin.png')),
    html.Div(html.P("___Caitlin")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=3,
        )
    

])

if __name__ == '__main__':
    app.run_server(debug=True)