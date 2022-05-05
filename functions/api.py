import requests
import json

def getdata(hkuid,datetime):
    list = datetime.split('_')
    datetime2=list[0]+' '+list[1]
    params4 = {"hkuid": hkuid, "datetime": datetime2}
    response = requests.post("https://shielded-tor-28383.herokuapp.com/studysafe_core/api_trace",
                             data=json.dumps(params4), headers={'content-type': 'application/json'})
    data=json.loads(response.text)
    return data

