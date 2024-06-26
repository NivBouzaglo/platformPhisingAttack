import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots



data_arr = []


def arrange_by_department():
    global data_arr
    departments = {}
    x = []
    y = []
    for emp in data_arr:
        if emp['department'] in departments.keys():
            departments[emp['department']] += 1
        else:
            departments[emp['department']] = 1
    return [k for k in departments.keys()], [v for v in departments.values()]



def go_statistics():
    from main import num_of_emp
    global data_arr

    failed_emp = len(data_arr)
    succeeded_emp = num_of_emp - failed_emp
    if succeeded_emp < 0 :
        x1 = ['Failed']
        y1 = [failed_emp]
    else:
        x1 = ['Succeed', 'Failed']
        y1 = [succeeded_emp, failed_emp]
    x2, y2 = arrange_by_department()

    fig = make_subplots(rows=2, cols=1)

    fig.add_trace(
        go.Bar(x=x1, y=y1),
        row=1, col=1)

    fig.add_trace(
        go.Bar(x=x2, y=y2),
        row=2, col=1)

    fig.update_layout(
        title='Phishing Statistics ',
        height=600,
        width=800,
        barmode='group'  # Display bars side by side
    )

    fig.show(config={'displayModeBar': True})






def parse_data(file_path):
    global data_arr
    with open(file_path, 'r', encoding="utf8") as file:
        for line in file.readlines():
            current_dict = {}
            if "Name" in line:
                # Parse the JSON string into a dictionary
                line = line.strip()
                fields = line.split(",")
                for f in fields:
                    f = f.strip(' ').split(":")
                    current_dict[f[0].strip('"')] = f[1].strip('"')
                data_arr.append(current_dict)
        print(data_arr)



def show_statistics():
    """ Main function """
    downloads_path = os.path.expanduser("~/Downloads")  # fallback
    file_path = os.path.join(downloads_path, "data_from_website.txt")

    parse_data(file_path)

    # os.remove(file_path)
    #
    go_statistics()

