import requests
import json
from urllib.parse import urlencode

def fetch_market_data():
    """
    get API data from SZSE and return high and low columns
    """

    # API URL
    base_url = "https://www.szse.cn/api/market/ssjjhq/getTimeData"
    
    # API params
    params = {
        "random": "0.8288812635870546",  
        "marketId": "1",
        "code": "000001",
        "language": "EN"
    }
    
    # header
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    
    try:
        # combine URL and params
        url = f"{base_url}?{urlencode(params)}"
        
        # send GET request
        response = requests.get(url, headers=headers, timeout=10)

        # check the status code
        status_code = response.status_code

        # Verify if the request was successful (status code 200)
        if status_code == 200:

            # Parse JSON data
            data = response.json()

            # Extract high and low
            high = float(data['data']['high'])
            low = float(data['data']['low'])  
            
            return {"high": high, "low": low}
        
        else:
            raise Exception(f"API request failed with status code: {status_code}")
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"API parse error: {e}")
    
    except (KeyError, ValueError, json.JSONDecodeError) as e:
        raise Exception(f"json decode error: {e}")
    
def verify_high_low(data):
    """
    verify high > low
    """
    assert data["high"] > data["low"], f"verify failed; High ({data['high']}) <= Low ({data['low']})"
    return True


if __name__ == "__main__":
    try:
        # Fetch market data
        market_data = fetch_market_data()
        
        # Verify if high price is greater than low price
        verify_high_low(market_data)

        print("Verification passed: high > low")
        print(f"high = {market_data['high']:.2f}, low = {market_data['low']:.2f}")
        
    except AssertionError as ae:
        # verification failure exception
        print(f"Verification failed: {str(ae)}")

    except KeyError as ke:
        # exception for missing fields in the data
        print(f"Data error: Missing required field - {str(ke)}")

    except ValueError as ve:
        # exception for data type conversion failure
        print(f"Data format error: Unable to convert data - {str(ve)}")

    except requests.exceptions.RequestException as re:
        # API request-related exceptions
        print(f"API request failed: {str(re)}")

    except Exception as e:
        # any unexpected exceptions
        print(f"Unknown error: {str(e)}")