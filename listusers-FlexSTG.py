import requests

import config

headers = {
  'Content-Type': 'application/vnd.nativ.mio.v1+json',
  'Authorization': config.flexAuthorization
}

payload = {}

url = "https://stgflex.mam.olympicchannel.com/api/users"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)