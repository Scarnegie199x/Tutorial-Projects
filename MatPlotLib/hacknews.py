from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r= requests.get(url)
print(f"Status Code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
repo_names, stars = [], []
for submission_id in submission_ids[:10]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"ID: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()




    submission_dict = {
        'title': response_dict['title'],
        'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],

    }
    submission_dicts.append(submission_dict)
    repo_names.append(response_dict['title'])
    stars.append(response_dict['descendants'])

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse = True)

for submission_dict in submission_dicts:
    print(f"Title: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")



data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': 'Most-Starred Pythong projects on Github',
    'xaxis': {'title': 'Title'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos1.html')
