import json,requests

def get(menu):
    url = "http://jarbot.top/bot/bot/page.php?page="+menu
    data = requests.get(url)
    data = data.text
    cur = json.loads(data)
    name = cur["page"]["text"]
    return name
