import sys

def sub_tabl() -> tuple:
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
    return COMPANIES, STOCKS

def stock_prices(input_str: str):
    companies, stocks = sub_tabl()
    input_str = input_str.lower()
    for company, stock in companies.items():
        if (input_str == company.lower()):
            print(stocks[stock])
            return
    print("Unknown company")

def type_main():
    if len(sys.argv) == 2:
        stock_prices(sys.argv[1])

if __name__ == '__main__':
    type_main()
    # stock_prices(input).len = 2

