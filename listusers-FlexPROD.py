import requests

url = "https://flex.mam.olympicchannel.com/api/users"

payload = {}
headers = {
  'Authorization': 'Basic YXJlbWE6aFM0M0BEdlR5Q0t2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)