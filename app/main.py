import matplotlib
matplotlib.use('Agg')
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import show, curdoc
from bokeh.layouts import layout
import rubric
import interactive_mcdm
import features_checklist
import instructions
import tool_descriptions

doc = curdoc()

doc.title = "QDAS Assessment Toolkit"

rubric = rubric.p
mcdm = interactive_mcdm.app_layout
features = features_checklist.p
instr = instructions.app_layout
desc = tool_descriptions.ToolDesc().app_layout

instr_tab = Panel(child=instr, title="Introdcution")
tab3 = Panel(child=rubric, title="Rubric")
tab2 = Panel(child=features, title="Features Checklist")
tab4 = Panel(child=mcdm, title="MCDM")
tab1 = Panel(child=desc, title="Briefs")

tabs = Tabs(tabs=[instr_tab, tab1, tab2, tab3, tab4], width=475)


app_layout = layout([tabs])
doc.add_root(app_layout)
