import requests
from datetime import date
from datetime import timedelta

base_url = "https://lda.senate.gov/api/v1/"
auth_key = "9f6dc2637d955714db2c8a6e33e5b46990e9b10f"


def latest_contributions():
    url = base_url + "contributions/"
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    headers = {"Authorization": auth_key}
    params = {"filing_dt_posted_after": yesterday,
              "contribution_amount_min": "1"}
    response = requests.get(url, headers=headers, params=params)
    print(response.json())


def latest_filings(range=1):
    url = base_url + "filings/"
    yesterday = (date.today() - timedelta(days=range)).isoformat()
    headers = {"Authorization": auth_key}
    params = {"filing_dt_posted_after": yesterday, "affiliated_organization_country": ["US"],
              "filing_amount_min": "10000"}
    response = requests.get(url, headers=headers, params=params)
    print(response)
    print([s["url"] for s in response.json()[
          'results'] if s["filing_type"] not in ["RR", "RA"]])


latest_filings()
