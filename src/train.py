import extract
import learn
import webbrowser
import urllib3
from bs4 import BeautifulSoup
import json

post_details = extract.query_craigslist()
# with open('./posts.json') as posts_json:
#     post_details = json.load(posts_json)

countsByGramByProhibited = {}
countsByGramByProhibited[True] = {}
countsByGramByProhibited[False] = {}

for post_detail in post_details:
    post = {}
    post['url'] = post_detail['url']
    post['id'] = post_detail['id']
    post['name'] = post_detail['name']
    post['where'] = post_detail['where']
    print(post_detail)

    url = post_detail['url']
    print(url)
    # webbrowser.open(url)

    # page = urllib2.urlopen(url)
    # soup = BeautifulSoup(page, 'html.parser')

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    soup = BeautifulSoup(response.data)

    textEl = soup.find('section', attrs={'id': 'postingbody'})
    print(textEl.text)
    post['text'] = textEl.text

    res = input('Give me a value');
    post['isProhibited'] = res == 'y'

    learn.handle_text(countsByGramByProhibited[post['isProhibited']], post['text'])

    print(countsByGramByProhibited)

    with open('./posts.json') as posts_json:
        posts = json.load(posts_json)
    
    posts.append(post)
    with open('./posts.json', mode='w') as f:
        f.write(json.dumps(posts, indent=2))



# https://stackoverflow.com/questions/26745519/converting-dictionary-to-json-in-python
# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
