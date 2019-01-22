import ipywidgets as widgets
from ipywidgets import Layout
import cx_Oracle
import sqlalchemy
import glob
import pandas as pd
import sys
import os
import json
import pickle
from collections import Counter
from database import connect
#from params import params

###############################################################################
# To build the connectionstring properly, it's necessary to know the parameters
# like host, port and service name. In this case, this parameters are stored in
# the params.json file. Several other stuff like png's are also loaded.
###############################################################################

with open('params.json') as stream:
    params = json.load(stream)

with open("hwr_logo.png", "rb") as logo:
    image = logo.read()

with open('tasks', 'rb') as f:
    tasks = pickle.load(f)
    
prohibited_words = ['order by', 'desc', 'asc', 'group by']
    
###############################################################################
# Now the single elements like textboxes, buttons are initialized.
###############################################################################    

tab_nest = widgets.Tab(layout={'border': '2px solid tomato',
                               'width': '100%', 'height': '100%'})

user_name = widgets.Text(description='Username:', layout={'width': '30%'})
user_pw = widgets.Password(description='Password:', layout={'width': '30%'})

tab_login = widgets.VBox(children=[user_name, user_pw],
                         layout={'height': '100%'})

logo = widgets.Image(
    value=image,
    format='png',
    width='90%',
    height=350)

logo_box = widgets.VBox(children=[logo])

welcome_text = widgets.HTML(
    value='''Hi, melde dich einfach mit deiner Ora- Kennung
    + Passwort an und es kann los gehen!''', width='100%',
    height=400)
welcome_box = widgets.VBox(children=[welcome_text])

tab_welcome = widgets.HBox(children=[logo_box, welcome_box])

dropdown = widgets.Dropdown(
    options=[t for t in tasks], rows=15,
    description='Aufgabe:',
    disabled=False
)

chk_view = widgets.Output(width='100%', height='20px', rows=4)
chk_box = widgets.HBox(children=[chk_view])

check_button = widgets.Button(description='Check now!',
                              layout=Layout(width='50%', height='30px'))

query = widgets.Textarea(layout=Layout(width='100%', height='100px', rows=4))
query_input = widgets.HBox(children=[check_button])
ddown = widgets.HBox(children=[dropdown])
ddown_input = widgets.HBox(children=[ddown, query])

query_output = widgets.VBox(children=[tab_login, ddown_input,
                                      query_input, chk_box],
                            layout={'border': '2px solid tomato',
                                    'height': '100%'})

tab_nest.children = [tab_welcome, query_output]

tab_nest.set_title(0, 'Welcome')
tab_nest.set_title(1, 'Query Checker')


@chk_view.capture(clear_output=True)
def in_button_clicked(b):
    with chk_view:
        widgets.clear_output()

    user = user_name.value
    passwd = user_pw.value
    connect(user, passwd)

@chk_view.capture(clear_output=True)
def out_button_clicked(b):
    if os.path.isfile('constr.json'):
        os.remove('constr.json')

    print('file deleted or doesnt exist')


###############################################################################
# check() handles the proper connection. In this usecase it is a unique
# connection. That means every time the user clicks on the 'check' button, 
# a connection will be established. Perhaps it would be more common to use 
# a session object. But for this usecase it should be absolute sufficient.
# according to the underlying connection pooling mechanism,
# a connection object is returned to the connection pool at the end of the function.
# This function provides also the functionality to compare two result sets.
###############################################################################    

@chk_view.capture(clear_output=True)
def check():

    username = user_name.value
    password = user_pw.value    


    try:
        e = f'oracle+cx_oracle://{username}:{password}@{params["host"]}:{str(params["port"])}/?service_name={params["service_name"]}'
        constring = {"con": e}

        with open('constr.json', 'w') as file:
            json.dump(constring, file, default=str)

    except BaseException as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    try:
        dsn = cx_Oracle.makedsn(params['host'], str(params['port']), service_name=params['service_name'])
        db = sqlalchemy.create_engine('oracle+cx_oracle://'+username+':'+password+'@'+dsn)
        engine = db.connect()
    except BaseException:
        print('Unable to connect to the database. Check your network or user credentials.')

###############################################################################
# Now the connection object should be established. The next lines within
# this function provide the logic behind the comparison of two result sets 
# First, the sample resultset will be loaded. Then, the zip() function will
# transpose the 'unordered-list-of-unordered-lists'. 
# Next step is to check whether keywords like 
# i.e. "desc" (which will order the set in descending order) are used in the 
# query. If not, the transposed, unordered lists will sorted in both sets.
# The Counter() method counts how often a certain list occurs in both sets.
# In the end, the 'counts' for each set will be compared.
###############################################################################

    frame_as_list1 = tasks[dropdown.value]


    sql2 = f'''{query.value} '''
    frame2 = pd.read_sql_query(sql2, db)
    frame_as_list2 = frame2.values.tolist()
    
    
    trans1 = [list(i) for i in zip(*frame_as_list1)]
    trans2 = [list(i) for i in zip(*frame_as_list2)]
    
    ordered = False
    
    for wrds in prohibited_words:
        if contains_word(wrds, query.value):
            ordered = True
            return ordered

    
    if ordered is False:
        for lists in trans1:
            lists.sort()
            
        for lists in trans2:
            lists.sort()

    trans1 = map(tuple, trans1)
    trans2 = map(tuple, trans2)
    checked = Counter(trans2) == Counter(trans1)

    if checked is True:
        print('Sehr gut, Du hast das richtige Ergebnis!')
    else:
        print('Das war leider nicht das richtige Ergebnis.')

    engine.close()


###############################################################################
# The check_button_clicked function clears the prvious outputs and calls the
# check() function
###############################################################################    

@chk_view.capture(clear_output=True)
def check_button_clicked(b):

    with chk_view:
        widgets.clear_output()

    try:
        check()

    except:
        print('unanble to ckeck')

###############################################################################
# disp() is responsible for displaying the widget
###############################################################################           

def disp():
    display(tab_nest)

###############################################################################
# get_creds() is used to provide the connection string to work with the 
# sql-magic extension.
############################################################################### 

def get_creds():
    with open('constr.json', 'r') as stream:
        io = json.load(stream)
    return io

def contains_word(s, w):
    return f' {w} ' in f' {s} '


check_button.on_click(check_button_clicked)

