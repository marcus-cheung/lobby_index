import requests
from datetime import date
from datetime import timedelta

base_url = "https://lda.senate.gov/api/v1/"
auth_key = "9f6dc2637d955714db2c8a6e33e5b46990e9b10f"
headers = {"Authorization": auth_key}


def build_params():
    pass


def get_latest_filings(range=1):
    # Build URL
    url = base_url + "filings/"
    # Build Params
    filing_after_dt = (date.today() - timedelta(days=range)).isoformat()
    params = {"filing_dt_posted_after": filing_after_dt,
              "client_country": ["US"],
              "filing_amount_min": "10000",
              "filing_type": ["Q1Y"]}
    # Make request
    response = requests.get(url, headers=headers, params=params)
    json = None
    if response.status_code == 200:
        json = response.json()
        print(json)


def extract_filing_data(json):
    return


get_latest_filings()
