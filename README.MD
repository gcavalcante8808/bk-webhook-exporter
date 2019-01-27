[![Build Status](https://cloud.drone.io/api/badges/gcavalcante8808/bk-webhook-exporter/status.svg)](https://cloud.drone.io/gcavalcante8808/bk-webhook-exporter)
[![codecov](https://codecov.io/gh/gcavalcante8808/buildkite-webhook-exporter/branch/master/graph/badge.svg)](https://codecov.io/gh/gcavalcante8808/bk-webhook-exporter)

Buildkite-webhook-exporter
--------------------------

A project that generates prometheus metrics from webhooks received from buildkite.

Requirements
------------

Docker and docker-compose installed and working.

How To Run
----------

After cloning the project, create a `.env` file in the project root with the value from the buildkite token, in the format `TOKEN=YOURTOKENHERE`.

The file will be read automatically by docker-compose during the `docker-compose up -d` command and will start the application.
 
You can view the metrics page by acessing the `localhost:500/metrics` page.

The project is configured to listen on port 5000 by default and the endpoint that will receive the buildkite webhooks
is `/webhook-receiver`.

*Warning*: The configuration defined in the default `docker-compose.yml` file is suited to developmented only. If you plan to use the project in production
deactivate the DEBUG env var by setting it to 0 in the `environment` section.

Configuring Buildkite to send Notifications Through Webhooks
------------------------------------------------------------

You going to need a server that is acessible trough the internet and to deploy the application on it.

Go to `https://buildkite.com/organizations/<YOUR COMPANY>/services/webhook/new` site and create a new webhook
pointing to one of your public servers running the project, using the value:

```
    http://<YOUR_SERVER_ADDR>:5000//webhook-receiver

```

In the example above, is assumed that you are using the docker-compose or at least the port 5000 redirect to provide the endpoint.

After that, retry some builds and check the `/metrics` page. If you want to protect the `metrics` endpoint, I recommend
the use of a NGINX in front of the app (More info at the #Production Mode Topic Bellow).

Production Mode
---------------

It is recommended to use a NGINX with a WSGI Container to make the project available to the world but the scenario with gunicorn+nginx configured in the docker-compose is on the roadmap.

RoadMap
-------

Some good stuff that I thought for now:

* Add support for nginx+gunicorn on docker-compose.yml example;
* Add Metrics per job name.

Something else that be in the issues tab.

Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)
