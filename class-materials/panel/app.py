# %%
import bw2io as bi
import bw2data as bd
import bw2calc as bc
from bw_graph_tools import NewNodeEachVisitGraphTraversal
import pandas as pd
import panel as pn

#https://panel.holoviz.org/developer_guide/extensions.html#extension-plugins
pn.extension()

# BRIGHTAY SETUP ################################################################

def check_for_useeio_brightway_project():
    if 'USEEIO-1.1' not in bd.projects:
        bi.install_project(project_key="USEEIO-1.1", overwrite_existing=True)
    bd.projects.set_current(name='USEEIO-1.1')
    useeio = bd.Database("USEEIO-1.1")
    return useeio

useeio = check_for_useeio_brightway_project()

# PANEL SETUP ###################################################################

search_string =''
lca_score = 0
df_activities = pd.DataFrame()

# https://panel.holoviz.org/reference/widgets/TextInput.html
widget_text_input = pn.widgets.TextInput(
    name='Text Input',
    placeholder='Enter a search string here...'
)

# https://panel.holoviz.org/reference/widgets/Button.html
widget_button = pn.widgets.Button(
    name='Click me to calculate LCA score!',
    button_type='primary'
)

# https://panel.holoviz.org/reference/widgets/StaticText.html
widget_static_text = pn.widgets.StaticText(
    name='Selected Database Activity',
    value="Nothing yet"
)

# https://panel.holoviz.org/reference/panes/DataFrame.html
widget_df = pn.widgets.DataFrame(
    df_activities,
    name='DataFrame'
)

# https://panel.holoviz.org/reference/indicators/Dial.html
widget_dial = pn.indicators.Dial(name='LCA Score', value=lca_score, bounds=(0, 1), format='{value} kg(CO2)')

pn.indicators.Dial(
    name='Engine', value=2500, bounds=(0, 3000), 
    colors=[(0.2, 'green'), (0.8, 'gold'), (1, 'red')]
)

# CALCULATION FUNCTIONS ######################################################


def select_database_activity(search_string):
    # https://docs.brightway.dev/en/latest/content/gettingstarted/objects.html#object-selection
    selected_activity = [
        node for node in useeio
        if search_string in node['name'].lower()
        and 'product' in node['type']
    ][0] # this just selects the first element in the list
    return selected_activity


def perform_lca_and_path_analysis(
    selected_activity,
) -> pd.DataFrame:
    # https://docs.brightway.dev/en/latest/content/gettingstarted/lca.html#calculate-one-lcia-result
    lca = bc.LCA(
        demand={selected_activity: 1},
        method=('Impact Potential', 'GCC') # global climate change
    )
    lca.lci()
    lca.lcia()
    lca_score = round(lca.score,2)

    # https://docs.brightway.dev/projects/graphtools/en/latest/content/api/bw_graph_tools/graph_traversal/index.html#bw_graph_tools.graph_traversal.NewNodeEachVisitGraphTraversal
    graph_traversal_result = NewNodeEachVisitGraphTraversal.calculate(lca, cutoff=0.01)

    return lca_score, pd.DataFrame.from_dict(graph_traversal_result['nodes'], orient='index')

# INTERACTIVE ELEMENTS #######################################################

def update_interactive_elements(event):
    selected_activity = select_database_activity(search_string=widget_text_input.value)
    widget_static_text.value = selected_activity['name']
    lca_score, df_activities = perform_lca_and_path_analysis(selected_activity=selected_activity)
    widget_df.value = df_activities
    widget_dial.value = lca_score


# https://panel.holoviz.org/reference/widgets/Button.html#buttonhttps://panel.holoviz.org/reference/widgets/Button.html#button
widget_button.on_click(update_interactive_elements)

# https://panel.holoviz.org/reference/layouts/Column.html
pn.Column(
    widget_text_input,
    widget_button,
    widget_static_text,
    widget_df,
    widget_dial
).servable()