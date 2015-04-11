import requests, simplejson, urlparse
from BeautifulSoup import BeautifulSoup

def get_stream_info(url):
    resp = requests.get(url)
    html = resp.content
    bs = BeautifulSoup(html)
    data_node = bs.find("meta", attrs={'name': 'broadcast-data'})
    content = data_node.get("content")
    data = simplejson.loads(content)
    token_node = bs.find("meta", attrs={'name': 'token-id'})
    token_id = token_node.get("content")
    return {
        'data': data,
        'token_id': token_id
    }

def get_periscope_url_from_tweet(status):
    entities = status._json.get('entities')
    if not entities: return
    urls = entities.get('urls', [])
    for url in urls:
        expanded_url = url['expanded_url']
        parsed = urlparse.urlparse(expanded_url)
        if parsed.netloc == 'www.periscope.tv':
            return expanded_url

