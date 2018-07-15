import requests

API_URL = 'https://api.idex.market/returnTicker/'


def returnTicker(ticker):      
    params = dict(
        market='ETH_' + ticker
    )
    response = requests.post(API_URL, json=params)
    if response.ok:
        rdata = response.json()

        last = rdata['last']
        high = rdata['high']
        low = rdata['low']
        pc = rdata['percentChange']
        vol = rdata['baseVolume']

        fdata = f'`Last: {last:.10}\tHigh: {high:.10}\tLow: {low:.10}\tChange: {pc:.4}%\t Volume: {vol:.6}ETH`'
    else:
        if response.status_code == 504:
            return 'Idex is slow, try again'
        else:
            return response.status_code

    return fdata