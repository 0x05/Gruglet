import requests

API_URL = 'https://api.idex.market/returnTicker/'

def returnTicker(ticker):
   
    #ticker = 'ETH_' + ticker
   
    print(f'{ticker}') #dbg
  
    params = dict(
        market='ETH_' + ticker
    )
    response = requests.post(API_URL, json=params)
    if response.ok:
        
        rdata = response.json()
        print(f'{rdata}')
        
    else:
        if response.status_code == 504:
            return 'Idex is a slow pos, try again'
        else:
            return response.status_code

    return rdata