import json
# rule = pd.read_csv('app/rule.csv',sep=';')
rule = None
with open('app/rule.json') as json_file:
        rule = json.load(json_file)
import requests
MAX_RATING = 5

def getNIM(nim):
    print('API Called :(')
    response = requests.get('https://v2-api.sheety.co/387597a00c54c8555a31efa648221b3e/infoTa/formResponses1', headers={'Authorization': 'Bearer tupai-terbang'})
    assert response.status_code == 200
    assert type(nim) == int
    mks = [i for i in response.json()['formResponses1'] if i['nim'] == nim]
    return mks

def getSummary(nim):
    mks = getNIM(nim)
    print(mks)
    # mks = [{'id': 2, 'timestamp': '19/07/2020 2:14:28', 'nim': 1301174068, 'kalkulusIb': 3, 'logikaMatematikaA': 4, 'dasarAlgoritmaDanPemrograman': 1, 'matematikaDiskritA': 3, 'kalkulusIib': 4, 'pemodelanBasisData': 2, 'sistemDigital': 4, 'strukturData': 2, 'matriksDanRuangVektor': 5, 'probabilitasDanStatistikaA': 2, 'pemrogramanBerorientasiObyekA': 5, 'analisisDanPerancanganPerangkatLunak': 2, 'sistemBasisData': 4, 'desainDanAnalisisAlgoritma': 4, 'organisasiDanArsitekturKomputer': 4, 'teoriBahasaDanAutomata': 2, 'jaringanKomputer': 3, 'kecerdasanBuatan': 2, 'sistemOperasiA': 4, 'pemrogramanWeb': 3, 'implementasiDanPengujianPerangkatLunak': 2, 'dasarPemodelanDanSimulasi': 3, 'interaksiManusiaDanKomputerA': 4, 'sistemParalelDanTerdistribusi': 3, 'pembelajaranMesin': 2, 'inginMemilihTrackTaYangMana?': 'Advanced AI'}]
    if len(mks) <= 0:
        return {"error": "NIM Not Found!"}
    else:
        mks = mks[0]
    summary = {}
    for track in rule:
        keys = [i.lower() for i in rule[track]]
        keys = [''.join([t.capitalize() if i != 0 else t for i,t in enumerate(m.split())]) for m in keys]
        val = [mks.get(key) for key in keys]
        summary[track] = sum(val) / (len(rule[track]) * MAX_RATING)
    print(summary)
    total = sum(summary.values())
    for k in summary:
        summary[k] = (summary[k]/total)*100
    summary = {k: summary[k] for k in sorted(summary, key=summary.get, reverse=True)}
    return summary
    # return {'Modelling and Simulation': 36.734693877551024, 'IOT': 32.6530612244898, 'Advanced AI': 30.612244897959183}

def checkNIM(nim):
    # data = []
    # with open('app/cache.json') as json_file:
    #     data = json.load(json_file)
    # if str(nim) not in data.keys():
    res = getSummary(nim)
    #     data[nim] = res
    # else :
    #     res = data[str(nim)]
    # with open('app/cache.json', 'w') as json_file:
    #     json.dump(data, json_file)
    return res

if __name__ == "__main__":
    print(getSummary(1301174068))