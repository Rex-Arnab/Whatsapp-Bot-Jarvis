from amzsear import api

url = api.getSearchPage('Harry Potter Books',page_num=1)

for i in range(len(url[0])):
    print(url[0][i]["name"])
    print(url[0][i]["prices"])
    print(url[0][i]["rating"])
    print("\n=================\n")
