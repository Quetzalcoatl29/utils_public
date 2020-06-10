import dash
import dash_core_components as dcc
import dash_html_components as html




app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Dashboard con Plotly-Dash'),
    dcc.Graph(
        id='ejemplo 1',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Personal que se tomo del barandal'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Distancimiento social correcto'},
            ],
            'layout': {
                'title': 'Grafica de barras simple y linea con tags '
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)