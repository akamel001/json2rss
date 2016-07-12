from flask import *
import requests, json, datetime, os
from werkzeug.contrib.atom import AtomFeed

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
