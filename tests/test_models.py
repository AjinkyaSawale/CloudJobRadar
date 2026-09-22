from cloud_job_radar.models import Job


def test_job_uses_default_optional_values():
    job = Job(
        source_id="123",
        company="Example Company",
        title="DevOps Engineer",
        location="Dublin",
        url="https://example.com/jobs/123",
        source="greenhouse",
    )

    assert job.description == ""
    assert job.posted_at is None