
def sendACASMS(contactno = "1234567890"):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello Officer You have been Registread to Active City Application &language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "OmgfGSeqd49CbLrTwUAN0MPJxyt3ZE1l7FV2RDcv58uKjhaXnBymtEP9Agv2q3VscNwIDiQaronejlZM",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    d1= response.text
    return d1


import json
d = sendACASMS()
dd = json.loads(d)
print(type(dd))
print(dd["message"])
print(dd["return"])
