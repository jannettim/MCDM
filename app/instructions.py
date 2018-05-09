from bokeh.models import ColumnDataSource, Paragraph, Div
from bokeh.layouts import widgetbox, layout


p_width = 500
header_font_size = 21
p_font_size = 12

open = Paragraph(text="Introduction for QDAS Assessment Toolkit", width=p_width, style={"font-size": "{}pt".format(header_font_size)})

intro_text = Div(text="""
This microsite provides a toolkit for comparing the pros and cons of 7 qualitative data analysis options:<br>
<blockquote>
&#8226 Atlas.ti<br>
&#8226 Dedoose<br>
&#8226 MAXQDA<br>
&#8226 Nvivo<br>
&#8226 QDA Miner<br>
&#8226 TOM <br>
&#8226 Transana<br>
</blockquote>

The toolkit includes 4 tools:<br>
<blockquote>
1. <b>Briefs</b> on 7 QDA software options<br>
2. A comprehensive, comparative <b>Features Checklist</b><br>
3. A <b>Scoring Rubric</b> for scoring performance on 16 dif)ferentiating features<br>
4. A <b>Multi-Criteria Decision-Making Model (MCDM</b> for helping the decision maker determine which features they value most, and which software is best based on their values<br>
</blockquote>
For more information, including a step-by-step tutorial for using the MCDM model please see the User Guide, here. Otherwise, a brief overview of the MCDM model is provided below.
""", width=p_width, style={"font-size": "{}pt".format(p_font_size)})

h1 = Paragraph(text="Multi-Criteria Decision Making (MCDM) Model", width=p_width,
               style={"font-size": "{}pt".format(header_font_size)})

mcdm_text = Div(text="""
<b>Step 1</b> Choose which of the 16 criteria is important to you:
<blockquote>
-       <b>Review</b> the best and worst performance on each criterion to understand the range of capabilities associated with each feature. These are listed on the next page and not on the website. Refer to this list as you complete the MCDM exercise<br>
-       To <b>select</b> multiple criteria, hold down the control key<br>
-       <b>Hit</b> ‘submit criteria’ after you’ve finished selecting all of the criteria you value<br>
</blockquote>
<b>Step 2</b> Rank Each Criterion using Swing-Weighting:
<blockquote>
-       <b>Review</b> each ‘best on one, worse on all else” scenarios. The best and worst values are shown in the tooltips by hovering over each cell<br>
-       <b>Rank</b> each scenario using the rank dropdowns<br>
-       <b>Hit</b> ‘calculate ranks’ to advance to the next step<br>
</blockquote>
<b>Step 3</b> Weight each scenario
<blockquote>
-       Use the slider to <b>weight</b> each scenario. The scenario ranked as 1 is automatically weighted at 100. Each successively ranked scenario is weighted can be weighted as less than or equal to the scenario preceding it. How much less preferable is this scenario in relation to this first? All weights are in relation to the<br>
-       Hit ‘update model’<br>
</blockquote>
<b>Step 4</b> Review results
""", width=p_width, style={"font-size": "{}pt".format(p_font_size)})

app_layout = layout([open,
                     intro_text,
                     h1,
                     mcdm_text])