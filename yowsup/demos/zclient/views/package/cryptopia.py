import requests,json

def get(c):
    q = ""
    c= c.upper()
    c = c.split("-")

    url = "https://www.cryptopia.co.nz/api/GetMarkets"
    data = requests.get(url)
    data = data.text
    pairs = json.loads(data)
    q += "Total Pairs in Market : "+str(len(pairs["Data"]))+"\n"
    for one in pairs["Data"]:
        if one["Label"] == c[0]+"/"+c[1]:
            q+="AskPrice : "+str(one["AskPrice"])+"\n"
            q+="BidPrice : "+str(one["BidPrice"])
        elif one["Label"] == c[1]+"/"+c[0]:
            q+="AskPrice : "+str(one["AskPrice"])+"\n"
            q+="BidPrice : "+str(one["BidPrice"])
    return q
