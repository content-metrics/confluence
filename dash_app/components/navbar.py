# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("home", href="/home")),
                dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            ] ,
            brand="Confluence",
            brand_href="/home",
            color="dark",
            dark=True,
        ), 
    ])

    return layout