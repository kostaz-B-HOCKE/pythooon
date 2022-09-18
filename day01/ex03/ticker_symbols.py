import sys

def data(company):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    if company not in COMPANIES.values():
        return 'Unknown company'
    inv_COMPANIES = {value: key for key, value in COMPANIES.items()} 
    print(inv_COMPANIES[company], STOCKS[company])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        data(sys.argv[1].upper())