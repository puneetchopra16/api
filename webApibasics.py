import requests,json

result = requests.get("https://api.forismatic.com/api/1.0/?lang=en&method=getQuote&format=json")
res=json.loads(result.text)
print(res["quoteText"])
