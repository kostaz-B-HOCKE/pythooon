import sys

def data(part):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    tickers = {value: key for key, value in COMPANIES.items()}
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    part_cap = part.capitalize()
    part_up = part.upper()
    if part_cap in COMPANIES:
        return f'{part_up} is a ticker symbol for {STOCKS[COMPANIES[part_cap]]}'
    elif part_up in tickers:
        return f'{part_up} is a ticker symbol for {tickers[part_up]}'
    return f'{part} is an unknown company or an unknown ticker symbol'

def f(string):
    str_split = string.replace(',', ' , ').split()
    count = str_split.count(',')
    if count * 2 + 1 == len(str_split):
        for elem in str_split:
            if elem != ',':
                print(data(elem.strip(',')))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        f(sys.argv[1])

