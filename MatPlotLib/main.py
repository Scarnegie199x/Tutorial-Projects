import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language'

headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)


response_dict = r.json()

repo_dicts = response_dict['items']

#Explore information about the repositories

repo_names,stars = [],[]


for repo_dict in repo_dicts:

    repo_names.append(repo_dict['language'])
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type':'bar',
    'x':repo_names,
    'y':stars,
}]

my_layout = {
    'title':'Most-Starred Pythong projects on Github',
    'xaxis':{'title':'Repository'},
    'yaxis':{'title':'Stars'},
}

fig = {'data':data,'layout':my_layout}
offline.plot(fig, filename = 'python_repos.html')

