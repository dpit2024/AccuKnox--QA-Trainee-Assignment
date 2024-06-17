import requests

# Configuration
API_KEY = 'f3f70ca9femsha1438fd8943849dp189a29jsn3ebfa14b4710'  # Replace with your Human API key from RapidAPI
API_HOST = 'humanapi.p.rapidapi.com'
BASE_URL = f'https://{API_HOST}/v1/human'

HEADERS = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY,
}

# List of endpoints to check
ENDPOINTS = [
    '',
    'activities/daily_summary?date=2022-01-01',
    'heart_rate?start_time=2022-01-01T00:00:00Z&end_time=2022-01-02T00:00:00Z',
    'sleeps?start_time=2022-01-01T00:00:00Z&end_time=2022-01-02T00:00:00Z'
]

EXPECTED_STATUS_CODE = 200

def check_endpoint_health(endpoint):
    url = f'{BASE_URL}/{endpoint}'
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == EXPECTED_STATUS_CODE:
            print(f'Endpoint {url} is UP. Status code: {response.status_code}')
        else:
            print(f'Endpoint {url} is DOWN. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to reach {url}: {e}')

def main():
    for endpoint in ENDPOINTS:
        check_endpoint_health(endpoint)

if __name__ == '__main__':
    main()
