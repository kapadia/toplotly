
import os
import json
from dateutil.parser import parse

import plotly
from plotly.graph_objs import Histogram, Scatter, Scatter3d, Data, Layout, XAxis, YAxis, ZAxis, Figure


__version__ = '0.0.1'


def is_numeric(x):
    
    try:
        float(x)
        return True
    except ValueError:
        return False


def is_date(d):
    
    try:
        parse(d)
        return True
    except ValueError, AttributeError:
        return False


def is_string(x):
    return is_numeric(x) + is_date(x) == 0


def format_data(data):
    
    data = json.loads(''.join(data))
    
    keys = data[0].keys()
    
    # Check column type
    sidx = [ idx for idx, key in enumerate(keys) if is_string(data[0][key]) ]
    
    values = [ [ d.get(key) for key in keys ] for d in data ]
    values = zip(*values)
    
    if len(sidx) == 1:
        text = values.pop(sidx[0])
        keys.pop(sidx[0])
    else:
        text = None
    
    return {
        'layout': {
            'axes': keys
        },
        'data': {
            'values': values,
            'text': text
        }
    }


def get_histogram(data):
    
    values = data['values']
    return Data([
        Histogram(
            x=values
        )
    ])


def get_scatter2d(data):
    
    values = data['values']
    return Data([
        Scatter(
            x=values[0],
            y=values[1],
            mode='markers',
            text=data['text']
        )
    ])


def get_scatter3d(data):
    
    values = data['values']
    return Data([
        Scatter3d(
            x=values[0],
            y=values[1],
            z=values[2]
        )
    ])


def post(filename, data, fileopt='new', title=None, world_readable=True):
    
    # Get username and api key
    username = os.environ.get('PLOTLY_USERNAME')
    api_key = os.environ.get('PLOTLY_API_KEY')
    
    plotly.tools.set_credentials_file(username=username, api_key=api_key)
    
    axes = data['layout']['axes']
    
    nAxes = len(axes)
    
    get_data = {
        1: get_histogram,
        2: get_scatter2d,
        3: get_scatter3d
    }
    
    axes_kwargs = ['xaxis', 'yaxis', 'zaxis']
    axes_obj = [XAxis, YAxis, ZAxis]
    
    layout_kwargs = { axes_kwargs[idx]: axes_obj[idx](title=axis) for idx, axis in enumerate(axes) }
    dataobj = get_data[nAxes](data['data'])
    layout = Layout(**layout_kwargs)
    
    fig = Figure(data=dataobj, layout=layout)
    print fig
    
    # r = plotly.plotly.plot(fig, filename=filename)
    # print r
    
    