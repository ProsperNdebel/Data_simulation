import requests
from datetime import datetime, timedelta
import tradermade as tm


def fetch_forex_data(base_currency, target_currency=None, start_date=None, end_date=None, interval=None):
    """
    Fetch Forex data from a specified API.

    Parameters:
        api_key (str): API key for authentication.
        base_currency (str): The base currency code.
        target_currency (str): The target currency code.
        start_date (str): Start date for the data retrieval (format: 'YYYY-MM-DD').
        end_date (str): End date for the data retrieval (format: 'YYYY-MM-DD').

    Returns:
        dict: A dictionary containing the fetched Forex data, where the keys are the time frames
              and the value is a list of values of how the data has varied
    """

    API_URL = 'https://marketdata.tradermade.com/api/v1/timeseries?start_date=2015-01-01&end_date=2015-05-01&api_key=Q06DBW2VTPvO_ZVTMR0W'
    api_key = '4XO4f_4tRrrimblaTwL2'

    # Example API request parameters

    tm.set_rest_api_key(api_key)

    # returns live data - fields is optional
    # data1 = tm.live(currency='EURUSD,GBPUSD', fields=["bid", "mid", "ask"])

    # returns historical data for the currency requested interval is daily, hourly, minute - fields is optional
    # data2 = tm.historical(currency='EURUSD,GBPUSD', date="2021-04-22",
    #                       interval="daily", fields=["open", "high", "low", "close"])

    # returns timeseries data for the currency requested interval is daily, hourly, minute - fields is optional
    data = tm.timeseries(currency=base_currency, start=start_date, end=end_date,
                         interval=interval, fields=["open", "high", "low", "close"])

    # data2 = tm.cfd_list()  # gets list of all cfds available

    # gets list of all currency codes available add two codes to get code for currencypair ex EUR + USD gets EURUSD
    # data3 = tm.currency_list()
    return data
