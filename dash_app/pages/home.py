# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc


# Define the page layout
layout = dbc.Container([

    dbc.Row([
        html.Br(),
        html.Hr(),
        html.H2('Confluence'),
        dbc.Row([
            dbc.Col(
                [
                    html.P("""
        est un outil qui vous permet de mesurer en temps réel l'audience de
        vos influenceurs pour vos campagnes marketing et vos placements de produit.
        Accédez à la meilleure base de données d'influenceurs et aux meilleurs outils de gestion.
        """)
                ]
            ),

            dbc.Col(
                    [
                        dbc.Form(   
                                    dbc.Row(
                                        
                                        [
                                            
                                            dbc.Col(
                                                dbc.Input(type="email", placeholder="Entreprise"),
                                                className="me-3",
                                            ),
                                            
                                            dbc.Col(
                                                dbc.Input(type="password", placeholder="Email"),
                                                className="me-3",
                                            ),
                                            dbc.Col(dbc.Button("Oui je veux!", color="primary"), width="auto"),
                                        ],
                                        className="g-2",
                                    )
                                )
                    ]
                )
            ]),
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4("youtube", className="card-title"),
                        html.P(
                            className="card-text",
                        ),
                    ]
                ),
                dbc.CardImg(src="/assets/youtubex.png", top=True),
            ],
            style={"width": "20rem"},
        ),
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4("tik tok", className="card-title"),
                        html.P(
                            className="card-text",
                        ),
                    ]
                ),
                dbc.CardImg(src="/assets/tiktokx.png", top=True),
            ],
            style={"width": "20rem"},
        ),
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4("instagram", className="card-title"),
                        html.P(
                            className="card-text",
                        ),
                    ]
                ),
                dbc.CardImg(src="/assets/instagramx.png", top=True),
            ],
            style={"width": "20rem"},
        ),
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4("facebook", className="card-title"),
                        html.P(
                            className="card-text",
                        ),
                    ]
                ),
                dbc.CardImg(src="/assets/facebookx.png", top=True),
            ],
            style={"width": "20rem"},
        ),
    ])
])
