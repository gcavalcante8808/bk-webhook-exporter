from prometheus_client import generate_latest

import falcon


class MetricsView:
    def on_get(self, req, resp):
        data = generate_latest()
        resp.content_type = 'text/plain; version=0.0.4; charset=utf-8'
        resp.body = str(data.decode('utf-8'))


class WebHookReceiver:
    def on_post(self, req, resp):
        if req.valid_event and req.valid_token:
            req.buildkite_event.value.inc()
            resp.status = falcon.HTTP_204
