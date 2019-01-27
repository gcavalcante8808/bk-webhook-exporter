from falcon import testing

from bk_webhook_prometheus.app import app
from bk_webhook_prometheus.supported_events import BuildKiteEvents

import json
import random
import os

import pytest


@pytest.fixture
def client():
    return testing.TestClient(app)


def _generate_event_for_post():
    event = random.choice(list(BuildKiteEvents))
    event_name = event.name.replace('_', '.').lower()

    return event_name


def test_get_webhook_endpoint(client):
    response = client.simulate_get('/webhook-receiver')

    assert response.status_code == 405


def test_post_on_endpoint_without_token(client):
    headers = {"X_BUILDKITE_EVENT": _generate_event_for_post()}
    response = client.simulate_post('/webhook-receiver', json=json.dumps({}), headers=headers)

    assert response.status_code == 401


def test_post_on_endpoint_with_bad_token(client):
    headers = {"X_BUILDKITE_TOKEN": "anytoken",
               "X_BUILDKITE_EVENT": _generate_event_for_post()}

    response = client.simulate_post('/webhook-receiver', json=json.dumps({}), headers=headers)

    assert response.status_code == 403


def test_get_on_metrics_endpoint(client):
    response = client.simulate_get("/metrics")

    assert response.status_code == 200


def test_event_metric_count_when_post_to_webhook_endpoint(client):
    event = random.choice(list(BuildKiteEvents))
    event_name = event.name.replace('_', '.').lower()
    headers = {"X_BUILDKITE_TOKEN": os.environ.get("BUILDKITE_TOKEN"),
               "X_BUILDKITE_EVENT": event_name}

    client.simulate_post('/webhook-receiver', json=json.dumps({}), headers=headers)
    sample_total = event.value.collect()[0].samples[0]

    assert sample_total.value == 1
