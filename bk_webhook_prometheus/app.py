from werkzeug.serving import run_simple
from wsgiref import simple_server

from bk_webhook_prometheus.resources import MetricsView, WebHookReceiver
from bk_webhook_prometheus.middlewares import CheckTokenMiddleware, CheckEventMiddleware

import falcon
import os


BUILDKITE_TOKEN = os.environ.get("BUILDKITE_TOKEN")
DEBUG = int(os.environ.get("DEBUG", 0))
assert BUILDKITE_TOKEN

app = falcon.API(middleware=[
    CheckTokenMiddleware(token=BUILDKITE_TOKEN),
    CheckEventMiddleware()
])

app.add_route('/webhook-receiver', WebHookReceiver())
app.add_route('/metrics', MetricsView())

if __name__ == '__main__':
    if DEBUG:
        run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
    else:
        httpd = simple_server.make_server('0.0.0.0', 5000, app)
        httpd.serve_forever()
