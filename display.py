import os
import plotly.express as px

def display_results(dir):
    data = []
    labels = []
    for path in os.listdir(dir):
        if 'results.txt' in path:
            name = path.split('.')
            file = open(path, 'r')
            string = file.readline()
            strings = string.split()
            data.append(strings[2])
            labels.append(name[0])
    print(data)
    print(labels)
    fig = px.bar(x = labels, y = data, title = 'Similarity of SARS-CoV-2', labels = {'x':'Virus', 'y':'Percent'})
    fig.show()

