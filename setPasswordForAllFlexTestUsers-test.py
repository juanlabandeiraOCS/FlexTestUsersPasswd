import requests
import json

import config

headers = {
  'Content-Type': 'application/vnd.nativ.mio.v1+json',
  'Authorization': config.flexAuthorization
}

passwordTestUser = config.passwordTestUser
devTestUsers = {
    "ocssystemsuser00":"3719952"
}

for key in devTestUsers:
    url = "https://devflex.mam.olympicchannel.com/api/users/" + devTestUsers[key]  + "/password"
    payload = json.dumps({
        "password": passwordTestUser
    })

    response = requests.request("PUT", url, headers=headers, data=payload)
    print (response.json())
