from dataclasses import dataclass


@dataclass
class Job:
    source_id: str
    company: str
    title: str
    location: str
    url: str
    source: str
    description: str = ""
    posted_at: str | None = None