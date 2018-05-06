from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import widgetbox, layout, row, column
from bokeh.models import Div, Dropdown

import os
import re
import pandas as pd

file_path = os.path.dirname(os.path.abspath(__file__))


class ToolDesc:

    def __init__(self):

        self.rubric = pd.read_excel(os.path.join(file_path, "data/Rubric.xlsx"), "Rubric v3")

        self.tool_list = self.rubric.drop(["Category", "Criteria", "Grading Scale", "Definition"], axis=1).columns

        self.tool_dir = os.listdir(os.path.join(file_path, "static/images"))

        self.select_tool = Dropdown(menu=list(zip(self.tool_list, self.tool_list)),
                                    label="Choose Tool", button_type="primary")
        self.select_tool.on_change("value", self.select_callback)

        self.app_layout = layout(self.select_tool)

    def select_callback(self, attr, old, new):

        self.get_images(new)

    def get_images(self, tool):

        print(self.app_layout.children)

        tool_images = []

        for t in self.tool_dir:

            if t == tool:

                img_dir = os.path.join("app", "static/images", t)

                images = os.listdir(img_dir)
                y = [int(re.search(r"_(\d+)\.png$", i).group(1)) for i in images]
                img_path = [os.path.join(img_dir, i) for i in images]
                tool = [t, ]*len(images)

                tool_images.extend(list(zip(y, img_path)))

        div_layout = []

        for i in sorted(tool_images):

            div_layout.append(Div(text="<img src = '{}'>".format(i[1])))

        if len(self.app_layout.children) > 1:
            self.app_layout.children.pop(1)

        # except IndexError:

            # pass

        self.app_layout.children.append(layout(div_layout))