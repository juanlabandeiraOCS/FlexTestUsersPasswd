import requests
import json


headers = {
  'Content-Type': 'application/vnd.nativ.mio.v1+json',
  'Authorization': 'Basic YXJlbWE6aFM0M0BEdlR5Q0t2'
}

passwordTestUser = "Tururu!202401"
devTestUsers = {
    "iocviewuser00":"3719944",
    "obsvideouser00":"3719947",
    "obsviewuser00":"3719943",
    "ocsapproveruser00":"3719946",
    "ocsarchiveuser00":"3719951",
    "ocsmamuser00":"3719950",
    "ocsopsuser00":"3719948",
    "ocsopsuser01":"5152635",
    "ocssystemsuser00":"3719952",
    "ocstest00":"3719984",
    "ocsvideouser00":"3719945",
    "ocsvideousersuper00":"3741822",
    "ocsviewuser00":"3719942"
}

stgTestUsers = {
    "iocviewuser00":"453",
    "obsvideouser00":"461",
    "obsviewuser00":"379",
    "ocsapproveruser00":"368",
    "ocsarchiveuser00":"412",
    "ocsmamuser00":"362",
    "ocsopsuser00":"349",
    "ocsopsuser01":"369",
    "ocssystemsuser00":"435",
    "ocstest00":"439",
    "ocsvideouser00":"363",
    "ocsvideousersuper00":"445",
    "ocsviewuser00":"386"
}

prodTestUsers = {
    "iocviewuser00":"27228767",
    "obsvideouser00":"27236110",
    "obsviewuser00":"27228766",
    "ocsapproveruser00":"27228761",
    "ocsapproveruser01":"42681338",
    "ocsarchiveuser00":"27228762",
    "ocsmamuser00":"27236106",
    "ocsopsuser00":"27228763",
    "ocsopsuser01":"31792175",
    "ocssystemsuser00":"27228764",
    "ocstest00":"27236109",
    "ocsvideouser00":"27236107",
    "ocsvideousersuper00":"30779316",
    "ocsviewuser00":"27236108"
}

for key in devTestUsers:
    url = "https://devflex.mam.olympicchannel.com/api/users/" + devTestUsers[key]  + "/password"
    payload = json.dumps({
        "password": passwordTestUser
    })

    response = requests.request("PUT", url, headers=headers, data=payload)
    print (response.json())

for key in stgTestUsers:
    url = "https://stgflex.mam.olympicchannel.com/api/users/" + stgTestUsers[key]  + "/password"
    payload = json.dumps({
        "password": passwordTestUser
    })

    response = requests.request("PUT", url, headers=headers, data=payload)
    print (response.json())

for key in prodTestUsers:
    url = "https://flex.mam.olympicchannel.com/api/users/" + prodTestUsers[key]  + "/password"
    payload = json.dumps({
        "password": passwordTestUser
    })

    response = requests.request("PUT", url, headers=headers, data=payload)
    print (response.json())