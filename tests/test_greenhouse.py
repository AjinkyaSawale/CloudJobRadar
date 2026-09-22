from unittest.mock import Mock, patch

from cloud_job_radar.connectors.greenhouse import fetch_jobs


@patch("cloud_job_radar.connectors.greenhouse.requests.get")
def test_fetch_jobs_normalizes_greenhouse_response(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "jobs": [
            {
                "id": 123,
                "title": "DevOps Engineer",
                "location": {"name": "Dublin, Ireland"},
                "absolute_url": "https://example.com/jobs/123",
                "content": "<p>Build and maintain cloud platforms.</p>",
            }
        ]
    }
    mock_get.return_value = mock_response

    jobs = fetch_jobs("example", "Example Company")

    assert len(jobs) == 1
    assert jobs[0].source_id == "123"
    assert jobs[0].company == "Example Company"
    assert jobs[0].title == "DevOps Engineer"
    assert jobs[0].location == "Dublin, Ireland"
    assert jobs[0].source == "greenhouse"
    assert jobs[0].description == "Build and maintain cloud platforms."

    mock_response.raise_for_status.assert_called_once()