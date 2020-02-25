import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
markdown_text = '''
### QUEST DASHBOARD
This is how quests are going for each student
'''
app.layout = html.Div([
    'Dylan Barton'
    app.layout = html.Div([
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
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=8,
        ),
    
	'Daniel Smalley'
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=5,
        ),

	'Stephen Griffith'
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=3,
        ),
  
'Dan Kurtz'
 'not questing'
    dcc.Slider(
    min=0,
    max=10,
    marks={2:'First Milestone',5:'Mid Milestone',8:'Last Milestone', 10:'Writeup Submitted' },
    value=0,
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