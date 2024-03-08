import json
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.subplots as ps
employees_data = []

def show_data_per_department(output_file):
    """"""
    global employees_data

    data_per_departments = {}  # {department: sum of failed employees from this department}

    for emp in employees_data:

        emp_department = emp['Department']

        if emp_department in data_per_departments.keys():
            data_per_departments[emp_department] = data_per_departments[emp_department] + 1

        else:
            data_per_departments[emp_department] = 1

    sorted_data_per_departments = dict(sorted(data_per_departments.items(), key=lambda item: item[1]))

    show_subplots(sorted_data_per_departments, emp)
    json.dump(sorted_data_per_departments, output_file)



def go_statistics():

    with open("parsed_data.json", "w") as output_file:
        # open an array in json file
        output_file.write("[\n")

        # Failed - per department
        show_data_per_department(output_file)

        # close the array in json file
        output_file.write("]\n")



def show_subplots(data, emp):

    departments = list(data.keys())
    employees = list(data.values())

    failed_count = sum(employees)
    total_employees = 100

    percent_failed = (failed_count / total_employees) * 100

    # Create bar graph
    fig = go.Figure(data=[go.Bar(x=departments, y=employees)])

    # Adding title and labels
    fig.update_layout(title='Number of Employees per Department',
                      xaxis_title='Department',
                      yaxis_title='Number of Employees',
                      width=1000, height=500,
                      margin=dict(b=100))  # Adding bottom margin for space

    # Add annotation for failed count
    fig.add_annotation(text=f'Failed: {failed_count} employees',
                       xref='paper', yref='paper',
                       x=0.05, y=0.9, showarrow=False)

    # Show the plot
    pio.show(fig)
    names = []
    departments = []
    for emp in employees_data:
        names.append(emp['Name'] )
        departments.append(emp["Department"])
    # Create a table to display additional details
    table_trace = go.Table(
        header=dict(values=['Name', 'Department']),
        cells=dict(values=[names,departments]),
    )

    # Add table to the figure
    table_figure = go.Figure(data=table_trace)

    # Show the table
    pio.show(table_figure)

def parse_data_from_json():
    """ Main function """
    global employees_data

    with open("data_from_website.json", 'r') as json_file:

        json_data = json.load(json_file)
        employees_data = json_data['employees_data']

        for row in employees_data:
            print(row)

        go_statistics()
