from dash import Dash, html, dcc, callback, Output, Input
from dash.dependencies import ALL
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

events = [
    {"date": "03/22", "title": "Ξεκίνησα δουλειά στο Wolfsburg", "type": "✔️", "category": "done"},
    {"date": "02/23", "title": "Αγόρασα το σπίτι στην Ελλάδα", "type": "🏡", "category": "real_estate"},
    {"date": "04/23", "title": "Άνοιξα επενδυτικό λογαριασμό & έκανα την πρώτη μου επένδυση", "type": "💰", "category": "finance"},
    {"date": "06/23", "title": "Πρώτη δόση για το σπίτι", "type": "💰", "category": "finance"},
    {"date": "11/24", "title": "Αλλαγή εργοδότη", "type": "💼", "category": "career"},
    {"date": "06/25", "title": "Milestone: 25.000€ σε επενδύσεις", "type": "💰", "category": "finance"},
    {"date": "2025", "title": "Στόχος: 2η στρατηγική επένδυσης (ETF + Real Estate)", "type": "🎯", "category": "goal"},
    {"date": "2026", "title": "Στόχος: Έναρξη παθητικού εισοδήματος", "type": "🎯", "category": "goal"},
    {"date": "06/27", "title": "Milestone: 50.000€ σε επενδύσεις", "type": "💰", "category": "finance"},
    {"date": "11/27", "title": "Ξεχρέωσα το σπίτι", "type": "🏡", "category": "real_estate"},
    {"date": "2028", "title": "Στόχος: 2ο ακίνητο & αναβάθμιση ρόλου", "type": "🎯", "category": "goal"},
    {"date": "2029", "title": "Στόχος: Προσωπικό brand ή επιχείρηση, sabbatical", "type": "🎯", "category": "goal"},
    {"date": "06/30", "title": "Milestone: 100.000€ σε επενδύσεις", "type": "💰", "category": "finance"},
    {"date": "2031", "title": "Στόχος: Επαγγελματική αυτονομία / Remote από Ελλάδα", "type": "🎯", "category": "goal"},
    {"date": "2032", "title": "Ολοκλήρωση 10ετούς πλάνου: ≥150.000€, 2 παθητικά εισοδήματα", "type": "🎯", "category": "goal"},
]

filters = [
    {"label": "Όλα", "value": "all"},
    {"label": "Οικονομικά", "value": "finance"},
    {"label": "Στόχοι", "value": "goal"},
    {"label": "Καριέρα", "value": "career"},
    {"label": "Ακίνητα", "value": "real_estate"},
    {"label": "Ολοκληρωμένα", "value": "done"},
]

# Βρίσκουμε μοναδικές χρονιές από τα δεδομένα
def extract_year(date_str):
    # date_str πχ "03/22" ή "2025" ή "06/27"
    if "/" in date_str:
        # πχ "03/22" -> 2022
        parts = date_str.split("/")
        year = parts[1]
        if len(year) == 2:
            year_full = "20" + year
            return year_full
        return year
    else:
        # πχ "2025"
        return date_str

years = sorted(set(extract_year(e["date"]) for e in events))
years_options = [{"label": y, "value": y} for y in years]
years_options.insert(0, {"label": "Όλα", "value": "all"})

app.layout = html.Div(
    [
        html.H1("📆 Timeline 2022–2032", style={"textAlign": "center", "marginBottom": "30px"}),
        # Φίλτρα κατηγορίας
        html.Div(
            [
                dbc.Button(
                    f["label"],
                    id={"type": "filter-button", "index": f["value"]},
                    color="primary",
                    outline=True,
                    className="me-2 mb-2",
                    n_clicks=0,
                )
                for f in filters
            ],
            style={"textAlign": "center", "marginBottom": "20px"},
        ),
        # Φίλτρο χρονιάς
        html.Div(
            dcc.Dropdown(
                id="year-filter",
                options=years_options,
                value="all",
                clearable=False,
                style={"width": "200px", "margin": "auto", "marginBottom": "50px"},
            )
        ),
        # Timeline container
        html.Div(
            id="timeline-container",
            style={
                "position": "relative",
                "padding": "40px 20px",
                "borderTop": "4px solid #ccc",
                "display": "flex",
                "justifyContent": "space-between",
                "minWidth": "900px",
                "overflowX": "auto",
            },
        ),
        dcc.Store(id="active-filter", data="all"),
        dcc.Interval(id="interval", interval=200, n_intervals=0, max_intervals=len(events)),
    ],
    style={"maxWidth": "1200px", "margin": "auto", "fontFamily": "Arial, sans-serif"},
)


@callback(
    Output("active-filter", "data"),
    [Input({"type": "filter-button", "index": ALL}, "n_clicks")],
    prevent_initial_call=True,
)
def update_filter(n_clicks_list):
    import dash
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        filter_value = eval(button_id)["index"]
        return filter_value


@callback(
    Output("timeline-container", "children"),
    [Input("active-filter", "data"), Input("year-filter", "value"), Input("interval", "n_intervals")],
)
def update_timeline(active_filter, year_filter, n_intervals):
    # Φιλτράρισμα κατηγορίας
    if active_filter == "all":
        filtered = events
    else:
        filtered = [e for e in events if e["category"] == active_filter]

    # Φιλτράρισμα χρονιάς
    if year_filter != "all":
        filtered = [e for e in filtered if extract_year(e["date"]) == year_filter]

    visible_events = filtered[: n_intervals + 1]

    items = []

    for idx, event in enumerate(filtered):
        is_visible = idx < len(visible_events)
        is_top = idx % 2 == 0
        style = {
            "minWidth": "150px",
            "maxWidth": "180px",
            "position": "relative",
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "opacity": 1 if is_visible else 0,
            "transform": "translateY(0)" if is_visible else ("translateY(-20px)" if is_top else "translateY(20px)"),
            "transition": "opacity 0.5s ease, transform 0.5s ease",
            "zIndex": 10,
            "margin": "0 10px",
        }
        connector_style = {
            "position": "absolute",
            "top": "24px",
            "left": "50%",
            "width": "2px",
            "backgroundColor": "#ccc",
            "transform": "translateX(-50%)",
            "height": "40px" if is_top else "60px",
            "zIndex": 5,
        }

        event_card = html.Div(
            [
                html.Div(event["type"], style={"fontSize": "24px", "marginBottom": "5px"}),
                html.Div(event["date"], style={"fontWeight": "600"}),
                html.Div(event["title"], style={"color": "#555", "fontSize": "14px", "marginTop": "5px"}),
            ],
            style={
                "backgroundColor": "white",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.15)",
                "borderRadius": "8px",
                "padding": "10px 15px",
                "maxWidth": "180px",
                "textAlign": "center",
                "marginBottom": "10px" if is_top else "0",
                "marginTop": "0" if is_top else "10px",
            },
        )

        items.append(
            html.Div(
                [
                    html.Div(style=connector_style),
                    event_card,
                ],
                style=style,
            )
        )

    return items


if __name__ == "__main__":
    app.run(debug=True)
