#KEY: TMJ8L8L702WBEGDC

import requests
import json

APIKey = "TMJ8L8L702WBEGDC"

def get_quote(ticket):
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticket + "&apikey=" + APIKey)
    response_py_ob = json.loads(response.content)
    time_index = (response_py_ob["Meta Data"]["3. Last Refreshed"][:10])
    quote = (response_py_ob["Time Series (Daily)"][time_index]["4. close"])
    return quote

