import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
markdown_text = '''
### EHL Quests
(an update)
'''


app.layout = html.Div(
   
    html.H1('Heading', style={'backgroundColor':'blue'},
    
    [
    dcc.Markdown(children=markdown_text),
    html.Label('Researchers'),
    dcc.Dropdown(
        options=[
            {'label': 'Dylan Barton', 'value': 'DCB'},
            {'label': u'Daniel Smalley', 'value': 'DS'},
            {'label': 'Wes Rodgers', 'value': 'WR'},
            {'label': 'Annie Lastname', 'value': "AL"}
        ],
        value='MTL'
    ),
    html.Img(src=app.get_asset_url('dylan2.png')),   
    html.Div(html.P("Dylan")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=5,
        ),
    html.Img(src=app.get_asset_url('caitlin.png')),
    html.Div(html.P("Caitlin")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=3,
        ),
    
    html.Div(html.P("Dan")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=8,
        ),
    
    html.Div(html.P("Mitchell")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=5,
        ),
   
    html.Div(html.P("Ximena")),
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=8,
        ),
  
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    )
])
if __name__ == '__main__':
    app.run_server(debug='True')