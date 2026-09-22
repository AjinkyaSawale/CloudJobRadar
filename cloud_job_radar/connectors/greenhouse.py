from html import unescape

import requests
from bs4 import BeautifulSoup

from cloud_job_radar.models import Job


BASE_URL = "https://boards-api.greenhouse.io/v1/boards"


def clean_description(description: str) -> str:
    decoded_description = unescape(description)
    soup = BeautifulSoup(decoded_description, "html.parser")
    return soup.get_text(" ", strip=True)


def fetch_jobs(board_token: str, company: str) -> list[Job]:
    url = f"{BASE_URL}/{board_token}/jobs"

    response = requests.get(
        url,
        params={"content": "true"},
        timeout=15,
    )
    response.raise_for_status()

    jobs = []

    for item in response.json().get("jobs", []):
        job = Job(
            source_id=str(item["id"]),
            company=company,
            title=item["title"],
            location=item.get("location", {}).get("name", "Unknown"),
            url=item["absolute_url"],
            source="greenhouse",
            description=clean_description(item.get("content", "")),
            posted_at=None,
        )
        jobs.append(job)

    return jobs