import requests

def calculate_average_fng(url: str, limit=30):
    response = requests.get(url, params={'limit': limit, 'date_format': 'us'})
    data = response.json()['data']
    values = list(map(lambda x: int(x['value']), data))
    average = round(sum(values) / len(values))
    return average

def check_average(average: int, threshold: int):
    return average <= threshold
