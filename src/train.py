import extract
import webbrowser


posts = extract.query_craigslist()

for post in posts:
    webbrowser.open(post['url'])
    res = input('Give me a value');
    print(res)
