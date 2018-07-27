import requests,json

def get(c):
    q = ""
    c= c.lower()
    c = c.split("-")
    url = "https://www.zebapi.com/api/v1/market/ticker/"+c[0]+"/"+c[1]
    data = requests.get(url)
    data = data.text
    pairs = json.loads(data)
    q+=c[0].upper()+" TO "+c[1].upper()+"\n"
    q+="Market : "+str(pairs["market"])+"\n"
    q+="Buy : "+str(pairs["buy"])+"\n"
    q+="Sell : "+str(pairs["sell"])+"\n"
    q+="Volume : "+str(pairs["volume"])
    return q

