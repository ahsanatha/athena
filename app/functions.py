import pandas as pd
rule = pd.read_csv('app/rule.csv',sep=';')
import requests
import json 

def getSummary(nim):
    print('API Called :(')
    response = requests.get('https://v2-api.sheety.co/387597a00c54c8555a31efa648221b3e/infoTa/formResponses1', headers={'Authorization': 'Bearer tupai-terbang'})
    assert response.status_code == 200
    assert type(nim) == int
    mks = [i for i in response.json()['formResponses1'] if i['nim'] == nim]
    if len(mks) <= 0:
        return {"error": "NIM Not Found!"}
    else:
        mks = mks[0]
    summary = {}
    for g in rule.groupby('Track'):
        keys = [i.lower() for i in g[1].MK_support.values.tolist()]
        keys = [''.join([t.capitalize() if i != 0 else t for i,t in enumerate(m.split())]) for m in keys]
        val = [mks.get(key) for key in keys]
        summary[g[0]] = sum(val)
    total = sum(summary.values())
    for k in summary:
        summary[k] = (summary[k]/total)*100
    summary = {k: summary[k] for k in sorted(summary, key=summary.get, reverse=True)}
    return summary
    # return {'Modelling and Simulation': 36.734693877551024, 'IOT': 32.6530612244898, 'Advanced AI': 30.612244897959183}

def checkNIM(nim):
    data = []
    with open('app/cache.json') as json_file:
        data = json.load(json_file)
    if str(nim) not in data.keys():
        res = getSummary(nim)
        data[nim] = res
    else :
        res = data[str(nim)]
    with open('app/cache.json', 'w') as json_file:
        json.dump(data, json_file)
    return res