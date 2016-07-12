from flask import *
import requests, json
from werkzeug.contrib.atom import AtomFeed
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    p = dict(tags='devops')
    data = requests.get('https://remoteok.io/index.json', params=p).json()
    feed = AtomFeed("My Blog", feed_url=request.url,
                    url=request.host_url,
                    subtitle="My example blog for a feed test.")

    for item in data:
        time_obj = datetime.datetime.fromtimestamp(float(item['epoch']))
        feed.add(item['company'], item['description'], content_type='html', url=item['url'], id=item['id'], published=time_obj, updated=time_obj)
    return feed.get_response()

if __name__ == '__main__':
      app.run(debug=True)
