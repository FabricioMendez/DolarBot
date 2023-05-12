import requests
def getDolarValue():
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url).json()
    
    return response


print(getDolarValue())