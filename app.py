import dash
import dash_core_components as dcc
import dash_html_components as html
from graph import f1
from graph import f2
from graph import f3
from graph import f4
from graph import f5

app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div([

#Row 1 heading

        html.Div([
          html.H1("", className='four columns'),
          html.H1("Homework 3 ", className='four columns'),
          html.H1("", className='four columns')
          ], className="row"),
#Row 2 First graph (barplot)
        html.Div([
          html.Div("Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does. Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:", className='three columns'),
          html.Div("The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected.", className='three columns'),
          html.Div([
              (dcc.Graph(id="figure_1", figure= f1,className='six columns'))
            ])
         ], className= "row"),
#Row 3 Second graph        
        html.Div([
          html.Div("One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.", className='three columns'),
          html.Div([
              (dcc.Graph(id="figure_2", figure= f2,className='six columns'))
            ]),
          html.Div("", className='three columns')
         ], className= "row"),
#Row 4 Boxplot and table
         html.Div([
          html.Div("The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected).", className='three columns'),
          html.Div([
              (dcc.Graph(id="figure_3", figure= f3,className='six columns'))
            ]),
          html.Div([
              (dcc.Graph(id="figure_4", figure= f4,className='three columns'))
            ])
         ], className= "row"),       

#Row 5 Roadmap
            html.Div([
          html.Div("Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap", className='three columns'),
          html.Div([
              (dcc.Graph(id="figure_5", figure= f5,className='seven columns'))
            ]),
          html.Div("", className='two columns')
         ], className= "row")




    ])

if __name__ == '__main__':

              app.run_server(debug=True)