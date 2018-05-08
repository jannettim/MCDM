from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import widgetbox, layout, row, column
from bokeh.models import Div, Dropdown, Paragraph

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

        tool_images = []

        for t in self.tool_dir:

            if t == tool:

                img_dir = os.path.join("app/static/images", t)
                txt_dir = os.path.join("app/static/text", t)

                images = os.listdir(img_dir)
                texts = os.listdir(txt_dir)

                y = [int(re.search(r"_(\d+)\.(png|txt)$", i).group(1)) for i in images]
                y += [int(re.search(r"_(\d+)\.(png|txt)$", i).group(1)) for i in texts if i != ".gitignore"]
                img_path = [os.path.join(img_dir, i) for i in images]
                txt_path = [os.path.join(txt_dir, i) for i in texts]

                all_files = img_path + txt_path

                tool_images.extend(list(zip(y, all_files)))

        div_layout = []

        count = 0

        #434343

        for i in sorted(tool_images):

            file_type = re.search(r"\.(png|txt)$", i[1]).group(1)

            if file_type == "txt":

                try:
                    head = re.search(r"_(h\d)_", i[1]).group(1)
                except AttributeError:

                    head = None

                if head == "h1":

                    font_size = 26

                elif head == "h2":

                    font_size = 20

                elif head == "h3":

                    font_size = 14

                else:

                    font_size = 11

                with open(i[1], "r") as rf:

                    txt = rf.read()

                div_layout.append(Div(text=txt, style={"font-size": "{}pt".format(font_size)}, width=500))
            else:

                div_layout.append(Div(text="<img src = '{}'>".format(i[1])))

        if len(self.app_layout.children) > 1:
            self.app_layout.children.pop(1)

        # except IndexError:

            # pass

        self.app_layout.children.append(layout(div_layout))

if __name__ == '__main__':
    td = ToolDesc()
    td.get_images("MAXQDA")