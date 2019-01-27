from bk_webhook_prometheus.supported_events import BuildKiteEvents

import falcon


class CheckTokenMiddleware:
    def __init__(self, token):
        self.token = token

    def process_request(self, req, resp):
        if '/metrics' in req.path:
            return

        token = req.headers.get("X-BUILDKITE-TOKEN", False)
        if not token:
            resp.status = falcon.HTTP_401
            req.valid_token = False
            return

        if token != self.token:
            resp.status = falcon.HTTP_403
            req.valid_token = False
            return

        req.valid_token = True


class CheckEventMiddleware:
    def process_request(self, req, resp):
        if '/metrics' in req.path:
            return

        event_header = req.headers.get("X-BUILDKITE-EVENT")
        if not event_header:
            resp.status = falcon.HTTP_400
            req.valid_event = False
            return

        event_name = event_header.replace('.', '_').upper()
        event = getattr(BuildKiteEvents, event_name, False)
        if not event:
            resp.status = falcon.HTTP_400
            req.valid_event = False
            return

        req.valid_event = True
        req.buildkite_event = event
